import time

from bs4 import BeautifulSoup
import requests

def find_products():
    html = requests.get(
        'https://www.amazon.com.br/s?k=teclado+mec%C3%A2nico+logitech+sem+fio&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HHS04956C30I&sprefix=teclado+mec%C3%A2nico+logitech+sem+fio%2Caps%2C185&ref=nb_sb_noss_2').text

    soup = BeautifulSoup(html, 'lxml')
    results = soup.find_all('div', class_='a-section a-spacing-base')

    for index, result in enumerate(results):
        title = result.find('span',
                            class_='a-size-base-plus a-color-base a-text-normal').text
        rating = result.find('span', class_='a-icon-alt').text
        reviews = result.find('span', class_='a-size-base s-underline-text').text
        price = result.find('span', class_='a-offscreen').text
        product_link = result.find('a', class_='a-link-normal s-no-outline')
        product_link = product_link['href']

        with open(f'../results/amazon-result-{index}.txt', 'w') as f:
            f.write(f'Title: {title.strip()} \n')
            f.write(f'Rating: {rating.strip()} \n')
            f.write(f'Reviews: {reviews.strip()} \n')
            f.write(f'Price: {price.strip()} \n')
            f.write(f'Product Link: https://www.amazon.com.br{product_link}')
        print('Product saved')

if __name__ == '__main__':
    while True:
        find_products()
        time.sleep(30)