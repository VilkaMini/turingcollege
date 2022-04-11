import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import math
import sys

def scraper(number: int, keyword: str) -> pd.DataFrame:
  """Scrapes Shein clothes store using 2 step process
  
  Step 1:
  Finds a url of a garment by searching fora given keyword
  Step 2:
  Goes through the pages of that garment and collects title, price, item and image urls
  """
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  url = "https://eur.shein.com/"
  browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
  browser.get(url)
  html = browser.page_source

  main_page_soup = BeautifulSoup(html, "html.parser")
  a_tag = main_page_soup.find("a", title=keyword)
  try:
    keyword_href = a_tag['href']
  except:
    return "No such category"

  items_dict = {"category": [], "title": [], "price": [], "item_url": [], "image_url": []}
  for n in range(1, 1+math.ceil(number/120)):
    browser.get(keyword_href+f"&page={n}")
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("section", class_="S-product-item j-expose__product-item product-list__item"):
      item_found = item.find("a")
      items_dict["category"].append(keyword)
      items_dict["title"].append(item_found['data-title'])
      items_dict["price"].append(item_found['data-price'])
      items_dict["item_url"].append("https://eur.shein.com" + item_found['href'])
      items_dict["image_url"].append(item_found.find("img")['src'])
  
  return pd.DataFrame(items_dict)