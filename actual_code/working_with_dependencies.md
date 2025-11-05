# Create a virtual environment

- VS Code
- python -m venv .venv

# Install any packages you need

- Make sure that (.venv) on the command line
  - Mac `source .venv/bin/activate`
  - PC `.venv\bin\activate`
- pip install <package-name>

# Freeze/Save our dependencies

- `pip freeze > requirements.txt`

# Install someone else's dependencies

- `pip install -r requirements.txt`
