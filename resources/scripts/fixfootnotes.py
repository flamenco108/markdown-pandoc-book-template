#! /usr/bin/python3
import re
import sys

with open(sys.argv[1], "r+") as file:
    data = file.read()

    """
        We have to work in 2 passes so that we don't overwrite the next
        footnote in the document. So if we have numerical matches and we 
        start a normal write cycle we would overwrite the value with the 
        value of the next match. So 1 would be overwritten by 2. etc...

        so we take an intermediary step where we first use footnote-<index>
        in order to have a decent numerical baseline. Afterwards we overwrite
        it with the correct number.

        We match [^<text>] where it is not the beginning of the line.

        This function expects that the footnote in the text and the footnote
        itself have the same tag.
    """

    """ 
        TODO indien meerdere files een nummer hergebruiken is er een issue
        Best enkel de eerste match aanpassen.

        Case: Stel dat chapter 1 een note heeft met nr 14 en chapter 2 ook.
        Dan worden beide aangepast omdat de nummer hetzelfde is in de match
    """

    matches = re.findall(r".(\[\^[a-zA-Z0-9-_ ]+\])", data)
    for index, match in enumerate(matches):
        data = re.sub(re.escape(match), f"[^footnote-{index}]", data)

    matches = re.findall(r".(\[\^[a-zA-Z0-9-_ ]+\])", data)
    for index, match in enumerate(matches):
        data = re.sub(re.escape(match), f"[^{index + 1}]", data)

    file.seek(0)
    file.write(data)
    file.truncate()
