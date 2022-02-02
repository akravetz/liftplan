.DEFAULT_GOAL:=help

.PHONY: lint
lint:
       pylint


.PHONY: clean
clean: ## Resets development environment.
	rm -f .coverage
	rm -rf .eggs/
	rm -f .env
	rm -rf .tox/
	rm -rf build/
	rm -rf dbt.egg-info/
	rm -f dbt_project.yml
	rm -rf dist/
	rm -f htmlcov/*.{css,html,js,json,png}
	rm -rf logs/
	rm -rf target/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -depth -delete

.PHONY: help
help: ## Show this help message.
	@echo 'usage: make [target] [USE_DOCKER=true]'
	@echo
	@echo 'targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo 'options:'
	@echo 'use USE_DOCKER=true to run target in a docker container'
