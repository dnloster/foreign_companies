import csv
import requests
from bs4 import BeautifulSoup

# Mở file chứa danh sách link
with open('/company_links.txt', 'r') as f:
    links = [line.strip() for line in f]

# Mở file chứa danh sách tên công ty tương ứng
with open('/results.txt', 'r') as f:
    companies = [line.strip() for line in f]

# Mở file CSV để ghi dữ liệu
with open('/companies.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Viết tiêu đề cho các cột
    writer.writerow(['Tên công ty', 'Tên quốc tế', 'Mã số thuế', 'Địa chỉ', 'Người đại diện', 'Số điện thoại', "Ngành nghề kinh doanh"])

    # Duyệt từng link và công ty tương ứng
    for link, company in zip(links, companies):

        # Tải nội dung trang web từ link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        print('pass ' + link)

        # Trích xuất các trường dữ liệu cần thiết từ soup
        company_name = soup.find('th', attrs={"itemprop": "name"}).find('span').text
        taxId = "'" + soup.find('td', attrs={"itemprop": "taxID"}).find('span').text
        address = soup.find('td', attrs={"itemprop": "address"}).find('span').text
        alumni = soup.find('tr', attrs={"itemprop": "alumni"}).find('span').text
        telephone = ""
        if soup.find('td', attrs={"itemprop": "telephone"}) == None:
            telephone = "Bị ẩn theo yêu cầu doanh nghiệp"
        elif soup.find('td', attrs={"itemprop": "telephone"}) != None:
            telephone = "'" + soup.find('td', attrs={"itemprop": "telephone"}).text
        business = ""
        if soup.find('table', class_='table') == None:
            business_list = ""
        elif soup.find('table', class_='table') != None:
            businesses = soup.find('table', class_='table').find('tbody').find_all('tr')
            for business in businesses:
                business_list = business.find_all('td')[1].find('a').text

        # Ghi dữ liệu vào file CSV
        writer.writerow([company_name, company, taxId, address, alumni, telephone, business_list])