import requests
from stem import Signal
from stem.control import Controller
import argparse

def connect_tor():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_password')  # Replace with your Tor password
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        raise RuntimeError(f'Error connecting to Tor: {str(e)}')

def scrape(url):
    try:
        connect_tor()
        response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        return response.text
    except requests.RequestException as e:
        raise RuntimeError(f'Error fetching URL: {str(e)}')

def main():
    parser = argparse.ArgumentParser(description='Scrape data from an onion URL.')
    parser.add_argument('--url', required=True, help='Onion URL to scrape')
    args = parser.parse_args()

    try:
        html = scrape(args.url)
        print(html)
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
