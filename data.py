import requests
import json
from bs4 import BeautifulSoup

url = 'https://alltomfgas.se/koldmedietabell'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table_body = soup.find('tbody')
gas_rows = table_body.find_all('tr')


gases = {}

for gas in gas_rows:
    tds = gas.find_all('td')
    name = tds[0].get_text().split()[0].strip()
    gwp = tds[1].get_text().strip()

    gases[name] = gwp



with open('gases.json', 'w') as f:
    json.dump(gases, f)
