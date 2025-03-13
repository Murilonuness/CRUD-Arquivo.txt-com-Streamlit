import streamlit as st
import time

def apresentacao():
    st.title('Crud com arquivo.txt')
    st.write('Aqui vamos integrar um CRUD básico para mostrar minhas habilidades manipulando dados de um arquivo.txt')

apresentacao()
st.markdown('----')

def cadastro_usuarios(nome, email, telefone):
    try:
        with open("usuarios.txt", "r", encoding="UTF8") as arquivo: 
            dados = arquivo.readlines()
    except FileNotFoundError:
        dados = []

    for linha in dados:
        if linha.strip() == f'E-mail: {email}':
            feedback.error("Usuário já cadastrado. Tente outro e-mail.")
            time.sleep(3)
            feedback.empty()
            return

    with open("usuarios.txt", "a", encoding="UTF8") as arquivo:
        arquivo.write(f'Nome: {nome}\nE-mail: {email}\nTelefone: {telefone}\n')

    feedback.success('Usuário cadastrado com sucesso.')
    time.sleep(3)
    feedback.empty()

st.title("Cadastro de Usuário")
st.write('Em baixo você pode se cadastrar utilizando um e-mail válido. Todos os dados são obrigatórios!')

nome = st.text_input("Nome")
email = st.text_input("E-mail")
telefone = st.text_input("Telefone")
feedback = st.empty()

if st.button("Cadastrar"):
    if not email or not telefone or not nome:
        feedback.error("Dados insuficientes, preencha todos os campos.")
        time.sleep(3)
        feedback.empty()
    elif not telefone.isdigit():
        feedback.error("Digite apenas números no campo de telefone.")
        time.sleep(3)
        feedback.empty()
    elif '@' not in email:
        feedback.error("É obrigatório ter um e-mail que contenha '@'!")
        time.sleep(3)
        feedback.empty()
    else:
        cadastro_usuarios(nome, email, telefone)

st.markdown('----')

def atualizar_usuario():    
    st.title('Atualizar Usuário')
    st.write('Aqui você pode atualizar seus dados pelo e-mail cadastrado')

    emailBusca = st.text_input("Digite o e-mail cadastrado anteriormente")
    email = st.text_input("Novo e-mail")
    nome = st.text_input("Novo nome")
    telefone = st.text_input("Novo telefone")
    feedback = st.empty()

    if st.button("Atualizar"):
        if not email or not nome or not telefone or not emailBusca:
            feedback.error('Todos os dados são obrigatórios.')
            time.sleep(3)
            feedback.empty()
        elif '@' not in email or '@' not in emailBusca:
            feedback.error('É necessário preencher os dados de e-mail, além de conter "@" no e-mail.')
            time.sleep(3)
            feedback.empty()
        elif not telefone.isdigit():
            feedback.error('É necessário preencher o campo de telefone apenas com números')
            time.sleep(3)
            feedback.empty()
        else:
            with open('usuarios.txt', 'r', encoding='UTF8') as arquivo:
                dados = arquivo.readlines()
                encontrado = False

            for listaAtual in range(len(dados)):
                if dados[listaAtual].strip() == f'E-mail: {emailBusca}':
                    dados[listaAtual] = f'E-mail: {email}\n'
                    dados[listaAtual - 1] = f'Nome: {nome}\n'
                    dados[listaAtual + 1] = f'Telefone: {telefone}\n'
                    encontrado = True
                    break

            if encontrado:
                with open('usuarios.txt', 'w', encoding='UTF8') as arquivo:
                    arquivo.writelines(dados)
                feedback.success('Dados atualizados com sucesso!')
                time.sleep(3)
                feedback.empty()
            else:
                feedback.error('Usuário não encontrado. A atualização não foi realizada.')
                time.sleep(3)
                feedback.empty()
atualizar_usuario()
st.markdown('----')

def excluir_usuario():
    try:
        with open("usuarios.txt", "r", encoding="UTF8") as arquivo:
            dados = arquivo.readlines()
    except FileNotFoundError:
        dados = []

    st.title("Exclusão de Usuário")
    st.write("A seguir você pode excluir seu cadastro em nosso sistema")

    emailBusca = st.text_input("Digite o e-mail cadastrado anteriormente", key="excluir_email")
    feedback = st.empty()

    if st.button("Excluir"):
        if not emailBusca:
            feedback.error("Preencha o e-mail para excluir.")
            time.sleep(3)
            feedback.empty()
            return

        if '@' not in emailBusca:
            feedback.error("O e-mail deve conter '@'!")
            time.sleep(3)
            feedback.empty()
            return

        encontrado = False
        novo_dados = []

        for i in range(0, len(dados), 3):
            nome = dados[i].strip()
            email = dados[i + 1].strip()
            telefone = dados[i + 2].strip()

            if email == f"E-mail: {emailBusca}":
                encontrado = True
                continue
            else:
                novo_dados.append(nome + "\n")
                novo_dados.append(email + "\n")
                novo_dados.append(telefone + "\n")

        if encontrado:
            with open("usuarios.txt", "w", encoding="UTF8") as arquivo:
                arquivo.writelines(novo_dados)
            feedback.success("Usuário excluído com sucesso.")
        else:
            feedback.error("Usuário não encontrado.")

        time.sleep(3)
        feedback.empty()
excluir_usuario()
st.markdown('----')