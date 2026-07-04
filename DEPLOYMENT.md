# Legal Strategy Swarm - Streamlit App

A 3-layer AI agent swarm for analyzing legal cases and recommending strategies.

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.10+
- GROQ API Key ([Get one free](https://console.groq.com))

### Installation

1. **Clone/navigate to the project:**
```bash
cd swarm_strategy
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

5. **Run the Streamlit app:**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Add Streamlit app"
git push origin main
```

### Step 2: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Choose the branch and set main file to `app.py`
5. Click "Deploy"

### Step 3: Add Secrets

In Streamlit Cloud dashboard:
1. Go to your app settings
2. Add secret: `GROQ_API_KEY` = your Groq API key

## 📊 How It Works

The app takes a case description and runs it through:

1. **Layer 1: Battlefield Understanding**
   - Analyzes case fundamentals
   - Identifies key facts and legal issues
   - Assesses case strength

2. **Layer 2: Specialized Strategies** (Parallel)
   - Plaintiff perspective
   - Defendant perspective
   - Evidence analysis
   - Risk assessment
   - Settlement framework

3. **Layer 3: Strategic Judgment**
   - Synthesizes all analysis
   - Calculates win probabilities
   - Recommends action plan with milestones

## 📝 Example Input

```
Client paid 50% for services on Jan 1, 2024. 
Services were due by April 1, 2024.
Defendant did not deliver. 
No response to communications.
```

## 🎨 UI Features

- Clean, intuitive interface
- Expandable sections for detailed analysis
- Metrics dashboard for win probabilities
- Color-coded strategy recommendations
- Actionable step-by-step plans

## ⚙️ Environment Variables

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

## 📦 Project Structure

```
swarm_strategy/
├── app.py                   # Streamlit app (main UI)
├── graph.py                 # LangGraph orchestration
├── requirements.txt         # Dependencies
├── core/                    # Shared utilities
│   ├── llm.py
│   ├── state.py
│   └── schemas.py
├── layer_1_understanding/   # Case analysis
├── layer_2_strategy/        # Parallel agents
└── layer_3_coordination/    # Judgment & planning
```

## 🔐 Security

- Never commit `.env` file (it's in .gitignore)
- Use Streamlit Secrets for production
- GROQ API keys are sensitive—protect them

## 📄 License

For internal use only.

## 🆘 Troubleshooting

**Rate limit errors?**
- Wait a few seconds and try again
- Consider upgrading your Groq tier

**Import errors?**
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct virtual environment

**Missing .env?**
- Create `.env` file with your GROQ_API_KEY

## 💡 Tips

- Keep case descriptions concise for faster analysis
- Review all three layers for comprehensive insights
- Use settlement probability to gauge negotiation viability
- Follow the recommended action plan for best results
