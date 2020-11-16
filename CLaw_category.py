from bs4 import BeautifulSoup
import os
import urllib.request
import requests
import pandas as pd

# List link of arg
dct_link = {'CPU': '/cpu-bo-vi-xu-ly', 'MAIN': '/mainboard-bo-mach-chu',
            'RAM': '/ram-bo-nho-trong', 'HDD': '/o-cung-hdd-desktop',
            'SSD': '/o-cung-ssd', 'VGA': '/vga-card-man-hinh',
            'CASE': '/vo-case', 'PSU': '/nguon-may-tinh',
            'FAN': '/tan-nhiet-cooling', 'KEY_BOARD': '/ban-phim-may-tinh',
            'MOUSE': '/chuot-may-tinh', 'MONITOR': '/man-hinh-may-tinh'
            }
# dct_link = {'MAIN': '/mainboard-bo-mach-chu'}

link = "https://www.hanoicomputer.vn"

try:
    os.mkdir('category_table/')
except:
    None


def get_category_link(URL):
    category_link_list = []
    df = pd.DataFrame()
    source = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source)

    # Find category in URLsite
    category_list = soup.find_all('div', class_='p-filter-item')
    # print(category_list)
    for link_element in category_list:
        element_content = []
        # name of content category
        category_content = link_element.span.contents
        for a_tag in link_element.find_all('a'):
            category_element_link = a_tag.attrs['href']
            element_content.append(str(a_tag.contents[0]))
            # remake link from a_tag
            if 'https://www.hanoicomputer.vn/' in category_element_link:
                category_link_list.append(category_element_link)

            elif '//' in category_element_link:
                category_link_list.append('https://www.hanoicomputer.vn/' + category_element_link.split('/')[-1])
                #  print(category_link.split('/')[-1])
            elif '/' not in category_element_link:
                category_link_list.append('https://www.hanoicomputer.vn/' + category_element_link)
            else:
                category_link_list.append('https://www.hanoicomputer.vn' + category_element_link)

        # make dataframe and save it to csv file
        df_element = pd.DataFrame({category_content[0]: element_content})
        df = pd.concat([df, df_element], axis=1)
        # print(df)
    return df, category_link_list


def claw_element_obj(key, lst_link):
    df_current_category = pd.read_csv('Category/category_' + key + '.csv')
    lst_code_category = list(df_current_category['Code'])
    # for each link in category_link_list to find code in each category and compare it with colum code in category_*.csv file
    for element_link in lst_link:
        source = urllib.request.urlopen(element_link)
        element_soup = BeautifulSoup(source)
        # identification arg
        obj_code = []
        lst_check_obj = []
        name_element = ''

        # find name of category if '=' in obj_link cut it
        if '=' in element_link:
            name_element = element_link.split('=')[-1]
        else:
            name_element = element_link.split('/')[-1]

        # count page
        try:
            page_max = element_soup.find('div', class_='paging').find_all('a')[-2].contents[0]
        except:
            page_max = 1

        # find code of object in current site
        for page_number in range(1, int(page_max) + 1):
            if '?' in element_link:
                link_extract = element_link.split('?')
                current_url = link_extract[0] + '/' + str(page_number) + '/?' + link_extract[1]
            else:
                current_url = element_link + '/' + str(page_number) + '/'
            source = urllib.request.urlopen(current_url)
            currentpage_soup = BeautifulSoup(source)
            lst_objs = currentpage_soup.find_all('div', class_='p-component item')
            # find each code in the lst_objs
            for obj in lst_objs:
                list_p_tag = obj.find_all('p', class_='p-sku')
                for i in list_p_tag:
                    if 'Mã SP' in str(i):
                        p_tag = str(i.contents[0]).split(' ')
                        obj_code.append(p_tag[-1])  # return obj_code

        # compare each code in obj_code vs code in category_*.csv file
        # compare each code in df_code_category vs obj_code, if code in df_code_category(code in category_*.csv in the list obj_code: set it's True)
        for code in lst_code_category:
            if code in obj_code:
                lst_check_obj.append('Yes')
                print(code)
                print(obj_code.index(code))
            else:
                lst_check_obj.append('No')

        df_current_obj = {name_element: lst_check_obj}
        df_current_obj = pd.DataFrame(df_current_obj)
        df_current_category = pd.concat([df_current_category, df_current_obj], axis=1)
        df_current_category.to_csv('Category/category_' + key + '.csv', index=False)

        print('-' * 80)
        print(f'element name    : {name_element}')
        print(f'element link    : {element_link}')
        print(len(obj_code))
        print(f'element code    : {obj_code}')
        print(f'category_code   : {lst_code_category}')
        print(f'compare code_obj: {lst_check_obj}')
        print(df_current_obj)
        print(df_current_category)
        print(f"{'*' * 80}\n")

    return df_current_category


for key, value in dct_link.items():
    url = link + value
    df, link_category = get_category_link(url)
    df.to_csv('category_table/' + 'category_table' + key + '.csv')
    claw_element_obj(key, link_category)
