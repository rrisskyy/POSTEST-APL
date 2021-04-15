import os
import mysql.connector

conn = mysql.connector.connect( host="localhost", user="root", password="", database="toko-pancing" )
mycursor = conn.cursor()

COLUMN = 7





def query(query):
    mycursor.execute(query)
    items = mycursor.fetchall()
    conn.commit()
    return items

  
items = query("SELECT * FROM tokopancing ORDER BY harga")
# "id": item[0][0],
# "jenis": item[0][1],
# "brand": item[0][2],
# "varian": item[0][3],
# "warna": item[0][4],
# "harga": item[0][5],
# "stok": item[0][6],


def clr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def header():
    return ("+____________________________________________________________________________________________________________________________________________________+\n" 
    + "|____ID_____|_______JENIS_______|__________BRAND__________|__________VARIAN__________|______WARNA______|______HARGA_______|___STOK___|____NO_SERI____|")
def footer():
    return ("+___________+___________________+_________________________+__________________________+_________________+__________________+__________+_______________+")





def spacing (item, i):
    a = ''
    if i < 9 :
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(7) + "|".ljust(3)
    if i >= 9:
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(6) + "|".ljust(3)
    a += str(item[i][1]).ljust(17) + "|".ljust(3)
    a += str(item[i][2]).ljust(23) + "|".ljust(3)
    a += str(item[i][3]).ljust(24) + "|".ljust(3)
    a += str(item[i][4]).ljust(15) + "|".ljust(3)
    a += "Rp. "+ str(item[i][5]).ljust(12) + "|".ljust(4)
    a += str(item[i][6]).ljust(7) + "|".ljust(3)
    a += str(item[i][0]).ljust(13) + "|".ljust(3)

    return a



def pembayaran(id, jenis, brand, varian, warna, harga, stok, totalHarga):
    result = query(f"SELECT * FROM tokopancing WHERE `id` = {id}")
    count = int(input("Berapa Buah? :   "))
    harga = result[0][5] * count
    totalHarga += harga
    print("Harga Barang  =  ", result[0][5], " x ", count, "  =  ", harga)
    return totalHarga
        



def daftarBarang(items):
    print(header())
    for i in range(len(items)) :
        print(spacing(items, i))
    print(footer())
        

def barangTersedia(items):
    barangKosong = 0
    print(header())
    for i in range(len(items)) :
        if (items[i][6] != 0) :
            # clr()
            print(spacing(items, i))
        else :
            barangKosong+=1
    print(footer())
    if (barangKosong == 0) : 
        print("\n\nKeterangan: \nSEMUA BARANG TERSEDIA!")
    

def barangKosong(items):
    barangKosong = 0
    print(header())
    for i in range(len(items)) :
        if (items[i][6] == 0) :
            print(spacing(items, i))
            barangKosong+=1
        else :
            continue
    print(footer())
    if (barangKosong == 0) : 
        print("\n\nKeterangan: \nTIDAK ADA BARANG KOSONG!")





def cari(items) :   
    keyword = input("\n\nKetikkan Sesuatu Untuk Mencari :     ") 
    param = f"SELECT * FROM tokopancing WHERE `jenis` LIKE '%{keyword}%' OR `brand` LIKE '%{keyword}%' OR `varian` LIKE '%{keyword}%' OR `warna` LIKE '%{keyword}%'"
    equalItems = query(param)
    clr()
    print(f"\n\n\nHasil Pencarian {keyword} : ")
    daftarBarang(equalItems)
    


def orderby(keyword, item):
    global items
    param = f"SELECT * FROM tokopancing ORDER BY {keyword}"
    item = query(param)
    items = item
    daftarBarang(items)





class Barang:
    def __init__(self, id, jenis, brand, varian, warna, harga, stok) :
        self.id = id
        self.jenis = jenis
        self.brand = brand
        self.varian = varian
        self.warna = warna
        self.harga = harga
        self.stok = stok

    def tambahBarang(self) :
        param = "INSERT INTO `tokopancing` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `stok`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.id, self.jenis, self.brand, self.varian, self.warna, self.harga, self.stok)
        mycursor.execute(param, val)
        conn.commit()
        print("Berhasil!!")

    def tambahStok(self) :
        stokBaru = int(input("Masukkan Jumlah Stok :    "))
        stokBaru += self.stok
        param = f"UPDATE `tokopancing` SET `stok` = {stokBaru} WHERE id = {self.id}"
        query(param)
        print("Berhasil!!")

    def ubahHargaBarang(self) : 
        hargaBaru = int(input("Masukkan Harga Baru :     "))
        param = "UPDATE tokopancing SET harga = {} WHERE id = {}".format(hargaBaru, self.id)
        query(param)
        print("Berhasil!!")

    def hapusBarang(self) :
        yakin = input("APAKAH ANDA YAKIN INGIN MENGHAPUS BARANG INI (Y/N) ? :    ")
        if (yakin.upper() == "Y") :
            param = "DELETE FROM tokopancing WHERE id = {}".format(self.id)
            query(param)
            print("Berhasil!!")
        elif (yakin.upper() == "N") :
            menu()
        else :
            print("Input yang anda Masukkan SALAH!")









