# 🚦 Road Safety Intervention GPT

**National-Level Hackathon Submission**  
**Problem Statement 1.3**: *Identification of road safety interventions using a GPT-based AI tool*

---

## 📋 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Project Structure](#project-structure)
- [Sample Input/Output](#sample-inputoutput)
- [Future Enhancements](#future-enhancements)
- [Team & Credits](#team--credits)

---

## 🎯 Overview

**Road Safety Intervention GPT** is an intelligent recommendation system that helps identify appropriate road safety interventions for specific safety issues. The system combines traditional machine learning (TF-IDF similarity matching) with modern AI (GPT-3.5) to provide accurate, context-aware recommendations backed by relevant IRC clauses and standards.

The tool processes natural language descriptions of road safety problems and returns ranked intervention recommendations along with AI-generated explanations, making it valuable for:
- 🏗️ **Highway Engineers** planning safety improvements
- 👮 **Traffic Authorities** addressing accident-prone areas
- 📊 **Policy Makers** designing evidence-based interventions
- 🎓 **Researchers** analyzing road safety measures

---

## 🚨 Problem Statement

**Challenge**: Develop a GPT-based AI tool to identify appropriate road safety interventions from a curated database based on user-described safety issues.

**Input**: CSV database containing road safety interventions with context (problem types, categories, IRC clauses, implementation details)

**Output**: Ranked recommendations with:
1. Matching interventions from database
2. Relevance scores
3. AI-generated explanations referencing specific IRC clauses
4. Implementation details and context

---

## ✨ Key Features

### 🔍 Intelligent Search
- **TF-IDF Similarity Matching**: Fast, accurate retrieval of relevant interventions
- **Multi-column Search**: Searches across problem types, categories, and details
- **Ranked Results**: Scored by relevance (0-1 scale)

### 🤖 AI-Powered Explanations
- **GPT-3.5 Integration**: Generates human-readable reasoning
- **Context-Aware**: References specific IRC clauses and problem context
- **Professional Output**: 3-4 sentence explanations suitable for technical reports

### 🎨 User-Friendly Interface
- **Streamlit Frontend**: Clean, interactive web UI
- **Visual Relevance Indicators**: Color-coded matches (🟢 High, 🟡 Medium, 🟠 Low)
- **Expandable Cards**: Detailed views with full intervention specifications
- **Real-time API Integration**: Seamless backend communication

### 🏗️ Production-Ready Architecture
- **Flask REST API**: Scalable backend with health checks
- **One-Click Launcher**: Automatic startup of both servers
- **Error Handling**: Comprehensive fallback mechanisms
- **Modular Design**: Easy to extend and maintain

### 🔐 Secure & Configurable
- **Environment Variables**: API keys stored securely in `.env`
- **Graceful Degradation**: Works perfectly without GPT (TF-IDF only)
- **CORS Support**: Ready for cross-origin deployments

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend** | Flask 3.0+ | REST API server |
| **Frontend** | Streamlit 1.28+ | Interactive web interface |
| **AI Engine** | OpenAI GPT-3.5-turbo | Natural language explanations |
| **Search Engine** | scikit-learn (TF-IDF) | Semantic similarity matching |
| **Data Processing** | Pandas & NumPy | CSV processing and analysis |
| **Environment** | python-dotenv | Configuration management |
| **Language** | Python 3.13 | Core development |

---

## 🏛️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interface                         │
│                   (Streamlit Frontend)                      │
│              http://localhost:8501                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ POST /recommend
                     │ {description, top_n}
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                     Flask Backend API                       │
│                  http://localhost:5000                      │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  1. Receive Query                                    │  │
│  │  2. TF-IDF Similarity Search → Rank Results         │  │
│  │  3. Send Top Matches to GPT-3.5                     │  │
│  │  4. Generate Context-Aware Explanation              │  │
│  │  5. Return {matches, scores, explanation}           │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────┬─────────────────────────┬──────────────────────┘
             │                         │
             ▼                         ▼
     ┌───────────────┐        ┌────────────────┐
     │  TF-IDF Engine│        │  OpenAI API    │
     │  (scikit-learn)│        │  (GPT-3.5)     │
     └───────┬───────┘        └────────────────┘
             │
             ▼
     ┌────────────────┐
     │ GPT_Input_DB.csv│
     │  50 Records     │
     └────────────────┘
```

**Workflow**:
1. User describes road safety issue in natural language
2. Streamlit sends query to Flask API
3. TF-IDF engine searches database and ranks matches
4. Top matches sent to GPT-3.5 for explanation generation
5. API returns recommendations + AI reasoning
6. Streamlit displays results with visual indicators

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9 or higher (tested on Python 3.13)
- pip package manager
- OpenAI API key (optional, for AI explanations)

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd Road-Safety
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages**:
- `flask>=3.0.0` - Backend API
- `streamlit>=1.28.0` - Frontend UI
- `scikit-learn>=1.3.0` - TF-IDF search
- `pandas>=2.0.0` - Data processing
- `openai>=1.0.0` - GPT integration
- `python-dotenv>=1.0.0` - Environment management

### Step 3: Configure Environment Variables

Create a `.env` file in the project root:
```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=sk-proj-your-api-key-here
```

**Note**: The application works perfectly without an API key (TF-IDF only mode). AI explanations require a valid OpenAI API key with available credits.

### Step 4: Verify Data File
Ensure `GPT_Input_DB.csv` exists in the project root (provided by hackathon organizers).

---

## 🚀 How to Run

### Option 1: One-Click Launcher (Recommended)
```bash
python run_project.py
```

This will:
- ✅ Start Flask backend (port 5000)
- ✅ Start Streamlit frontend (port 8501)
- ✅ Perform health checks
- ✅ Open browser automatically
- ✅ Display real-time logs from both servers

**Stop the application**: Press `Ctrl+C` in the terminal

---

### Option 2: Manual Start (Advanced)

**Terminal 1 - Backend**:
```bash
python app.py
```
Backend will start at http://localhost:5000

**Terminal 2 - Frontend**:
```bash
streamlit run streamlit_app.py
```
Frontend will start at http://localhost:8501

---

## 📖 Usage Guide

### 1. **Access the Application**
Open your browser and navigate to: `http://localhost:8501`

### 2. **Describe the Road Safety Issue**
Enter a natural language description, for example:
- *"Damaged road signs near school zone"*
- *"High-speed vehicles in residential area"*
- *"Poor visibility at night on highway"*
- *"Frequent accidents at intersection"*

### 3. **Select Number of Recommendations**
Choose how many top matches you want (1-20, default: 5)

### 4. **View Results**
The system displays:
- **📊 Metrics**: Result count, search method, AI status
- **🎯 Ranked Matches**: Color-coded by relevance
  - 🟢 **High Relevance** (≥30%)
  - 🟡 **Medium Relevance** (15-30%)
  - 🟠 **Low Relevance** (<15%)
- **📋 Intervention Details**: Problem type, category, IRC clause, specifications
- **💡 AI Insight** (if enabled): GPT-generated explanation with context

### 5. **Expand Details**
Click on any recommendation card to view:
- Full problem description
- Detailed implementation data
- Relevant IRC clauses
- Safety category

---

## 📁 Project Structure

```
Road-Safety/
│
├── 📄 app.py                    # Flask backend API
│   ├── POST /recommend          # Main recommendation endpoint
│   ├── GET /health              # Health check endpoint
│   └── OpenAI GPT integration   # AI explanation generation
│
├── 🎨 streamlit_app.py          # Streamlit frontend UI
│   ├── User input form
│   ├── API communication
│   └── Results visualization
│
├── 🔍 tfidf_search.py           # TF-IDF similarity engine
│   ├── Vectorization
│   ├── Similarity computation
│   └── Result ranking
│
├── 📊 load_data.py              # Data loading utilities
│   ├── CSV parsing
│   ├── Encoding detection
│   └── DataFrame creation
│
├── 🚀 run_project.py            # One-click launcher
│   ├── Process management
│   ├── Health checks
│   └── Browser automation
│
├── 🧪 test_openai.py            # OpenAI API key tester
│
├── 📋 GPT_Input_DB.csv          # Road safety interventions database
│   └── 50 curated records       # (Provided by organizers)
│
├── 📦 requirements.txt          # Python dependencies
│
├── 🔐 .env                      # Environment variables (API keys)
│
├── 📖 README.md                 # This file
│
└── 🚫 .gitignore                # Git ignore rules
```

---

## 📝 Sample Input/Output

### Input Example
```
Description: "Damaged road signs and poor visibility at highway exit"
Top N: 5
```

### Output Example

**Match 1** (Relevance: 67%)
```
Problem Type: Road Sign Damage
Category: Traffic Management
IRC Clause: IRC:67-2012 (Road Signs)

Details:
Replace damaged regulatory signs with retro-reflective materials.
Install illuminated signs at critical locations. Conduct quarterly
maintenance inspections.

💡 AI Insight:
This intervention directly addresses damaged road signs by recommending 
retro-reflective replacements per IRC:67-2012 standards. The inclusion 
of illuminated signage specifically tackles poor visibility concerns at 
highway exits, combining both aspects of your reported issue.
```

**Match 2** (Relevance: 54%)
```
Problem Type: Visibility Enhancement
Category: Highway Safety
IRC Clause: IRC:35-2015 (Road Lighting)
...
```

---

## 🚀 Future Enhancements

### Planned Features
- [ ] **Image Upload**: Support for accident scene photos
- [ ] **PDF Report Generation**: Downloadable intervention reports
- [ ] **Multi-language Support**: Hindi, regional languages
- [ ] **Historical Analytics**: Track common intervention types
- [ ] **Cost Estimation**: Budget calculator for interventions
- [ ] **Map Integration**: Geolocation-based recommendations
- [ ] **Batch Processing**: Upload multiple issues via CSV
- [ ] **Admin Dashboard**: Database management interface

### Technical Improvements
- [ ] Fine-tuned GPT model on road safety domain
- [ ] Vector database (Pinecone/Weaviate) for faster search
- [ ] Caching layer (Redis) for repeated queries
- [ ] User authentication and session management
- [ ] Deployment on cloud platform (AWS/Azure/GCP)
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

## 🔧 Troubleshooting

### Issue: "Connection Error - Cannot reach Flask API"
**Solution**: Ensure Flask backend is running on port 5000
```bash
# Check if port is in use
netstat -ano | findstr :5000

# Restart using launcher
python run_project.py
```

### Issue: "AI explanations not appearing"
**Solution**: Check OpenAI API key setup
```bash
# Test API key
python test_openai.py

# Verify .env file exists and contains valid key
```

### Issue: "ModuleNotFoundError"
**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "Encoding errors in CSV"
**Solution**: The system auto-detects encoding (utf-8, latin-1, iso-8859-1, cp1252). Ensure `GPT_Input_DB.csv` is not corrupted.

---

## 🤝 Team & Credits

### Development Team
- **Team Name**: [Your Team Name]
- **Members**: 
  - [Member 1 Name] - Backend Development & AI Integration
  - [Member 2 Name] - Frontend Development & UI/UX
  - [Member 3 Name] - Data Processing & Search Engine
  - [Member 4 Name] - Testing & Documentation

### Acknowledgements
- **Hackathon Organizers** for problem statement and dataset
- **OpenAI** for GPT-3.5 API
- **scikit-learn** community for TF-IDF implementation
- **Streamlit & Flask** teams for excellent frameworks

### References
- IRC (Indian Roads Congress) Standards
  - IRC:67-2012 - Code of Practice for Road Signs
  - IRC:35-2015 - Code of Practice for Road Lighting
  - IRC:99-2018 - Manual for Road Safety Audit
- WHO Road Safety Guidelines
- Ministry of Road Transport & Highways (MoRTH) publications

---

## 📄 License

This project was developed for [Hackathon Name] and is intended for educational and demonstration purposes.

---

## 📞 Contact

For queries regarding this submission:
- **Email**: [your-team-email@example.com]
- **GitHub**: [repository-link]
- **Documentation**: [project-documentation-link]

---

## 🎯 Hackathon Submission Details

**Problem Statement**: 1.3 - Identification of road safety interventions using a GPT-based AI tool  
**Submission Date**: November 2025  
**Status**: ✅ Fully Functional (AI module ready, requires OpenAI credits)

**Key Achievement**: Successfully integrated traditional ML (TF-IDF) with modern AI (GPT) to create a robust, production-ready road safety recommendation system with graceful degradation and modular architecture.

---

<div align="center">

**Built with ❤️ for Road Safety**

*Making Indian roads safer, one intervention at a time* 🚦

</div>
