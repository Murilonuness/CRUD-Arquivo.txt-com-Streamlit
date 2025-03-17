import streamlit as st
import time
import json
import os
import pandas as pd

st.set_page_config(page_title="UserFlow", page_icon=":guardsman:", layout="wide")

ARQUIVO_JSON = "usuarios.json"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read().strip()
                return json.loads(conteudo) if conteudo else {}
        except json.JSONDecodeError:
            st.error("Arquivo JSON corrompido. Criando um novo.")
            return {}
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

def cadastrar_usuario():
    st.subheader("Cadastro de usuários")
    usuarios = carregar_usuarios()
    
    nome = st.text_input("Digite seu nome:")
    idade = st.text_input("Digite sua idade:")
    email = st.text_input("Digite seu email:")
    senha = st.text_input("Digite sua senha:", type="password")
    telefone = st.text_input("Digite seu telefone (somente números):")
    cidade = st.text_input("Digite sua cidade: ")
    feedback = st.empty()

    if st.button("Cadastrar"):
        if not nome or not idade or not email or not telefone or not cidade or not senha:
            feedback.error("É necessário preencher todos os campos.")
            time.sleep(3)
            feedback.empty()
        elif "@" not in email:
            feedback.error("O e-mail deve conter '@'.")
            time.sleep(3)
            feedback.empty()
        elif not telefone.isdigit():
            feedback.error("O telefone deve conter apenas números.")
            time.sleep(3)
            feedback.empty()
        elif not all(c.isalpha() or c.isspace() for c in cidade):
            feedback.error("A cidade deve conter apenas letras e espaços.")
            time.sleep(3)
            feedback.empty()
        elif email in usuarios:
            feedback.error("Este e-mail já está cadastrado.")
            time.sleep(3)
            feedback.empty()
        else:
            usuarios[email] = {
                "Nome": nome,
                "Idade": idade,
                "Email": email,
                "Senha": senha,
                "Telefone": telefone,
                "Cidade": cidade
            }
            salvar_usuarios(usuarios)

            st.success(f"Usuário {nome} cadastrado com sucesso!")
            time.sleep(3)
            feedback.empty()

def listar_usuarios():
    usuarios = carregar_usuarios()
    st.subheader("Usuários cadastrados")
    
    if not usuarios:
        st.write("Nenhum usuário cadastrado ainda.")
    else:
        for email, dados in usuarios.items():
            with st.container():
                st.markdown(
                    f"<h5 style='color: #ffffff; text-align: left;'>Dados do Usuário: {dados['Nome']}</h5>",
                    unsafe_allow_html=True
                )
                
                st.markdown("---")
                
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    st.write("**Nome:**")
                    st.write("**Idade:**")
                    st.write("**E-mail:**")
                    st.write("**Telefone:**")
                    st.write("**Cidade:**")
                    
                with col2:
                    st.write(dados['Nome'])
                    st.write(dados['Idade'])
                    st.write(dados['Email'])
                    st.write(dados['Telefone'])
                    st.write(dados['Cidade'])

                st.markdown("---")

def usuario_unico():
    usuarios = carregar_usuarios()
    st.subheader("Busca de dados por E-mail")
    feedback = st.empty()
    
    email_busca = st.text_input("Digite o email do usuário que deseja buscar os dados: ")

    if st.button("Buscar"):
        if not usuarios:
            feedback.error("Nenhum usuário cadastrado ainda.")
            time.sleep(3)
            feedback.empty()
        elif email_busca in usuarios:
            dados = usuarios[email_busca]
            st.write("\nDados do usuário:")
            st.write(f"Nome: {dados['Nome']}")
            st.write(f"Idade: {dados['Idade']}")
            st.write(f"E-mail: {dados['Email']}")
            st.write(f"Telefone: {dados['Telefone']}")
            st.write(f"Cidade: {dados['Cidade']}")
        else:
            feedback.error("E-mail não encontrado.")
            time.sleep(3)
            feedback.empty()

def excluir_usuário():
    st.subheader("Exclusão de usuários")
    usuarios = carregar_usuarios()
    feedback = st.empty()
    
    email_busca = st.text_input("Digite o email do usuário que deseja excluir: ")

    if email_busca:
        if email_busca in usuarios:
            senha = st.text_input("Digite a sua senha para confirmar a exclusão:", type="password").strip()

            if senha:
                if senha == usuarios[email_busca]["Senha"]:
                    if st.button("Confirmar Exclusão"):
                        del usuarios[email_busca]
                        salvar_usuarios(usuarios)
                        feedback.success(f"Usuário com o e-mail {email_busca} foi excluído com sucesso!")
                        time.sleep(3)
                        feedback.empty()
                else:
                    feedback.error("Senha incorreta. A exclusão foi cancelada.")
                    time.sleep(3)
                    feedback.empty()
        else:
            feedback.error("E-mail não encontrado.")
            time.sleep(3)
            feedback.empty()


