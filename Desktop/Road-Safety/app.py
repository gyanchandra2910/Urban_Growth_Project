"""
Flask API for Road Safety Recommendations
Provides TF-IDF search with optional OpenAI RAG enhancement

ONE-CLICK START (PowerShell):
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python app.py" ; Start-Sleep -Seconds 3 ; Start-Process powershell -ArgumentList "-NoExit", "-Command", "streamlit run streamlit_app.py"
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from tfidf_search import tfidf_search

app = Flask(__name__)
CORS(app)

# Check if OpenAI is available and configure
OPENAI_AVAILABLE = False
openai_client = None

try:
    from openai import OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    if OPENAI_API_KEY and OPENAI_API_KEY.startswith('sk-'):
        openai_client = OpenAI(api_key=OPENAI_API_KEY)
        OPENAI_AVAILABLE = True
        print("OpenAI integration enabled")
        print(f"API key loaded: {OPENAI_API_KEY[:20]}...")
    else:
        print("OPENAI_API_KEY not found or invalid format")
except ImportError:
    print("OpenAI package not installed")
except Exception as e:
    print(f"OpenAI initialization error: {e}")

@app.route('/recommend', methods=['POST'])
def recommend():
    """POST /recommend - Get road safety recommendations"""
    try:
        if not request.is_json:
            return jsonify({'ok': False, 'error': 'Content-Type must be application/json', 'data': None}), 400
        
        data = request.get_json()
        description = data.get('description', '').strip()
        
        if not description:
            return jsonify({'ok': False, 'error': 'Missing required field: description', 'data': None}), 400
        
        top_n = data.get('top_n', 5)
        if not isinstance(top_n, int) or top_n < 1 or top_n > 20:
            return jsonify({'ok': False, 'error': 'Field "top_n" must be between 1 and 20', 'data': None}), 400
        
        matches = tfidf_search(description, top_n=top_n)
        
        response_data = {
            'matches': matches,
            'method': 'tfidf',
            'query': description,
            'count': len(matches),
            'rag_enabled': False
        }
        
        # Generate AI explanation if OpenAI is available and we have matches
        if OPENAI_AVAILABLE and matches:
            try:
                explanation = generate_rag_explanation(description, matches)
                if explanation:
                    response_data['explanation'] = explanation
                    response_data['rag_enabled'] = True
                    print(f"Generated AI explanation for query: '{description[:50]}...'")
            except Exception as e:
                print(f"Failed to generate AI explanation: {str(e)}")
                # Continue without AI explanation - don't fail the request
        
        return jsonify({'ok': True, 'error': None, 'data': response_data}), 200
    
    except Exception as e:
        return jsonify({'ok': False, 'error': f'Internal server error: {str(e)}', 'data': None}), 500

def generate_rag_explanation(query, matches):
    """Generate AI-powered explanation using OpenAI GPT"""
    if not openai_client or not matches:
        return None
    
    # Get the top match for detailed reference
    top_match = matches[0]
    
    # Build context from top 3 matches
    context = "\n\n".join([
        f"Match {i}: Problem Type: {m['problem']}\n"
        f"IRC Clause: {m['clause']}\n"
        f"Details: {m['data'][:300]}"
        for i, m in enumerate(matches[:3], 1)
    ])
    
    prompt = f"""You are an expert road safety engineer familiar with IRC (Indian Roads Congress) codes and regulations.

User's Road Safety Issue:
"{query}"

Top Matching Interventions from Database:
{context}

Task:
Explain why the top recommended intervention (IRC Clause {top_match['clause']}) fits this road safety issue. Your explanation should:

1. Clearly state what the road safety problem is
2. Explain why IRC Clause {top_match['clause']} is the most relevant regulation
3. Describe the specific intervention or corrective action required
4. Mention any safety implications if not addressed

Keep your response professional, concise (3-4 sentences), and actionable for road safety personnel."""

    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a road safety expert specializing in IRC codes and traffic safety interventions."
                },
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=250
        )
        
        explanation = response.choices[0].message.content.strip()
        return explanation
        
    except Exception as e:
        print(f"OpenAI API error: {str(e)}")
        return None

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({'status': 'healthy', 'openai_available': OPENAI_AVAILABLE}), 200

@app.route('/', methods=['GET'])
def index():
    """API information"""
    return jsonify({
        'name': 'Road Safety Recommendation API',
        'version': '1.0.0',
        'endpoints': {
            'POST /recommend': 'Get recommendations',
            'GET /health': 'Health check',
            'GET /': 'API info'
        },
        'features': {'tfidf_search': True, 'openai_rag': OPENAI_AVAILABLE}
    }), 200

if __name__ == '__main__':
    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    
    print("\n" + "="*80)
    print("ROAD SAFETY RECOMMENDATION SYSTEM")
    print("="*80)
    print("\nPROJECT OVERVIEW:")
    print("   A TF-IDF-based semantic search engine for IRC road safety compliance")
    print("   Searches across 50 road safety records with automatic IRC code references")
    print("\nFEATURES:")
    print(f"   - TF-IDF Search: Enabled")
    print(f"   - OpenAI RAG: {'Enabled' if OPENAI_AVAILABLE else 'Disabled'}")
    print("\nACCESS POINTS:")
    print("   - Flask API: http://127.0.0.1:5000")
    print("   - Streamlit UI: http://localhost:8501 (run separately)")
    print("\nAPI ENDPOINTS:")
    print("   - POST /recommend - Get road safety recommendations")
    print("     Request: {\"description\": \"query text\", \"top_n\": 5}")
    print("   - GET  /health    - Health check")
    print("   - GET  /          - API info")
    print("\nQUICK START STREAMLIT:")
    print("   Open new terminal: streamlit run streamlit_app.py")
    print("="*80 + "\n")
    print("Starting Flask server...\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
