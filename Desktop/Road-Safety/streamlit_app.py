"""
Streamlit App for Road Safety Recommendations
Provides an interactive UI for searching road safety issues
"""

import streamlit as st
import requests
import sys
import os

# Add current directory to path for direct imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuration
st.set_page_config(
    page_title="Road Safety Recommender",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Backend configuration
BACKEND_URL = "http://localhost:5000"
USE_BACKEND = True  # Set to False to use direct function calls

# Try to import search functions for local mode
try:
    from tfidf_search import tfidf_search
    LOCAL_MODE_AVAILABLE = True
except ImportError:
    LOCAL_MODE_AVAILABLE = False

def call_backend_api(description, method, top_n):
    """
    Call the Flask backend API with proper error handling
    """
    try:
        st.info("🔌 Connecting to API...")
        
        response = requests.post(
            f"{BACKEND_URL}/recommend",
            json={
                "description": description,
                "top_n": top_n
            },
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        # Parse JSON response
        try:
            response_data = response.json()
        except ValueError:
            return None, f"Invalid JSON response from server (status: {response.status_code})"
        
        # Handle new response format: {ok, error, data}
        if response.status_code == 200:
            if response_data.get('ok'):
                st.success("✅ Recommendations loaded!")
                return response_data.get('data'), None
            else:
                error_msg = response_data.get('error', 'Unknown error')
                return None, f"API Error: {error_msg}"
        else:
            error_msg = response_data.get('error', f'HTTP {response.status_code}')
            return None, f"API Error ({response.status_code}): {error_msg}"
    
    except requests.exceptions.ConnectionError:
        return None, "❌ Cannot connect to backend server.\n\nMake sure Flask is running:\n`python run_project.py` or `python app.py`"
    except requests.exceptions.Timeout:
        return None, "⏱️ Request timed out. Server may be overloaded. Please try again."
    except requests.exceptions.RequestException as e:
        return None, f"Network error: {str(e)}"
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

def call_local_search(description, method, top_n):
    """
    Call search functions directly (local mode)
    """
    try:
        if method.lower() == 'tfidf':
            results = tfidf_search(description, top_n=top_n)
            return {
                'matches': results,
                'method': 'tfidf',
                'query': description,
                'count': len(results),
                'rag_enabled': False
            }, None
        else:
            return None, f"Method '{method}' not supported in local mode. Only 'tfidf' is available."
    except Exception as e:
        return None, f"Local search error: {str(e)}"

def render_results(data):
    """
    Render search results in a nice table/card format
    """
    if not data or 'matches' not in data:
        st.warning("⚠️ No data received from server")
        return
    
    matches = data['matches']
    count = data.get('count', len(matches))
    method = data.get('method', 'tfidf')
    query = data.get('query', '')
    rag_enabled = data.get('rag_enabled', False)
    
    # Summary header with metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Results Found", count)
    with col2:
        st.metric("🔍 Search Method", method.upper())
    with col3:
        st.metric("🤖 AI Enhanced", "Yes" if rag_enabled else "No")
    
    st.markdown(f"**Search Query:** _{query}_")
    st.divider()
    
    # Show AI explanation if available
    if rag_enabled and 'explanation' in data:
        st.info("💡 **AI-Generated Insight**")
        st.markdown(data['explanation'])
        st.divider()
    
    # Show matches
    if not matches:
        st.warning("⚠️ No matching results found. Try different keywords or adjust your search.")
        return
    
    st.subheader(f"📋 Top {count} Recommendations")
    
    # Create a nice table view
    for rank, match in enumerate(matches, 1):
        # Color-coded relevance
        if match['score'] >= 0.3:
            score_color = "🟢"
        elif match['score'] >= 0.15:
            score_color = "🟡"
        else:
            score_color = "🟠"
        
        # Create expandable card for each result
        with st.expander(
            f"{score_color} **#{rank}** | {match['problem']} | Score: {match['score']:.4f} | Clause: {match['clause']}",
            expanded=(rank == 1)  # First result expanded by default
        ):
            # Two-column layout
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown("#### 📊 Metadata")
                st.markdown(f"**Record ID:** `{match['id']}`")
                st.markdown(f"**Relevance:** `{match['score']:.4f}`")
                st.markdown(f"**IRC Clause:** `{match['clause']}`")
                
                # Visual relevance indicator
                relevance_pct = int(match['score'] * 100)
                st.progress(match['score'])
                st.caption(f"{relevance_pct}% relevant")
            
            with col2:
                st.markdown("#### 🔴 Problem Description")
                st.markdown(f"**{match['problem']}**")
                
                st.markdown("#### 📖 Full Details")
                data_text = match['data']
                
                # Show full text in a nice box with proper text color
                st.markdown(f"""
                <div style='background-color: #f0f2f6; padding: 15px; border-radius: 5px; border-left: 4px solid #1f77b4; color: #262730;'>
                {data_text}
                </div>
                """, unsafe_allow_html=True)
    
    # Summary at the end
    st.divider()
    st.success(f"✅ Displayed all {count} recommendations")

# ============================================================================
# MAIN APP
# ============================================================================

# Header
st.title("🚦 Road Safety Recommender")
st.markdown("Search and analyze road safety issues with IRC code references")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Backend mode selection
    mode = st.radio(
        "Search Mode",
        ["Backend API", "Local (Direct)"],
        help="Backend API: Calls Flask server (with OpenAI RAG)\nLocal: Direct function calls (faster, no RAG)"
    )
    
    USE_BACKEND = (mode == "Backend API")
    
    if USE_BACKEND:
        st.info("🌐 Using Flask backend at `localhost:5000`")
        
        # Test backend connection
        try:
            response = requests.get(f"{BACKEND_URL}/health", timeout=2)
            if response.status_code == 200:
                health = response.json()
                st.success("✅ Backend connected")
                if health.get('openai_available'):
                    st.success("✨ OpenAI RAG enabled")
            else:
                st.error("❌ Backend not responding")
        except:
            st.warning("⚠️ Backend not available")
            st.code("python app.py", language="bash")
    else:
        if LOCAL_MODE_AVAILABLE:
            st.success("✅ Local mode ready")
        else:
            st.error("❌ Local mode not available")
    
    st.divider()
    
    # Number of results
    top_n = st.slider(
        "Number of Results",
        min_value=1,
        max_value=20,
        value=5,
        help="How many top results to display"
    )
    
    st.divider()
    
    # About section
    st.markdown("### 📚 About")
    st.markdown("""
    This tool helps identify road safety issues using IRC (Indian Roads Congress) codes.
    
    **Features:**
    - TF-IDF semantic search
    - OpenAI-powered insights
    - IRC code references
    """)

# Main content area
st.markdown("---")

# Search interface
col1, col2 = st.columns([3, 1])

with col1:
    description = st.text_input(
        "🔍 Describe the road safety issue:",
        placeholder="e.g., damaged road signs, missing speed limit signs, faded markings...",
        help="Enter a description of the road safety problem you want to search for"
    )

with col2:
    method = st.selectbox(
        "Search Method",
        ["TF-IDF", "Fuzzy", "Keyword"],
        help="TF-IDF: Semantic search (recommended)\nFuzzy: String matching\nKeyword: Exact keyword matching"
    )

# Search button
search_button = st.button("🔎 Recommend", type="primary", use_container_width=True)

# Perform search when button is clicked
if search_button:
    if not description or not description.strip():
        st.warning("⚠️ Please enter a description to search.")
    else:
        # Call appropriate backend
        if USE_BACKEND:
            data, error = call_backend_api(description, method, top_n)
        else:
            if LOCAL_MODE_AVAILABLE:
                with st.spinner("🔍 Searching locally..."):
                    data, error = call_local_search(description, method, top_n)
            else:
                error = "Local mode not available. Please use Backend API mode."
                data = None
        
        # Display results or error
        if error:
            st.error(error)
            
            # Show helpful troubleshooting info
            if "connect" in error.lower():
                st.info("💡 **Troubleshooting:**\n\n1. Make sure Flask server is running\n2. Run: `python run_project.py`\n3. Check if http://127.0.0.1:5000/health is accessible")
        elif data:
            st.markdown("---")
            render_results(data)
        else:
            st.error("❌ Unexpected error: No data and no error message received")

# Help section at bottom
with st.expander("ℹ️ How to Use"):
    st.markdown("""
    ### Getting Started
    
    1. **Enter Description**: Type a description of the road safety issue
    2. **Choose Method**: Select search method (TF-IDF recommended)
    3. **Click Recommend**: Get matching results with IRC codes
    
    ### Search Methods
    
    - **TF-IDF**: Best for semantic/conceptual searches. Finds documents with similar meaning.
    - **Fuzzy**: Best for approximate string matching. Finds similar text patterns.
    - **Keyword**: Exact keyword matching. Finds documents containing specific words.
    
    ### Understanding Results
    
    - **Rank**: Position in search results (1 = best match)
    - **Score**: Relevance score (0.0 to 1.0, higher is better)
    - **Problem**: Type of road safety issue
    - **Clause**: Relevant IRC code clause
    - **Details**: Full description and specifications
    - **AI Insight**: GPT-generated explanation (when available)
    
    ### Tips
    
    - Use natural language descriptions
    - Include specific details (e.g., "damaged", "missing", "height")
    - Try different search methods for best results
    - Adjust number of results in sidebar
    
    ### Backend Setup
    
    To enable OpenAI RAG features:
    
    ```bash
    # Set API key
    $env:OPENAI_API_KEY="your-key-here"
    
    # Start Flask backend
    python app.py
    
    # Start Streamlit app (in new terminal)
    streamlit run streamlit_app.py
    ```
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 10px;'>"
    "🚦 Road Safety Recommender | Powered by IRC Codes & AI"
    "</div>",
    unsafe_allow_html=True
)
