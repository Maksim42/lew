from . import sqliteDB
from .. import consui


currentWord = None

class SmartDict:
    """Interface for datebase conection"""
    def __init__(self, db_path):
        # DB driver conection
        self.db = None
        # record containing curent word
        self.currentWord = None
        # TODO: db validation
        self.db = sqliteDB.SQLiteDB(db_path)

    def Close(self):
        """Save closing dictionari"""
        self.db.Close()

    def Current(self):
        """Return current word"""
        if self.currentWord is None:
            self.Random()
        return self.currentWord['w']

    def Translate(self):
        """Return translastion string for current word"""
        if self.currentWord is None:
            self.Random()
        return self.currentWord['t']

    def Random(self, lern=False):
        """Select random word from dictanary"""
        self.currentWord = self.db.GetRanLern(lern)

    def Lern(self):
        """Change lerning status of word"""
        # TODO: inverting status
        self.db.SetLerning(self.currentWord['id'])

    def ExtendLern(self, size=10):
        """Extend lernning words list"""
        self.db.ExtendLernPull(size)
