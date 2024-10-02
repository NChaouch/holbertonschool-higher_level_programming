#!/usr/bin/python3

"""
define prototype's
"""


import json
import csv

"""
code
"""


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
