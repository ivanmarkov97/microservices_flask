import typing as t

from pymysql import connect

from .domain import User


class DBConnector:

    def __init__(self, config: dict):
        self.config = config

    def get_user(self, login: str, password: str) -> t.Optional[User]:
        connection = connect(**self.config)
        cursor = connection.cursor()
        sql_statement = """
            SELECT 
                login, 
                password, 
                name 
            FROM users
            WHERE 1=1
                AND login='{login}'
                AND password='{password}'
        """.format(login=login, password=password)

        cursor.execute(sql_statement)
        schema = [column[0] for column in cursor.description]
        db_result = cursor.fetchone()

        user = None
        if db_result:
            user = User(**dict(zip(schema, db_result)))

        cursor.close()
        connection.close()

        return user
