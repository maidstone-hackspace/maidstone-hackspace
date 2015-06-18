# fabricad
#
# VERSION               0.0.1

FROM     ubuntu:14.04
MAINTAINER Oliver Marks "olymk2@gmail.com"

# make sure the package repository is up to date

RUN \
    apt-get update &&   \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common python-software-properties && \
    apt-get install -y python-requests python-lxml python-flask python-tz

RUN add-apt-repository -y ppa:oly/ppa
RUN apt-get update
RUN apt-get install -y python-scaffold

ADD site /var/www/


#allow access to flask
EXPOSE 5000 5000

#RUN /bin/sh -c 'cd /var/www; python index.py'

ENTRYPOINT /bin/sh -c 'cd /var/www; python index.py'
