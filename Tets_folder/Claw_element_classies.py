from bs4 import BeautifulSoup
import os
import urllib.request
import requests
import pandas as pd

# List link of arg
dct_link = {'Cpu': '/cpu-bo-vi-xu-ly', 'Main': '/mainboard-bo-mach-chu',
            'Ram': '/ram-bo-nho-trong', 'Hdd': '/o-cung-hdd-desktop',
            'Ssd': '/o-cung-ssd', 'Vga': '/vga-card-man-hinh',
            'Case': '/vo-case', 'Psu': '/nguon-may-tinh',
            'Fan': '/tan-nhiet-cooling', 'Keyboard': '/ban-phim-may-tinh',
            'Mouse': '/chuot-may-tinh', 'Monitor': '/man-hinh-may-tinh'
            }
# dct_link = {'Main' : '/mainboard-bo-mach-chu'}

link = "https://www.hanoicomputer.vn"

try:
    os.mkdir('Categories/Element/')
except:
    None


def get_category_link(URL):
    category_link_list = []
    df = pd.DataFrame()
    source = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source)

    # Find category in URLsite
    element_list = soup.find_all('div', class_='p-filter-item')
    # print(category_list)
    for link in element_list:
        element_content = []
        # name of content category
        category_content = link.span.contents
        for a_tag in link.find_all('a'):
            element_link = a_tag.attrs['href']
            # element_content.append(str(element_link))
            # remake link from a_tag
            if 'https://www.hanoicomputer.vn/' in element_link:
                category_link_list.append(element_link)
                element_content.append(str(element_link))
            elif '//' in element_link:
                category_link_list.append('https://www.hanoicomputer.vn/' + element_link.split('/')[-1])
                element_content.append(str(element_link))
            elif '/' not in element_link:
                category_link_list.append('https://www.hanoicomputer.vn/' + element_link)
                element_content.append(str(element_link))
            else:
                category_link_list.append('https://www.hanoicomputer.vn' + element_link)
                element_content.append(str(element_link))
        # make dataframe and save it to csv file
        df_element = pd.DataFrame({category_content[0]: element_content})
        df = pd.concat([df, df_element], axis=1)
        # print(df)
    return df, category_link_list


def claw_element_data(key, lst_element):
    df_current_element = pd.read_csv('Categories/Element/element_' + key + '.csv')
    lst_code_category = list(df_current_element['Code'])
    # for each link in category_link_list to find code in each category and compare it with colum code in category_*.csv file
    for element_link in lst_element:
        source = urllib.request.urlopen(element_link)
        element_soup = BeautifulSoup(source)
        # identification arg
        pdct_code = []
        lst_check_pdct = []
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
            lst_pdct = currentpage_soup.find_all('div', class_='p-component item')
            # find each code in the lst_objs
            for pdct in lst_pdct:
                list_p_tag = pdct.find_all('p', class_='p-sku')
                for i in list_p_tag:
                    if 'Mã SP' in str(i):
                        p_tag = str(i.contents[0]).split(' ')
                        pdct_code.append(p_tag[-1])  # return obj_code

        # compare each code in obj_code vs code in category_*.csv file
        # compare each code in df_code_category vs obj_code, if code in df_code_category(code in category_*.csv in the list obj_code: set it's True)
        for code in lst_code_category:
            if code in pdct_code:
                lst_check_pdct.append('Yes')
                print(code)
                print(pdct_code.index(code))
            else:
                lst_check_pdct.append('No')

        df_current_obj = {name_element: lst_check_pdct}
        df_current_obj = pd.DataFrame(df_current_obj)
        df_current_category = pd.concat([df_current_category, df_current_obj], axis=1)
        df_current_category.to_csv('Categories/Element/element_' + key + '.csv', index=False)

        print('-' * 80)
        print(f'element name    : {name_element}')
        print(f'element link    : {element_link}')
        print(len(pdct_code))
        print(f'element code    : {pdct_code}')
        print(f'category_code   : {lst_code_category}')
        print(f'compare code_obj: {lst_check_pdct}')
        print(df_current_obj)
        print(df_current_category)
        print(f"{'*' * 80}\n")

    return df_current_category


for key, value in dct_link.items():
    url = link + value
    df, link_category = get_category_link(url)
    df.to_csv('Categories/Category_classify/' + key + '_category' + '.csv', index=False)
    claw_element_data(key, link_category)