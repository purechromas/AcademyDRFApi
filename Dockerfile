FROM alpine

WORKDIR /myapp

COPY ./requirements.txt .
COPY . .

RUN apk update && apk upgrade
RUN apk add --update --no-cache python3 py3-pip
RUN pip install -r /myapp/requirements.txt

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1


