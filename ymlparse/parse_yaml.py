# -*- coding:utf-8 -*-
#!/usr/bin/env python
############################
#File Name: parse_yaml.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-09-07 12:54:27
############################
from __future__ import print_function
import argparse
import yaml

def change_yaml_file(key, value, file_name, new_file_name):
    with open(file_name, 'r' ) as f:
        data = yaml.full_load(file(file_name, 'r'))
        if key:
            print(data.get(key))
            new_data = print_dict(data, key, value)
            print(new_data)

    if new_file_name:
        try:
            with open(new_file_name, 'w') as f: 
                yaml.dump(new_data, f, default_flow_style=False)
        except Exception as e:
            print(e)

def print_dict(d, key, value):
    for k, v in d.iteritems():
	if k == key:
           d[k]=value
           return d
        else:
            if isinstance(v, dict):
                v = print_dict(v, key, value)
    return d

def command_line_parse():
    parser = argparse.ArgumentParser(description='parse and change yaml configure file')
    parser.add_argument('-k', '--key', help='configure parameter name')
    parser.add_argument('-r', '--replace', help='the parameters you want change')
    parser.add_argument('-f', '--filename', help='yaml file name ')
    parser.add_argument('-n', '--newfilename', help='yaml file name you save ')

    args = parser.parse_args()

    change_yaml_file(args.key, args.replace, args.filename, args.newfilename)



if __name__ == '__main__':
    command_line_parse()

