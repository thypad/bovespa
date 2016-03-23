*******
bovespa
*******
This package reads the historical stock quote files made available by BM&FBovespa at:
http://www.bmfbovespa.com.br/en_us/services/market-data/historical-data/spot-market/historical-data/

The historical quotes can be downloaded for a whole year or for specific days, with that said,
any historical quote files you download from the link above is a simple text file in which the
data is specified in a format given by this document: <missing link>


To install this package, do::

    pip install bovespa


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

Some of the information in the stockquote records are:

- stock symbol
- open price
- high price 
- low price
- close price
- volume
- financial volume

To print the date, stock symbol and close price of each record in the file, you can do this::

    import bovespa
    
    bf = bovespa.File(<path to file>)
    for rec in bf.query(stock='PETR3'):
        print('<{}, {}, {}>'.format(rec.date, rec.stock_symbol, rec.price_close))


**Warning**:

Even though you can read the prices of the historical files with this package, do realize that the prices are
not adjusted for things like splits, dividends and so on, so if you compare the prices obtained with these files
with the prices in well-known stock quote websites, there will be differences. If you want to check if the code
does indeed get correct prices, just use a recent date (few days ago), that should be safe. I plan to adjust the
prices for the historical data, but that is a big project, because I'll need dividend history and other such
things, so for now, it is what it is.
