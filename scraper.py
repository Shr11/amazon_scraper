import requests
from bs4 import BeautifulSoup

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0',
    'Accept-language': 'en-US, en;q=0.5'
}

def get_product_details(product_url: str) -> dict:
        try:
            product_details = {}
            
            page = requests.get(product_url, headers=headers)
            soup = BeautifulSoup(page.content, features='lxml')
            title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
            extracted_price = soup.find('span', attrs={'class': 'a-price'}).get_text().strip()
            price = '$' + extracted_price.split('$')[1]
            
            # Adding it to the product details dictionary
            product_details['title'] = title
            product_details['price'] = price
            
            return product_details
        except Exception as e:
            print(f"failed with exception {e}")
            
            
url = input("Enter the URL of the product: ")
details = get_product_details(url)

print(details)