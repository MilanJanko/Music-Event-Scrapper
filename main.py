import requests
import selectorlib


url = "http://programmer100.pythonanywhere.com/tours/"
headers = HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; '
                  'Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """ Scrape the page source from given url"""
    response = requests.get(url, headers=headers)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


if __name__ == '__main__':
    scrapped = scrape(url)
    extracted = extract(scrapped)
    print(extracted)
