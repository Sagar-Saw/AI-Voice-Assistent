# AI Voice Assistant

A voice assistant that supports both English and Hindi language.

# Features
- Voice input via microphone
- AI responses using Groq (LLaMA 3.1)
- Text to speech output
- Streamlit web interface

# Requirements
- Python 3.10 or above
- Groq API key

# Setup

1. Clone the repository
   git clone your-repo-url

2. Create virtual environment
   python -m venv venv

3. Activate virtual environment
   venv\Scripts\activate

4. Install dependencies
   pip install -r requirements.txt

5. Create .env file
   Copy .env.example and rename it to .env
   Add your Groq API key inside it

# Run

Terminal version
   python main.py

Web UI version
   streamlit run ui.py