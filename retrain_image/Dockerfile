FROM gcr.io/tensorflow/tensorflow:latest-devel
MAINTAINER Yousaf Syed "mmesunny@gmail.com"

RUN apt-get update

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN mkdir -p /entry_point
ADD train.sh /entry_point/train.sh

ENTRYPOINT ["/entry_point/train.sh"] 
RUN ["chmod", "+x", "/entry_point/train.sh"]
