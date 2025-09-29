import streamlit as st
from controller import ItemController

controller = ItemController()
st.title("Cadastro de Itens")
menu = ["Cadastrar Item", "Listar Itens"]
escolha = st.sidebar.selectbox("Menu", menu)

if escolha == "Cadastrar Item":
    st.subheader("Novo Item")
    nome = st.text_input("Nome")
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=0, step=1)
    if st.button("Salvar"):
        controller.criarItem(nome, descricao, quantidade)
        st.success("Item cadastrado com sucesso")
elif escolha == "Listar Itens":
    st.subheader("Itens Cadastrados")
    itens = controller.obterTodosOsItens()
    if itens:
        for item in itens:
            st.text(str(item))
    else:
        st.info("Nenhum item cadastrado ainda")
