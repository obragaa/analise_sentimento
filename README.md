# Analisador de Sentimentos

Este projeto é um analisador de sentimentos construído com Django, que permite aos usuários inserir um texto para análise de sentimentos. Utiliza a API da OpenAI para realizar análises complexas e apresentar um feedback mais detalhado sobre o sentimento do texto inserido. O projeto também é configurado para rodar em containers Docker, facilitando a implantação e a portabilidade.

## Pré-requisitos

Para executar este projeto, você precisará ter instalado em sua máquina:
```
- Python 3.8 ou superior
- Docker e Docker Compose
- Uma c
have de API da OpenAI (para análise de sentimentos usando GPT)
```
## Configuração do Ambiente

### Clone o Repositório

```bash
git clone https://seu-repositorio.git
cd seu-repositorio
```

### Configuração do Docker

Crie um arquivo `Dockerfile` na raiz do seu projeto e um `docker-compose.yml` para configurar os serviços necessários.

### Variáveis de Ambiente

Defina as seguintes variáveis de ambiente no seu sistema ou diretamente no `docker-compose.yml`:

- `OPENAI_API_KEY`: Sua chave de API da OpenAI.

## Execução

Para construir e iniciar o projeto usando Docker, execute:

```bash
docker-compose up --build
```

Isso irá instalar todas as dependências necessárias e iniciar o servidor Django.

## Uso

Acesse `http://localhost:8000` no seu navegador para interagir com a aplicação. Você pode realizar análises de sentimentos inserindo textos na interface provida pela aplicação.

## Estrutura do Projeto

- `analisador/`: Aplicação Django principal, contendo as views, models e templates.
- `docker-compose.yml`: Configuração do Docker Compose para orquestrar containers.
- `Dockerfile`: Instruções para construir a imagem Docker do projeto.

## Contribuição

Sua contribuição é bem-vinda! Por favor, consulte `CONTRIBUTING.md` para mais detalhes sobre como contribuir para este projeto.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes.

## Agradecimentos

- OpenAI, pelo fornecimento da API que potencializa a análise de sentimentos.
- Toda a comunidade Django, pelo suporte e recursos.

## Imagem final desse projeto

![Screenshot at 2024-04-10 15-24-57](https://github.com/obragaa/analise_sentimento/assets/60896979/b503ebc9-7e06-4d77-80ac-fcbc77f1a169)
