all: deps

	@python manage.py runserver 0.0.0.0:1111


test: clean deps

	@pip install -r test_requirements.txt
	@coverage run --source='wisefi' manage.py test
	@coverage report

clean:

	@find . -name "*.pyc" -delete
	@find . -name "*.coverage" -delete

deps:
	@pip install -r base_requirements.txt

html:
	make html -C docs/

