# Analisador de Sentimentos com Django

## Visão Geral

Este projeto é uma aplicação web desenvolvida com o framework Django, que oferece uma interface para análise de sentimentos de textos inseridos pelos usuários. Utilizando a biblioteca `TextBlob` em conjunto com `Googletrans`, o sistema é capaz de determinar a natureza do sentimento expresso no texto (positivo, negativo ou neutro) e traduzir textos não ingleses para inglês antes da análise, garantindo uma avaliação mais precisa.

## Funcionalidades

- **Análise de Sentimento**: Permite aos usuários submeter textos para análise e receber como resposta a natureza do sentimento expresso.
- **Tradução Automática**: Textos em línguas diferentes do inglês são automaticamente traduzidos para garantir a eficácia da análise.
- **Autenticação de Usuários**: Sistema de login/logout para gestão de sessões de usuários.
- **Histórico de Análises**: Os resultados das análises são salvos e podem ser consultados pelo usuário.

## Tecnologias Utilizadas

- **Backend**: Django, TextBlob, Googletrans
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (padrão do Django para projetos em desenvolvimento)
- **Conteinerização**: Docker (opcional)

## Pré-requisitos

- Python 3.8+
- Pip
- Virtualenv (opcional)
- Docker e Docker Compose (opcional)

## Configuração do Ambiente

### Clone o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_PROJETO>
```

### Ambiente Virtual

Recomenda-se a criação de um ambiente virtual para instalação das dependências:

```bash
python -m venv env
source env/bin/activate
```

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Configurações Iniciais

Aplicar as migrações do Django para configurar o banco de dados:

```bash
python manage.py migrate
```

Criar um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

## Execução

### Servidor Django

Para executar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

### Docker (Opcional)

Para construir e rodar o aplicativo usando Docker:

```bash
docker-compose up --build
```

## Acesso ao Aplicativo

Após iniciar o servidor, acesse `http://localhost:8000` no navegador para interagir com a aplicação.

## Estrutura do Projeto

Detalhes sobre a organização dos diretórios e arquivos principais.

## Contribuição

Instruções para contribuir com o projeto, incluindo convenções de codificação, testes e processo de pull request.

## Licença

Detalhes da licença sob a qual o projeto é disponibilizado, por exemplo, MIT.

## Agradecimentos

Agradecimentos à comunidade open-source e a todos que contribuíram para o projeto.

## Imagem final desse projeto

![Screenshot at 2024-04-10 15-24-57](https://github.com/obragaa/analise_sentimento/assets/60896979/b503ebc9-7e06-4d77-80ac-fcbc77f1a169)
