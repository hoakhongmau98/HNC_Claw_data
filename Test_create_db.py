from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pandas as pd
import logging
import psycopg2


from os import listdir
from sqlalchemy import create_engine

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#
# # engine = create_engine('sqlite:///db_test.sqlite3', echo=False)
# Cpu_dataframe = pd.read_csv('./Csv/Cpu.csv', index_col=False)
#
# # Cpu_dataframe.to_sql('Cpu', con=db.engine)
# db.create_all()
# # print(Cpu_dataframe.columns)
#
# list_file = listdir('Csv/')
# dct_file = {}
# for file in list_file:
#     file_name = file.split('.')[0]
#     dct_file[file_name] = file

df.to_sql(name='client_history', con=db.engine, index=False)

category_dataframe = {Cpu_category: 'Cpu_category', Case_category: 'Case_category', Fan_category: 'Fan_category',
                      Keyboard_category: 'Keyboard_category', Hdd_category: 'Hdd_category',
                      Monitor_category: 'Monitor_category', Mouse_category: 'Mouse_category',
                      Monitor_category: 'Monitor_category', Psu_category: 'Psu_category', Ram_category: 'Ram_category',
                      Ssd_category: 'Ssd_category', Vga_category: 'Vga_category'}

category_table_dataframe = {Cpu_category_table: 'Cpu_category_table', Case_category_table: 'Case_category_table',
                            Fan_category_table: 'Fan_category_table',
                            Keyboard_category_table: 'Keyboard_category_table',
                            Hdd_category_table: 'Hdd_category_table',
                            Monitor_category_table: 'Monitor_category_table',
                            Mouse_category_table: 'Mouse_category_table',
                            Monitor_category_table: 'Monitor_category_table', Psu_category_table: 'Psu_category_table',
                            Ram_category_table: 'Ram_category_table',
                            Ssd_category_table: 'Ssd_category_table', Vga_category_table: 'Vga_category_table'}

