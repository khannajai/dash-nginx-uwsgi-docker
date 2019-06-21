FROM tiangolo/uwsgi-nginx-flask:python3.6
LABEL maintainer="maintainer"

COPY requirements.txt /tmp/
COPY ./app /app

RUN pip install -U pip && pip install -r /tmp/requirements.txt

ENV NGINX_WORKER_PROCESSES auto