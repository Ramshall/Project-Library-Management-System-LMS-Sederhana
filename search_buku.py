import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd


class BookSearch():
    def __init__(self):
        try:
            self.myconn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1312',
                database = 'db_lms')
            print("\nMySQL database connection successfull")
        except Error as err:
            print(f"Error: {err}")
    
    def search_book(self):
        self.book_name = input('Masukkan nama buku: ')

        try:
            sql_query = pd.read_sql("SELECT * FROM book WHERE nama_buku='"+self.book_name+"'", self.myconn)
            df = pd.DataFrame(sql_query, columns = ['id_buku', 'nama_buku', 'kategori', 'stock'])
            print('..............................')
            print(df)
        except mysql.connector.Error as err:
            print("Failed to insert query into user table {}". format(err))
