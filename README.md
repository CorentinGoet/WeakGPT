# WeakGPT

Vulnerable LLM chatbot  used to demo prompt injections
This chatbot is built in Python using:
- [LangChain](https://www.langchain.com/) for the Python backend
- [StreamLit](https://streamlit.io/) for the web UI
- [Groq](https://groq.com/) & [Mistral](https://mistral.ai/) for the LLM

## Installation

Get an API key from Groq:

- Go to https://console.groq.com/keys, create a free account
- Create an API key
- Write your API key to a `.env`file:
```bash
echo "GROQ_API_KEY=<your API key>" > .env
```

Install the required libraries in Python.

```bash
pip install streamlit langchain langchain-groq python-dotenv
```

## Run the app

Launch the streamlit service:

```bash
python3 -m streamlit run app.py
```


