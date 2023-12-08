## Setting up project for the first time
1. Write all dependencies into setup.cfg (install_requires and extras_require).
2. Create venv (python -m venv .venv) and activate it (".venv\scripts\activate" or "source .venv/bin/activate")
3. Update pip (python -m pip install -U pip)
3. Install pip-tools (pip install pip-tools)
4. Update/Create `requirements.txt`
    - with Development dependencies
        > pip-compile --extra dev setup.cfg
    - or only with Runtime dependencies
        > pip-compile setup.cfg
5. Install dependencies (pip install -U -r requirements.txt)
6. Install project into local venv (pip install -e .[extra])

## Generate Dataclasses from xsd
```xsdata testbench_xsd\itb-project-export.xsd --output attrs --config .\xsdata_config.xml```

## Fix unreadable Enums in newly generated model
```python .\fix_model.py .\libdoc2testbench\project_dump_model\itb_project_export.py```


