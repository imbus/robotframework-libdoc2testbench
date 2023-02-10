# Contributing

## Development Environment Setup
1. Install Python 3.7

2. Open a terminal in this repository

3. Create the virtual environment .venv

    > /path/to/python37/python -m venv .venv

4. Activate the virtual environment

    > .venv/scripts/activate

4. Install the dependencies

    > pip install -r requirements.txt


## Build, Install and Run

- Build and install the package
    > pip install -e .

- Run the application
    > Libdoc2TestBench <LIBRARY> <output.zip>

- Create a python wheel and publish it to pypi
    createPip_whl_tar.bat / createPip_whl_tar.sh


## Adding New Dependencies
1. Install pip-tools (to pin dependencies)

    > python -m pip install pip-tools

2. In `setup.py` add a package to the corresponding section

    - Development dependencies: `dev` extra under `options.extras_require`

    - Runtime dependencies: `install-requires`

3. Update `requirements.txt`
    - Development dependencies

        > pip-compile --extra dev

    - Runtime dependencies
    
        > pip-compile

4. Create a commit with `setup.py`, `requirements.txt`, `pyproject.toml` explaining why the dependency was added.
