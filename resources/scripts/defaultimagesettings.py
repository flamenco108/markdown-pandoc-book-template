#! /usr/bin/python3
import re
import sys
from pprint import pprint
"""
    Set default image settings if not present
"""

with open(sys.argv[1], "r+") as file:
    data = file.read()

    regex_images = r"(\(resources/images/[\w\s/\-\.]+\)\s*\n$)"

    # matches = set(re.findall(regex_images, data, flags=re.MULTILINE))   
    # pprint(matches)

    data = re.sub(regex_images, r"\g<1>{width=60%}\n", data, flags=re.MULTILINE)
    
    file.seek(0)
    file.write(data)
    file.truncate()