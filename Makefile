PACKAGE_NAME=degel-python-utils
PYTHON=python
PIPENV=pipenv

# Setup project on new machine
.PHONY: install
install:
	@$(PIPENV) install --dev


# Install git hooks on new machine
.PHONY: hooks
hooks:
	@pre-commit install


# Cleanup temp files
.PHONY: clean
clean:
	@rm -rf build dist *.egg-info


# Lint source
.PHONY: lint
lint:
	@$(PIPENV) run flake8 src tests


# Run all tests
.PHONY: test
test:
	@$(PIPENV) run pytest


# Build, e.g. for distribution
.PHONY: build
build:
	@$(PIPENV) run $(PYTHON) -m build


# Publish to Pypi
# Note: relies on API key in ~/.pypirc
.PHONY: publish
publish: build
	@$(PIPENV) run twine upload dist/*


# Default target
.PHONY: all
all: install lint test build
