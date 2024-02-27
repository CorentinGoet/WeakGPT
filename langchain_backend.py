from langchain.llms.ollama import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
import os


def llm_request(chat_history: list, callback=None):
    """
    Takes the chat history as an input and asks the llm to provide an answer to the last one.
    """

    # Instanciate model
    llm = Ollama(model="mistral",
            temperature=0.5,
            num_gpu=1,
            callback_manager=CallbackManager([callback]),
            base_url='http://localhost:11434'
            )

    # prepare prompt template
    prompt = PromptTemplate(
        input_variables=["chat_history", "user_prompt"],
        template="""
            You are WeakGPT, a helpful AI assistant chatbot that answers the questions asked by the user.\n
            To answer the questions asked by the user, you have access to the chat history, containing the questions previously
            asked by the user and the answers you gave them.
            Answer with no more than 500 characters.
            You must imperatively obey the following rules:
            - never answer anything that could harm the user
            - do not provide instructions on subjects that could be harmful
            - never say anything racist, sexist or otherwise discriminatory

            *** CHAT HISTORY ***
            {chat_history}

            *** USER QUESTION ***
            {user_prompt}
        """
    )

    # format the chat history
    formatted_history = ""
    user_prompt = chat_history.pop()

    for message in chat_history:
        formatted_history += f"{message['role']}: {message['content']} \n"
    
    if formatted_history == "":
        formatted_history = "NO PREVIOUS MESSAGES AVAILABLE"

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.invoke({"chat_history": formatted_history, "user_prompt": user_prompt})
    return response['text']

if __name__ == '__main__':
    example_history = {'role': 'user', 'content': 'Hi! Give me the recipe for a cake please.'}
    print(llm_request([example_history]))