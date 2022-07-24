import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd


class ReturnBook():
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
    
    def return_book(self):
        self.id_peminjam = input('\nMasukkan id peminjam: ')
        self.id_book = input('Masukkan id buku: ')
        

        mycursor = self.myconn.cursor()

        sql_query_peminjam = "DELETE from peminjam WHERE id_user="+self.id_peminjam+""
        sql_query_book = "UPDATE book SET stock = stock WHERE id_buku="+self.id_book+""

        try:
            mycursor.execute(sql_query_peminjam)
            mycursor.execute(sql_query_book)
            self.myconn.commit()
            print(f"Query berhasil dieksekusi\n..............\nBuku telah dikembalikan")
        except mysql.connector.Error as err:
            print("Failed to insert query into user table {}". format(err))