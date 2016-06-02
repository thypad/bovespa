import csv

from ..utils import layout
from ..utils.record import Record


def process_line(line):
    return line.decode()[:-2]


class BovespaFile:
    def __init__(self, path):
        self.path = path
        self.__recnum = 0 # number of stockquote records
        self.__origin = ''
        self.__name = ''

        self.__header = None
        self.__trailer = None

        self._validate()

    def _validate(self):
        # get first and last line of file
        with open(self.path, 'rb') as f:
            first_line = process_line(f.readline())
            f.seek(-(layout.reclen + 2), 2) # jump to last line
            last_line = process_line(f.readline())

        first_rec = Record(first_line) # header record
        last_rec = Record(last_line) # trailer record

        if first_rec.type != 'header':
            raise Exception('header record is missing')
        elif last_rec.type != 'trailer':
            raise Exception('trailer record is missing')

        print(first_rec.info)

        self.__header == first_rec.info
        self.__trailer == last_rec.info

        self.__date = last_rec.info['DATGER']
        self.__recnum = last_rec.info['TOTREG'] - 2
        self.__origin = last_rec.info['CODORI']
        self.__name = last_rec.info['NOMARQ']

    @property
    def header(self):
        return self.__header

    @property
    def trailer(self):
        return self.__trailer

    @property
    def name(self):
        return self.__name

    @property
    def origin(self):
        return self.__origin

    @property
    def date(self):
        return self.__date

    def __len__(self):
        return self.__recnum

    def __repr__(self):
        return 'BovespaFile()'.format(self.path)

    def __str__(self):
        desc =  'file path: {}\n' +\
                'internal name: {}\n' +\
                'file origin: {}\n' +\
                'creation date: {}\n' +\
                'number of records: {}'

        desc = desc.format(self.path, self.name, self.origin, self.date, len(self))
        return desc

    def stockquotes(self, code=None):
        quotes = []
        with open(self.path, 'rb') as f:
            for line in f:
                rec = Record(process_line(line))
                if rec.type == 'stockquote': # ignore header and trailer records
                    if code is None or rec.stock_code == code:
                        quotes.append(rec)

        return quotes

    def to_pandas(self):
        pass

    def to_csv(self, outpath, stock_code=None):
        with open(self.path, 'rb') as f:
            with open(outpath, 'w') as csvfile:
                fieldnames = layout.stockquote.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for line in f:
                    rec = Record(process_line(line))

                    if rec.type == 'stockquote':
                        if rec.stock_code == stock_code or stock_code is None:
                            writer.writerow(dict(rec.info))
