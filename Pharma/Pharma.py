from lxml import html
from lxml import etree
import csv
import requests
import pandas as pd

# URL = 'https://peshawar.infoisinfo.com.pk/search/pharmaceutical'
URL = 'https://peshawar.infoisinfo.com.pk/card/zaynoon-pharmaceuticals-pvt-ltd/132025'

htmlDoc = requests.get(URL)

tree = etree.HTML(htmlDoc.content)

# print(htmlDoc.text)

Link_Xpath = '//a[@class="view-company"]/@href'
Company_Name = '//h1[@class="title_com name"]/text()'
Phone_Number = '//a[contains(@href,"tel:")]/@href'
Address_Xpath     = '//div[@class="address_com address.address mid-wrapper"]/span/text()'

Full_Address = []


Links = tree.xpath (Link_Xpath)

Name_list = []
Phone_list = []
Address_list = []
# print(Phone)

#'''
for link in Links:

    link_resp = requests.get(link)
    tree_link = etree.HTML(link_resp.content)

    # print(link_resp.content)
    # exit()

    Name =  tree_link.xpath (Company_Name)
    Phone = tree_link.xpath (Phone_Number)
    Address = tree_link.xpath(Address_Xpath)




    # for addr in Address:
    #     Full_Address.append(addr)

    # Name_list.append(Name)
    Phone_list.append(Phone)
    # Address_list.append(Full_Address)

    # print(Name)
    # print(Phone)
    # print (Address)



# Data =  {'Name' :  Name_list, 'Address' :  Address_list , 'Phone' : Phone_list}

# df = pd.DataFrame (Data)
# print(df)
# df.to_csv('Data.csv')

# Rows =  [Name_list,Phone_list,Address_list]

# Fields = ['Name','Phone','Address']
# with open('GFG', 'w') as f:
#     write = csv.writer(f)
#
#     write.writerow(Fields)
#     write.writerows(Rows)
# print(Name_list)
print(Phone_list)
# print(Address_list)

#'''
