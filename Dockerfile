FROM alpine

WORKDIR /myapp

COPY ./requirements.txt .
COPY . .

RUN apk update && apk upgrade
RUN apk add --update --no-cache python3 py3-pip
RUN pip install -r /myapp/requirements.txt

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD python3 --version && pip --version
