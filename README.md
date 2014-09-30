[![Coverage Status](https://coveralls.io/repos/vitoratair/switch-tester/badge.png)](https://coveralls.io/r/vitoratair/switch-tester)
[![Build Status](https://travis-ci.org/vitoratair/switch-tester.svg?branch=master)](https://travis-ci.org/vitoratair/switch-tester)
[![Code Health](https://landscape.io/github/vitoratair/switch-tester/master/landscape.png)](https://landscape.io/github/vitoratair/switch-tester/master)


# Project switch-tester
======


## What is it?

This project was born with two goals.
1 - Test switches on production line. 
2 - Storage defect indexes

## Start guide


Python, django and sqlite were the technologies to do it, so, it very simple to use and install. There is a step by step to do the installation.

1 -  Clone the <b>git</b> repository

```
git clone https://github.com/vitoratair/switch-tester
```
	
2 - Install <b>virtualenv</b> on the repository created

```
virtualenv switch-tester
cd switch-tester
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
Django version 1.6, using settings 'switch-tester.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.	
```


