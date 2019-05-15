FROM tiangolo/uwsgi-nginx:python2.7

EXPOSE 8000

RUN pip install prometheus_client

ENV UWSGI_INI /covilha/uwsgi.ini

COPY ./static /static_assets/homersimpson

COPY ./application /covilha

COPY ./apps.conf /etc/nginx/conf.d

COPY ./prestart.sh /app/prestart.sh

COPY ./start_prometheus.py /app/start_prometheus.py

WORKDIR /covilha



