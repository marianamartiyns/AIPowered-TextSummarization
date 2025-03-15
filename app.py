import streamlit as st
from langchain_deepseek import ChatDeepSeek
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import os

# Carregar variáveis do ambiente
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

def generate_response(txt):

    # Instanciar o modelo LLM com a chave da DeepSeek
    llm = ChatDeepSeek(model="deepseek-chat", temperature=0, max_tokens=None, timeout=None, max_retries=2, api_key=deepseek_api_key)
    #llm = ChatDeepSeek(temperature=0, api_key="deepseek_api_key")

    # Dividir o texto
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(txt)
    
    # Criar múltiplos documentos
    docs = [Document(page_content=t) for t in texts]
    
    # Resumir o texto
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    return chain.run(docs)

# Título da página
st.set_page_config(page_title='🦜🔗 Text Summarization App')
st.title('🦜🔗 Text Summarization App')

# Entrada de texto
txt_input = st.text_area('Enter your text', '', height=200)

# Formulário para entrada do usuário
result = []
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted and txt_input:
        with st.spinner('Calculating...'):
            response = generate_response(txt_input)
            result.append(response)

if len(result):
    st.info(response)