from . import sqliteDB

# DB driver conection
db = sqliteDB.SQLiteDB(".\words.db")
# record containing curent word
currentWord = None

def Close():
    """Save closing dictionari"""
    db.Close()

def Current():
    """Return current word"""
    if currentWord is None:
        Random()
    return currentWord['w']

def Translate():
    """Return translastion string for current word"""
    if currentWord is None:
        Random()
    return currentWord['t']

def Random(lern=False):
    """Select random word from dictanary"""
    global currentWord
    currentWord = db.GetRanLern(lern)

def Lern():
    """Change lerning status of word"""
    # TODO: inverting status
    db.SetLerning(currentWord['id'])

def ExtendLern(size=10):
    """Extend lernning words list"""
    db.ExtendLernPull(size)
