FROM python:3.11.4-slim-buster

WORKDIR /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate