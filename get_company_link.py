import re

urls = []
with open ("links_raw.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        pattern = r"/url\?q=(.*?)&"
        match = re.search(pattern, line)
        if match:
            url = match.group(1)
            urls.append(url)
        else:
            print("No match found.")
with open ('company_links.txt', 'w') as f:
    for url in urls:
        f.write(url + '\n')
