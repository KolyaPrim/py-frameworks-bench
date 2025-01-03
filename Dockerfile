FROM python:3.10-slim


RUN apt-get update && \
    apt-get -y install --no-install-recommends build-essential

ENV PIP_DISABLE_PIP_VERSION_CHECK=0

RUN /usr/local/bin/pip install --no-cache-dir \
    wheel \
    gunicorn \
    orjson \
    ujson \
    uvicorn[standard]

ONBUILD COPY requirements.txt /app/requirements.txt
ONBUILD RUN /usr/local/bin/python -m pip install --upgrade pip && \
    /usr/local/bin/pip install --no-cache-dir -r requirements.txt
ONBUILD COPY . /app

EXPOSE 8080
WORKDIR /app
