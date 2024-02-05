# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN pip install -r /app/requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]