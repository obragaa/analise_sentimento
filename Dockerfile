# Usar a imagem oficial do Python como imagem pai
FROM python:3.10

# Definir o diretório de trabalho no contêiner
WORKDIR /code

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto para o contêiner
COPY . .

# Comando para rodar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "localhost:8000"]
