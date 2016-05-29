from . import file

def reader(stream):
    return file.BovespaFileReader(stream)
