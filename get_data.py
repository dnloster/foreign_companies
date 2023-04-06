import json
import requests
from get_page import *

def get_page():
    url = 'https://www.investmentmap.org/api/affiliates/by-affiliate?economicActivityCode=TT&hostCountryCode=704&investingCountryCode=000&companyType=foreign_affiliate&offset=0&limit=15&locale=en'
    response = requests.get(url)
    data = response.text
    return json.loads(data)["dataTotalCount"]

page = get_page()
# print(page)
urls = []
data = []

for i in range(0, page + 15, 300):
    url_type = f'https://www.investmentmap.org/api/affiliates/by-affiliate?economicActivityCode=TT&hostCountryCode=704&investingCountryCode=000&companyType=foreign_affiliate&offset={i}&limit=300&locale=en'
    urls.append(url_type)

for url in urls:
    print(url)
    response = requests.get(url)
    data_parse = response.text
    # data.extend(json.loads(data_parse)["data"]["rows"])
    for row in json.loads(data_parse)["data"]["rows"]:
        if row['data']['PARENT_COUNTRY']['value'] != "VIETNAM":
            data.append(row['data']['NAME']['value'])

with open("results1.txt", "w") as f:
    for item in data:
        f.write(item + "\n")

print("Data written to file 'results.txt'")


