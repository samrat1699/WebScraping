from bs4 import BeautifulSoup
import requests

try:     
    source = requests.get('https://www.rokomari.com/list/42757/%E0%A6%B6%E0%A7%87%E0%A6%B7+%E0%A7%A7+%E0%A6%AC%E0%A6%9B%E0%A6%B0%E0%A7%87%E0%A6%B0+%E0%A6%B0%E0%A6%95%E0%A6%AE%E0%A6%BE%E0%A6%B0%E0%A6%BF%E0%A6%B0+%E0%A6%AC%E0%A7%87%E0%A6%B8%E0%A7%8D%E0%A6%9F%E0%A6%B8%E0%A7%87%E0%A6%B2%E0%A6%BE%E0%A6%B0+%E0%A6%AC%E0%A6%87%E0%A6%B8%E0%A6%AE%E0%A7%82%E0%A6%B9')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    #print(soup)

    books = soup.find('div', class_ = 'container').find_all('div')
    #print(len(books))

    for book in books:
        title = book.find('div', class_ = 'book-list-wrapper ')
        print(title)
        break



except Exception as e:
    print(e)    
