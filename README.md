## Prerequisits:

- Installed __python__ (actual verion);

- Installed __venv__ package for work with Virtual Environments;

- Installed __pip__ package for installing required packages.


## Steps to reproduce:
Install package for virtual environment:

`` python -m venv .venv``

then activate virtual environment (this command for Linux, for Mac OS and Windows will be other):

`` source .venv/bin/activate `` 

then intall all required packages:

`` pip install -r requirements.txt ``

and finally:

`` python main.py ``

## Tests:

`` python -m unittest discover tests/ ```