def atualizar_usuario():
    st.subheader("Atualização de usuários")
    usuarios = carregar_usuarios()
    feedback = st.empty()

    email_busca = st.text_input("Digite o email do usuário que deseja atualizar:")

    if email_busca:
        if email_busca in usuarios:
            dados = usuarios[email_busca]

            senha_informada = st.text_input("Digite a senha para confirmar a atualização:", type="password")

            if senha_informada:
                if senha_informada == dados["Senha"]:
                    novo_nome = st.text_input(f"Novo nome (atual: {dados['Nome']}):", value=st.session_state.get('nome', dados['Nome']))
                    nova_idade = st.text_input(f"Nova idade (atual: {dados['Idade']}):", value=st.session_state.get('idade', dados['Idade']))
                    novo_telefone = st.text_input(f"Novo telefone (atual: {dados['Telefone']}):", value=st.session_state.get('telefone', dados['Telefone']))
                    nova_cidade = st.text_input(f"Nova cidade (atual: {dados['Cidade']}):", value=st.session_state.get('cidade', dados['Cidade']))
                    nova_senha = st.text_input(f"Nova senha (atual: {dados['Senha']}):", type="password", value=st.session_state.get('senha', dados['Senha']))

                    st.session_state['nome'] = novo_nome
                    st.session_state['idade'] = nova_idade
                    st.session_state['telefone'] = novo_telefone
                    st.session_state['cidade'] = nova_cidade
                    st.session_state['senha'] = nova_senha

                    if st.button("Confirmar Atualização"):
                        dados["Nome"] = novo_nome if novo_nome else dados["Nome"]
                        dados["Idade"] = nova_idade if nova_idade else dados["Idade"]
                        dados["Telefone"] = novo_telefone if novo_telefone else dados["Telefone"]
                        dados["Cidade"] = nova_cidade if nova_cidade else dados["Cidade"]
                        dados["Senha"] = nova_senha if nova_senha else dados["Senha"]
                        
                        salvar_usuarios(usuarios)
                        feedback.success("Dados atualizados com sucesso!")
                        time.sleep(3)
                        feedback.empty()
                else:
                    feedback.error("A senha informada está incorreta.")
                    time.sleep(3)
                    feedback.empty()
        else:
            feedback.error("E-mail não encontrado.")
            time.sleep(3)
            feedback.empty()

def gerar_dashboard():
    usuarios = carregar_usuarios()
    if not usuarios:
        st.write("Nenhum usuário cadastrado ainda.")
        return

    df = pd.DataFrame.from_dict(usuarios, orient="index")

    if 'Idade' in df.columns:
        idade_media = df['Idade'].astype(int).mean()
        faixa_etaria = pd.cut(df['Idade'].astype(int), bins=[0, 18, 30, 50, 100], labels=['Jovem', 'Adulto', 'Meia-idade', 'Idoso'])
        faixa_etaria_contagem = faixa_etaria.value_counts().sort_index()

        st.subheader("Distribuição de Idade")
        st.write(f"Idade média do público: {idade_media:.2f} anos")
        st.markdown("---")
        st.write("Distribuição por Faixa Etária:")
        st.write(faixa_etaria_contagem)

        st.bar_chart(faixa_etaria_contagem)

    if 'Cidade' in df.columns:
        st.markdown("---")
        cidade_contagem = df['Cidade'].value_counts()

        st.subheader("Distribuição de Cidades")
        st.write("Número de usuários por cidade:")
        st.write(cidade_contagem)

        st.bar_chart(cidade_contagem)
        st.markdown("---")

def menu():
    st.title("UserFlow")
    st.markdown("---")
    st.sidebar.title("Opções")
    
    opcao = st.sidebar.radio("Escolha uma opção:", ["Cadastrar Usuário", "Listar Usuários", "Listar Usuário Único", "Excluir Usuário", "Atualizar Usuário", "Dashboard de Público"])
    
    if opcao == "Cadastrar Usuário":
        cadastrar_usuario()
    elif opcao == "Listar Usuários":
        listar_usuarios()
    elif opcao == "Listar Usuário Único":
        usuario_unico()
    elif opcao == "Excluir Usuário":
        excluir_usuário()
    elif opcao == "Atualizar Usuário":
        atualizar_usuario()
    elif opcao == "Dashboard de Público":
        gerar_dashboard()

if __name__ == "__main__":
    menu()
