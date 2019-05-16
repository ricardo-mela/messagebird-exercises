FROM tiangolo/meinheld-gunicorn-flask:python3.7

ENV VARIABLE_NAME=app_dispatch

RUN pip install prometheus_client datetime pytz

COPY ./app /app

COPY ./static /static_assets


