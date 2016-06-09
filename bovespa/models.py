from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    name = Column(String(50))
    cnpj = Column(String(50))
    sector = Column(String(12))

    def __repr__(self):
    	return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)


class Stockquote(Base):
    __tablename__ = 'stockquotes'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    stock_code = Column(String(50))

    price_open = Column(Float)
    price_close = Column(Float)
    price_close = Column(Float)

    cnpj = Column(String(50))
    sector = Column(String(12))

    def __repr__(self):
    	return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)



