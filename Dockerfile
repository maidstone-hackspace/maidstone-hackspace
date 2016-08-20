FROM olymk2/uwsgi

ENV SERVER_ENVIRONMENT DEVELOPMENT
ENV SITE_FOLDER /etc/sites/mysite/

#COPY website/config/nginx/maidstone-hackspace.org.uk.ini /etc/sites/nginx/maidstone-hackspace.org.uk.ini
#COPY website/config/uwsgi/maidstone-hackspace.org.uk.ini /etc/sites/uwsgi/maidstone-hackspace.org.uk.ini

RUN apk add --update --no-cache libssl1.0 libxml2 libxslt ca-certificates
RUN apk add --update --no-cache py-psycopg2 py-lxml py-flask py-pillow py-openssl py-cffi

RUN apk add --update --no-cache build-base make bzr python3-dev libffi-dev openssl-dev libxml2-dev libxslt-dev && \
    pip3 install lxml && \
    pip3 install --no-cache-dir lxml dateutils requests requests-oauthlib mailer gocardless paypalrestsdk pytz nose2 oauthlib flask flask-login pymysql misaka && \
    pip3 install --no-cache-dir bzr+lp:scaffold/trunk#egg=scaffold && \
    apk del build-base make bzr python3-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# RUN pip3 install --no-cache-dir dateutils requests requests-oauthlib gocardless paypalrestsdk pytz nose2 oauthlib flask flask-login pymysql misaka
# RUN pip3 install --no-cache-dir bzr+lp:scaffold/trunk#egg=scaffold

#CMD ["setup.sh"]
#ENTRYPOINT ["setup.sh"]

# make sure the package repository is up to date
#RUN \
#    apt-get update &&   \
#    apt-get upgrade -y && \
#    apt-get install -y libssl-dev libffi-dev nano && \
#    apt-get install -y software-properties-common python-software-properties && \
#    apt-get install -y software-properties-common python-pip python-dev python-nose2 && \
#    apt-get install -y python-mysqldb python-psycopg2 python-requests-oauthlib  python-dateutil python-requests python-lxml python-flask python-flask-login python-pillow  && \
#    apt-get install -y cssmin slimit && \
#    add-apt-repository -y ppa:oly/ppa && \
#    apt-get update && \
#    apt-get install -y python-scaffold



#allow access to flask
#EXPOSE 5000 5002
#WORKDIR /var/www/website/


#RUN /bin/sh -c 'cd /var/www/site; python index.py'
#ENTRYPOINT /bin/sh -c 'scaffold import && python index.py'

#docker build -t mhackspace .
#docker run -d --name=mhackspace_container --restart=always mhackspace 
#docker run -it -v /etc/uwsgi/apps-enabled/:/etc/uwsgi/apps-enabled/ -v sockets:/data/sockets --entrypoint sh --name mhackspace olymk2/mhackspace 
#docker run -it -v /etc/uwsgi/apps-enabled/:/etc/uwsgi/apps-enabled/ -v sockets:/data/sockets -v /var/www/test.maidstone-hackspace.org.uk/site:/var/www --name mhackspace olymk2/mhackspace 
#accesss on dockerip 172.17.0.?:5000
#https://hub.docker.com/r/olymk2/mhackspace/
