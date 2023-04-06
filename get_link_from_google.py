import requests
from bs4 import BeautifulSoup

links = []

with open("/results.txt", "r", encoding="latin-1") as f:
    lines = f.readlines()
    for company_name in lines:
        response = requests.get("https://www.google.com/search?q=" + requests.utils.quote(company_name)+ "+masothue.com")
        content = response.text
        soup = BeautifulSoup(content, "html.parser")
        search_results = soup.find_all("div", class_="egMi0 kCrYT")
        first_result = search_results[0].find('a')['href']
        print(first_result)
        links.append(first_result)

with open ('/links_raw.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')