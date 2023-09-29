PYTHON=python3.10

run:
	$(PYTHON) script.py
gen:
	$(PYTHON) gen_data.py

send_to_api:
	$(PYTHON) src/send_data_to_api.py
reformat:
	$(PYTHON) -m black .
	$(PYTHON) -m isort .