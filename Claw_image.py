from bs4 import BeautifulSoup
import os
import urllib.request
import requests
import pandas as pd

obj_dct = []
dct_link = {'CPU': '/cpu-bo-vi-xu-ly', 'MAIN': '/mainboard-bo-mach-chu',
            'RAM': '/ram-bo-nho-trong', 'HDD': '/o-cung-hdd-desktop',
            'SSD': '/o-cung-ssd', 'VGA': '/vga-card-man-hinh',
            'CASE': '/vo-case', 'PSU': '/nguon-may-tinh',
            'FAN': '/tan-nhiet-cooling', 'KEY_BOARD': '/ban-phim-may-tinh',
            'MOUSE': '/chuot-may-tinh', 'MONITOR': '/man-hinh-may-tinh'
            }

# dct_link = {'MAIN' : '/mainboard-bo-mach-chu'}
try:
    os.mkdir('img/')
except:
    None
try:
    os.mkdir('Csv/')
except:
    None
try:
    os.mkdir('Error/')
except:
    None
try:
    os.mkdir('Category/')
except:
    None
link = "https://www.hanoicomputer.vn"


def claw_infor_objects(key, url):
    error_object = []
    infor_object = []
    category_object = []
    source = urllib.request.urlopen(url)
    soup = BeautifulSoup(source)
    # find and count pages
    page_max = soup.find('div', class_='paging').find_all('a')[-2].contents[0]
    # edit url for per page
    try:
        os.mkdir('img/' + key)
    except:
        None
    for page_number in range(int(page_max) + 1):
        current_url = url + '/' + str(page_number) + '/'
        source = urllib.request.urlopen(current_url)
        soup = BeautifulSoup(source)
        # print(soup.prettify)

        # download file.html
        # file_name = soup.title.string+'.html'
        # urllib.request.urlretrieve(link, file_name)

        lst_objs = soup.find_all('div', class_='p-component item')
        for obj in lst_objs:
            code = ''
            name = ''
            base_price = ''
            sale_price = ''
            link_img = ''
            Product_parameters = []
            # find code object
            p_tag = obj.find_all('p', class_="p-sku")
            for i in p_tag:
                if 'Mã SP' in str(i):
                    p_tag = str(i.contents[0]).split(' ')
                    code = p_tag[-1]
            # div p-info
            infor_objs = obj.find('div', {'class': 'p-info'})
            name = str(infor_objs.h3.a.contents[0])  # name object
            price_objs = infor_objs.find('span', class_='p-price js-get-minPrice')
            sale_price = str(price_objs.attrs['data-price'])  # sale price
            base_price = str(price_objs.attrs['data-marketprice'])  # base price
            hover_infor = obj.find_all('div', class_="hover_content_pro tooltip-2019")
            try:
                obj_parameters = hover_infor[0].find('div', {
                    'class': 'hover_offer '}).contents  # content cua thong so san pham
                for i in range(0, len(obj_parameters) - 1, 2):
                    infor = obj_parameters[i].split('\n                    ')[-1]
                    if ' ' is infor or '\n' is infor:
                        None
                    else:
                        Product_parameters.append(infor)
            except:
                Product_parameters = ['']
            warranty_objs = hover_infor[0].find_all('tr')[2].find_all('td')
            if len(warranty_objs) == 2:
                if 'Bảo hành' in str(warranty_objs[0]):
                    if 'tháng' in str(warranty_objs[1]):
                        warranty_objs = str(warranty_objs[1]).split('<td>')[1].split('</td>')[0]
                    else:
                        warranty_objs = '24 tháng'
            link_img = obj.find('img', class_='lazy').attrs['data-src']
            # print(link_img)

            # if obj have an image => save obj, else save obj an error
            file_name = link_img.split('/')[-1]
            Img_directory = 'img/' + key + '/' + file_name
            try:
                with open('img/' + key + '/' + file_name, mode='wb') as f:
                    respons = requests.get(link_img)
                    f.write(respons.content)
                infor_object.append({'Code': code, 'Name': name, 'Bao hanh': warranty_objs,
                                     'Base_price': base_price, 'Slase_price': sale_price,
                                     'Img_directory': Img_directory,
                                     'Thong so san pham': Product_parameters})
                category_object.append({'Code': code, 'Name': name})
            except:
                error_object.append({'Code': code, 'Name': name, 'Bao hanh': warranty_objs,
                                     'Base_price': base_price, 'Slase_price': sale_price,
                                     'Img_directory': Img_directory,
                                     'Thong so san pham': Product_parameters})
            print(f"Code:               {code}")
            print(f"Name:               {name}")
            print(f'Base_price:         {base_price}')
            print(f'Sale_price:         {sale_price}')
            print(f'Img_directory:      {Img_directory}')
            print(f'URL:                {current_url}')
            print(f'Thong so san pham:  {Product_parameters}')
            print(f'Bao hanh:           {warranty_objs}')
            print('*' * 80)

    return infor_object, error_object, category_object


# Call func
# claw_infor_objects(url)
for key, value in dct_link.items():
    url = link + value
    print(url)
    print('-' * 80)
    obj_dct = claw_infor_objects(key, url)
    csv_file_name = 'Csv/' + key + '.csv'
    error_file_name = 'Error/' + key + '.csv'
    category_file_name = 'Category/category_' + key + '.csv'
    df = pd.DataFrame(obj_dct[0])
    df_error = pd.DataFrame(obj_dct[1])
    df_category = pd.DataFrame(obj_dct[2])
    df.to_csv(csv_file_name)
    df_error.to_csv(error_file_name)
    df_category.to_csv(category_file_name, index=False)
    # print(obj_dct)
