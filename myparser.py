import re
from pack.dict import sqliteDB

def ParseRaw(source, lineParser, max=0):
    """Parse raw text file to line tokens"""
    count = 0
    with open(source, 'r', encoding="utf-8") as file:
        for line in file:
            if max != 0 and count >= max:
                return
            items = lineParser(line)
            # print(items)
            if items is not None:
                count += 1
                # print("ParseRaw: {}".format(items))
                yield items

pSpace = re.compile('\S+')
pPronoun = re.compile('\[[^\]]*\]')

def LineP(line):
    """Parse line to tokens"""
    items = pSpace.findall(line)
    if items is None:
        return None
    if len(items) < 5:
        return None
    pron = pPronoun.findall(line)[0]
    line = re.sub(pPronoun, '', line, 1)
    items = pSpace.findall(line)
    result = {'w': items[1]}
    result['t'] = ' '.join(items[2:-1])
    result['p'] = pron
    return result

def WriteToFile(source, fileName):
    """Write string items to file"""
    with open(fileName, 'wt+', encoding="utf-8") as file:
        for item in source:
            file.write(item + '\n')

def WriteToDb(source, db):
    """Write tokens to db"""
    for word in source:
        db.InsertWord(word['w'], word['t'], word['p'])

def main():
    pass

main()
