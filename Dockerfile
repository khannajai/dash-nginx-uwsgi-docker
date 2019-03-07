FROM tiangolo/uwsgi-nginx-flask:python3.5
LABEL maintainer="Jai Khanna jai41khanna@gmail.com"

COPY requirements.txt /tmp/
COPY ./app /app

RUN pip3 install -r /tmp/requirements.txt

ENV NGINX_WORKER_PROCESSES auto