import time

from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.amazon.com.br/s?k=teclado+mec%C3%A2nico+logitech+sem'
                    '+fio&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HHS04956C30I'
                    '&sprefix=teclado+mec%C3%A2nico+logitech+sem+fio%2Caps%2C185&ref'
                    '=nb_sb_noss_2').text

soup = BeautifulSoup(html, 'lxml')
results = soup.find_all('div', class_='a-section a-spacing-base')

print(results)