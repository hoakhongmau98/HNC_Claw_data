from create_db import db, ProductInfor
import pandas as pd
from os import listdir


list_file = listdir('Csv/')
dct_file = {}
for file in list_file:
    file_name = file.split('.')[0]
    dct_file[file_name] = file

Cpu_dataframe = pd.read_csv('./Csv/CPU.csv')
Case_dataframe = pd.read_csv('./Csv/CASE.csv')
Fan_dataframe = pd.read_csv('./Csv/FAN.csv')
Hdd_dataframe = pd.read_csv('./Csv/HDD.csv')
Keyboard_dataframe = pd.read_csv('./Csv/KEY_BOARD.csv')
Main_dataframe = pd.read_csv('./Csv/MAIN.csv')
Mouse_dataframe = pd.read_csv('./Csv/MOUSE.csv')
Monitor_dataframe = pd.read_csv('./Csv/MONITOR.csv')
Psu_dataframe = pd.read_csv('./Csv/PSU.csv')
Ram_dataframe = pd.read_csv('./Csv/RAM.csv')
Ssd_dataframe = pd.read_csv('./Csv/SSD.csv')
Vga_dataframe = pd.read_csv('./Csv/VGA.csv')

list_dataframe = [Cpu_dataframe, Case_dataframe, Fan_dataframe, Keyboard_dataframe, Hdd_dataframe,
                  Main_dataframe, Mouse_dataframe, Monitor_dataframe, Psu_dataframe, Ram_dataframe,
                  Ssd_dataframe, Vga_dataframe]
for dataframe in list_dataframe:
    for row in range(len(dataframe)):
        Object = ProductInfor(dataframe.iloc[row]['Code'], dataframe.iloc[row]['Name'], dataframe.iloc[row]['Bao hanh'],
                              str(dataframe.iloc[row]['Base_price']), str(dataframe.iloc[row]['Slase_price']),
                              dataframe.iloc[row]['Img_directory'], dataframe.iloc[row]['Thong so san pham'])

        db.session.add(Object)
        db.session.commit()

Cpu_category = pd.read_csv('./Category/CPU.csv')
Case_category = pd.read_csv('./Category/CASE.csv')
Fan_category = pd.read_csv('./Category/FAN.csv')
Hdd_category = pd.read_csv('./Category/HDD.csv')
Keyboard_category = pd.read_csv('./Category/KEY_BOARD.csv')
Main_category = pd.read_csv('./Category/MAIN.csv')
Mouse_category = pd.read_csv('./Category/MOUSE.csv')
Monitor_category = pd.read_csv('./Category/MONITOR.csv')
Psu_category = pd.read_csv('./Category/PSU.csv')
Ram_category = pd.read_csv('./Category/RAM.csv')
Ssd_category = pd.read_csv('./Category/SSD.csv')
Vga_category = pd.read_csv('./Category/VGA.csv')

