import requests
from bs4 import BeautifulSoup


def main():
    first_url = input("Enter the first url: ")
    print("Looking up for: " + first_url)
    r = requests.get(first_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # array_links = []
    # searched_links = []
    
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == "__main__":
    main()