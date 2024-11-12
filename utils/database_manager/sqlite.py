import sqlite3
class Database:  #Bu klass ma'lumotlar bazasi bilan bog'liq barcha funksiyalarni o'z ichiga oladi.
    def __init__(self, path_to_db="main.db"): #Bu yerda ma'lumotlar bazasi faylining manzili (path_to_db) beriladi. Agar berilmasa, main.db fayli ishlatiladi.
        self.path_to_db = path_to_db
    @property
    def connection(self): # Ma'lumotlar bazasiga ulanish.
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit: # Agar commit talab qilinsa, o'zgarishlarni saqlaymiz.
            connection.commit()
        if fetchall: # Agar barcha natijalarni olish kerak bo'lsa:
            data = cursor.fetchall() #barch natijalrni olamiz
        if fetchone: # Agar faqat bitta natija kerak bo'lsa:
            data = cursor.fetchone() #faqat bitta natijani olamiz
        connection.close() # Ma'lumotlar bazasiga bo'lgan aloqani yopamiz.
        return data #natijalarni qayytaramiz

    def users_table(self):
        sql = """
               CREATE TABLE IF NOT EXISTS Users (
               id SERIAL PRIMARY KEY,
               fullname VARCHAR(255) NULL,
               telegram_id BIGINT NOT NULL UNIQUE,
               language VARCHAR(3)
               );
               """
        self.execute(sql, commit=True)

    def channels_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Channels (
                 id SERIAL PRIMARY KEY,
                 channel_name NOT NULL,
                 channel_id NOT NULL,
                 channel_members_count NOT NULL
                 );
                 """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([ # Berilgan parametrlar bo'yicha SQL so'rovini formatlaymiz.
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int = None, fullname: str = None, telegram_id: str = None , language: str = 'en'):
        sql = """
        INSERT INTO Users(id, fullname,telegram_id, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id,fullname,telegram_id,language), commit=True)

    def add_channel(self,id: int = None, channel_name: str = None, channel_id: str = None, channel_members_count: int = None):
        sql = """
        INSERT INTO Channels(id, channel_name, channel_id, channel_members_count) VALUES(?, ?, ?, ?)
        """
        self.execute(sql,parameters=(id,channel_name,channel_id,channel_members_count), commit=True)

    def delete_channel(self,channel_id):
        sql = """
        DELETE FROM Channels WHERE channel_id = ?
        """
        self.execute(sql, parameters=(channel_id,), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_all_channels(self):
        sql = """
        SELECT * FROM Channels
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def get_user_language(self, telegram_id: int):
        sql = """
        SELECT language FROM Users WHERE telegram_id = ? 
        """
        result = self.execute(sql, parameters=(telegram_id,), fetchone=True)
        return result[0]  # qaytarilgan natijadan tilni olish

    def select_channel(self, **kwargs):
        sql = "SELECT * FROM Channels WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_language(self, langauge,telegram_id):
        sql = f"""
        UPDATE Users SET language=? WHERE telegram_id=?
        """
        return self.execute(sql, parameters=(langauge,telegram_id), commit=True)