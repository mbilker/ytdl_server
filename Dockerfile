FROM python:3.6-onbuild

RUN apt-get update && apt-get -y install youtube-dl
