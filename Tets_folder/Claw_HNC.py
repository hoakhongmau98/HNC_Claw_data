from bs4 import BeautifulSoup
import os
import urllib.request
import requests
import pandas as pd

pdct_dct = []
dct_link = {'Cpu': '/cpu-bo-vi-xu-ly', 'Main': '/mainboard-bo-mach-chu',
            'Ram': '/ram-bo-nho-trong', 'Hdd': '/o-cung-hdd-desktop',
            'Ssd': '/o-cung-ssd', 'Vga': '/vga-card-man-hinh',
            'Case': '/vo-case', 'Psu': '/nguon-may-tinh',
            'Fan': '/tan-nhiet-cooling', 'Keyboard': '/ban-phim-may-tinh',
            'Mouse': '/chuot-may-tinh', 'Monitor': '/man-hinh-may-tinh'
            }

# dct_link = {'Cpu': '/cpu-bo-vi-xu-ly'}
try:
    os.mkdir('Categories/img/')
except:
    None
try:
    os.mkdir('Categories/Product/')
except:
    None
try:
    os.mkdir('Categories/Error/')
except:
    None
try:
    os.mkdir('Categories/Element/')
except:
    None
link = "https://www.hanoicomputer.vn"


def claw_infor_product(key, url):
    error_product = []
    infor_product = []
    element_product = []
    lst_code = []

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

        lst_pdcts = soup.find_all('div', class_='p-component item')
        for pdct in lst_pdcts:
            code = ''
            name = ''
            base_price = ''
            sale_price = ''
            link_img = ''
            warranty_pdct = ''
            product_parameters = ''

            # find code product
            p_tag = pdct.find_all('p', class_="p-sku")
            for i in p_tag:
                if 'Mã SP' in str(i):
                    p_tag = str(i.contents[0]).split(' ')
                    code = p_tag[-1]

            # check code, if code is already exist, break
            if code not in lst_code:
                lst_code.append(code)
                # div p-info
                infor_pdct = pdct.find('div', {'class': 'p-info'})
                name = str(infor_pdct.h3.a.contents[0])  # name product
                price_pdct = infor_pdct.find('span', class_='p-price js-get-minPrice')
                sale_price = str(price_pdct.attrs['data-price'])  # sale price
                base_price = str(price_pdct.attrs['data-marketprice'])  # base price
                hover_infor = pdct.find_all('div', class_="hover_content_pro tooltip-2019")

                try:
                    pdct_parameters = hover_infor[0].find('div', {
                        'class': 'hover_offer '}).contents  # content cua thong so san pham
                    for i in range(0, len(pdct_parameters) - 1, 2):
                        infor = pdct_parameters[i].split('\n                    ')[-1].split('\r')[0]
                        if ' ' is infor or '\n' is infor:
                            None
                        else:
                            product_parameters = product_parameters + infor + '.'
                except:
                    product_parameters = ''

                warranty_pdct = hover_infor[0].find_all('tr')[2].find_all('td')
                if len(warranty_pdct) == 2:
                    if 'Bảo hành' in str(warranty_pdct[0]):
                        if 'tháng' in str(warranty_pdct[1]):
                            warranty_pdct = str(warranty_pdct[1]).split('<td>')[1].split('</td>')[0]
                        else:
                            warranty_pdct = '24 tháng'
                link_img = pdct.find('img', class_='lazy').attrs['data-src']
                # if obj have an image => save obj, else save obj an error
                file_name = link_img.split('/')[-1]
                img_directory = 'img/' + key + '/' + file_name

                try:
                    with open('img/' + key + '/' + file_name, mode='wb') as f:
                        respons = requests.get(link_img)
                        f.write(respons.content)
                    infor_product.append({'code': code, 'name': name, 'bao_hanh': warranty_pdct,
                                          'base_price': base_price, 'slase_price': sale_price,
                                          'img_directory': img_directory,
                                          'infor_product': product_parameters})
                    element_product.append({'Code': code, 'Name': name})
                except:
                    error_product.append({'Code': code, 'Name': name, 'Bao hanh': warranty_pdct,
                                          'Base_price': base_price, 'Slase_price': sale_price,
                                          'Img_directory': img_directory,
                                          'Thong so san pham': product_parameters})
                print(f"Code:               {code}")
                print(f"Name:               {name}")
                print(f'Base_price:         {base_price}')
                print(f'Sale_price:         {sale_price}')
                print(f'Img_directory:      {img_directory}')
                print(f'URL:                {current_url}')
                print(f'Thong so san pham:  {product_parameters}')
                print(f'Bao hanh:           {warranty_pdct}')
                print('*' * 80)
            return infor_product, error_product, element_product


# Call func
# claw_infor_objects(url)
for key, value in dct_link.items():
    url = link + value
    print(url)
    print('*' * 80)
    pdct_dct = claw_infor_product(key, url)
    csv_file_name = 'Product/' + key + '.csv'
    error_file_name = 'Error/' + key + '.csv'
    category_file_name = 'Element/element' + key + '.csv'
    df = pd.DataFrame(pdct_dct[0])
    df_error = pd.DataFrame(pdct_dct[1])
    df_category = pd.DataFrame(pdct_dct[2])
    df.to_csv(csv_file_name, index=False)
    df_error.to_csv(error_file_name, index=False)
    df_category.to_csv(category_file_name, index=False)

