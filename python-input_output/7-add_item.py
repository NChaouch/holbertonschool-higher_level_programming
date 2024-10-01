#!/usr/bin/python3

"""
code
"""


import sys  # for access arg of line command
import os  # for check if file exist

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"  # file of save list

my_list = []

if os.path.exists(filename):
    # if exist the contain is load on my_list
    my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])  # contain all arg start 1

save_to_json_file(my_list, filename)
