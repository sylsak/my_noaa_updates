import requests
from bs4 import BeautifulSoup

class NOAAScraper:

    def __init__(self, noaa_content_url):
        self.url = noaa_content_url

    def call_webpage(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.find('pre').text

        except requests.exceptions.ConnectionError as conn_error:
            print(f"Connection Error {conn_error}")
            raise

        except requests.exceptions.HTTPError as http_error:
            print(f"Http Error {http_error}")
            raise

        except requests.exceptions.Timeout as timeout_error:
            print(f"Timeout Error {timeout_error}")
            raise




