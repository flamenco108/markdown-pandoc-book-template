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
            "find": r"adhv",
            "replace": r"aan de hand van"
        },
        {
            # fix sup tags
            "find": r"</*sup>",
            "replace": r"^"
        },
        {
            # fix bullet lists
            "find": r"^([\s]*)\*\s",
            "replace": r"\g<1>- "
        },
        {
            # remove image warning
            "find": r'^<p\sid="gdcalert.*</p>',
            "replace": ""
        },
        {
            # replace alt text with image_todo,
            "find": r'^!\[alt_text\].*tooltip"\)',
            "replace": r"IMAGE_TODO"
        },
        {
            # replace markdown links with normal links,
            "find": r"\[(.*)\]\(.*\)",
            "replace": r"\g<1>"
        },
        {
            # remove extra footnote newline
            "find": r"\]:\n\s+",
            "replace": r"]:"
        },
        {
            # fix space included in bold text ' **' to '** '
            "find": r"\*\*(\w+)\s\*\*",
            "replace": r"**\g<1>** "
        },
        {
            # remove ' \'
            "find": r"\s\\",
            "replace": r""
        },
        {
            # fix double newlines
            "find": r"^\n+",
            "replace": r"\n"
        },
        {
            # set table to one line so we can fix it with regex later
            # makes it easier to convert with https://jmalarcon.github.io/markdowntables/
            "find": r"^\s*((</*table>|</*tr>|</*td>).*)\n",
            "replace": r"\g<1>"
        }
    ]

    for regex in regex_list:
        print(f"Running {regex['find']}")
        data = re.sub(regex['find'], regex['replace'], data, flags=re.MULTILINE)

    file.seek(0)
    file.write(data)
    file.truncate()