import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


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
    #first_url = input("Enter the first url: ")
    first_url = "http://www.coltec.ufmg.br/coltec-ufmg/"
    print("Looking up for: " + first_url)
    r = requests.get(first_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # array_links = []
    # searched_links = []
    
    for link in soup.find_all('a'):
        fine_ref = filter_ref(first_url, link.get('href'))
        print(fine_ref)
        

'''
    foreach ($linklist as $link) {
            // If the link isn't already in our crawl array add it, otherwise ignore it.
            if (!in_array($l, $already_crawled)) {
                    $already_crawled[] = $l;
                    $crawling[] = $l;
                    // Output the page title, descriptions, keywords and URL. This output is
                    // piped off to an external file using the command line.
                    echo get_details($l)."\n";
            }
        }
        // Remove an item from the array after we have crawled it.
        // This prevents infinitely crawling the same page.
        array_shift($crawling);
        // Follow each link in the crawling array.
        foreach ($crawling as $site) {
            follow_links($site);
        }
'''


if __name__ == "__main__":
    main()