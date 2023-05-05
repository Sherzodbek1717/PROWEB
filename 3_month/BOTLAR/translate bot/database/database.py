import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_user_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users(
            telegram_id BIGINT PRIMARY KEY,
            user_name VARCHAR(100),
            phone_number VARCHAR(15)
        )'''
        self.execute(sql, commit=True)

    def insert_telegram_id(self, telegram_id):
        sql = ''' INSERT INTO users(telegram_id) VALUES (?)
        ON CONFLICT DO NOTHING'''
        self.execute(sql, parameters=(telegram_id,), commit=True)

    def check_user(self, telegram_id):
        sql = '''SELECT user_name, phone_number FROM users
        WHERE telegram_id = ?
        '''
        return self.execute(sql, parameters=(telegram_id,), fetchone=True)

    def register(self, user_name, phone_number, telegram_id):
        sql = '''UPDATE users SET username = ?, phone_number = ?, WHERE telegram_id = 2'''
        self.execute(sql, parameters=(user_name, phone_number, telegram_id), commit=True)


        











