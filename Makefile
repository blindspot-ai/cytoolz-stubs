.PHONY: help build clean clean-build setup setup-dev release-check flake8-check twine-release-test

.DEFAULT: help
help:
	@echo "make build"
	@echo "       build distribution directories"
	@echo "make clean"
	@echo "       clean virtual environment and distribution"
	@echo "make clean-build"
	@echo "       clean distribution directories"
	@echo "make setup"
	@echo "       setup development environment"
	@echo "make setup-dev"
	@echo "       setup virtualenv and development environment"
	@echo "make flake8-check"
	@echo "       run flake8 code style check"
	@echo "make release-check"
	@echo "       run release checks"
	@echo "make twine-release-test"
	@echo "       release to test pypi using twine"

build: clean-build
	@echo ">>> building ftoolz distribution"
	python setup.py sdist

clean: clean-build
	rm -rf venv

clean-build:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

setup: clean
	pip install -U -e .[dev,test]

setup-dev: clean
	virtualenv -p python3 venv
	./venv/bin/pip install -U pip
	./venv/bin/pip install -U setuptools
	./venv/bin/pip install -U -e .[dev,test]

flake8-check:
	@echo ">>> enforcing PEP 8 style with flake8 in cytoolz-stubs"
	flake8 --config=.flake8 cytoolz-stubs || ( echo ">>> flake8 check failed"; exit 1; )

release-check: flake8-check

twine-release-test: build
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
