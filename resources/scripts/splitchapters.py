#! /usr/bin/python3
import re
import sys
from pprint import pprint

"""
    Splits chapters. All chapters defined in splitchapters[] will receive a /newpage 
    before the chapter. The chapter following will also receive a /newpage to start 
    on a new page.

    Chapter name is case sensitive.
"""

splitchapters = ["Oefeningen"]

with open(sys.argv[1], "r+") as file:
    data = file.read()

    # First insert a /newpage before
    for chapter in splitchapters:
        regex_chapter = fr"^#+ {chapter}"

        matches = set(re.findall(regex_chapter, data, flags=re.M))


        for index, match in enumerate(matches):
            data = re.sub(fr"^{re.escape(match)}", f"\\\\newpage \n{match}", data, flags=re.M)

    """
        Loop all chapters, If we find a chapter that is in the list we mark it and 
        look for the next chapter that starts at the same level or higher. When 
        found we inserta \newpage
    """
    
    regex_all_chapters = r"(?P<heading>#{1,6}) (?P<title>.*)"
    lookup_level = None

    for match in re.finditer(regex_all_chapters, data):
        groups = match.groupdict()

        # If its one of the titles we are looking for calculate the 
        # heading level and continue
        if groups['title'] in splitchapters:
            lookup_level = len(groups['heading'])
            continue

        current_level = len(groups['heading'])

        # if the heading level is smaller or equal we split
        if lookup_level and current_level <= lookup_level:
            data = re.sub(f"{groups['heading']} {groups['title']}", f"\\\\newpage \n{groups['heading']} {groups['title']}", data)
            lookup_level = None


    file.seek(0)
    file.write(data)
    file.truncate()
