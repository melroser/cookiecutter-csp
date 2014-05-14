.PHONY: clean-pyc clean-build docs

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean - remove build & Python file artifacts"
	@echo "clean-all - remove build, Python file, sdist, and test artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-build clean-pyc
	rm -fr *.egg
	rm -fr tests/__pycache__
	rm -fr docs/coverage/htmlcov
	rm -fr docs/.coverage
	rm -fr docs/_build
	rm -rf docs/graphs/deps.pdf
	rm -rf docs/graphs/callgraph.pdf

lint:
	flake8 csputil tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source {{ cookiecutter.project_name }} setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs: docs/api/epydoc.css docs/api/python_syntax.css
	rm -fr docs/api/python docs/graphs
	mkdir docs/api/python
	mkdir docs/graphs
	epydoc -v -o docs/api/python --name="Common Software Platform" --url http://www.seagate.com --no-frames --css docs/api/epydoc.css --graph all src/python/csp
	cp docs/api/python_syntax.css docs/api/python/
	open docs/api/python/index.html

release: clean-build clean-pyc
	python setup.py sdist upload

sdist:clean-build clean-pyc
	python setup.py sdist
	ls -l dist
