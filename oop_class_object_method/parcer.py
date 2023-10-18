import requests
from bs4 import BeautifulSoup as bs4

headers = {
    "Accept":'*/*',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.2271 YaBrowser/23.9.0.2271 Yowser/2.5 Safari/537.36'
    }

url = "https://itproger.com"
session = requests.Session()
try:
    req = session.get(url, headers=headers)

    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all("div", attrs={"class":"article"})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print("{} - https://itproger.com/{}".format(title,href))
        # print(divs)
        # print(soup)
    else:
        print("Mistake")
except Exception:
    print("Mistake in url address")