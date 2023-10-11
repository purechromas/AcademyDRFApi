FROM python:3.11-slim

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y gcc libjpeg-dev libpq-dev
RUN apt-get install pip -y

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

copy . /code

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]