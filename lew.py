#! /usr/bin/env python3
from pack.dict import smartDict
from pack import consui as ui
from pack import filesys

def main():
    # TODO: global config file
    db_path = filesys.open_file_dialogue("./db")
    sdict = smartDict.SmartDict(db_path)
    line = ui.CommandPromt('lew', ['q', "quite", "exit"])
    line.add_command(['?', 'h', "help"], print_help)
    line.add_command(['w', "word"],
                     lambda: ui.write(sdict.Current()))
    line.add_command(['t', "translation"],
                     lambda: ui.write(sdict.Translate()))
    line.add_command(['n', "next"],
                     sdict.Random)
    line.add_command(['lern'],
                     sdict.Lern)
    line.add_command(['extend'],
                     sdict.ExtendLern)
    # TODO: comand: p, show pronounce
    # TODO: comand: cul, clear unlerning from the lerning word list
    line.show()

def print_help():
    """Print help information"""
    ui.write("""\
Lerning English Word help:
    ?, h, help - print this help
    w, word - show the english word
    t, translation - show the russian translation
    n, next - select a next word
    lern - mark a word as lerning
    extend - extend the lerning words list 
    q, quite, exit - close this program\
""")

main()
