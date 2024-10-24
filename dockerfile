# FROM python:3.12
FROM tiangolo/uwsgi-nginx-flask:python3.12

RUN pip install flask Flask-MySQLdb

COPY ./app /app