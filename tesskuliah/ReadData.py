# Mengimpor modul mysql.connector untuk berinteraksi dengan database MySQL
import mysql.connector

# Menghubungkan ke database MySQL dengan parameter host, user, dan password
mydb = mysql.connector.connect(
  host="127.0.0.1",     # Alamat IP host database
  user="root",          # Nama pengguna database
  password=""            # Kata sandi database (kosong dalam contoh ini)
)
mycursor = mydb.cursor() # Membuat objek cursor untuk menjalankan perintah SQL

# mycursor.execute("SELECT * FROM master")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# Membuat dan menjalankan perintah SQL SELECT untuk mengambil data tertentu dari tabel "master"
mycursor.execute("SELECT Nama, Harga from master") 
myresult = mycursor.fetchall() # Mengambil semua hasil dari perintah SQL SELECT
for i in myresult: # Menampilkan hasil query
    print(i)
    mydb.close # Menutup koneksi ke database setelah selesai menggunakan data