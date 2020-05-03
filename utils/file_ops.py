import glob
import json
import os
import streamlit as st


PY_CONFIG = os.path.join(os.getcwd(), "python_paths.json")
REPO_CONFIG = os.path.join(os.getcwd(), "repos.json")
CONFIG_FILES = {"Python Executables": PY_CONFIG, "Repositories": REPO_CONFIG}


def choose_dir(dirs_dict):
    if len(dirs_dict) > 0:
        choice_dir = st.sidebar.selectbox(
            "Which Repo?", sorted([k for k in dirs_dict.keys()]))
    else:
        st.error("Missing repository configuration.")
        choice_dir = ""
    return choice_dir


def choose_script(dirs_dict):
    # Assume user configured ONLY directories with py file(s)
    script_key = ""
    chosen_dir = choose_dir(dirs_dict)

    scripts = dict()
    # Add options for Perl, maybe?
    py_filter = "/*.py"
    for f in glob.iglob(dirs_dict[chosen_dir] + py_filter):
        scripts[os.path.basename(f)] = f

    if len(scripts) == 0:
        st.error("Unable to find any scripts.")
    else:
        script_key = st.sidebar.selectbox(
            "Which script?",
            sorted([os.path.basename(name) for name in scripts]))

    return scripts, script_key


def get_json(which_file):
    with open(CONFIG_FILES[which_file], 'r') as file_input:
        return json.load(file_input)


def read_config():
    return get_json("Python Executables")


def read_repos():
    return get_json("Repositories")


def save_json(new_json, which_file):
    with open(CONFIG_FILES[which_file], 'w') as file_output:
        json.dump(new_json, file_output, indent=2)


def virtualenv_check(curr_repo):
    # look for repos that may use pipenv or virtual env.
    for file_name in glob.iglob(curr_repo + '/*'):
        if os.path.basename(file_name) in ('Pipfile', 'env'):
            st.sidebar.markdown(
                """{} uses a **virtualenv**\n\nRun with *pipenv run python*"""
                .format(os.path.basename(curr_repo)))
            return True
    return False
