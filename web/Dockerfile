###########
# BUILDER #
###########

FROM python:3.11.2-slim-buster as builder

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt update && apt install -y\
    gcc \
    libpq-dev \
    libffi-dev \
    build-essential \
    python3-dev
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

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

# Install dependencies
RUN apt update && apt install -y \
    libpq-dev \
    vim \
    git

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*
RUN rm -r /wheels

# Create directories project
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# chown all the files to the app user
RUN adduser django
RUN chown -R django:django /vol
RUN chown -R django:django /web
RUN chmod -R 755 /vol/web
RUN chmod -R 755 /web

# change to the django user
USER django
