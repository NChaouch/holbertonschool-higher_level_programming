#!/usr/bin/python3

"""
define prototype's
"""


import xml.etree.ElementTree as ET

"""
code
"""


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")  # create elem root of doc xml
    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)  # create subelem with name key
        elem.text = str(value)  # str go to the contain text
    tree = ET.ElementTree(root)  # create tree xml from elem root
    # write tree xml in filename
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)  # analyze the file xml and create tree
    root = tree.getroot()  # get elem root of tree xml
    result = {}  # dic initialize empty for stock result
    for child in root:  # traverse each child of elem root
        result[child.tag] = child.text
    return result
