FROM ubuntu:latest
MAINTAINER Omid

RUN apt update
#RUN apt upgrade -y
#RUN apt install apt-utils -y

RUN mkdir /var/www/
RUN mkdir /var/www/crawler/
WORKDIR /var/www/crawler/

ADD . .
ENV DEBIAN_FRONTEND="noninteractive"

RUN apt install python3-pip -y

RUN pip install -r /var/www/crawler/requirements.txt
