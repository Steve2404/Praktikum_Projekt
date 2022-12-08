from bs4 import BeautifulSoup
import pprint
import requests
import re


url = "https://fr.wikipedia.org/wiki/Twitter"
woerter = []
row_worter = []
elements = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "a"]
character = ["/", "\\", ":", ".", ",", "#", "[", "]", "(", ")"]
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for el in elements:
    wort = [wo.getText() for wo in soup.find_all(name=el)]
    row_worter.extend(wort)

for w in row_worter:
    woerter.extend(w.replace("/", " ").split())

correct = []
for letter in woerter:
    for ch in character:
        if ch in letter:
            print(f"je suis le caractere: {ch}")
            print(f"je suis la: {letter}")
            " ".join(letter.split().remove(ch))
            correct.append(letter)
    print(letter)
print(correct)
