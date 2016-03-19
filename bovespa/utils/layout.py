"""
The comments are in portuguese here, so we can be faithful to the original layout
document, which is written in portuguese.
"""
from collections import namedtuple
from collections import OrderedDict


LayoutData = namedtuple('LayoutData', ['slice', 'type', 'description'])

reclen = 245 # total size of a single register in bytes
rectype = slice(0, 2) # byte position of register type





header = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'Tipo do Registro')), # tipo '00'
    ('NOMARQ', LayoutData(slice(2, 15), 'string', 'Nome do Arquivo')),
    ('CODORI', LayoutData(slice(15, 23), 'string', 'Código de Origem')),
    ('DATGER', LayoutData(slice(23, 31), 'date', 'Data de Geração do Arquivo')),
    ('RESERV', LayoutData(slice(31, 245), 'string', 'Espaço em Branco'))
])

stockquote = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'Tipo do Registro')), # tipo '01'
    ('DATPRG', LayoutData(slice(2, 10), 'date', 'Data do Pregão')),
    ('CODBDI', LayoutData(slice(10, 12), 'string', 'Código BDI')),
    ('CODNEG', LayoutData(slice(12, 24), 'string', 'Código da Ação')),
    ('TPMERC', LayoutData(slice(24, 27), 'string', 'Tipo de Mercado')),
    ('NOMRES', LayoutData(slice(27, 39), 'string', 'Nome Resumido')),
    ('ESPECI', LayoutData(slice(39, 49), 'string', 'Especificação')),
    ('PRAZOT', LayoutData(slice(49, 52), 'string', 'Prazo em Dias')),
    ('MODREF', LayoutData(slice(52, 56), 'string', 'Moeda')),
    ('PREABE', LayoutData(slice(56, 69), 'float', 'Preço de Abertura')),
    ('PREMAX', LayoutData(slice(69, 82), 'float', 'Preço Máximo')),
    ('PREMIN', LayoutData(slice(82, 95), 'float', 'Preço Mínimo')),
    ('PREMED', LayoutData(slice(95, 108), 'float', 'Preço Médio')),
    ('PREULT', LayoutData(slice(108, 121), 'float', 'Preço de Fechamento')),
    ('PREOFC', LayoutData(slice(121, 134), 'float', 'Melhor Preço de Compra')),
    ('PREOFV', LayoutData(slice(134, 147), 'float', 'Melhor Preço de Venda')),
    ('TOTNEG', LayoutData(slice(147, 152), 'integer', 'Número de Negócios')),
    ('QUATOT', LayoutData(slice(152, 170), 'integer', 'Quantidade de Ações Negociadas')),
    ('VOLTOT', LayoutData(slice(170, 188), 'float', 'Volume de Ações Negociadas')),
    ('PREEXE', LayoutData(slice(188, 201), 'float', '')),
    ('INDOPC', LayoutData(slice(201, 202), 'string', '')), 
    ('DATVEN', LayoutData(slice(202, 210), 'date', '')),
    ('FATCOT', LayoutData(slice(210, 217), 'integer', 'Fator de Cotação')),
    ('PTOEXE', LayoutData(slice(217, 230), 'integer', '')),
    ('CODISI', LayoutData(slice(230, 242), 'string', 'Código ISIN do Ativo')),
    ('DISMES', LayoutData(slice(242, 245), 'string', ''))
])

trailer = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'Tipo do Registro')),  # tipo '99'
    ('NOMARQ', LayoutData(slice(2, 15), 'string', 'Nome do Arquivo')),
    ('CODORI', LayoutData(slice(15, 23), 'string', 'Código de Origem')),
    ('DATGER', LayoutData(slice(23, 31), 'date', 'Data de Geração do Arquivo')),
    ('TOTREG', LayoutData(slice(31, 42), 'integer', 'Número Total de Registros (incluindo header e trailer')),
    ('RESERV', LayoutData(slice(42, 245), 'string', 'Espaço em Branco'))
])


map = {
    '00': (header, 'header'),
    '01': (stockquote, 'stockquote'),
    '99': (trailer, 'trailer')
}


if __name__ == '__main__':
    import pprint

    print('\n------- Header Layout -------\n')
    pprint.pprint(header)
    print('')

    print('\n------- Stockquote Layout -------\n')
    pprint.pprint(stockquote)
    print('')

    print('\n------- Trailer Layout -------\n')
    pprint.pprint(trailer)
    print('')
