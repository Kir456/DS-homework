import requests
from bs4 import BeautifulSoup


url = 'https://ru.wikipedia.org/wiki/Башня'
resp = requests.get(url)


if resp.status_code == 200:

    soup = BeautifulSoup(resp.text, 'html.parser')

    header = soup.find('h1')
    if header:
        header_text = header.text.strip()

        clean_header = header_text.replace("[править | править код]", "").strip()
    
        print(f"Термин: {clean_header}")
    
    par = soup.find('p')
    if par:
        par_text = par.text.strip()

        clean_par = par_text
        for i in range(1, 4):
            clean_par = clean_par.replace(f"[{i}]", "").strip()
        clean_par = clean_par.replace("а́", "а").strip()

        print(f"Определение термина: {clean_par}")
else:
    print(f"Failed to retrieve the webpage. Status code: {resp.status_code}")
