import sqlite3


class BotDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def product_exists(self, product_url):
         result = self.cursor.execute("SELECT url FROM usersTG WHERE  url = ?", (product_url,))
         if bool(len(result.fetchall())) == False:
              return False
         return True
    
    def add_product(self, id, product_name, product_price, url):
         self.cursor.execute("INSERT INTO usersTG(telegramID, product_name, product_price, url) VALUES (?, ?, ?, ?)", (id, product_name, product_price, url,))
         self.conn.commit()


