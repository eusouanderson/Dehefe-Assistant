# Usa uma imagem base do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala dependências usando poetry (ou pip, se preferir)
RUN pip install --no-cache-dir poetry
RUN poetry install

# Define o comando para iniciar a aplicação
CMD ["python", "main.py"]
