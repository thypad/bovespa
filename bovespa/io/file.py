from ..utils import layout
from ..utils.record import Record


class BovespaFileReader:
    def __init__(self, stream):
        self.stream = stream
        self.__recnum = 0 # number of stockquote records
        self.__origin = ''
        self.__name = ''

        self._validate()

    def _validate(self):
        # get first and last line of stream
        first_line = self.stream.readline().decode()[:-2]
        self.stream.seek(-(layout.reclen + 2), 2) # jump to last line
        last_line = self.stream.readline().decode()[:-2]

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

    def __len__(self):
        return self.__recnum

    def __iter__(self):
        return self

    @property
    def name(self):
        return self.__name

    @property
    def origin(self):
        return self.__origin

    @property
    def date(self):
        return self.__date

    def __repr__(self):
        return 'BovespaFileReader(stream.)'.format(self.path)

    def __str__(self):
        desc =  'file path: {}\n' +\
                'internal name: {}\n' +\
                'file origin: {}\n' +\
                'creation date: {}\n' +\
                'number of records: {}'

        desc = desc.format(self.path, self.name, self.origin, self.date, len(self))
        return desc

    def query(self, stock=None):
        self.stream.seek(0) # go to the beginning of stream

        for line in self.stream:
            rec = Record(line.decode()[:-2])
            #rec = Record(line[:-2]) # remove newline
            if rec.type == 'stockquote': # ignore header and trailer records
                if stock is None or rec.stock_code == stock:
                    yield rec
