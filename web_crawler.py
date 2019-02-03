import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def filter_ref(full_url, ref):
    fine_ref = ""

    # starts with one back slash '/'
    # '/home/login.php'
    if ref[:1] == "/" and ref[:2] != "//" :
        fine_ref = urlparse(full_url).scheme +  "://" + urlparse(full_url).netloc + ref

    # starts with two bslashes '//'
    # '//www.youtube.com/upload'
    elif ref[:2] == "//" :
        fine_ref = urlparse(full_url).scheme + ":" + ref
   
    # start with a dot slash './'
    # './about.php'
    elif ref[:2] == "./" :
        fine_ref = urlparse(full_url).scheme + "://" + urlparse(full_url).netloc + urlparse(full_url).path + ref[2:]

    # starts with a anchor '#'
    # '#sectionB'

    elif ref[0] == "#" :
        fine_ref = urlparse(full_url).scheme + "://" + urlparse(full_url).netloc + urlparse(full_url).path + ref

    # starts with two dots and slash '../'
    # '../link.html'

    elif ref[:3] == "../" :
        fine_ref = urlparse(full_url).scheme + "://" + urlparse(full_url).netloc + "/" + ref

    # javascript links
    elif ref[:11] == "javascript:" :
        return ""

    # missing scheme and host on url
    # 'page.php'
    elif ref[:5] != "https" and ref[:4] != "http" :
        fine_ref = urlparse(full_url).scheme + "://" + urlparse(full_url).netloc + "/" + ref

    # already fine ref
    elif ref[:5] == "https" or ref[:4] == "http" :
        fine_ref = ref

    return fine_ref


def main():
    #first_url = input("Enter the first url: ")
    first_url = "http://localhost:8080/"
    print("Looking up for: " + first_url)
    r = requests.get(first_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # array_links = []
    # searched_links = []
    
    for link in soup.find_all('a'):
        fine_ref = filter_ref(first_url, link.get('href'))
        print(fine_ref)


if __name__ == "__main__":
    main()