import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd
from datetime import date as dt
from datetime import timedelta as td


class IssueBook():
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
    
    def issue_book(self):
        self.id_peminjam = input('\nMasukkan id peminjam: ')
        self.id_buku = input('Masukkan id buku: ')
        self.nama_peminjam = input('Masukkan nama peminjam: ')
        self.nama_buku = input('Masukkan nama buku: ')
        begin_date = dt.today() # setiap input dimasukkan akan otomatis memasukkan tanggal saat itu
        end_date = begin_date + td(days=7) # setiap buku yang dipinjam akan berdurasi 7 hari untuk pengembalian
        

        mycursor = self.myconn.cursor()

        sql_insert_query = "INSERT INTO peminjam VALUES ('"+self.id_peminjam+"','"+self.id_buku+"','"+self.nama_peminjam+"','"+self.nama_buku+"','"+str(begin_date)+"','"+str(end_date)+"');"
        sql_query_update = "UPDATE book SET stock = stock - 1 WHERE id_buku="+self.id_buku+""
        try:
            mycursor.execute(sql_insert_query)
            mycursor.execute(sql_query_update)
            self.myconn.commit()
            print(f"Query berhasil dieksekusi\n..............\nBuku dipinjamkan ke :{self.nama_peminjam}\n..............")
        except mysql.connector.Error as err:
            print("Failed to insert query into user table {}". format(err))
    
    def view_issue(self):
        sql_query = pd.read_sql('SELECT * FROM peminjam', self.myconn)

        df = pd.DataFrame(sql_query, columns = ['id_user', 'id_buku', 'nama_user', 'nama_buku', 'tanggal_pinjam', 'tanggal_pengembalian'])
        print(df)