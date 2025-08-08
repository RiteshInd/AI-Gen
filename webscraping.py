from bs4 import BeautifulSoup
import requests
import pandas as pd
from io import StringIO

url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"

req=requests.get(url)

soup=BeautifulSoup(req.text, 'html.parser')
print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))
    
tags=soup("img")
for tag in tags:
    print(tag.get('src'),None)

table_html = str(soup.find("table", {"class": "wikitable"}))
df = pd.read_html(StringIO(table_html))[0]

df.to_csv("countries_and_capitals.csv", index=False)


# pip install selenium

# Also download ChromeDriver (must match your Chrome version) and add it to your system PATH, or specify the full path in the script.


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time

# # Set up Chrome in headless mode (no GUI)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # comment this if you want to see the browser
# chrome_options.add_argument("--disable-gpu")

# # Use ChromeDriver (you can set path here if not in PATH)
# driver = webdriver.Chrome(options=chrome_options)

# # Load the page
# url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"
# driver.get(url)

# # Wait for JS to load (if needed)
# time.sleep(3)

# # Get the fully rendered DOM
# full_dom = driver.page_source

# # Print or save it
# print(full_dom)

# # Always close the driver
# driver.quit()




# pip install playwright
# playwright install

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     page.goto("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages")
#     full_dom = page.content()
#     print(full_dom)
#     browser.close()


