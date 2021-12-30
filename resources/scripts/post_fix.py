#! /usr/bin/python3
import re
import sys
from pprint import pprint

with open(sys.argv[1], "r+") as file:
    data = file.read()

    # Bijv, Bijv., bijv en bijv. fixen

    regex_list = [
        {
            # adhv to aan de hand van
            "find": r"(\.png\))$",
            "replace": r"\g<1>{width=60%}"
        }
    ]

    for regex in regex_list:
        print(f"Running {regex['find']}")
        data = re.sub(regex['find'], regex['replace'], data, flags=re.MULTILINE)

    file.seek(0)
    file.write(data)
    file.truncate()