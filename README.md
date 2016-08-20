# maidstone-hackspace
Repository for the maidstone hackspace website

To get started checkout the project to your machine.

    git clone https://github.com/olymk2/maidstone-hackspace.git

To suggest changes to the site hit the fork button on the github page, then make your changes in your own branch when your ready 
push your changes to your github account and create a pull request back into the main branch where it can be reviewed and merged
if everything is okay.


The simplest way to setup this site is to use docker-compose so please install that from this site https://docs.docker.com/engine/installation/ 
and make sure the quick start guide works https://docs.docker.com/machine/get-started/ then you can use the commands below to test and make changes.

    docker-compose up 
    
    docker volume create --name sockets
    docker run -it -v /etc/uwsgi/apps-enabled/:/etc/uwsgi/apps-enabled/ -v /var/www:/var/www -v sockets:/data/sockets --name mhackspace olymk2/mhackspace

If you plan on making large changes consider discussing it first so you dont waste your own time.

Generating static content
-------------------------

Most of the content is generated statically to avoid hitting a database on each request.

To generate static content you can run the code below.

``` python generate.py ```


Testing the payment systems
---------------------------

Both paypal and gocardless clearly show that you are using the sandbox in the url.

for paypal you can use this email and password 

    email = contact-buyer@maidstone-hackspace.org.uk
    password = Mhackspace

To test the gocardless integration you can use these card details

    sortcode = 200000
    account number = 55779911

Run locally with uwsgi on port 9090

    uwsgi --plugins python --http-socket :9090 -w wsgi

Run locally with flask

    python index.py


Developers recommendations
--------------------------

To run the tests you can use one of the following

````
nose2
python -m unittest discover
````

run this in the root to setup pre commit checks, it will run unit tests and check code

    ln -s developers/pre-commit.sh .git/hooks/pre-commit
