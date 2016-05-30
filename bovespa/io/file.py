import csv

from ..utils import layout
from ..utils.record import Record


class BovespaFile:
    def __init__(self, path):
        self.path = path
        self.__recnum = 0 # number of stockquote records
        self.__origin = ''
        self.__name = ''

        self._validate()

    def _validate(self):
        # get first and last line of file
        with open(self.path, 'rb') as f:
            first_line = f.readline().decode()[:-2]
            f.seek(-(layout.reclen + 2), 2) # jump to last line
            last_line = f.readline().decode()[:-2]

        first_rec = Record(first_line) # header record
        last_rec = Record(last_line) # trailer record

        if first_rec.type != 'header':
            raise Exception('header record is missing')
        elif last_rec.type != 'trailer':
            raise Exception('trailer record is missing')

        self.__date = last_rec.info['DATGER']
        self.__recnum = last_rec.info['TOTREG'] - 2
        self.__origin = last_rec.info['CODORI']
        self.__name = last_rec.info['NOMARQ']

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

    def query(self):
        pass
        #self.stream.seek(0) # go to the beginning of stream

        #for line in self.stream:
        #    rec = Record(line.decode()[:-2])
            #rec = Record(line[:-2]) # remove newline
        #    if rec.type == 'stockquote': # ignore header and trailer records
        #        if stock is None or rec.stock_code == stock:
        #            yield rec

    def to_pandas(self):
        pass

    def to_csv(self, outpath, query={'stock_code': 'HGTX3'}):
        with open(self.path, 'rb') as f:
            with open(outpath, 'w') as csvfile:
                fieldnames = layout.stockquote.keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for line in f:
                    rec = Record(line.decode()[:-2])

                    if rec.type == 'stockquote' and rec.stock_code == query['stock_code']:
                        writer.writerow(dict(rec.info))
