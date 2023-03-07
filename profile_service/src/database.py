import typing as t

from pymysql import connect

from .domain import UserMainInfo, UserAdditionalInfo


class DBConnector:

    def __init__(self, config: dict):
        self.config = config

    def get_user_main_info(self, user_id: str) -> t.Optional[UserMainInfo]:
        connection = connect(**self.config)
        cursor = connection.cursor()
        sql_statement = """
            SELECT 
                login, 
                name 
            FROM users_profile
            WHERE 1=1
                AND user_id='{user_id}'
        """.format(user_id=user_id)

        cursor.execute(sql_statement)
        schema = [column[0] for column in cursor.description]
        db_result = cursor.fetchone()

        user_main_info = None
        if db_result:
            user_main_info = UserMainInfo(**dict(zip(schema, db_result)))

        cursor.close()
        connection.close()

        return user_main_info

    def get_user_additional_info(self, user_id: str) -> t.Optional[UserAdditionalInfo]:
        connection = connect(**self.config)
        cursor = connection.cursor()
        sql_statement = """
            SELECT 
                number_of_friends
            FROM users_profile_add
            WHERE 1=1
                AND user_id='{user_id}'
        """.format(user_id=user_id)

        cursor.execute(sql_statement)
        schema = [column[0] for column in cursor.description]
        db_result = cursor.fetchone()

        user_additional_info = None
        if db_result:
            user_additional_info = UserAdditionalInfo(**dict(zip(schema, db_result)))

        cursor.close()
        connection.close()

        return user_additional_info
