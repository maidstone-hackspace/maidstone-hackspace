# maidstone-hackspace
Repository for the maidstone hackspace website

To get started checkout the project to your machine.

    git clone https://github.com/olymk2/maidstone-hackspace.git

To suggest changes to the site hit the fork button on the github page, then make your changes in your own branch when your ready 
push your changes to your github account and create a pull request back into the main branch where it can be reviewed and merged
if everything is okay.

The simplest way to setup this site locally to test and make changes is to run.

    docker build -t maidstone-hackspace .
    docker run -p 5000:5000 maidstone-hackspace

If you plan on making large changes consider discussing it first so you dont wast your own time.

Generating static content
-------------------------

Most of the content is generated statically to avoid hitting a database on each request.

To generate static content you can run the code below.

``` python generate.py ```




Run locally with uwsgi on port 9090

uwsgi --plugins python --http-socket :9090 -w wsgi

Run locally with flask
python index.py
