import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool


def get_html(url):
    r = requests.get(url)   #Response
    return r.text           # returns html code of page


def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    tds = soup.find("table", id ="currencies-all").find_all("td", class_="currency-name")
    links = []
    for td in tds:
        a = td.find("a").get("href")
        link = "https://coinmarketcap.com" + a
        links.append(link)
    
    return links 

    

def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")
    try:
        name = soup.find("h1", class_="text-large").text.strip()
    except:
        name = ""
    try:
        price = soup.find("span", id ="quote_price").text.strip()
    except:
        price = ""
    data = {"name": name, "price": price}
    

    return data

def write_csv(data):
    with open("coinmarketcap.csv", "a") as f:
        write = csv.writer(f)
        write.writerow((data["name"], data["price"]))
    

def make_pool(url):
	write_csv(get_page_data(get_html(url)))


def main():
    start = datetime.now()
    url = "https://coinmarketcap.com/all/views/all/"
    all_links = get_all_links(get_html(url))
    
    with Pool(40) as p:
    	p.map(make_pool, all_links)
    

    end = datetime.now()

    total = end - start
    print(str(total))




if __name__ == "__main__":
    main()
