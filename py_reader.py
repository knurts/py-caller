"""Pick which python calls a script."""
import streamlit as st

from utils.file_ops import read_repos, choose_script


def show():
    st.title("Python Reader")
    scripts_locations = read_repos()
    if st.sidebar.checkbox("Show json configuration."):
        st.write(scripts_locations)
    scripts, script_key = choose_script(scripts_locations)

    try:
        with open(scripts[script_key], encoding="utf8") as show_file:
            st.code(show_file.read())
    except:
        # Only the finest exception handling...
        pass
