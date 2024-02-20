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

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Your message..."):
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # add to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = llm_request(st.session_state.messages.copy())
        with st.chat_message("assistant"):
            st.markdown(response)
            # for chat-gpt style use st.write_stream
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == '__main__':
    main()