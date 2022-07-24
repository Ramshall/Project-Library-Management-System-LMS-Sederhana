from sqlite3 import sqlite_version_info
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd


class BookLibrary():
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
    
    def add_book(self):
        self.kode_buku = input('\nMasukkan kode buku: ')
        self.book_name = input('Enter book name: ')
        self.category = input('Masukkan kategori buku: ')
        self.stock = input('Stok buku: ')
        
        mycursor = self.myconn.cursor()

        sql_insert_query = "INSERT INTO book VALUES ('"+self.kode_buku+"','"+self.book_name+"','"+self.category+"','"+self.stock+"');"

        try:
            mycursor.execute(sql_insert_query)
            self.myconn.commit()
            print("Query berhasil dieksekusi\n..............\nData entered successfully")
        except mysql.connector.Error as err:
            print("Failed to insert query into user table {}". format(err))
    
    def view_book(self):
        mycursor = self.myconn.cursor()

        sql_query = pd.read_sql('SELECT * FROM book', self.myconn)

        df = pd.DataFrame(sql_query, columns = ['id_buku', 'nama_buku', 'kategori', 'stock'])
        print(df)