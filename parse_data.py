#!/usr/bin/env python3

data = ["width", "height", "entry", "exit", "output_file", "perfect"]

def open_file(file_name):
    with open(file_name, "r") as f:
        data_list = f.read()
    return data_list


def parse_data(file_data: list) -> dict:
    if not file_data:
        raise ValueError("missing config params")
    data_dict = {}
    try:
        for item in file_data:
            parts = item.split("=")
            data_dict[parts[0].lower()] = parts[1]
    except Exception as v:
        return f"error : you need to entre key = value"
    return data_dict

def check_prop(dict_data):
    data_parssed = {}
    
    for key,val in dict_data.items():
        if key == "width" or key == 'height':
            try:
                check = int(float(val))
                data_parssed[key] = check
            except Exception:
                return f"error : value is not correct"
        elif key == "entry" or key == "exit":
            pass
    return data_parssed


f = open_file('config.txt').split('\n')
d = parse_data(f)
a = check_prop(d)
print(a)