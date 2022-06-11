import mysql.connector


class Database(object):
    def __init__(self, hostname, username, pword, database_name):
        self.connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=pword,
            database=database_name,
            auth_plugin='mysql_native_password'
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_cursor(self):
        return self.connection.cursor()
