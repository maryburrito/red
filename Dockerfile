FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV HTTPS on

ENV GUNICORN_PORT 8000
EXPOSE 8000

RUN mkdir /django

WORKDIR /django
ADD requirements.txt /django/requirements.txt
RUN pip install -r requirements.txt

ADD . /django/

ENTRYPOINT ["/django/run.sh"]

