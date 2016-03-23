*******
bovespa
*******

Introduction
============

This package reads the historical stock quote files made available by BM&FBovespa at:

http://www.bmfbovespa.com.br/pt_br/servicos/market-data/historico/mercado-a-vista/cotacoes-historicas/

The historical quotes can be downloaded for a whole year or for specific days, with that said,
any historical quote files you download from the link above is a simple text file that has a
specified layout, also available in the link above.

Installation
============
To install this package, do::

    pip install bovespa


Usage
=====
To use this package to read historical quote files and print the records, do::

    import bovespa
    
    bf = bovespa.File(<path to file>)
    for rec in bf.query():
        print(rec)
        
Right now, the File class is very simple, and the query() method accepts only
one parameter specifying one stock symbol to look for in the file, like this::

    import bovespa
    
    bf = bovespa.File(<path to file>)
    for rec in bf.query(stock='PETR3'):
        print(rec)


The bf.query() method does not create a list of Records in memory, it yields the next record as
necessary.

The Record object represents a record that is defined in the documentation of the file format (already
cited here), each file has one header record, which is the first record in the file, and one trailer
record, which is the last record in the file. The other records are stockquote records, and carry
various information on daily stock trading.

Some of the information in the stockquote records (and how it's usually called in portuguese) are:

- date             ("data do pregão")
- stock symbol     ("símbolo da ação")
- open price       ("preço de abertura")
- high price       ("preço máximo")
- low price        ("preço mínimo")
- close price      ("preço de fechamento")
- volume           ("quantidade total")
- financial volume ("volume total")

To print the date, stock symbol and close price of each record in the file, you can do this::

    import bovespa
    
    bf = bovespa.File(<path to file>)
    for rec in bf.query(stock='PETR3'):
        print('<{}, {}, {}>'.format(rec.date, rec.stock_symbol, rec.price_close))


**Warning**:

The main motivation of the development of this package is to create a way to go from the historical stock
quotes given by bovespa, to the adjusted quotes you get in big stock websites, which take into account
splits, dividends and so on. Performance is not a big issue here, rather than fast, this package should
be complete, that is, it should allow someone to do whatever they want to do with the information present
in the bovespa historical stock quotes files. One other objective is to store the data that we obtain from
other places in simple formats, maybe csv, so that anyone can use that data, even if they don't know python.

So, summing up, this package wants to be given a bovespa historical stock quote file as input, and it will
create a simple interface to extract information present in it, so you can store it in pandas, or in a
database of your choice, AND in the future, it will also adjust the stock price history for splits, dividends, etc.

Beware that since the historic stock quote prices given by bovespa are not adjusted for things like splits,
dividends and so on, if you compare the prices obtained with these files with the prices in well-known
stock quote websites, there will be differences. If you want to check if the code does indeed get correct
prices, just use a recent date (few days ago), that should be safe. I plan to adjust the prices for the
historical data, but that is a big project, because I'll need dividend history and other such
things, so for now, it is what it is.
