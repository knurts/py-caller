# py-caller
Use Streamlit to configure json for path to python or pipenv, and repositories to script locations. Read python file, and run python files.

1. Exhibit that a streamlit app can use submodule to run python scripts, and results can be shown in the web browser.
```sh
    pipenv install streamlit
    pipenv run streamlit run app.py
```


2. Edit paths in python_paths and repos.json to your local paths. Can be done from the app, localhost:8501


3. To test
```sh
mkdir caller-test
cd caller-test
touch caller_test.py
```

Add following to caller_test.py
```sh
import argparse

parser = argparse.ArgumentParser(description="Argparse example")
parser.add_argument("-t", "--test", dest="test", action="store_true", default=False, help="it's a boolean")

args = parser.parse_args()
print("You made it into caller_test.py!")
print("\n")
if args.test:
    print("... and you activated it's alternate ending.")
    print("\n")
print("Goodbye.")
```

Add path to caller-test dir to repos.json, save. Use app to read and / or run caller_test.py. Should work with Python 2 or Python 3. Use optional arguments like -t (--test) or -h (--help) to see help output captured and displayed in the browser.

Removing the *import argparse* line from the script, the app should display both the import error from the called script, as well as the CalledProcessError for the subprocess.
