ARG IMAGE=debian
ARG TAG=buster
FROM $IMAGE:$TAG

RUN apt-get update && apt-get install -y init python python3 sudo bash ca-certificates iproute2 && apt-get clean;

CMD ["/sbin/init"]