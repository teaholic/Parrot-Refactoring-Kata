Python version of the Parrot Refactoring Kata
=============================================

I recommend creating a virtual python environment for this project. You will need at least version 3.10 of Python. 

> I didn't have Python 3.10 installed on a Windows machine. 
> Here's how I installed python3.10 as an additional Python version on Windows:
> - download [Python 3.10 installer](https://www.python.org/downloads/release/python-3100/)
> - execute Python 3.10 installer without adding this new version to PATH
> - in Git Bash terminal:
> ```buildoutcfg
> cd <MY_PATH_TO_THIS_REPO>/Python
> python3 -m pip install virtualenv
> python3 -m virtualenv venv-3.10 -p <MY_PATH_TO>/Python310/python.exe
> venv-3.10/Scripts/activate
|```


Then install the dependencies:

    python -m pip install -r requirements.txt

Run the tests:

    python -m pytest
