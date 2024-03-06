#!/usr/bin/python3
"""This module saves arguments to a a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    current_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    current_list = []

new_list = current_list + sys.argv[1:]
save_to_json_file(new_list, 'add_item.json')
