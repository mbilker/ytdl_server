FROM python:3.6

RUN apt-get update && apt-get -y install youtube-dl

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENV FLASK_APP main.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
