install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app run

start_tmp:
	flask --app page_analyzer/app --debug run --port 8000
