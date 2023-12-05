SHELL=/bin/bash
venv_dir=.venv
activate = ${venv_dir}/bin/activate


venv:
	(test -d ${venv_dir} || python3 -m venv ${venv_dir})
	. ${activate}; \
	pip install -r requirements.txt;

run-test: .venv
	pytest

run: .venv
	flask --app shorturl run

run-dev: venv
	flask --app shorturl run --debug

