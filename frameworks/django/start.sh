#!/bin/sh

cd ..
/usr/local/bin/python -m pip install --upgrade pip
/usr/local/bin/gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8080 app.app:app
