import os
import mysql.connector

conn = mysql.connector.connect( host="localhost", user="root", password="", database="toko-pancing" )
mycursor = conn.cursor()


def clr():
   _ = os.system('clear') if os.name == 'posix' else os.system('cls')

def query(query):
    mycursor.execute(query)
    items = mycursor.fetchall()
    conn.commit()
    return items

param = "harga"  
items = query("SELECT * FROM barang ORDER BY " + param)
    # "id": item[0][0],
    # "jenis": item[0][1],
    # "brand": item[0][2],
    # "varian": item[0][3],
    # "warna": item[0][4],
    # "harga": item[0][5],
    # "stok": item[0][6],


itemsBulanan = query("SELECT * FROM bulanan ORDER BY " + param)



def header():
    return (" ____________________________________________________________________________________________________________________________________________________\n" 
          + "|____ID_____|_______JENIS_______|__________BRAND__________|__________VARIAN__________|______WARNA______|______HARGA_______|___STOK___|____NO_SERI____|")
def footer():
    return ("⊥___________⊥___________________⊥_________________________⊥__________________________⊥_________________⊥__________________⊥__________⊥_______________⊥")





def spacing (item, i):
    a = ''
    if i < 9 :
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(7) + "|".ljust(3)
    if i >= 9:
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(6) + "|".ljust(3)
    a += str(item[i][1]).ljust(17) + "|".ljust(3)
    a += str(item[i][2]).ljust(23) + "|".ljust(3)
    a += str(item[i][3]).ljust(24) + "|".ljust(3)
    a += str(item[i][4]).ljust(15) + "|".ljust(3) + "Rp. "
    a += str(item[i][5]).ljust(12) + "|".ljust(4)
    a += str(item[i][6]).ljust(7)  + "|".ljust(7)
    a += str(item[i][0]).ljust(9)  + "|".ljust(3)
    return a



def pembayaran(id, jenis, brand, varian, warna, harga, stok, totalHarga, count):
    result = query(f"SELECT * FROM barang WHERE `id` = {id}")
    harga = result[0][5] * count
    totalHarga += harga
    print("Harga Barang  =  ", result[0][5], " x ", count, "  =  ", harga)
    
    return totalHarga
        



def daftarBarang(items):
    print(header())
    for i in range(len(items)) :
        print(spacing(items, i))
    print(footer())
        


def cari(items) :  
    while(True): 
        keyword = input("\n\nKetikkan Sesuatu Untuk Mencari :     ") 
        if (keyword == ""):
            print("Tidak Boleh Kosong!")
            continue
        param = f"SELECT * FROM barang WHERE `jenis` LIKE '%{keyword}%' OR `brand` LIKE '%{keyword}%' OR `varian` LIKE '%{keyword}%' OR `warna` LIKE '%{keyword}%'"
        equalItems = query(param)
        clr()
        print(f"\n\n\nHasil Pencarian {keyword} : ")
        break
    daftarBarang(equalItems)

    


def orderby(keyword, item):
    global items
    param = f"SELECT * FROM barang ORDER BY {keyword}"
    item = query(param)
    items = item
    daftarBarang(items)
    menu(keyword)





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
        param = "INSERT INTO `barang` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `stok`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.id, self.jenis, self.brand, self.varian, self.warna, self.harga, self.stok)
        mycursor.execute(param, val)
        conn.commit()
        print("Berhasil!!")

    def tambahStok(self) :
        stokBaru = int(input("Masukkan Jumlah Stok :    "))
        stokBaru += self.stok
        param = f"UPDATE `barang` SET `stok` = {stokBaru} WHERE id = {self.id}"
        query(param)
        print("Berhasil!!")

    def ubahHargaBarang(self) : 
        hargaBaru = int(input("Masukkan Harga Baru :     "))
        param = "UPDATE barang SET harga = {} WHERE id = {}".format(hargaBaru, self.id)
        query(param)
        print("Berhasil!!")

    def hapusBarang(self) :
        yakin = input("Apakah anda yakin ingin menghapus item ini (Y/N) ? :    ")
        if (yakin.upper() == "Y") :
            param = "DELETE FROM barang WHERE id = {}".format(self.id)
            query(param)
            print("Berhasil!!")
        elif (yakin.upper() == "N") :
            exit
        else :
            print("Input yang anda Masukkan SALAH!")









