# 🚀 LinkedIn Post Generator with Few-Shot Learning

An AI-powered LinkedIn Post Generator built with **Streamlit**, **LangChain**, and **Groq**. It leverages **few-shot prompting** based on real, high-performing posts to craft contextual, authentic LinkedIn content in both **English** and **Hinglish**.

---

## ✨ Features

- 🎯 **Few-Shot Learning Engine**: Learns tone, formatting, and hooks from curated past posts stored in `data/processed_posts.json`.
- 🌐 **Multilingual Support**: Generate posts in clean **English** or conversational **Hinglish** (Hindi + English blend).
- 📏 **Dynamic Lengths**:
  - **Short**: 1–5 lines (punchy quick takes, polls, observations)
  - **Medium**: 6–10 lines (tips, industry insights, mini-stories)
  - **Long**: 11–15 lines (deep dives, case studies, career journeys)
- ⚡ **Ultra-Fast LLM Inference**: Powered by Groq for near-instant responses.
- 🎨 **Clean Interactive Web UI**: Built with Streamlit for a fast and frictionless user experience.
- 🔄 **Automated Tag & Post Preprocessor**: Script included (`processed.py`) to parse, tag, and unify raw post archives.

---

## 🏗️ Architecture

```
├── data/
│   ├── raw_posts.json          # Raw input posts
│   └── processed_posts.json    # Enriched posts with line counts, tags & language
├── .env.example                # Template for environment variables
├── .gitignore                  # Prevents secrets and cache from being tracked
├── few_shots.py                # Few-shot sample retriever and category filter
├── llm_helper.py               # Groq LLM client setup
├── main.py                     # Streamlit frontend application
├── post_generator.py           # Prompt engineering and post synthesis
├── processed.py                # Pipeline to extract tags & metadata
└── requirements.txt            # Python dependencies
```

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Minimocoding/linkedin-post-generator.git
cd linkedin-post-generator
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and add your **Groq API Key** (get one free at [console.groq.com](https://console.groq.com/keys)):
   ```env
   GROQ_API_KEY=gsk_your_groq_api_key_here
   ```

### 5. Launch the App
```bash
streamlit run main.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 🧠 How the Few-Shot Engine Works

1. **Tag & Length Filtering**: When you select a topic, length, and language, [`few_shots.py`](few_shots.py) queries the indexed dataset (`data/processed_posts.json`).
2. **Context Injection**: Relevant matching posts are injected into the prompt as structural examples for the model.
3. **Generation**: Groq produces a fresh post that adopts the formatting, pacing, and vocabulary of top-performing content without copying.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
