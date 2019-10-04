FILES=ftfbroker cli
EXCLUDE=ftfbroker/protobuf

all: mypy lint sort_import


update:
	python setup.py develop
	pip install -r requirements.dev.txt

mypy:
	mypy $(FILES)

lint:
	flake8 $(FILES) --exclude=$(EXCLUDE)

sort_import:
	isort -rc $(FILES) --skip=$(EXCLUDE)

verify_import:
	isort --check-only -rc $(FILES)
