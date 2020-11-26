from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HNC_database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create db
class Product(db.Model):
    __tablename__ = "Product"

    code = db.Column('code', db.String(15), nullable=False, primary_key=True)
    name = db.Column('name', db.String(250), nullable=False)
    bao_hanh = db.Column('bao hanh', db.TEXT(20), nullable=False)
    base_price = db.Column('base_price', db.TEXT(20), nullable=False)
    slase_price = db.Column('slase_price', db.String(15), nullable=False)
    img_directory = db.Column('img_directory', db.String(250), nullable=False)
    infor_product = db.Column('infor_product', db.String(50))

    def __init__(self, code, name, bao_hanh, base_price, slase_price, img_directory, infor_product):
        self.code = code
        self.name = name
        self.bao_hanh = bao_hanh
        self.base_price = base_price
        self.slase_price = slase_price
        self.img_directory = img_directory
        self.infor_product = infor_product


db.create_all()
