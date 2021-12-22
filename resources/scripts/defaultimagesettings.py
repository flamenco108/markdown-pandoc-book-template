#! /usr/bin/python3
import re
import sys
from pprint import pprint
"""
    Set default image settings if not present
"""

with open(sys.argv[1], "r+") as file:
    data = file.read()

    regex_images = r"(!\[[\w\s-]+\]\([\w\s\./-]+\))\s*[^\{]"

    matches = set(re.findall(regex_images, data))
   
    for index, match in enumerate(matches):
        data = re.sub(re.escape(match), f"{match}{{width=50%}}", data)
    
    file.seek(0)
    file.write(data)
    file.truncate()
