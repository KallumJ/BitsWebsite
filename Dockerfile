FROM alpine:latest

MAINTAINER Nex <nex@bits.team>
LABEL Description="Bits Website"

## add non-root user
RUN addgroup --gid 1024 server-files
RUN adduser --uid 2048 --ingroup server-files --shell /bin/sh -D user

## install packages
RUN apk update
RUN apk add python3 acl git

## setup install dir
RUN mkdir /opt/bits-website/
RUN chown user /opt/bits-website/

## setup app dir
RUN mkdir /app/
ADD . /app/
RUN chown -R user /app/
RUN chmod -R g+rw /app/
RUN setfacl -m "default:group::rwx" /app/

## setup start script
COPY docker_entrypoint /opt/bits-website/start
RUN chmod +x /opt/bits-website/start

EXPOSE 5000/tcp

USER user
WORKDIR /app/
CMD /opt/bits-website/start