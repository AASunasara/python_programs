'''
3: Write a Python program to convert the Python dictionary object (sort by key) to
JSON data. Print the object members with indent level 4.
'''
import json


def main():
    py_dict = {
        "1" : {"one": 1, "type": "numeric"},
        "3" : {"threee": 3, "type": "numeric"},
        "2" : {"two": 2, "type": "numeric"},
        "7" : {"seven": 7,  "type": "numeric"},
        "c" : {"c": "C/c", "type": "alpha"},    
        "5" : {"five": 5, "type": "numeric"},
        "0" : {"zero": 0, "type": "numeric"},
        "a" : {"a": "A/a", "type": "alpha"},
    }
    sorted_dict = {}

    # sort dict by keys
    for index in sorted(py_dict.keys()):
        sorted_dict[index] = py_dict[index]

    print("Dict before sorting : \n", py_dict, "\n")
    print("Dict after sorting : \n", sorted_dict, "\n")
    print("JSON DATA : \n", json.dumps(sorted_dict, indent=4))


if __name__ == "__main__":
    main()