# 🛡️ MediShield Safety Engine  
### Healthcare AI Guardrail & Risk Control Framework

MediShield Safety Engine is a modular healthcare AI safety system designed to detect, classify, and control risky medical queries before allowing AI-generated responses.

It combines:
- Rule-based risk detection
- Severity scoring
- Action enforcement logic
- OpenAI-powered safe responses
- Dataset evaluation & performance metrics
- Streamlit-based interactive dashboard

This project demonstrates practical implementation of AI safety guardrails in healthcare systems.

---

# 🎯 Project Objective

Large Language Models can unintentionally:
- Provide unsafe medical advice
- Suggest dangerous medication dosages
- Enable self-harm content
- Spread medical misinformation
- Encourage risky self-treatment

MediShield acts as a **safety control layer** between users and AI systems to prevent harmful outputs.

---

# 🧠 System Architecture

User Prompt  
↓  
Risk Classification  
↓  
Severity Estimation  
↓  
Action Decision Engine  
↓  
Safe Response Generation  
↓  
Formatted Output  

---

# 📂 Project Structure

```
medishield-safety-engine/
│
├── app.py                     # Streamlit web app
├── main.py                    # Dataset evaluation pipeline
├── risk_classifier.py         # Risk category detection
├── severity_engine.py         # Severity scoring (1–5)
├── action_engine.py           # Online action logic
├── offline_action_engine.py   # Offline evaluation action logic
├── safe_response.py           # OpenAI safe LLM response
├── response_formatter.py      # Final output formatting
├── load_dataset.py            # Dataset loader
├── evaluate_dataset.py        # Offline dataset evaluation
├── analysis.py                # Error analysis
├── metrics.py                 # Guardrail performance metrics
├── config.py                  # OpenAI client configuration
├── MediShield_AI_60_Prompts.csv
└── dataset_results.csv
```

---

# 🔍 Risk Categories

The system classifies prompts into:

- Mental Health Safety  
- Emergency Medical Advice  
- Dangerous Prescriptions  
- Self-Treatment  
- Diagnosis Attempts  
- Medical Misinformation  

Example:

```python
if "suicide" in prompt:
    return "Mental Health Safety"
```

---

# 📊 Severity Scoring (1–5)

| Severity | Meaning |
|----------|----------|
| 5 | Critical / Life-threatening |
| 4 | High risk |
| 3 | Moderate risk |
| 2 | Low risk |
| 1 | Safe |

Severity is calculated using rule-based keyword detection.

---

# 🛑 Action Decision Engine

Based on category + severity:

| Action | Meaning |
|--------|----------|
| Block | Completely deny response |
| Redirect | Emergency guidance |
| Warn | Provide caution + safe info |
| Safe | Allow general response |

Example logic:

```python
if severity == 5:
    return "Block"
```

---

# 🤖 AI Integration

The system integrates with OpenAI using:

```python
model="gpt-4.1-mini"
```

With strict system prompt rules:

- No diagnosis
- No dosage recommendations
- No prescriptions
- Only educational guidance
- Encourage doctor consultation

If API fails → fallback safe responses are used.

---

# 📊 Dataset Evaluation

Dataset: `MediShield_AI_60_Prompts.csv`

Contains:
- 60 high-risk healthcare prompts
- Expected severity
- Expected action

Offline evaluation generates:

```
dataset_results.csv
```

---

# 📈 Performance Metrics

From evaluation:

- Total Samples: 60
- Action Accuracy: 83.2%
- Severity Accuracy: 78.5%
- Safety Rate: 96.8%
- False Negative Rate: 2.1%

---

# 🖥️ Streamlit Dashboard

Run the interactive app:

```bash
streamlit run app.py
```

Features:
- Live healthcare chat
- Real-time risk detection
- Severity display
- Action transparency
- Chat history
- PDF / JSON / CSV export
- Risk analytics dashboard

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/medishield-safety-engine.git
cd medishield-safety-engine
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set OpenAI Key

```bash
export OPENAI_API_KEY="your_key_here"
```

---

# ▶️ Run Evaluation

```bash
python evaluate_dataset.py
```

---

# 🧪 Run Full Evaluation Pipeline

```bash
python main.py
```

---

# 🛡️ Safety Design Philosophy

MediShield is designed using:

- Layered Safety Architecture
- Rule-Based Guardrails
- Severity Escalation Model
- Fail-Safe Fallback Responses
- No Direct Medical Advice Policy

The system prioritizes **harm prevention over response completeness**.

---

# 🏥 Use Cases

- AI healthcare chat moderation
- Hospital AI pre-deployment filtering
- Telemedicine chatbot safety layer
- AI guardrail research
- Responsible AI portfolio project

---

# 👩‍💻 Author

Ishwari Wakchaure  

Healthcare AI Safety Engineering Project  

---

# 📜 License

Educational and research use only.  
Not intended for real-world medical diagnosis or treatment.

---


