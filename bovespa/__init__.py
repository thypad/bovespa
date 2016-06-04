from .utils import record
from .io import file

import sqlite3

def stock_history(filepaths=None, stock_code=None):
    recs = record.RecordCollection()

    for path in filepaths:
        bf = file.BovespaFile(path)
        recs.add(bf.stockquotes(code=stock_code))

    return recs


class Bovespa:
    def __init__(self):
        self.cursor = None
        pass

    def connect(sqlite_file):
        conn = sqlite3.connect(sqlite_file)
        self.cursor = conn.cursor()

    def create_database(filelist, out=None):
        # create database from files

        conn = sqlite3.connect(out)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE company (name, cnpj, sector)''')


    def companies(self):
        cursor.execute('''CREATE TABLE company (name, cnpj, sector)''')
        pass
