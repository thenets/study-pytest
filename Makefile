formatter:
	@echo "Formatting with 'black'..."
	@source ~/venvs/learn/bin/activate \
		&& black --line-length 80 .

run:
	@source ~/venvs/learn/bin/activate \
		&& cd src/ \
		&& uvicorn main:app --reload

install-os-dependencies:
	sudo dnf install -y virtualenv python3.8

create-virtualenv:
	rm -rf ~/venvs/learn
	virtualenv --system-site-packages -p python3.8 ~/venvs/learn

	source ~/venvs/learn/bin/activate \
		&& pip install --upgrade \
			-r requirements.txt \
			-r requirements-dev.txt
