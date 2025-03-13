# CRUD com Arquivo de Texto

Este projeto implementa um CRUD utilizando Streamlit, onde é possível realizar as operações de Cadastro, Atualização e Exclusão de usuários. Os dados são armazenados em um arquivo `.txt`, e as manipulações de dados acontecem por meio de listas e arquivos de texto, demonstrando habilidades em manipulação de dados e a integração com páginas web usando Streamlit.

## Funcionalidades
- **Cadastro de Usuário**: O usuário pode cadastrar seu nome, e-mail e telefone. O e-mail é utilizado como identificador único.
- **Atualização de Dados**: O usuário pode atualizar seu nome, e-mail ou telefone com base no e-mail cadastrado.
- **Exclusão de Usuário**: O usuário pode excluir seu cadastro informando o e-mail.

## Tecnologias Usadas
- **Streamlit**: Framework para criação de interfaces web interativas e fáceis de usar em Python.
- **Manipulação de Arquivo .txt**: Os dados são salvos e manipulados em um arquivo `.txt`.
- **Python**: Lógica de programação utilizando listas, controle de fluxo (condicionais), loops e manipulação de arquivos.

## Como Usar
1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```
2. Instale as dependências do Streamlit:
    ```bash
    pip install streamlit
    ```
3. Execute o arquivo principal do Streamlit:
    ```bash
    streamlit run app.py
    ```

4. Acesse a interface em **http://localhost:8501** para realizar o Cadastro, Atualização e Exclusão de usuários.

## Funcionalidade do CRUD
- **Cadastro**:
  - O usuário informa seu nome, e-mail e telefone.
  - O sistema verifica se o e-mail já está cadastrado e, se não, o adiciona ao arquivo `.txt`.
- **Atualização**:
  - O usuário pode atualizar seus dados fornecendo o e-mail registrado e novos valores para o nome, e-mail ou telefone.
- **Exclusão**:
  - O usuário pode excluir seu cadastro, informando seu e-mail. O sistema remove os dados do arquivo.

## Estrutura do Código
- **app.py**: Este arquivo contém a implementação das funções do CRUD. Ele é responsável por:
  - Realizar o cadastro, verificação e armazenamento de dados em arquivo.
  - Permitir a atualização de dados já cadastrados.
  - Excluir dados com base no e-mail do usuário.
  - Utilizar Streamlit para a interface web.
- **usuarios.txt**: Este arquivo armazena os dados dos usuários em formato texto. Cada usuário é registrado com seu nome, e-mail e telefone.

## Exemplo de Dados no Arquivo `usuarios.txt`
    Nome: João
    E-mail: joao@example.com
    Telefone: 123456789
    Nome: Maria
    E-mail: maria@example.com
    Telefone: 987654321

## Deploy
O projeto está disponível para uso público. Você pode acessar a versão online do CRUD [aqui](https://crud-arquivo-txt-com-streamlit.onrender.com).

## Preview
Veja uma captura de tela da interface abaixo:

![Preview da Interface](/media/preview.jpg)

## Contribuindo
Sinta-se à vontade para contribuir para este projeto! Se encontrar algum problema ou quiser adicionar melhorias, por favor, abra uma issue ou envie um pull request. Você pode ver mais sobre meus projetos e contribuições em meu perfil no [GitHub](https://github.com/Murilonuness).

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
