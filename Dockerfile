FROM ubuntu:20.04

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update

#Install required softwared for the module
RUN apt-get -y install python3.6 python3-pip nginx 

RUN apt-get update && \
    apt-get install --yes curl wget unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /app
COPY ./app /app
WORKDIR /app