#!/usr/bin/python3

"""
define prototypes and import json
"""


import json

"""
code
"""


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    with open(filename, 'w') as file:
        json.dump(data, file)  # for data in format json and write in file


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r') as file:
        # for read and transform data's json on obj python
        data = json.load(file)
        return data