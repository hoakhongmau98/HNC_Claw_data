from create_db import db, Product
import pandas as pd

# product dataframe
Cpu_dataframe = pd.read_csv('./Csv/Cpu.csv')
Case_dataframe = pd.read_csv('./Csv/Case.csv')
Fan_dataframe = pd.read_csv('./Csv/Fan.csv')
Hdd_dataframe = pd.read_csv('./Csv/Hdd.csv')
Keyboard_dataframe = pd.read_csv('./Csv/Keyboard.csv')
Main_dataframe = pd.read_csv('./Csv/Main.csv')
Mouse_dataframe = pd.read_csv('./Csv/Mouse.csv')
Monitor_dataframe = pd.read_csv('./Csv/Monitor.csv')
Psu_dataframe = pd.read_csv('./Csv/Psu.csv')
Ram_dataframe = pd.read_csv('./Csv/Ram.csv')
Ssd_dataframe = pd.read_csv('./Csv/Ssd.csv')
Vga_dataframe = pd.read_csv('./Csv/Vga.csv')


# Category 
Cpu_category = pd.read_csv('./Category/Case_category.csv')
Case_category = pd.read_csv('./Category/Cpu_category.csv')
Fan_category = pd.read_csv('./Category/Fan_category.csv')
Hdd_category = pd.read_csv('./Category/Hdd_category.csv')
Keyboard_category = pd.read_csv('./Category/Keyboard_category.csv')
Main_category = pd.read_csv('./Category/Main_category.csv')
Mouse_category = pd.read_csv('./Category/Mouse_category.csv')
Monitor_category = pd.read_csv('./Category/Monitor_category.csv')
Psu_category = pd.read_csv('./Category/Psu_category.csv')
Ram_category = pd.read_csv('./Category/Ram_category.csv')
Ssd_category = pd.read_csv('./Category/Ssd_category.csv')
Vga_category = pd.read_csv('./Category/Vga_category.csv')


# Category_table 
Cpu_category_table = pd.read_csv('./Category_table/Case_category_table.csv')
Case_category_table = pd.read_csv('./Category_table/Cpu_category_table.csv')
Fan_category_table = pd.read_csv('./Category_table/Fan_category_table.csv')
Hdd_category_table = pd.read_csv('./Category_table/Hdd_category_table.csv')
Keyboard_category_table = pd.read_csv('./Category_table/Keyboard_category_table.csv')
Main_category_table = pd.read_csv('./Category_table/Main_category_table.csv')
Mouse_category_table = pd.read_csv('./Category_table/Mouse_category_table.csv')
Monitor_category_table = pd.read_csv('./Category_table/Monitor_category_table.csv')
Psu_category_table = pd.read_csv('./Category_table/Psu_category_table.csv')
Ram_category_table = pd.read_csv('./Category_table/Ram_category_table.csv')
Ssd_category_table = pd.read_csv('./Category_table/Ssd_category_table.csv')
Vga_category_table = pd.read_csv('./Category_table/Vga_category_table.csv')


# defind name of dataframes
product_dataframe = [Cpu_dataframe, Case_dataframe, Fan_dataframe, Keyboard_dataframe, Hdd_dataframe,
                     Main_dataframe, Mouse_dataframe, Monitor_dataframe, Psu_dataframe, Ram_dataframe,
                     Ssd_dataframe, Vga_dataframe]

category_dataframe = [Cpu_category, Case_category, Fan_category, Keyboard_category, Hdd_category, Main_category,
                      Mouse_category, Monitor_category, Psu_category, Ram_category, Ssd_category, Vga_category]

category_dataframe_name = ['Cpu_category', 'Case_category', 'Fan_category', 'Keyboard_category', 'Hdd_category',
                           'Main_category', 'Mouse_category', 'Monitor_category', 'Psu_category', 'Ram_category',
                           'Ssd_category', 'Vga_category']

category_table_dataframe = [Cpu_category_table, Case_category_table, Fan_category_table, Keyboard_category_table,
                            Hdd_category_table, Main_category_table, Mouse_category_table, Monitor_category_table,
                            Psu_category_table, Ram_category_table, Ssd_category_table, Vga_category_table]

category_table_dataframe_name = ['Cpu_category_table', 'Case_category_table', 'Fan_category_table',
                                 'Keyboard_category_table', 'Hdd_category_table', 'Main_category_table',
                                 'Mouse_category_table', 'Monitor_category_table', 'Psu_category_table',
                                 'Ram_category_table', 'Ssd_category_table', 'Vga_category_table']

#   insert dataframe to Product table
for dataframe in product_dataframe:
    for row in range(len(dataframe)):
        Object = Product(dataframe.iloc[row]['Code'], dataframe.iloc[row]['Name'], dataframe.iloc[row]['Bao hanh'],
                         str(dataframe.iloc[row]['Base_price']), str(dataframe.iloc[row]['Slase_price']),
                         dataframe.iloc[row]['Img_directory'], dataframe.iloc[row]['Thong so san pham'])

        db.session.add(Object)
        db.session.commit()

# insert dataframe to each table vs it name
for item in range(len(category_dataframe)):
    category_dataframe[item].to_sql(name=category_dataframe_name[item], con=db.engine, index=False)

# insert dataframe to each table vs it name
for item in range(len(category_table_dataframe)):
    category_table_dataframe[item].to_sql(name=category_table_dataframe_name[item], con=db.engine, index=False)
