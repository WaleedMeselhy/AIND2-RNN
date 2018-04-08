# nginx-gunicorn-flask

FROM python:3.6-slim



MAINTAINER Daniel Riti <dmriti@gmail.com>

ENV DEBIAN_FRONTEND noninteractive




RUN mkdir -p /deploy/tmp
COPY requirements.txt /deploy/tmp

RUN pip install -r /deploy/tmp/requirements.txt

