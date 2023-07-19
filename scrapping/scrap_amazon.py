import time

from bs4 import BeautifulSoup
import requests

results_list = []

def find_products():
    #https://www.amazon.com.br/s?k=teclado+mec%C3%A2nico+logitech+sem+fio&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HHS04956C30I&sprefix=teclado+mec%C3%A2nico+logitech+sem+fio%2Caps%2C185&ref=nb_sb_noss_2
    html = requests.get(
        'https://www.amazon.com.br/s?k=controle&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=OEE43GQSCJ5A&sprefix=contr%2Caps%2C320&ref=nb_sb_noss_2').text

    html_soup = BeautifulSoup(html, 'lxml')
    results = html_soup.find_all('div', class_='a-section a-spacing-base')

    for index, result in enumerate(results):
        title = result.find('span',
                            class_='a-size-base-plus a-color-base a-text-normal').text
                
        # some items may have not been rated
        rating = ''
        try:
            rating = result.find('span', class_='a-icon-alt').text
        except Exception as e:
            print(f'RATING ERR: {str(e)}')

        reviews = result.find('span', class_='a-size-base s-underline-text').text
        current_price = result.find('span', class_='a-offscreen').text

        # some items may not be in promo
        #original_price_value = ''
        try:
            original_price = result.find('span', class_='a-text-price')
            original_price_value = original_price.find('span', class_='a-offscreen').text
        except Exception as e:
            print(f'ORIGINAL PRICE ERR: {str(e)}')

        product_link = result.find('a', class_='a-link-normal s-no-outline')
        product_link = product_link['href']
        
        '''
        try:
            product_html = requests.get('https://www.amazon.com.br/Logitech-LIGHTSYNC-Bluetooth-Controles-Recarreg%C3%A1vel/dp/B085RLZ1C4/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HHS04956C30I&keywords=teclado%2Bmecanico%2Blogitech%2Bsem%2Bfio&qid=1689772807&sprefix=teclado%2Bmec%C3%A2nico%2Blogitech%2Bsem%2Bfio%2Caps%2C185&sr=8-1&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&th=1').text
            print(product_html)

            product_html_soup = BeautifulSoup(product_html, 'lxml')
            product_html_result = product_html_soup.find('table', id_='prodDetails')
            print(product_html_result)
            #brand = product_html_result.find('tr', class_='a-spacing-small po-brand').text
            #brand = brand.find('td', class_='a-span9').text
            #brand = brand.find('span', class_='a-size-base po-break-word').text
        except Exception as e:
            print(str(e))
        '''
        results_list.append({
            'Title': title.strip(),
            'Rating': rating.strip(),
            'Reviews': reviews.strip(),
            'Current Price': current_price.strip(),
            'Original Price': original_price_value.strip(),
            'Product Link': f'https://www.amazon.com.br{product_link}'
        })
        '''
        with open(f'../results/amazon-result-{index}.txt', 'w') as f:
            #f.write(f'Brand: {brand.strip()} \n')
            f.write(f'Title: {title.strip()} \n')
            f.write(f'Rating: {rating.strip()} \n')
            f.write(f'Reviews: {reviews.strip()} \n')
            f.write(f'Current Price: {current_price.strip()} \n')
            
            if original_price_value:
                f.write(f'Original Price: {original_price_value.strip()} \n')
            
            f.write(f'Product Link: https://www.amazon.com.br{product_link}')
        '''

    return results_list

find_products()

print(results_list)

'''
if __name__ == '__main__':
    while True:
        find_products()
        time.sleep(60)
'''