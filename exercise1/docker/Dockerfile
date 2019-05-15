FROM tiangolo/uwsgi-nginx:python2.7

ENV UWSGI_INI /covilha/uwsgi.ini

ENV LISTEN_PORT 8080

EXPOSE 81

COPY ./static /static_assets/homersimpson

COPY ./application /covilha

COPY ./apps.conf /etc/nginx/conf.d

WORKDIR /covilha



