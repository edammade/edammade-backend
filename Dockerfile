FROM ubuntu:20.04

MAINTAINER nonamep nonamep@setsuna.kr

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get update
RUN apt-get install -y --no-install-recommends python3.8 python3.8-dev python3-pip python3-setuptools python3-wheel gcc
RUN apt-get install -y git

RUN python3.8 -m pip install pip --upgrade

ADD . /backend

EXPOSE 8081

WORKDIR /backend

RUN pip3 install -r requirements.txt

CMD python3.8 api.py $dbname $dbpasswd