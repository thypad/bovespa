from datetime import datetime
from collections import OrderedDict

from . import layout
from . import content


class Record:
    def __init__(self, data=''):
        if len(data) != layout.reclen:
            raise Exception('data length is not {} bytes'.format(layout.reclen))

        self.__data = data
        self.__type = self.__data[layout.rectype]
        self.__layout = layout.map[self.__type][0]
        self.__info = None

        self.__info = self.parse_data()

    def parse_data(self):
        if self.__info is None:
            tmp = []

            for key in self.__layout.keys():
                info = self.__layout[key]
                value = self.__data[info.slice]#.decode()

                if info.type == 'string':
                    value = ' '.join(value.split())

                elif info.type == 'date':
                    value = datetime.strptime(value, '%Y%m%d').date()

                elif info.type == 'integer':
                    value = int(value)

                elif info.type == 'float':
                    value = int(value) / 100.0

                tmp.append((key, value))

            self.__info = OrderedDict(tmp)

        return self.__info

    @property
    def info(self):
        return self.__info

    @property
    def type(self):
        return layout.map[self.__type][1]

    @property
    def date(self):
        t = self.type

        if t == 'header' or t == 'trailer':
            return self._check('DATGER')

        elif t == 'stockquote':
            return self._check('DATPRG')

    @property
    def bdi_code(self):
        code =  self._check('CODBDI')
        if code == '':
            return code

        return content.bdi[code]

    @property
    def stock_code(self):
        return self._check('CODNEG')

    def _check(self, key):
        #if key not in self.__layout.keys():
        #    return ''

        return self.__info.get(key, '')

    @property
    def market(self):
        code = self._check('TPMERC')
        if code == '':
            return code

        return content.market[code]


    @property
    def isin_code(self):
        return self._check('CODISI')

    @property
    def company_name(self):
        return self._check('NOMRES')

    @property
    def especification(self):
        code = self._check('ESPECI')
        if code == '':
            return code

        if code in content.especi.keys():
            return content.especi[code]

        return code

    @property
    def price_open(self):
        return self._check('PREABE')

    @property
    def price_high(self):
        return self._check('PREMAX')

    @property
    def price_low(self):
        return self._check('PREMIN')

    @property
    def price_mean(self):
        return self._check('PREMED')

    @property
    def price_close(self):
        return self._check('PREULT')

    @property
    def num_trades(self):
        return self._check('TOTNEG')

    @property
    def volume(self):
        return self._check('QUATOT')

    @property
    def volume_financial(self):
        return self._check('VOLTOT')

    @property
    def board_lot(self):
        return self._check('FATCOT')

    def __str__(self):
        return 'Record({}, {}, R${})'.format(self.date,
                                           self.stock_code,
                                           self.price_close)

    def __repr__(self):
        return 'Record({})'.format(self.__data)


if __name__ == '__main__':

    with open('../../data/COTAHIST_D16032016.TXT') as f:
        lines = f.read().splitlines()

        for line in lines:
            rec = Record(line)
            #pprint.pprint(rec.info)
            if rec.stock_code == 'ITUB4':
                print('\n\n----------------')
                print('type: {}'.format(rec.type))
                print('date: {}'.format(rec.date))
                print('market: {}'.format(rec.market))
                print('bdi code: {}'.format(rec.bdi_code))
                print('stock code: {}'.format(rec.stock_code))
                print('isin code: {}'.format(rec.isin_code))
                print('company name: {}'.format(rec.company_name))
                print('especi: {}'.format(rec.especification))
                print('price open: {}'.format(rec.price_open))
                print('price high: {}'.format(rec.price_high))
                print('price low: {}'.format(rec.price_low))
                print('price mean: {}'.format(rec.price_mean))
                print('num trades: {}'.format(rec.num_trades))
                print('quantity: {}'.format(rec.volume))
                print('volume: {}'.format(rec.volume_financial))
