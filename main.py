import requests
import selectorlib
from send_email import send_email

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
    """ Extract CSS selector from scrapped web page"""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def save (extracted):
    with open('data.txt', 'a') as file:
        file.write(extracted + '\n')


def read (extracted):
    with open('data.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    scrapped = scrape(url)
    extracted = extract(scrapped)
    print(extracted)
    content = read(extracted)
    if extracted != 'No upcoming tours!':
        if extracted not in content:
            save(extracted)
            message = f'Hey, new event was found!'
            send_email(message=message)
