from sqlalchemy.orm import sessionmaker, declarative_base
from models import Publisher, Book, Shop, Stock, Sale, create_tables
from pprint import pprint
import json

class main_functions():
    def __init__(self, engine):
        self.engine = engine

    def create_db(self):
        create_tables(engine=self.engine)

    def autofill_db_data(self):
        with open('tests_data.json', 'r') as f:
            data = json.load(f)
            Session = sessionmaker(self.engine)
            session = Session()
            for element in data:
                if element['model'] == 'publisher':
                    instance = Publisher(name=element['fields']['name'])
                    session.add(instance)
                    session.commit()
                elif element['model'] == 'book':
                    instance = Book(title=element['fields']['title'], id_publisher=element['fields']['id_publisher'])
                    session.add(instance)
                    session.commit()
                elif element['model'] == 'shop':
                    instance = Shop(name=element['fields']['name'])
                    session.add(instance)
                    session.commit()
                elif element['model'] == 'stock':
                    instance = Stock(id_book=element['fields']['id_book'], id_shop=element['fields']['id_shop'], count=element['fields']['count'])
                    session.add(instance)
                    session.commit()
                elif element['model'] == 'sale':
                    instance = Sale(price=element['fields']['price'], date_sale=element['fields']['date_sale'], count=element['fields']['count'], id_stock=element['fields']['id_stock'])
                    session.add(instance)
                    session.commit()
            session.close()

    def info_book(self, criteria):
        Session = sessionmaker(self.engine)
        session = Session()
        if type(criteria) == int:
            for c in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.id == criteria).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
                print(f'{c.Book.title} | {c.Shop.name} | {c.Sale.price} | {c.Sale.date_sale}')
        else:
            for c in session.query(Publisher, Book, Stock, Shop, Sale).filter(Publisher.name == criteria).filter(Book.id_publisher == Publisher.id).filter(Stock.id_book == Book.id).filter(Shop.id == Stock.id_shop).filter(Sale.id_stock == Stock.id).all():
                print(f'{c.Book.title} | {c.Shop.name} | {c.Sale.price} | {c.Sale.date_sale}')
        
        
        