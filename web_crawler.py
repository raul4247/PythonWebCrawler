import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import deque
from urllib.request import urlopen

array_links = []
searched_links = []

def look_up():
    for link in array_links:
        r = urlopen(link)
        r_str = r.read()
        soup = BeautifulSoup(r_str, 'html.parser')

        for intern_link in soup.find_all('a'):
            fine_ref = filter_ref(link, intern_link.get('href'))
            array_links.append(link)
    

        if link not in searched_links:
            searched_links.append(link)

    array_links.pop(0)
    look_up()

def filter_ref(full_url, ref):
    fine_ref = ""
    # NoneType filtering
    if ref is None:
        return ""

    # starts with one back slash '/'
    # '/home/login.php'
    if ref[:1] == "/" and ref[:2] != "//" :
        fine_ref = urlparse(full_url).scheme +  "://" + urlparse(full_url).netloc + ref

    # starts with two bslashes '//'
    # '//www.youtube.com/upload'
    elif ref[:2] == "//" :
        fine_ref = urlparse(full_url).scheme + ":" + ref
   
    # starts with a dot slash './'
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
    # first_url = input("Enter the first url: ")
    first_url = "https://www.google.com.br"
    print("Looking up for: " + first_url)

    r = urlopen(first_url)
    r_str = r.read()
    soup = BeautifulSoup(r_str, 'html.parser')
    
    for link in soup.find_all('a'):
        fine_ref = filter_ref(first_url, link.get('href'))
        array_links.append(fine_ref)

    searched_links.append(first_url)    
    look_up()


if __name__ == "__main__":
    main()