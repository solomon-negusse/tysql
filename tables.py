from decimal import Decimal

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Date, DECIMAL, Integer, String, ForeignKey

engine = create_engine('postgresql://sol:@localhost/tysql', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    cust_id = Column(String, primary_key=True)
    cust_name = Column(String, nullable=False)
    cust_address = Column(String)
    cust_city = Column(String)
    cust_state = Column(String)
    cust_zip = Column(String)
    cust_country = Column(String)
    cust_contact = Column(String)
    cust_email = Column(String)


class OrderItems(Base):
    __tablename__ = 'orderitems'

    order_num = Column(Integer, ForeignKey('Orders.order_num'), primary_key=True)
    order_item = Column(Integer, primary_key=True)
    prod_id = Column(String, ForeignKey('Products.prod_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    item_price = Column(DECIMAL(precision=(8, 2), asdecimal=True),
        nullable=False)


class Orders(Base):
    __tablename__ = 'orders'

    order_num = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    cust_id = Column(String, ForeignKey('Customers.cust_id'), nullable=False)


class Products(Base):
    __tablename__ = 'products'

    prod_id = Column(String, primary_key=True)
    vend_id = Column(String, ForeignKey('Vendors.vend_id'), nullable=False)
    prod_name = Column(String, nullable=False)
    prod_price = Column(DECIMAL(precision=(8, 2), asdecimal=True),
        nullable=False)
    prod_desc = Column(String)


class Vendors(Base):
    __tablename__ = 'vendors'

    vend_id = Column(String, primary_key=True)
    vend_name = Column(String, nullable=False)
    vend_address = Column(String)
    vend_city = Column(String)
    vend_state = Column(String)
    vend_zip = Column(String)
    vend_country = Column(String)
