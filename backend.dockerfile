FROM python:3.9.4-slim

COPY ./backend/. app/
COPY .env .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
COPY ./backend/requirements.txt /app/requirements.txt

WORKDIR app
ENV PYTHONPATH=.
RUN pip install -r requirements.txt
RUN python -m uvicorn main:app_main --reload --host 0.0.0.0
