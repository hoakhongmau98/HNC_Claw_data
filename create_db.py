from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pandas as pd

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HNC_database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db = {'name': [1,5,4,57], 'number': ['a','as','asdf','sdf']}
df = pd.DataFrame(db)
print(df)
df.to_csv('test.csv')