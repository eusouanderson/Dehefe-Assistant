FROM python:3.12.0-slim-buster

WORKDIR /app

#Usando poetry 
RUN pip install poetry
COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD ["python", "main.py"]

EXPOSE 5000
