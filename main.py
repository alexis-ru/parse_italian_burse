import requests
from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd

url = 'https://www.borsaitaliana.it/borsa/azioni/tutti-gli-indici.html?lang=en'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table', class_='m-table -firstlevel')

headers = []
for i in table1.find_all('th'):
    title = i.text
    headers.append(title)

mydata = pd.DataFrame(columns=headers)
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

mydata.to_excel('italia_burse.xlsx')