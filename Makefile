

SETUP = setup.py install --user
PY3 = python3 $(SETUP) 
PY2 = python2 $(SETUP)

all: install-py3 call

install-py3:
	@$(PY3)

install-py2:
	@$(PY2)

call:
	@lumber-calc -vP lumber.json

