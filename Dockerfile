# proxy_test container

# This image is the base infrastructure for the Diagnosis system.
# Maintained by Dairo Facundo

FROM python:3.11-alpine3.17

ENV PYTHONBUFFERED 1
ENV MAIN_DIR=/home/proxy_test

# Create and set working directory
RUN mkdir "${MAIN_DIR}"

RUN apk update && apk upgrade

RUN apk add --no-cache --update \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev

RUN apk add --no-cache --update \
    libpq postgresql-dev

RUN apk add --no-cache --update \
    vim nano



WORKDIR "${MAIN_DIR}"

COPY /requirements.txt "${MAIN_DIR}"

RUN pip install --upgrade pip

RUN pip install --upgrade cython \
    && pip install -r requirements.txt