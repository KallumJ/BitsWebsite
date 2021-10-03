FROM alpine:latest

MAINTAINER Nex <nex@bits.team>
LABEL Description="Bits Website"

## add non-root user
RUN addgroup --gid 1024 server-files
RUN adduser --uid 2048 --ingroup server-files --shell /bin/sh -D user

## setup repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/main/" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community/" >> /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main/" >> /etc/apk/repositories

## install packages
RUN apk update
RUN apk add python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

## setup install dir
RUN mkdir /opt/bits-website/
RUN chown user /opt/bits-website/

## setup app dir
RUN mkdir /app/
RUN chown user /app/

## setup start script
COPY docker_entrypoint /opt/bits-website/start
RUN chmod +x /opt/bits-website/start

RUN groups user

EXPOSE 5000/tcp

USER user
WORKDIR /app/
CMD /opt/bits-website/start