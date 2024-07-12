import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def simple_request():
    response = requests.get('https://example.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title from requests/BeautifulSoup:", soup.title.string)

def selenium_test():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://example.com')
    print("Title from Selenium:", driver.title)
    driver.quit()

if __name__ == "__main__":
    print("Starting simple scraper test...")
    simple_request()
    selenium_test()
    print("Scraper test completed.")