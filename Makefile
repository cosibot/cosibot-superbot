#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = cosibot-superbot
PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


## Test python environment is setup correctly
test_environment:
	$(PYTHON_INTERPRETER) test/test_environment.py
