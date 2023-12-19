# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Mengimpor modul mysql.connector untuk berinteraksi dengan database MySQL
import mysql.connector

# Menghubungkan ke database MySQL dengan parameter host, user, password, dan database
mydb = mysql.connector.connect(
    host="127.0.0.1",   # Alamat IP host database
    user="root",        # Nama pengguna database
    password="",        # Kata sandi database 
    database="dbsCoba"  # Nama database yang digunakan
)

# Membuat objek cursor untuk menjalankan perintah SQL
xcursor=mydb.cursor()

# Membuat tabel "Master" dalam database dengan kolom-kolom yang ditentukan
tblMaster=""" CREATE TABLE Master (
Kode_Brg varchar(10) NOT NULL,
Nama varchar(50) NOT NULL,
Satuan varchar(25) NOT NULL,
Stok Int(4) NOT NULL,
Harga Decimal(8) NOT NULL,
Keterangan varchar (50))
"""

# Membuat tabel "Jual" dalam database dengan kolom-kolom yang ditentukan
xcursor.execute(tblMaster)
tblJual=""" CREATE TABLE Jual (
Kode_Brg varchar(10) NOT NULL,
No_Fak varchar(10) NOT NULL,
Jumlah int(4) NOT NULL,
Harga Decimal(8) NOT NULL,
Keterangan varchar (50))
"""
xcursor.execute(tblJual)

# Menampilkan pesan bahwa tabel telah berhasil dibuat
print("Tabel Berhasil Dibuat")