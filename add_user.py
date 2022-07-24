import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import pandas as pd


class UserLibrary():
    def __init__(self):
        try:
            self.myconn = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '1312',
                database = 'db_lms'
            )
            print("\nMySQL database connection successfull")

        except Error as err:
            print(f"Error: {err}")
    
    def add_user(self):
        self.name = input('\nMasukkan nama user: ')
        self.tanggal_lahir = input("Masukkan tanggal laahir (YYYY-MM-DD): ")
        self.pkj = input("Pekerjaan: ")
        self.almt = input("Masukkan Alamat: ")

        mycursor = self.myconn.cursor()

        sql_insert_query = "INSERT INTO user VALUES ('0','"+self.name+"','"+self.tanggal_lahir+"','"+self.pkj+"','"+self.almt+"');"

        try:
            mycursor.execute(sql_insert_query)
            self.myconn.commit()
            print(("Query berhasil dieksekusi\n..............\nData berhasil ditambahkan!"))

        except mysql.connector.Error as err:
            print("Failed to insert query into user table {}". format(err))
    
    def view_user(self):
        mycursor = self.myconn.cursor()

        sql_query = pd.read_sql('SELECT * FROM user', self.myconn)

        df = pd.DataFrame(sql_query, columns = ['id_user', 'u_name', 'tgl_lahir', 'pekerjaan', 'alamat'])

        print(df)


