install:
	poetry install

run:
	poetry run flask run

coverage:
	poetry run pytest --cov .
