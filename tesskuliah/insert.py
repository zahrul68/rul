# Mengimpor modul mysql.connector untuk berinteraksi dengan database MySQL
import mysql.connector

# Menghubungkan ke database MySQL dengan parameter host, user, password, dan database
mydb = mysql.connector.connect(
    host="127.0.0.1",   # Alamat IP host database
    user="root",        # Nama pengguna database
    password="",        # Kata sandi database 
    database="dbsCoba"  # Nama database yang digunakan
)

# Membuat objek cursor untuk memasukkan data ke dalam tabel
myinsert = mydb.cursor()

# memambahkan data hanya 1
#  Contoh pemasukan     satu data ke tabel "master" menggunakan query langsung
# myquery = """INSERT INTO master VALUES ("A01", "Mouse", "Unit", 10, 250000,"Samsung")""" 


#menambah data dengan banyak
# Contoh pemasukan banyak data ke tabel "master" menggunakan query parameterized
myquery = """INSERT INTO master VALUES (%s,%s,%s,%s,%s,%s)"""
dataInsert = [
    ("B01", "Mainboard", "Unit", 10, 500000, "Asus"),
    ("c01", "Monitor", "Unit", 5, 1500000, "LG 24 INC"),
    ("D01", "Notebook", "Unit", 3, 3500000, "Macbook Pro m3"),
    ("D01", "Netbook", "Unit", 5, 5500000, "Asus 360")]

#yang ini satu
# myinsert.execute(myquery) 

#yang ini banyak
myinsert.executemany(myquery, dataInsert) # Menggunakan metode executemany untuk memasukkan banyak data sekaligus
mydb.commit()  # Melakukan commit untuk menyimpan perubahan ke dalam database
print("Data Berhasil ditambahkan")