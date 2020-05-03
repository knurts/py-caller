"""Main module for the streamlit app"""
import streamlit as st

import py_reader
import py_runner
import json_configure


CHOICES = {
    "Read Scripts": py_reader,
    "Run Scripts": py_runner,
    "Configure": json_configure
}


def main():
    selection = st.sidebar.radio("", list(CHOICES.keys()))
    choice = CHOICES[selection]
    choice.show()


if __name__ == "__main__":
    main()
