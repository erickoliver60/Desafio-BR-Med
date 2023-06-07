# Desafio-BR-Med

## Instalação

- Instalar no venv os pacotes definidos no requirements.txt:

```pip install -r requirements.txt```

- Preparando o banco e as migrações:

```python manage.py makemigrations```

```python manage.py migrate```

- Coletando arquivos estáticos usados no projeto

```python manage.py collectstatic```

- Rodar o servidor:

```python manage.py runserver```

## Acessando a API:

- API:

```http://127.0.0.1:8000/```
