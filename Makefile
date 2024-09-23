install:
#installs requirements
	pip install --upgrade pip && pip install -r requirements.txt

format:
#formats files using Black
	black *.py

lint:
#checks to make sure Python files are formatted to industry standard using Ruff
	ruff check *.py lib/*.py

test:
#tests Python script & notebook files
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: 
	format lint

all:
	install format lint test
