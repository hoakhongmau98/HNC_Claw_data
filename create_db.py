from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HNC_database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# create db
class ProductInfor(db.Model):
    __tablename__ = "ProductInfor"

    code = db.Column('Code', db.String(15), nullable=False, primary_key=True)
    name = db.Column('Name', db.String(250), nullable=False)
    bao_hanh = db.Column('Bao hanh', db.TEXT(20), nullable=False)
    base_price = db.Column('Base_price', db.TEXT(20), nullable=False)
    slase_price = db.Column('Slase_price', db.String(15), nullable=False)
    img_directory = db.Column('Img_directory', db.String(250), nullable=False)
    thong_so_san_pham = db.Column('Thong_so_san_pham', db.String(50))

    def __init__(self, code, name, bao_hanh, base_price, slase_price, img_directory, thong_so_san_pham):
        self.code = code
        self.name = name
        self.bao_hanh = bao_hanh
        self.base_price = base_price
        self.slase_price = slase_price
        self.img_directory = img_directory
        self.thong_so_san_pham = thong_so_san_pham


db.create_all()
