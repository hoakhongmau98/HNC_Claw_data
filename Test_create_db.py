from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pandas as pd
from os import listdir
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = create_engine('sqlite:///db_test.sqlite3', echo=False)
Cpu_dataframe = pd.read_csv('./Csv/CPU.csv', index_col=False)

# Cpu_dataframe.to_sql('Cpu', con=engine)
# db.create_all()
print(Cpu_dataframe.columns)

list_file = listdir('Csv/')
dct_file = {}
for file in list_file:
    file_name = file.split('.')[0]
    dct_file[file_name] = file


