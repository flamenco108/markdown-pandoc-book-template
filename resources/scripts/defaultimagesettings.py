#! /usr/bin/python3
import re
import sys
import yaml
from pprint import pprint
"""
    Set default image settings if not present
"""

with open('meta.yml', 'r') as yaml_file:
    meta_settings = yaml.load(yaml_file, Loader=yaml.SafeLoader)

with open(sys.argv[1], "r+") as file:
    data = file.read()

    regex_images = r"(\(resources/images/[\w\s/\-\.]+\))\s*\n$"

    # matches = set(re.findall(regex_images, data, flags=re.MULTILINE))   
    # pprint(matches)

    data = re.sub(regex_images, fr"\g<1>{{width={meta_settings['default-image-width']}%}}\n", data, flags=re.MULTILINE)
    
    file.seek(0)
    file.write(data)
    file.truncate()