import mysql.connector # Mengimpor modul mysql.connector untuk berinteraksi dengan database MySQLl``
from mysql.connector import Error
try:
    dbsKoneksi = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password="",
        database="dbsCoba")
    mycursor = dbsKoneksi.cursor()
    mySql_insert_kol = """INSERT INTO master VALUES (%s,%s,%s,%s,%s,%s)"""
# Variabel data
    kode_brg=input("Kode Barang = ")
    nama=input("Nama Barang = ")
    satuan = input("Satuan   =")
    stok = input("stok       =")    
    harga = input("Harga     =")
    keterangan = input("Keterangan  = ")
# Parameter Variabel input record data
    entry_records = (kode_brg, nama,satuan, stok,harga,keterangan)
    mycursor.execute(mySql_insert_kol,entry_records)
    dbsKoneksi.commit()
    print(mycursor.rowcount, "Record inserted successfully into master table")
    mycursor.close()
except mysql.connector.Error as error:
    print("Failed to insert record into master table {}".format(error))
finally:
    if dbsKoneksi.is_connected():
        dbsKoneksi.close()
        print("Mysql connection is closed")