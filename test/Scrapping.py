from bs4 import BeautifulSoup
import pprint
import requests
import re

url = "https://fr.wikipedia.org/wiki/Twitter"
# url = "https://www.eurosport.fr/football/"





def scrapping_link(url:str)-> list[str]:
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    adresse = []
    string_r = r"^(https://)([A-Za-z0-9][-.%_/#]*)*/?$"
    string_e = re.compile(string_r)


    links = soup.find_all(name="a")
    for link in links:
        if var_link := link.get("href"):
            if string_e.search(var_link):
                adresse.append(var_link)

    return adresse
