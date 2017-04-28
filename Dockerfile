FROM python:3.6

RUN apt-get update && apt-get -y install libav-tools

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP main.py
EXPOSE 5000
ENTRYPOINT ["uwsgi", "--callable", "app", "--die-on-term", "--http", "0.0.0.0:5000", "--file", "main.py", "--master"]
