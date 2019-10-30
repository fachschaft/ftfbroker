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

.ONESHELL:
release:
	@read -p "Enter version:" version
	echo __version__ = \'$$version\' > ftfbroker/__init__.py
	git add ftfbroker/__init__.py
	git commit -m "Release version $$version"
	git tag $$version
