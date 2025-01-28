import requests
from bs4 import BeautifulSoup

def scrape():
    url = 'https://www.reddit.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    print(soup)

    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print('*********Title*********** ', title)
    print('*********Text*********** ',text)
    print('*********Link*********** ',link)

if __name__ == '__main__':
    scrape()