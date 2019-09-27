.PHONY: clean train-interactive action-server webserver webserver-debug nlu-server

TEST_PATH=./

help:
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    train-interactive"
	@echo "        Starts interactive training mode"
	@echo "    action-server"
	@echo "        Starts the server for custom action."
	@echo "    webserver"
	@echo "        Starts rasa server"
	@echo "    webserver-debug"
	@echo "        Starts rasa server in debugging mode"
	@echo "    nlu-server"
	@echo "        Starts rasa NLU server"
	@echo "    cmdline"
	@echo "       This will load the assistant in your terminal for you to chat."


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf docs/_build

train-interactive:
	rasa interactive --endpoints endpoints.yml

action-server:
	rasa run actions

webserver:
	rasa run -m models --enable-api --log-file logs/out.log --endpoints endpoints.yml

webserver-debug:
	rasa run -m models --enable-api --log-file logs/out.log --endpoints endpoints.yml --debug --port 5005

nlu-server:
	rasa run --enable-api -m models/ --port 5045 --debug --log-file logs/nlu_out.log