[![Coverage Status](https://coveralls.io/repos/vitoratair/switch-tester/badge.png)](https://coveralls.io/r/vitoratair/switch-tester)
[![Build Status](https://travis-ci.org/vitoratair/switch-tester.svg?branch=master)](https://travis-ci.org/vitoratair/switch-tester)
[![Code Health](https://landscape.io/github/vitoratair/switch-tester/master/landscape.png)](https://landscape.io/github/vitoratair/switch-tester/master)


# Tester
======

![Logo](https://wh.intelbras.com.br/git/hackathon/tester/raw/master/production/core/static/assets/img/jokers1.jpg)

## What is it?

Tester is a django platform to control all kinds of needed tests.

More details soon 

## Start guide


Python, django and sqlite were the technologies to do it, so, it very simple to use and install. There is a step by step to do the installation.

1 -  Clone the <b>git</b> repository

```
git clone https://github.com/vitoratair/tester
```
	
2 - Install <b>virtualenv</b> on the repository created

```
virtualenv tester
cd tester
source bin/activate
```

3 - Install the <b>requirements</b>

```
make deps
```

4 - Sync the <b>database</b>

```
python manage.py syncdb
Creating tables ...
Installing custom SQL ...
Installing indexes ...
Installed 0 object(s) from 0 fixture(s)	
```

5 - Collect the <b>static files</b>

```
python manage.py collectstatic --noinput
...
...
```

5 - Run the <b>web server</b>

```
make
```

or 

```
python manage.py runserver
Validating models...
0 errors found
June 27, 2014 - 19:13:51
Django version 1.6, using settings 'production.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.	
```


