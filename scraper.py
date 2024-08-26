import requests
from stem import Signal
from stem.control import Controller
import argparse

def connect_tor():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Replace with your Tor password
        controller.signal(Signal.NEWNYM)

def scrape(url):
    connect_tor()
    response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
    return response.text

def main():
    parser = argparse.ArgumentParser(description='Scrape data from an onion URL.')
    parser.add_argument('--url', required=True, help='Onion URL to scrape')
    args = parser.parse_args()

    html = scrape(args.url)
    print(html)

if __name__ == '__main__':
    main()

