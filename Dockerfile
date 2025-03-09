# python:3.9-slim или новее
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Задаем переменную окружения (можно переопределить при запуске)
ARG BOT_TOKEN
ENV BOT_TOKEN=${BOT_TOKEN}

# Запускаем бота
CMD ["python", "main.py"]