#! /usr/bin/env python3
from pack.dict import smartDict
from pack.consui import consUI

def Main():
    # TODO: global config file
    consUI.headMesage = "lew"

    line = consUI.ComandLine('lew', ['q', "quite", "exit"])
    line.AddCommand(['?', 'h', "help"], PrintHelp)
    line.AddCommand(['w', "word"],
                    lambda:consUI.Output(smartDict.Current()))
    line.AddCommand(['t', "translation"],
                    lambda:consUI.Output(smartDict.Translate()))
    line.AddCommand(['n', "next"],
                    smartDict.Random)
    line.AddCommand(['lern'],
                    smartDict.Lern)
    line.AddCommand(['extend'],
                    smartDict.ExtendLern)
    # TODO: comand: p, show pronounce
    # TODO: comand: cul, clear unlerning from the lerning word list
    line.Show()

def PrintHelp():
    consUI.Output("""\
Lerning English Word help:
    ?, h, help - print this help
    w, word - show the english word
    t, translation - show the russian translation
    n, next - select a next word
    lern - mark a word as lerning
    extend - extend the lerning words list 
    q, quite, exit - close this program\
    """)

Main()