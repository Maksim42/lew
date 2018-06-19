#! /usr/bin/env python3
import lxml.html

shtml = 'raw.html'

def main():
    pass

def GetText(htmlFile):
    text = StringFromFile(htmlFile)
    htmle = lxml.html.fragment_fromstring(text)
    strings = htmle.findall('td')
    for c in htmle:
        if c.tag == 'table':
            tableRoot = c[0]
            for row in tableRoot:
                if row.tag == 'tr':
                    for line in row:
                        if line.tag == 'td':
                            yield(line.text)

def StringFromFile(fname, maxlen=-1):
    resStr = ''
    with open(fname, 'r', encoding="utf-8") as file:
        for line in file:
            resStr += line
            if maxlen > 0:
                maxlen -= 1
            if maxlen == 0:
                break
    return resStr

main()