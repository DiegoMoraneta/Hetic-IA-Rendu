import streamlit as st
from dotenv import load_dotenv
from cloud_utils import get_pdfs_from_s3
from langchain.chat_models import ChatOpenAI
from rag_utils import get_vectorstore, get_conversation_chain, get_text_chunks, get_pdf_text
from htmlTemplates import css, bot_template, user_template

def handle_userinput(user_question, use_rag=True):
    if use_rag and st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
    else:
        llm = ChatOpenAI()
        response = {'chat_history': [{"content": llm(user_question)}]}
    
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Discutez avec plusieurs PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Discutez avec plusieurs PDFs :books:")

    # Téléchargement depuis le cloud ou local
    use_cloud = st.sidebar.checkbox("Télécharger les fichiers depuis le cloud (S3)")
    bucket_name = ""
    pdf_docs = []

    if use_cloud:
        bucket_name = st.sidebar.text_input("Nom du bucket S3")
        if st.sidebar.button("Télécharger les documents"):
            with st.spinner("Téléchargement des documents depuis S3..."):
                pdf_docs = get_pdfs_from_s3(bucket_name)
    else:
        pdf_docs = st.file_uploader("Chargez vos fichiers PDF ici", accept_multiple_files=True)

    # Paramètre de température
    temperature = st.sidebar.slider("Température (créativité des réponses)", 0.0, 1.0, 0.7)

    if st.button("Traiter"):
        with st.spinner("Traitement des documents PDF..."):
            raw_text = get_pdf_text(pdf_docs)
            text_chunks = get_text_chunks(raw_text)
            vectorstore = get_vectorstore(text_chunks)
            st.session_state.conversation = get_conversation_chain(vectorstore, temperature)

    # Chatbot
    user_question = st.text_input("Posez une question :")
    if user_question:
        use_rag = st.checkbox("Activer RAG")
        handle_userinput(user_question, use_rag=use_rag)

if __name__ == "__main__":
    main()