def menu():
    items = query("SELECT * FROM tokopancing ORDER BY harga")
    # "id": item[0][0],
    # "jenis": item[0][1],
    # "brand": item[0][2],
    # "varian": item[0][3],
    # "warna": item[0][4],
    # "harga": item[0][5],
    # "stok": item[0][6],
    clr()
    print("SELAMAT DATANG DI TOKO PANCING".rjust(39))
    print("//=======================================================================================\\\\")
    print("||                                                                                       ||")
    print("||       1.  Pembayaran                                                                  ||")      # ✔
    print("||       2.  Lihat Daftar Barang                                                         ||")      # ✔
    print("||       3.  Lihat Barang Yang Masih Tersedia                                            ||")      # ✔
    print("||       4.  Lihat Barang Yang Kehabisan STOK                                            ||")      # ✔
    print("||       5.  Tambahkan Barang                                                            ||")      # ✔
    print("||       6.  Ubah Harga Barang                                                           ||")      # ✔
    print("||       7.  Hapus Barang                                                                ||")      # ✔
    print("||       8.  Cari Barang                                                                 ||")      # ✔
    print("||       9.  Urutkan Barang                                                              ||")         
    print("||       10. Tambah STOK                                                                 ||")         
    print("||       0.  Exit                                                                        ||")
    print("||                                                                                       ||")      
    print("\\\\=======================================================================================//\n")
    pil = input("Pilih Menu >>  ")



    if (pil == "1"):
        clr()
        daftarBarang(items)

        totalHarga = 0
        print("\nMasukkan Barang Yang Dibeli! ")
        print("Masukkan Angka 0 Jika Semua Barang Yang dibeli sudah dimasukkan")
        while(True) : 
            pil = int(input("\nMasukkan ID Barang  >>>        "))
            pil -= 1
            if(pil == -1) :
                print(f"Total Harga : {totalHarga}")
                break
            kwargs = {
                "id": items[pil][0],
                "jenis": items[pil][1],
                "brand": items[pil][2],
                "varian": items[pil][3],
                "warna": items[pil][4],
                "harga": items[pil][5],
                "stok": items[pil][6],
                "totalHarga": totalHarga
                }
            totalHarga += pembayaran(**kwargs)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "2"):
        clr()
        daftarBarang(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "3"):
        clr()
        barangTersedia(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "4"):
        clr()
        barangKosong(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "5"):
        jenis = input("Masukkan Jenis Barang :   ")
        brand = input("Masukkan Merk Barang :    ")
        varian = input("Masukkan Varian Barang :  ")
        warna = input("Masukkan Warna Barang :   ")
        harga = int(input("Masukkan Harga Barang :   "))
        stok = int(input("Masukkan Stok Barang :    "))
        barang = Barang(None, jenis, brand, varian, warna, harga, stok)
        barang.tambahBarang()
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "6"):
        clr()
        daftarBarang(items)

        pil = int(input("\nPilihlah Barang Yang Harganya Ingin anda ubah (ID) :      "))
        pil -= 1
        
        kwargs = {
            "id": items[pil][0],
            "jenis": items[pil][1],
            "brand": items[pil][2],
            "varian": items[pil][3],
            "warna": items[pil][4],
            "harga": items[pil][5],
            "stok": items[pil][6]
            }

        barang = Barang(**kwargs)
        barang.ubahHargaBarang()
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "7"):
        clr()
        daftarBarang(items)

        pil = int(input("\nPilihlah Barang Yang Ingin Anda Hapus (ID) :      "))
        pil -= 1

        kwargs = {
            "id": items[pil][0],
            "jenis": items[pil][1],
            "brand": items[pil][2],
            "varian": items[pil][3],
            "warna": items[pil][4],
            "harga": items[pil][5],
            "stok": items[pil][6]
            }
        
        barang = Barang(**kwargs)
        barang.hapusBarang()
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "8"):
        clr()
        daftarBarang(items)
        cari(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()       
    if (pil == "9"):
        clr()
        print("//=======================================================================================\\\\")
        print("||                                                                                       ||")
        print("||                                                                                       ||")
        print("||   1.  Urutkan Berdasarkan Jenis                                                       ||")      # ✔
        print("||   2.  Urutkan Berdasarkan Brand                                                       ||")      # ✔
        print("||   3.  Urutkan Berdasarkan Warna                                                       ||")      # ✔
        print("||   4.  Urutkan Berdasarkan Varian                                                      ||")      # ✔
        print("||   5.  Urutkan Berdasarkan Harga                                                       ||")      
        print("||                                                                                       ||")
        print("||                                                                                       ||")      
        print("\\\\=========================================================================+=============//\n")

        pilCari = input("ANDA INGIN MENGURUTKAN BERDASARKAN : ")
        orderby(pilCari.lower(), items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "10"):
        clr()
        daftarBarang(items)

        pil = int(input("\nPilihlah Barang Yang Ingin Anda Tambah (ID) :      "))
        pil -= 1

        kwargs = {
            "id": items[pil][0],
            "jenis": items[pil][1],
            "brand": items[pil][2],
            "varian": items[pil][3],
            "warna": items[pil][4],
            "harga": items[pil][5],
            "stok": items[pil][6]
            }
        barang = Barang(**kwargs)
        barang.tambahStok()
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu()
    if (pil == "0"):
        print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM!!!")
        exit
menu()
