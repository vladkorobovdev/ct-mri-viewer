FROM python:3.14.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Копируем исходный код
COPY ./src /app/src

CMD ["fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
