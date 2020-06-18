"""
The comments are in portuguese here, so we can be faithful to the original layout
document, which is written in portuguese.
"""
from collections import namedtuple
from collections import OrderedDict


LayoutData = namedtuple('LayoutData', ['slice', 'type', 'description'])

reclen = 245  # total size of a single register in bytes
rectype = slice(0, 2)  # byte position of register type

header = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'TIPO DE REGISTRO')),  # tipo '00'
    ('NOMARQ', LayoutData(slice(2, 15), 'string', 'NOME DO ARQUIVO')),
    ('CODORI', LayoutData(slice(15, 23), 'string', 'CÓDIGO DA ORIGEM')),
    ('DATGER', LayoutData(slice(23, 31), 'date', 'DATA DA GERAÇÃO DO ARQUIVO')),
    ('RESERV', LayoutData(slice(31, 245), 'string', 'RESERVA'))
])

stockquote = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'TIPO DE REGISTRO')),  # tipo '01'
    ('DATPRG', LayoutData(slice(2, 10), 'date', 'DATA DO PREGÃO')),
    ('CODBDI', LayoutData(slice(10, 12), 'string', 'CÓDIGO BDI')),
    ('CODNEG', LayoutData(slice(12, 24), 'string', 'CÓDIGO DE NEGOCIAÇÃO DO PAPEL')),
    ('TPMERC', LayoutData(slice(24, 27), 'string', 'TIPO DE MERCADO')),
    ('NOMRES', LayoutData(slice(27, 39), 'string', 'NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL')),
    ('ESPECI', LayoutData(slice(39, 49), 'string', 'ESPECIFICAÇÃO DO PAPEL')),
    ('PRAZOT', LayoutData(slice(49, 52), 'string', 'PRAZO EM DIAS DO MERCADO A TERMO')),
    ('MODREF', LayoutData(slice(52, 56), 'string', 'MOEDA DE REFERÊNCIA')),
    ('PREABE', LayoutData(slice(56, 69), 'float', 'PREÇO DE ABERTURA DO PAPEL- MERCADO NO PREGÃO')),
    ('PREMAX', LayoutData(slice(69, 82), 'float', 'PREÇO MÁXIMO DO PAPEL- MERCADO NO PREGÃ')),
    ('PREMIN', LayoutData(slice(82, 95), 'float', 'PREÇO MÍNIMO DO PAPEL- MERCADO NO PREGÃO')),
    ('PREMED', LayoutData(slice(95, 108), 'float', 'PREÇO MÉDIO DO PAPEL- MERCADO NO PREGÃO')),
    ('PREULT', LayoutData(slice(108, 121), 'float', ' PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL-MERCADO NO PREGÃO')),
    ('PREOFC', LayoutData(slice(121, 134), 'float', 'PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL- MERCADO')),
    ('PREOFV', LayoutData(slice(134, 147), 'float', 'PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL- MERCADO')),
    ('TOTNEG', LayoutData(slice(147, 152), 'integer', 'NEG. - NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL- MERCADO NO PREGÃO')),
    ('QUATOT', LayoutData(slice(152, 170), 'integer', 'QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO')),
    ('VOLTOT', LayoutData(slice(170, 188), 'float', 'VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO')),
    ('PREEXE', LayoutData(slice(188, 201), 'float', 'PREÇO DE EXERCÍCIO PARA O MERCADO DE OPÇÕES OU VALOR DO CONTRATO PARA O MERCADO DE TERMO SECUNDÁRIO')),
    ('INDOPC', LayoutData(slice(201, 202), 'string', 'INDICADOR DE CORREÇÃO DE PREÇOS DE EXERCÍCIOS OU VALORES DE CONTRATO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO')),
    ('DATVEN', LayoutData(slice(202, 210), 'date', 'DATA DO VENCIMENTO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO')),
    ('FATCOT', LayoutData(slice(210, 217), 'integer', 'FATOR DE COTAÇÃO DO PAPE')),
    ('PTOEXE', LayoutData(slice(217, 230), 'integer', 'PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO SECUNDÁRIO')),
    ('CODISI', LayoutData(slice(230, 242), 'string', 'CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL')),
    ('DISMES', LayoutData(slice(242, 245), 'string', 'NÚMERO DE DISTRIBUIÇÃO DO PAPEL'))
])

trailer = OrderedDict([
    ('TIPREG', LayoutData(slice(0, 2), 'string', 'TIPO DE REGISTRO')),  # tipo '99'
    ('NOMARQ', LayoutData(slice(2, 15), 'string', 'NOME DO ARQUIVO')),
    ('CODORI', LayoutData(slice(15, 23), 'string', 'CÓDIGO DA ORIGEM')),
    ('DATGER', LayoutData(slice(23, 31), 'date', 'DATA DA GERAÇÃO DO ARQUIVO')),
    ('TOTREG', LayoutData(slice(31, 42), 'integer', 'TOTAL DE REGISTROS')),
    ('RESERV', LayoutData(slice(42, 245), 'string', 'RESERVA'))
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
