import json
import streamlit as st

from utils.file_ops import *


def add(current_json):
    new_key = st.text_input("New Key")
    new_value = st.text_input("New Value")
    if new_key and new_value:
        current_json[new_key] = new_value
    return current_json


def remove(current_json):
    index = st.radio("Remove which key?", list(current_json.keys()))
    if index in current_json:
        del current_json[index]
    else:
        st.error("Invalid key, try again.")
    return current_json


def edit(current_json):
    index = st.radio("Edit which entry?", list(current_json.keys()))
    if index:
        new_key = st.text_input("New Key", value=index)
        new_value = st.text_input("New Value", value=current_json[index])

    if new_key != index and new_value != current_json[index]:
        # Remove old entry, add new key, new value
        if index in current_json:
            del current_json[index]
            current_json[new_key] = new_value
    elif new_key != index:
        # Remove entry, add new key, old value
        old_value = current_json[index]
        if index in current_json:
            del current_json[index]
            current_json[new_key] = old_value
    elif new_value != current_json[index]:
        # Update value, keep old key
        if index in current_json:
            current_json[index] = new_value
    else:
        pass  # Nothing edited yet

    return current_json


def take_action(which_action, which_file):
    curr_json = get_json(which_file)
    if which_action == "Add":
        new_json = add(curr_json)
    elif which_action == "Remove":
        new_json = remove(curr_json)
    elif which_action == "Edit":
        new_json = edit(curr_json)
    else:
        st.error("Action not available", which_action)
    st.write("Unsaved JSON:", curr_json)
    return new_json


def show():
    st.title("Application Configuration")
    which_file = st.sidebar.selectbox("Which file?", list(CONFIG_FILES.keys()))
    action = st.sidebar.radio("Action:", ["Add", "Remove", "Edit"])
    new_json = take_action(action, which_file)
    if st.sidebar.button("Save"):
        save_json(new_json, which_file)
    st.write("Current JSON:", get_json(which_file))
