FROM python:3.11.2-slim-buster

# Metadata
LABEL name="Library API"
LABEL maintainer="scjorge"
LABEL version="0.1"

# Env Sets
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Project Python definition
RUN mkdir /web
WORKDIR /web
COPY . .

# Install python dependencies
RUN apt update && apt-get install gcc -y
RUN pip install -r requirements.txt

# Set directories project
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser web
RUN chown -R web:web /vol
RUN chmod -R 755 /vol/web
RUN chmod -R 755 /web

USER web
