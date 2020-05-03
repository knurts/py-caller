"""Pick which python calls a script."""
import os
import streamlit as st
import subprocess

from utils.file_ops import (
    read_config,
    read_repos,
    choose_script,
    virtualenv_check
)


def show():
    st.title("Python Runner")
    py_options = read_config()
    scripts_locations = read_repos()

    if st.sidebar.checkbox("Show json configurations."):
        st.write(py_options)
        st.write(scripts_locations)

    scripts, script_key = choose_script(scripts_locations)

    if script_key:
        uses_virtualenv = virtualenv_check(os.path.dirname(scripts[script_key]))
        py_key = st.sidebar.radio("Which python?", list(py_options.keys()))
        py_cmd = py_options[py_key]

        additional_args = st.sidebar.text_input("Script arguments?")

        if st.sidebar.button("Run"):
            st.subheader("Running " + py_cmd + " " + scripts[script_key] + " " + additional_args)
            try:
                if uses_virtualenv and 'pipenv' in py_cmd:
                    cmd = [py_cmd, "run", "python", scripts[script_key]]
                else:
                    cmd = [py_cmd, scripts[script_key]]

                if additional_args:
                    cmd.append(additional_args)

                output_str = subprocess.check_output(cmd,
                                                    stderr=subprocess.STDOUT)
                for line in output_str.decode(encoding='UTF-8').splitlines():
                    st.write(line)
            except subprocess.CalledProcessError as e:
                for line in e.output.decode(encoding='UTF-8').splitlines():
                    st.write(line)
                st.write(e)
                pass
