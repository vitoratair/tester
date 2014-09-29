all: deps
	@python manage.py runserver 0.0.0.0:1111

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.coverage" -delete

deps:
	@pip install -r requirements.txt

sync:
	python manage.py syncdb

test:
	@pip install -r test_requirements.txt
	@coverage run --source='production.core' manage.py test
	@coverage report
	@flake8 production
