import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publishers'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
         return f'{self.name}'

class Book(Base):
    __tablename__ = 'books'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(40), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publishers.id'), nullable=False)

    publisher = relationship(Publisher, backref='publishers')

    def __str__(self):
         return f'{self.title}: {self.id_publisher}'


class Shop(Base):
    __tablename__ = 'shops'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    def __str__(self):
         return f'{self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref = 'books')
    shop = relationship(Shop, backref = 'shops')

    def __str__(self):
         return f'{self.id_book}: {self.id_shop}: {self.count}'



class Sale(Base):
    __tablename__ = 'sales'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='stock')

    def __str__(self):
         return f'{self.price}: {self.date_sale} : {self.id_stock}: {self.count}'

def create_tables(engine):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)