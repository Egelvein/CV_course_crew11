FROM python:3.10.0-alpine

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt .
RUN pip install -r requirements.txt
RUN celery -A .  worker -l info --concurrency=2 --without-gossip --pool=solo

COPY . .