FROM python:3.12-slim

# Добавляем группу и пользователя
RUN groupadd -r groupdjango && useradd -r -g groupdjango userdj

# Устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Обновляем пакеты и устанавливаем зависимости для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app/www/siteauto

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальные файлы
COPY . .

# Устанавливаем пользователя
# Для разработки с volume mount лучше оставаться root, чтобы избежать проблем с правами доступа
# USER userdj