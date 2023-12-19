# Mengimpor modul mysql.connector untuk berinteraksi dengan database MySQL
import mysql.connector

# Menghubungkan ke database MySQL dengan parameter host, user, dan password
mydb = mysql.connector.connect(
  host="127.0.0.1",     # Alamat IP host database
  user="root",          # Nama pengguna database
  password=""            # Kata sandi database (kosong dalam contoh ini)
)


# Membuat objek cursor untuk menjalankan perintah SQL
mycursor = mydb.cursor()


# Menjalankan perintah SQL untuk membuat database baru dengan nama "dbsCoba"
mycursor.execute("CREATE DATABASE dbsCoba")   