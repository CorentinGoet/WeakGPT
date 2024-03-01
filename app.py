import streamlit as st
from langchain_backend import llm_request


def main():
    st.set_page_config(
        page_title="WeakGPT",
        page_icon="🤖"
    )

    st.header("WeakGPT 🤖😵‍💫")

    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_container = st.container()
    # Display chat messages
    for message in st.session_state.messages:
        with chat_container.chat_message(message["role"]):
            st.markdown(message["content"]) 
    
    
    if prompt := st.chat_input("Your message..."):
        with chat_container.chat_message("human"):
            st.markdown(prompt)
    
        # add to history
        st.session_state.messages.append({"role": "human", "content": prompt})

        with chat_container.chat_message("ai"):
            
            response = llm_request(st.session_state.messages.copy())
            st.markdown(response)
            st.session_state.messages.append({"role": "ai", "content": response})
            
            

if __name__ == '__main__':
    main()