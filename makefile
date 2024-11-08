init:
	$(shell python3 -m venv env)
	$(shell source env/bin/activate)
	$(shell pip3 install -r requirements.txt)

.PHONY: init