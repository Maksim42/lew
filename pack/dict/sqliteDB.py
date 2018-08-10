import sqlite3

from .. import filesys

class SQLiteDB:
    def __init__(self, dbname):
        # TODO: checking file existing
        # TODO: generik exeption handler?
        # TODO: conection and cursor as property
        # TODO: make class for word representation
        self.conection = sqlite3.connect(dbname)
        self.cursor = self.conection.cursor()

    def AddNewWord(self, word, translation):
        """Add new word to db
        Return True if word added, False in ather cases
        """
        # TODO: check new word is exist in DataBase
        #self.FindWord(word)
        self.InsertWord(word, translation)
        return True

    def InsertWord(self, word, translation, transcribtion=None):
        insertT = """   INSERT INTO words
                        VALUES (?, ?, ?)"""
        self.cursor.execute(insertT, (word, translation, transcribtion))
        self.conection.commit()

    def FindWord(self, string):
        """Find word in word db"""
        raise NotImplementedError

    def ExtendLernPull(self, size=10):
        """Extend lerning pull"""
        upadteLern = """INSERT INTO lern
                            SELECT
                                words.ROWID, 0
                            FROM words LEFT JOIN lern
                                ON words.ROWID = lern.word
                            WHERE lern.word IS NULL
                            ORDER BY RANDOM()
                            LIMIT ?"""
        self.cursor.execute(upadteLern, (size,))
        self.conection.commit()

    def GetRanLern(self, lerning=False):
        """Get random word from lern pull
        Retrun word object
        """
        selectRND = """ SELECT
                            lern.ROWID,
                            words.word,
                            words.translation
                        FROM lern LEFT JOIN words
                            ON lern.word = words.ROWID
                        WHERE lern.lerning = ?
                        ORDER BY RANDOM()
                        LIMIT 1"""
        self.cursor.execute(selectRND, (lerning,))
        result = self.cursor.fetchone()
        if result is None:
            result = (-1, '<ERROR>', '')
        result =    {
                        'w': result[1],
                        't': result[2],
                        'id': result[0]
                    }
        return result

    def SetLerning(self, id, value=True):
        """Change lerning status of curent word"""
        update = """UPDATE lern
                    SET lerning=?
                    WHERE lern.ROWID = ?"""
        self.cursor.execute(update, (value, id))
        self.conection.commit()

    def Status(self, extend=False):
        raise NotImplementedError

    def Close(self):
        """Close conection to db"""
        self.conection.close()

    def BoolTransform(self, arg):
        # ????
        if type(arg) == bool:
            return int(arg)
        else:
            return bool(arg)


def CreateDB(dbname):
    """Create empty word db"""
    db = None
    if filesys.find_and_delete(dbname):
        db = sqlite3.connect(dbname)
        print('Create db {}'.format(dbname))
    else:
        return

    createT = """   CREATE TABLE words (
                        word text,
                        translation text,
                        pronounce text NULL
                    )"""
    db.execute(createT)
    createT = """   CREATE TABLE lern (
                        word INTEGER,
                        lerning BOOL,
                        FOREIGN KEY(word) REFERENCES words(ROWID)
                    )"""
    db.execute(createT)
    db.commit()
    db.close()

def TestingDB(dbname):
    # TODO: make more useful
    dbO = SQLiteDB(dbname)
    db = dbO.conection

    Select(dbO.cursor, 'words')
    
    # dbO.ExtendLernPull()
    #dbO.SetLerning(1, False)

    Select(dbO.cursor, 'lern')

    # r = dbO.GetRanLern()
    # print("Random word:")
    # print(r)

    # db.commit()
    # dbO.Close()

def Select(dbCursor, table, limit=0):
    """Make SELECT operation in *db* from *table*\n
    Print result in console
    """
    print('SELECT {}:'.format(table))
    q = 'SELECT * FROM {}'.format(table)
    if limit > 0:
        q += ' LIMIT {}'.format(limit)
    r = dbCursor.execute(q)
    printList(r)

def printList(l):
    for item in l:
        print(item)
