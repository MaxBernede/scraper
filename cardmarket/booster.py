from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def start(conn, driver):
    try:
        # Wait for the table-body class to load (adjust the wait time if necessary)
        table_body = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table-body"))
        )
        # Find all card containers (divs or rows inside the table-body)
        cards = table_body.find_elements(By.CLASS_NAME, "row")
        print(f"Number of cards found: {len(cards)}")
        # Loop through the cards and get names and prices
        for card in cards:
            try:
            # Find the <a> tag for the card name and link
                name_div = card.find_element(By.CSS_SELECTOR, ".col-12.col-md-4.px-2.flex-column.align-items-start.justify-content-center")
                a_tag = name_div.find_element(By.TAG_NAME, "a")
                card_name = a_tag.text.strip()
                card_link = a_tag.get_attribute("href")  # Get the href attribute for the link

                # Find the corresponding price div with class "col-price"
                price_div = card.find_element(By.CLASS_NAME, "col-price")
                card_price = price_div.text.strip()

                # Output the card name, link, and price
                cursor.execute('''
                INSERT INTO booster (card_name, card_link, card_price)
                VALUES (?, ?, ?)
                ''', (card_name, card_link, card_price))

                # Commit the transaction
                conn.commit()
                print(f"Card found: {card_name}\nLink: {card_link}\nPrice: {card_price}")
            except Exception as e:
                continue
    finally:
        print("one page done")

def loop(conn, url):
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()
    for i in range(1, 15):
        driver.get(url + str(i))
        time.sleep(1)
        start(conn, driver)


# https://www.cardmarket.com/en/Pokemon/Products/Boosters
# https://www.cardmarket.com/en/Pokemon/Products/Boosters?site=2
if __name__ == "__main__":
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('datas.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS booster (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_name TEXT NOT NULL,
            card_link TEXT NOT NULL,
            card_price TEXT NOT NULL
        )
    ''')
    conn.commit()
    loop(conn, "https://www.cardmarket.com/en/Pokemon/Products/Boosters?site=")