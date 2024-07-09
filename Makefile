PACKAGE_NAME=degel-python-utils
PYTHON=python
PIPENV=pipenv
SRC_DIR=src

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
	@PYTHONPATH=$(SRC_DIR) $(PIPENV) run pytest


# Verify changelog contains the current version
.PHONY: verify-changelog
verify-changelog:
	@VERSION=$$( $(PIPENV) run python setup.py --version ) && \
	if ! grep -q "\[v$$VERSION\]" CHANGELOG.md; then \
		echo "CHANGELOG.md does not contain the current version ($$VERSION)"; \
		exit 1; \
	fi


# Verify no uncommitted changes
.PHONY: verify-all-committed
verify-all-committed:
	@if ! git diff-index --quiet HEAD --; then \
		echo "There are uncommitted changes in the working directory"; \
		exit 1; \
	fi


# Build, e.g. for distribution
.PHONY: build
build: verify-changelog verify-all-committed clean lint test
	@$(PIPENV) run $(PYTHON) -m build


# Publish to Pypi
# Note: relies on API key in ~/.pypirc
.PHONY: publish
publish: build
	@$(PIPENV) run twine upload dist/*
	@git push origin
	@git tag v$(shell $(PIPENV) run python setup.py --version)
	@git push origin --tags


# Default target
.PHONY: all
all: install lint test build
