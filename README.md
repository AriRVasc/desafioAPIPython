# Simulador de Empréstimo

Tendo a necessidade do time de parcerias de crédito, como desenvolvedora, criei uma API HTTP simuladora de empréstimo desenvolvida com FastAPI, utilizando autenticação JWT e integração com uma outra API de ofertas de empréstimos.

### Instalação
Através do GitBash:
1. Clone o repositório:
   git clone https://github.com/AriRVasc/desafioAPIPython.git
2. Navegue para o diretório do projeto:
   cd desafioAPIPython
3. Crie e ative um ambiente virtual (não é obrigatório mas recomendável, para que não haja conflitos de dependências):
   python3 -m venv env
   source env/bin/activate
4. Instale as depeências da aplicação:
   pip install -r requirements.txt

### Configuração
Para que o projeto execute será necessário configurar algumas informações:
Abra o arquivo authentication.py e altere a constante SECRET_KEY para a sua chave secreta desejada. Essa chave é usada para codificar e decodificar os tokens JWT.
No arquivo offer.py, na função get_emprestimos, altere o valor do campo "client_secret" para o valor correto. Esse campo será necessário para autenticar a API do parceiro e obter as ofertas de empréstimo.

### Uso
Para iniciar a aplicação, execute o arquivo main.py:
  python main.py

A aplicação será executada em http://localhost:8000.

Autenticação
Para autenticar e obter um token JWT, envie uma solicitação POST para http://localhost:8000/auth com os parâmetros username e password.
A resposta incluirá um campo access_token com o token JWT. Esse token deve ser incluído no cabeçalho Authorization para realizar simulações de empréstimo.

Simulação de Empréstimo
Para simular um empréstimo, envie uma solicitação GET para http://localhost:8000/emprestimo com os parâmetros da simulação (cpf, valor e parcelas) e inclua o token JWT. 
A resposta incluirá informações sobre a oferta de empréstimo adequada, se encontrada.

### Tecnologias Utilizadas
FastAPI: Um framework de desenvolvimento web em Python que permite criar APIs de forma rápida e eficiente.
Pydantic: Uma biblioteca que oferece suporte para validação e serialização de dados usando anotações de tipo Python.
JWT (JSON Web Tokens): Um método para tokenização de informações que é usado para autenticação e autorização no projeto.
requests: Uma biblioteca que permite fazer requisições HTTP para outras APIs.
cachetools: Uma biblioteca que fornece funcionalidades de cache para armazenar em cache informações de empréstimo.
uvicorn: Um servidor ASGI (Async Server Gateway Interface) de alto desempenho, usado para executar a aplicação FastAPI.

### Estrutura do Projeto
authentication.py: Contém as funções relacionadas à autenticação e geração de tokens JWT.
models.py: Define o modelo de dados Simulacao utilizando a biblioteca Pydantic.
offer.py: Contém as funções relacionadas à obtenção das ofertas de empréstimo a partir da API externa.
main.py: Arquivo principal que configura e inicia a aplicação FastAPI.
requirements.txt: Lista de dependências do projeto.








