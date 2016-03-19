from bovespa.record import Record
from bovespa.utils import layout

class File:
    def __init__(self, path=None):
        self.path = path
        self.__recnum = 0 # number of stockquote records
        self.__origin = ''
        self.__name = ''

        self._validate()

    def _validate(self):
        # read first line of file (header record)
        with open(self.path, 'rb') as f:
            first_line = f.readline().decode()[:-2] # first line
            f.seek(-(layout.reclen + 2), 2) # 2 means "from the end of the file"
            last_line = f.readline().decode()[:-2] # last line

        first_rec = Record(first_line) # header 
        last_rec = Record(last_line) # trailer
        
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
        return 'File(path={})'.format(self.path)

    def __str__(self):
        desc =  'file path: {}\n' +\
                'internal name: {}\n' +\
                'file origin: {}\n' +\
                'creation date: {}\n' +\
                'number of records: {}'

        desc = desc.format(self.path, self.name, self.origin, self.date, len(self))
        return desc
    
    def query(self, stock=None):
        with open(self.path, 'r') as f:
            for line in f:
                rec = Record(line[:-1]) # remove newline
                if rec.type == 'stockquote': # ignore header and trailer records
                    if stock is None or rec.stock_code == stock:
                        yield rec

    
if __name__ == '__main__':
    path = '../data/COTAHIST_D15032016.TXT'
    #path = '../data/COTAHIST_A2015.TXT'
   
    bf = File(path)

    for rec in bf.query():
        print(rec)
