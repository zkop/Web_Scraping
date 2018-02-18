import requests
from bs4 import BeautifulSoup
import csv

url = "https://apps.acgme.org/ads/Public/Programs/Search"

r = requests.get(url).text


soup = BeautifulSoup(r,"lxml")


states = len(soup.find("div", class_="listview-options-bar-filters listview-options-bar-filters-required").find("select", id="stateFilter").find_all("option")[1:])


search = "https://apps.acgme.org/ads/Public/Programs/Search?stateId="
for st in range(1,states+1):
    state = search + "{}".format(st)
    r = requests.get(state).text
    soup = BeautifulSoup(r, "lxml")
    pages = soup.find("tbody").find_all("td", class_="listview-cell listview-command-cell")
    
    
    for page in pages:
        page_url = page.find("a").get("href")

        data_page= "https://apps.acgme.org" + page_url

        r = requests.get(data_page).text

        soup = BeautifulSoup(r, "lxml")
        
        
        try:
            specialty = soup.find("div").find("dl", class_="dl-horizontal").find("dd").text.strip()
        except:
            specialty = None
        try:
            sponsoring = soup.find("div").find("dl", class_="dl-horizontal").find_all("dd")[-1].text.split("]")[1].strip()
        except:
            sponsoring = None

        try:
            address = soup.find("address").text.split(",")[1].strip()
        except:
            address = None

        try:
            web_address = soup.find("div", id="content-panel").find("a", target="_blank").get("href")
        except:
            web_address = None

        try:
            instut_email = soup.find("div",id="content-panel").find_all("div")[2].find_all("a")[-1].text
        except:
            instut_email= "None"
        
       
        with open("acgme.csv","a") as f:
            write = csv.writer(f)
            write.writerow(["specialty", "sponsoring", "address", "web_address","instut_email"])
            write.writerow([specialty, sponsoring, address, web_address,instut_email])


        

        
        
    


    print("qutardim")  
    break
        
       



        
        
    
    




