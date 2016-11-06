from bs4 import BeautifulSoup
import argparse
import urllib2
import urllib

def main():
    parser = argparse.ArgumentParser(description='Fetches all .pdf files from a link, faster than ligh...sound')
    parser.add_argument('link', metavar='link', type=str, nargs='+',
                       help='Link to fetch pdf files from.')


    args = parser.parse_args()

    url = (args.link[0])
    print(url)
    page=urllib2.urlopen(url)

    soup = BeautifulSoup(page.read(), "html.parser")
    links = soup.find_all('a')

    for l in links:
        if '.pdf' in l["href"]:
            if 'http' not in l:
                urllib.urlretrieve(url + l["href"], str(l["href"]) )
            else:
                urllib.urlretrieve(l["href"], str(l["href"]))
