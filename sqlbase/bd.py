import sqlite3


class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id) -> bool:
        """Проверяем, есть ли юзер в БД"""
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Получаем  ID юзера"""
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id):
        """Добавляем Юзера в БД"""
        self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
        return self.conn.commit()

    def add_item(self, item, price):
        """Добавляем Товар и Цену в БД"""
        self.cursor.execute("INSERT INTO 'users' ('item', 'price') VALUES (?, ?)", (item, price))
        return self.conn.commit()

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()
