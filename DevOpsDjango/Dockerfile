# Используем официальный Python образ как базу
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY reqs.txt .

RUN pip install --upgrade pip && pip install -r reqs.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
