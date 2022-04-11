# Database and web-scraping related functions
This repository is for functions used in 2.2.5 project by Turing College.

This repository and it's functions are designed to work in a google colab environment.

## Instalation:
```python
!pip install psycopg2
!pip install -U selenium
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import sys
import psycopg2
import pandas as pd
import numpy as np

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

!git clone https://github.com/VilkaMini/tc-225-files

!mv /content/tc-225-files/database.py /content/database.py
!mv /content/tc-225-files/sheinscraper.py /content/sheinscrapers.py

# After completing the above steps, populate database.py file with your database credentials
```

## Importing and using database functions:
```python
from database import create_tables, fill_table, fill_categories, get_data

# Creates items and categories tables
create_tables()

# Inserts categories (array) into categories table
fill_categories(['Skirts', 'T-Shirts', 'Dresses'])

# Inserts data from pandas dataframe to the sql database
df = pd.DataFrame(
    {'category': 'Skirt',
     'title': 'Some random skirt',
     'price': 12.99,
     'item_url': 'https://eur.shein.com/...',
     'image_url': '//img.ltwebstatic.com/images3_pi/...'
    }
)
fill_table(df)

# Gets data from items and category tables:
df = get_data()
```
## Importing and using scraper function:
```python
from sheinscrapers import scraper

# Scrapes shein site with given parameters and return a pandas DataFrame:

n = 3000 # Numbers of examples to scrape
keyword = "Blouses"

df = scraper(n, keyword)
```

## License:
The MIT License (MIT). Please see the license file for more information.