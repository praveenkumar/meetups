FROM fedora:latest
MAINTAINER Praveen Kumar <kumarpraveen.nitdgp@gmail.com>

RUN yum update -y && yum install -y python-requests \
python-pip python-flask

RUN pip install json2html

VOLUME /data

ADD movie_data /movie_data
RUN chmod 755 /movie_data/movie_data.py

EXPOSE 5000

ENTRYPOINT ["/movie_data/movie_data.py"]
CMD ["-h"]

