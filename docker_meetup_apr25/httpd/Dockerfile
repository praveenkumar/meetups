FROM fedora:latest
MAINTAINER Praveen Kumar <kumarpraveen.nitdgp@gmail.com>

RUN yum update -y && yum install -y nodejs npm
RUN npm install http-server -g

EXPOSE 8080

ENTRYPOINT ["http-server"]
CMD ["--help"]
