import mysql.connector 
from mysql.connector import Error

def create_db_connection(host_name='localhost', user_name='root', user_password='1312', db_name='db_lms'):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name)
        print("MySQL database connection successfull")
    except Error as err:
        print(f"Error: {err}")
    return connection





