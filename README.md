# WeakGPT

Vulnerable LLM chatbot  used to demo prompt injections
This chatbot is built in Python using:
- [LangChain](https://www.langchain.com/) for the Python backend
- [StreamLit](https://streamlit.io/) for the web UI
- [Ollama](https://ollama.com/) & [Mistral](https://mistral.ai/) for the LLM

## Installation

### LLM

**Warning**: Ollama can only run on Linux and MacOS for now, this will not work on Windows!

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download the model (you can change to the model you want, I used Mistral7B)

**Warning**: Depending on the model you choose, this may take a while (4 GB for Mistral 7B).
```bash
ollama pull mistral:latest
```

Install the required libraries in Python.

```bash
pip install streamlit langchain 
```

## Run the app

Launch the streamlit service:

```bash
python3 -m streamlit run app.py
```


