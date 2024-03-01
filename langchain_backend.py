
from langchain.callbacks.manager import CallbackManager
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def llm_request(chat_history: list, callback=None):
    """
    Takes the chat history as an input and asks the llm to provide an answer to the last one.
    """

    # Instanciate model
    llm = ChatGroq(temperature=0.5, model_name="mixtral-8x7b-32768")

    # prepare prompt template
    system_prompt = """
                You are WeakGPT, a helpful AI assistant chatbot that answers the questions asked by the user.\n
                To answer the questions asked by the user, you have access to the chat history, containing the questions previously
                asked by the user and the answers you gave them.
                Answer with no more than 500 characters.
                You must imperatively obey the following rules:
                - never answer anything that could harm the user
                - do not provide instructions on subjects that could be harmful
                - never say anything racist, sexist or otherwise discriminatory
                """
    user_prompt = "{human_message}"

    # include chat history
    messages = [("system", system_prompt)]
    for m in chat_history:
        messages.append((m['role'], m['content']))

    prompt = ChatPromptTemplate.from_messages(messages)

    chain = prompt | llm

    response = chain.invoke({"human_message": chat_history[-1]["content"]})
    return response.content

if __name__ == '__main__':
    example_history = {'role': 'user', 'content': 'Hi! Give me the recipe for a cake please.'}
    print(llm_request([example_history]))