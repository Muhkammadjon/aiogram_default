import sqlite3
from random import choices


class Database:
    def __init__(self, path_to_db="databases/database.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parametrs)
        data = None
        if commit:
            data = connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        # connection.close()
        cursor.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users( 
        id int NOT NULL, 
        name varchar(255) NOT NULL,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, name: str):
        sql = """
        INSERT INTO Users (id, name)
        VALUES (?, ?)
        """
        parametrs = (id, name)
        self.execute(sql, parametrs=parametrs, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parametrs
        ])
        return sql, tuple(parametrs.values())

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parametrs = self.format_args(sql, kwargs)
        return self.execute(sql, parametrs, fetchone=True)

def logger(statement):
    print(f"""
========================================================================================================================
Executing:
{statement}
========================================================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
