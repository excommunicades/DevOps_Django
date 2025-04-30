# Используем официальный Python образ как базу
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей
COPY reqs.txt .

# Устанавливаем pip и зависимости
RUN pip install --upgrade pip && pip install -r reqs.txt

# Копируем остальные файлы
COPY . .

# Создаем директорию для статики и даем на нее права
RUN mkdir -p /app/staticfiles && chmod -R 777 /app/staticfiles

# Выполняем команду collectstatic с подробным выводом
RUN python manage.py collectstatic --noinput --verbosity 3

EXPOSE 8000

# Запуск приложения через gunicorn
CMD ["uvicorn", "DevOpsDjango.wsgi:application", "--host", "0.0.0.0", "--port", "8000"]
