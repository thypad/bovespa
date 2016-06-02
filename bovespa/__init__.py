from .utils import record
from .io import file

def stock_history(filepaths=None, stock_code=None):
    recs = record.RecordCollection()

    for path in filepaths:
        bf = file.BovespaFile(path)
        recs.add(bf.stockquotes(code=stock_code))

    return recs


class Bovespa:
    def __init__(self):
        pass

    def companies(self):
        pass
