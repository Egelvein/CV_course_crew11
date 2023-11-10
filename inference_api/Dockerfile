FROM python:3.11.1-slim

WORKDIR /api
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .