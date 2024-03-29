install:
	poetry install

dev:
	poetry run flask --app page_analyzer:app run

start_tmp:
	flask --app page_analyzer/app --debug run --port 8000

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
