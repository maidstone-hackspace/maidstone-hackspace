# fabricad
#
# VERSION               0.0.1

FROM     ubuntu:16.04
MAINTAINER Oliver Marks "olymk2@gmail.com"

# make sure the package repository is up to date
RUN \
    apt-get update &&   \
    apt-get upgrade -y && \
    apt-get install -y libssl-dev libffi-dev && \
    apt-get install -y software-properties-common python-software-properties && \
    apt-get install -y python-mysqldb python-psycopg2 python-requests-oauthlib python-pip python-dev python-dateutil python-requests python-lxml python-flask python-flask-login python-pillow && \
    apt-get install -y cssmin slimit && \
    add-apt-repository -y ppa:oly/ppa && \ 
    apt-get update && \
    apt-get install -y python-scaffold

RUN pip install gocardless paypalrestsdk pytz

#allow access to flask
EXPOSE 5000 5002
WORKDIR /var/www/
#RUN /bin/sh -c 'cd /var/www/site; python index.py'
ENTRYPOINT /bin/sh -c 'cd /var/www/site; python index.py'

#docker build -t mhackspace .
#docker run -d --name=mhackspace_container --restart=always mhackspace 
#accesss on dockerip 172.17.0.?:5000
#https://hub.docker.com/r/olymk2/mhackspace/
