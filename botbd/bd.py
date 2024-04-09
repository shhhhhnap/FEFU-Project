import sqlite3


class BotDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id) -> bool:
        result = self.cursor.execute("SELECT telegramID FROM usersTG WHERE  telegramID = ?", (user_id,))
        if bool(len(result.fetchall())) == False:
             return False
        return True
    
    def add_user(self, user_id):
            self.cursor.execute("INSERT INTO usersTG(telegramID) VALUES (?)", (user_id,))
            self.conn.commit()
