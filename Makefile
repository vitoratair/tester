all: deps
	@python manage.py runserver 0.0.0.0:1111

clean:
	@find . -name "*.pyc" -delete
	@find . -name "*.coverage" -delete

deps:
	@pip install -r requirements.txt

sync:
	python manage.py syncdb
	python manage.py migrate	