def menu(param):
    items = query("SELECT * FROM barang ORDER BY " + param)
    clr()
    print("".rjust(39))
    print(" _______________________________________________________________________________________")
    print("|                                                     SELAMAT DATANG DI TOKO PANCING    |")
    print("|       1.  Kasir                                                                       |")      # ✔
    print("|       2.  Daftar Barang                                                               |")      # ✔
    print("|       3.  Urutkan Barang                                                              |")      # ✔
    print("|       4.  Cari Barang                                                                 |")      # ✔
    print("|       5.  Laporan Penjualan                                                           |")      
    print("|                                                                                       |")   
    print("|       0.  Exit                                                                        |")
    print("|                                                                                       |")   
    print("|                                                                                       |")    
    print("|_______________________________________________________________________________________|")      
    pil = input(" Pilih Menu >>  ")


    if (pil == "1"):
        clr()
        print(" _______________________________________________________________________________________")
        print("|                                                                          Menu Kasir   |")      
        print("|  Hai Admin...                                                                         |")
        print("|                                                                                       |")      
        print("|       1.  Pembayaran                                                                  |")      # ✔
        print("|       2.  Laporan Penjualan                                                           |")      
        print("|       3.  Data Pelanggan                                                              |")      
        print("|                                                                                       |")      
        print("|_______________________________________________________________________________________|")      
        print("|                                                                                       |")      
        print("|       4.  Lihat Daftar Barang                                                         |")      # ✔
        print("|       5.  Tambah Barang                                                               |")      # ✔
        print("|       6.  Hapus Barang                                                                |")      # ✔
        print("|       7.  Ubah Harga                                                                  |")      # ✔
        print("|       8.  Tambah Stok                                                                 |")      # ✔
        print("|                                                                                       |")      
        print("|       0.  Kembali                                                                     |")
        print("|                                                                                       |")      
        print("|                                                                                       |")    
        print("|_______________________________________________________________________________________|") 
        pil = input(" Pilih Menu >>  ")


        if (pil == "1"):
            clr()

            stokTersedia = "SELECT * FROM barang WHERE stok != 0 ORDER BY " + param
            items = query(stokTersedia)
            daftarBarang(items)
            totalHarga = 0

            print("\nMasukkan Barang Yang Dibeli! ")
            print("Masukkan Angka 0 Jika Semua Barang Yang dibeli sudah dimasukkan")
            while(True) : 
                pil = int(input("\nMasukkan ID Barang  >>>        "))
                pil -= 1
                if (pil != -1):
                    count = int(input("Berapa Buah? :   "))
                elif (pil == -1) :
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
                    "totalHarga": totalHarga,
                    "count": count
                    }
                newStok = kwargs["stok"] - kwargs["count"]
                if (kwargs["stok"] < kwargs["count"]) :
                    beli = input(f"Barang yang tersedia tidak cukup, Maukah anda membeli sebanyak {kwargs['stok']} (Y/N) ?")
                    if beli.upper() == "Y":
                        newStok = kwargs["stok"]
                    elif beli.upper() == "N":
                        break
                updatingStok = f'UPDATE barang SET stok = {newStok} WHERE id = {kwargs["id"]}'
                mycursor.execute(updatingStok)
                conn.commit()
                totalHarga += pembayaran(**kwargs)  
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)



        if (pil == "2") :
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                                  Laporan Penjualan    |")             
            print("|    1.  Bulan Ini                                                                      |")      
            print("|    2.  Tahun Ini                                                                      |")      
            print("|                                                                                       |")   
            print("|                                                                                       |")    
            print("|_______________________________________________________________________________________|") 
            pil = input(" Pilih Menu >>  ")


            if (pil == "1"):
                clr()
                print(" _______________________________________________________________________________________") 
                print("|                                                        Laporan Penjualan Bulan ini    |")             
                print("|    1.  Lihat Grafik Penjualan Bulan Ini                                               |")      
                print("|    2.  Lihat Barang Yang Terjual                                                      |")      
                print("|    3.  Lihat Keuntungan Bulan Ini                                                     |")      
                print("|                                                                                       |")   
                print("|                                                                                       |")    
                print("|_______________________________________________________________________________________|") 
                pil = input(" Pilih Menu >>  ")
                
                if (pil == "1"):
                    pass
                if (pil == "2"):
                    pass
                if (pil == "3"):
                    pass

            elif (pil == "2"):
                clr()
                print(" _______________________________________________________________________________________") 
                print("|                                                         Laporan Penjualan Tahun ini   |")             
                print("|    1.  Lihat Grafik Penjualan Tahun Ini                                               |")      
                print("|    2.  Lihat Barang Yang Terjual                                                      |")      
                print("|    3.  Lihat Keuntungan Tahun Ini                                                     |")      
                print("|                                                                                       |")   
                print("|                                                                                       |")    
                print("|_______________________________________________________________________________________|") 
                pil = input(" Pilih Menu >>  ")

                if (pil == "1"):
                    pass
                if (pil == "2"):
                    pass
                if (pil == "3"):
                    pass

        if (pil == "3") :
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                                     Data Pelanggan    |")             
            print("|    1.  Lihat Data Pelanggan                                                           |")      
            print("|    2.  Ubah Data Pelanggan                                                            |")   
            print("|                                                                                       |")   
            print("|                                                                                       |")       
            print("|_______________________________________________________________________________________|") 
            pil = input(" Pilih Menu >>  ")

            if (pil == "1"):
                pass
            elif(pil == "2"):
                pass



        if (pil == "4") :
            clr()

            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)


        if (pil == "5") :
            jenis = input("Masukkan Jenis Barang :   ")
            brand = input("Masukkan Merk Barang :    ")
            varian = input("Masukkan Varian Barang :  ")
            warna = input("Masukkan Warna Barang :   ")
            harga = int(input("Masukkan Harga Barang :   "))
            stok = int(input("Masukkan Stok Barang :    "))

            barang = Barang(None, jenis, brand, varian, warna, harga, stok)
            barang.tambahBarang()
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)

        
        
        if (pil == "6") :
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
            menu(param)


        if (pil == "7") :
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
            menu(param)

        if (pil == "8") :
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
            menu(param)


        if (pil == "0"):
            print("Terima Kasih Telah Menggunakan Program Ini (●'◡'●)つ !!!")
            exit






    elif (pil == "2"):
        items = query("SELECT * FROM barang ORDER BY " + param)
        clr()
        print(" _______________________________________________________________________________________")
        print("|                                                                      Daftar Barang    |")          
        print("|       1.  Lihat Semua Barang                                                          |")      # ✔
        print("|       2.  Lihat Barang Tersedia                                                       |")      # ✔
        print("|       3.  Lihat Barang Yang Kehabisan STOK                                            |")      # ✔
        print("|       4.  Cari Barang                                                                 |")      # ✔
        print("|       5.  Urutkan Barang                                                              |")      # ✔
        print("|                                                                                       |")   
        print("|       0.  Kembali                                                                     |")
        print("|                                                                                       |") 
        print("|                                                                                       |")         
        print("|_______________________________________________________________________________________|") 
        pil = input(" Pilih Menu >>  ")
        
        
        if (pil == "1") :
            clr()

            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)


        if (pil == "2") :
            clr()

            stokTersedia = "SELECT * FROM barang WHERE stok != 0 ORDER BY " + param
            items = query(stokTersedia)
            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)


        if (pil == "3") :
            clr()

            stokKosong = "SELECT * FROM barang WHERE stok = 0 ORDER BY " + param
            items = query(stokKosong)
            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)



        if (pil == "4") :
            clr()
            
            daftarBarang(items)
            cari(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)  


        if (pil == "5") :
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                                        Urut Barang    |")            
            print("|    1.  Urutkan Berdasarkan Jenis                                                      |")      # ✔
            print("|    2.  Urutkan Berdasarkan Brand                                                      |")      # ✔
            print("|    3.  Urutkan Berdasarkan Warna                                                      |")      # ✔
            print("|    4.  Urutkan Berdasarkan Varian                                                     |")      # ✔
            print("|    5.  Urutkan Berdasarkan Harga                                                      |")      # ✔     
            print("|                                                                                       |")   
            print("|                                                                                       |")    
            print("|_______________________________________________________________________________________|") 

            pilCari = input("\n\tAnda ingin Mengurutkan Berdasarkan : ")    
            
            if (pilCari == "1"): pilCari = "Jenis"
            if (pilCari == "2"): pilCari = "Brand"
            if (pilCari == "3"): pilCari = "Warna"
            if (pilCari == "4"): pilCari = "Varian"
            if (pilCari == "5"): pilCari = "Harga"

            orderby(pilCari.lower(), items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param)


        if (pil == "0"):
            menu(param)





    if (pil == "3") :
        clr()
            
        daftarBarang(items)
        cari(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu(param)  


    if (pil == "4") :
        clr()
        print(" _______________________________________________________________________________________") 
        print("|                                                                        Urut Barang    |")            
        print("|    1.  Urutkan Berdasarkan Jenis                                                      |")      # ✔
        print("|    2.  Urutkan Berdasarkan Brand                                                      |")      # ✔
        print("|    3.  Urutkan Berdasarkan Warna                                                      |")      # ✔
        print("|    4.  Urutkan Berdasarkan Varian                                                     |")      # ✔
        print("|    5.  Urutkan Berdasarkan Harga                                                      |")  
        print("|                                                                                       |")        
        print("|                                                                                       |")    
        print("|_______________________________________________________________________________________|") 

        pilCari = input("\n\tAnda ingin Mengurutkan Berdasarkan : ")    
        
        if (pilCari == "1"): pilCari = "Jenis"
        if (pilCari == "2"): pilCari = "Brand"
        if (pilCari == "3"): pilCari = "Warna"
        if (pilCari == "4"): pilCari = "Varian"
        if (pilCari == "5"): pilCari = "Harga"

        orderby(pilCari.lower(), items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu(param)


    if (pil == "5") :
        clr()
        print(" _______________________________________________________________________________________") 
        print("|                                                                  Laporan Penjualan    |")             
        print("|    1.  Bulan Ini                                                                      |")      
        print("|    2.  Tahun Ini                                                                      |")  
        print("|                                                                                       |")   
        print("|                                                                                       |")         
        print("|_______________________________________________________________________________________|") 
        pil = input(" Pilih Menu >>  ")


        if (pil == "1"):
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                        Laporan Penjualan Bulan ini    |")             
            print("|    1.  Lihat Grafik Penjualan Bulan Ini                                               |")      
            print("|    2.  Lihat Barang Yang Terjual                                                      |")      
            print("|    3.  Lihat Keuntungan Bulan Ini                                                     |")      
            print("|                                                                                       |")    
            print("|                                                                                       |")    
            print("|_______________________________________________________________________________________|") 
            pil = input(" Pilih Menu >>  ")
            
            if (pil == "1"):
                pass
            if (pil == "2"):
                pass
            if (pil == "3"):
                pass

        elif (pil == "2"):
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                        Laporan Penjualan Tahun ini    |")             
            print("|    1.  Lihat Grafik Penjualan Tahun Ini                                               |")      
            print("|    2.  Lihat Barang Yang Terjual                                                      |")      
            print("|    3.  Lihat Keuntungan Tahun Ini                                                     |")    
            print("|                                                                                       |")   
            print("|                                                                                       |")     
            print("|_______________________________________________________________________________________|") 
            pil = input(" Pilih Menu >>  ")

            if (pil == "1"):
                pass
            if (pil == "2"):
                pass
            if (pil == "3"):
                pass


    if (pil == "0") :
        menu(param)

menu(param)
