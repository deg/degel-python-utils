PACKAGE_NAME:=degel_python_utils
PYTHON:=python
PIPENV:=pipenv
SRC_DIR:=src

.DEFAULT_GOAL := help

# Set the shell to run all recipe lines in a single shell session
.ONESHELL:

# Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
	    helpMessage = match(lastLine, /^# (.*)/); \
	    if (helpMessage) { \
	        helpCommand = $$1; sub(/:$$/, "", helpCommand); \
	        printf "  %-20s %s\n", helpCommand, substr(lastLine, RSTART + 2, RLENGTH - 2); \
	    } \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ""
.PHONY: help


# Setup pipenv environment and git hooks
install:
	@$(PIPENV) install --dev
	@pre-commit install
.PHONY: install


# Clean up
clean:
	@rm -rf build docs dist *.egg-info
	@rm -rf .mypy_cache .pytest_cache .venv Pipfile.lock
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
.PHONY: clean


# Lint the code
lint:
	@$(PIPENV) run flake8 $(SRC_DIR) tests
.PHONY: lint


# Run tests
test:
	@PYTHONPATH=$(SRC_DIR) $(PIPENV) run pytest
.PHONY: test


# List outdated dependencies
outdated:
	@pipenv install --dev
	@pipenv update --outdated
.PHONY outdated:


# Verify changelog contains the current version
verify-changelog:
	@VERSION=$$( $(PIPENV) run python setup.py --version ) && \
	if ! grep -q "\[v$$VERSION\]" CHANGELOG.md; then \
		echo "CHANGELOG.md does not contain the current version ($$VERSION)"; \
		exit 1; \
	fi
.PHONY: verify-changelog


# Verify no uncommitted changes
verify-all-committed:
	@if ! git diff-index --quiet HEAD --; then \
		echo "There are uncommitted changes in the working directory"; \
		exit 1; \
	fi
.PHONY: verify-all-committed


# Generate documentation
document:
	@$(PIPENV) run pdoc -o docs $(SRC_DIR)/$(PACKAGE_NAME)
.PHONY: document


# Build, e.g., for distribution
build: verify-changelog verify-all-committed lint test
	@rm -rf dist
	@$(PIPENV) run $(PYTHON) -m build
	@$(PIPENV) run twine check dist/*
.PHONY: build


# Publish to PyPI and update GitHub Pages
# Note: relies on API key in ~/.pypirc
publish: build document
	@$(PIPENV) run twine upload dist/*
	@git push origin
	$(eval VERSION=$(shell $(PIPENV) run $(PYTHON) setup.py --version))
	@git tag v$(VERSION)
	@git push origin --tags
	@$(PIPENV) run ghp-import -n -p -f docs -m "Update documentation for version $(VERSION)"
.PHONY: publish
