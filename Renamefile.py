from os import rename, listdir


# ****************************************
# old file
# ****************************************


# Test on Test_folder
# print(f"old folder: {listdir('Tets_folder/')}")
# rename(r'Tets_folder/category_tableHDD.csv', r'Tets_folder/new_name.csv')
# print(f"new folder: {listdir('Tets_folder/')}")

name_element = ['cpu', 'main', 'psu', 'ram', 'vga', 'case', 'fan', 'hdd', 'ssd', 'keyboard', 'mouse', 'monitor']
print(f"old folder: {listdir('Category/')}")
# oldname = Category_CPU.csv
lst_file = listdir('Category/')
for file in lst_file:
    name_file = file.split('.')[0]
    piece_name = name_file.split('_')
    if piece_name[1].lower() is name_element:
        new_name = piece_name[1][0].upper() + piece_name[1][1:].lower() + '_' + piece_name[0].lower()
        old_name = 'Category/' + file
        new_name = 'Category/' + new_name
        rename(old_name, new_name)
print(f"new folder: {listdir('Category/')}")
print('-'*80)

print(f"old folder: {listdir('Category_table/')}")
# oldname = category_tableMain
lst_file = listdir('Category_table/')
for file in lst_file:
    name_file = file.split('.')[0]
    piece_name = name_file.split('_')
    for name in name_element:
        if name in piece_name[1].lower():
            name_element_index = piece_name[1].lower().find(name)
            new_name = piece_name[1][name_element_index:][0].upper() + piece_name[1][name_element_index:][
                                                                       1:].lower() + '_' + piece_name[0].lower() + '_' + \
                       piece_name[1][:name_element_index].lower() + '.csv'
            old_name = 'Category_table/' + file
            new_name = 'Category_table/' + new_name
            rename(r''+old_name, r''+new_name)
            print(new_name)
print(f"new folder: {listdir('Category_table/')}")
print('-'*80)