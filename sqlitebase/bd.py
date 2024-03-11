import sqlite3


class BotDB:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id) -> bool:
        self.cursor.execute("SELECT telegramID from user_info WHERE 'telegramID' = ?", (user_id,))
        if self.cursor.fetchone() is None:
            print('Добавляем вас в базу данных...')
            self.cursor.execute("INSERT INTO user_info VALUES (?)", (user_id,))
            print('Внесли вас в базу данных!')
        else:
            pass

    def add_item(self, product, price):
        self.cursor.execute()                   