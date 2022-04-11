import psycopg2
import pandas as pd

database = ""
user=""
password=""
host=""
port=""

def create_tables() -> str:
  '''Creates items and categories tables'''
  connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
  )
  cur = connection.cursor()

  try:
    cur.execute('''
    CREATE TABLE categories (
      id serial PRIMARY KEY,
      category VARCHAR(50)
    );
    ''')

    cur.execute('''
    CREATE TABLE items (
      id serial PRIMARY KEY,
      title VARCHAR(100),
      price DECIMAL (6, 2),
      item_url VARCHAR(300),
      image_url VARCHAR(300),
      category_id INT
    );
    ''')

    cur.execute('''
    ALTER TABLE items 
    ADD FOREIGN KEY (category_id) 
    REFERENCES categories(id);
    ''')

    connection.commit()

  except:
    cur.close()
    connection.close()
    return "Tables already exist"

  cur.close()
  connection.close()
  return "Tables created"

def fill_categories(array: [str]) -> str:
  '''Inserts given categories into categories table'''
  connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
  )
  cur = connection.cursor()

  for categor in array:
    cur.execute(f'''
    INSERT INTO categories (category) 
    VALUES ('{categor}');
    ''')

  connection.commit()

  cur.close()
  connection.close()
  return "Categories added"

def fill_table(df: pd.DataFrame) -> str:
  '''Inserts data into items table'''
  connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
  )
  cur = connection.cursor()

  for index, row in df.iterrows():
    cur.execute(f'''
    INSERT INTO items(title, price, item_url, image_url, category_id)
    VALUES ('{row['title']}', {row['price']}, '{row['item_url']}', '{row['image_url']}', {row['category_nr']});
    ''')
  
  connection.commit()

  cur.close()
  connection.close()
  return "Database rows added"

def get_data() -> pd.DataFrame:
  '''Gets all relevant data from items and categories tables'''
  connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
  )
  cur = connection.cursor()

  cur.execute('''
  SELECT items.title, items.price, items.item_url, items.image_url, categories.category
  FROM items 
  LEFT JOIN categories 
  ON categories.id = items.category_id
  ''')

  df = pd.DataFrame(cur.fetchall())

  connection.commit()

  cur.close()
  connection.close()
  return df