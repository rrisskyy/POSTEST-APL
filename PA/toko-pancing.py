import os
import mysql.connector

conn = mysql.connector.connect( host="localhost", user="root", password="", database="toko-pancing" )
mycursor = conn.cursor()

items = []


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
# orders = query("SELECT * FROM orders ORDER BY " + param)

param1 = "first_name"
costumers = query("SELECT * FROM costumers ORDER BY " + param1)



def header():
    return (" ____________________________________________________________________________________________________________________________________________________\n" 
           + "|____ID_____|_______JENIS_______|__________BRAND__________|__________VARIAN__________|______WARNA______|______HARGA_______|___STOK___|____NO_SERI____|")
def footer():
    return ("⊥___________⊥___________________⊥_________________________⊥__________________________⊥_________________⊥__________________⊥__________⊥_______________⊥")


def header1():
    return (" ___________________________________________________________________________________________________________________________________________________________________________________________\n" 
           + "|____ID_____|__First Name__|__Last Name__|_____________E-mail____________|__Phone Number___|____________________________________________Address____________________________________________|")
def footer1():
    return ("⊥___________⊥______________⊥_____________⊥_______________________________⊥_________________⊥_______________________________________________________________________________________________⊥")




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



def spacing1 (item, i):
    a = ''
    if i < 9 :
        a = "|".ljust(4) + "[" + str(i+1) + "] ".ljust(6) + "|".ljust(3)
    if i >= 9:
        a = "|".ljust(4) + "[" + str(i+1) + "] ".ljust(5) + "|".ljust(3)
    a += str(item[i][1]).ljust(12) + "|".ljust(3)
    a += str(item[i][2]).ljust(11) + "|".ljust(3)
    a += str(item[i][4]).ljust(29) + "|".ljust(3)
    a += str(item[i][5]).ljust(15) + "|".ljust(3)
    a += str(item[i][3]).ljust(93) + "|".ljust(4)
    # a += str(item[i][0]).ljust(9)  + "|".ljust(3)
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
        


def daftarOrang(items):
    print(header1())
    for i in range(len(items)) :
        print(spacing1(items, i))
    print(footer1())        


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


class Orang:

    def __init__(self, id, first_name, last_name, address, email, phone_number) :
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def tambahOrang(self) :
        param1 = "INSERT INTO costumers (id, first_name, last_name, address, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.id, self.first_name, self.last_name, self.address, self.email, self.phone_number)
        mycursor.execute(param1, val)
        conn.commit()
        print("Berhasil!!")

    def ubah(self) : 
        print("\nAnda ingin mengubah Apa    ?\n\n")
        print(f"1). First Name :  {self.first_name}  ")
        print(f"2). Last Name :  {self.last_name}  ")
        print(f"3). Address :  {self.address}  ")
        print(f"4). Email :  {self.email}  ")
        print(f"5). Phone Number :  {self.phone_number}  ")
        print("\n\n\n0. Kembali Ke Menu     ")
        pil = input("\n\nPilih Menu :    ")

        while(True):
            if (pil == "1"):
                newFirstName = (input("Masukkan First Name Baru :    "))
                param1 = "UPDATE barang SET first_name = {} WHERE id = {}".format(newFirstName, self.id)
                query(param1)
                print("Berhasil!!")
                break
            if (pil == "2"):
                newLastName = (input("Masukkan First Name Baru :    "))
                param1 = "UPDATE barang SET last_name = {} WHERE id = {}".format(newLastName, self.id)
                query(param1)
                print("Berhasil!!")
                break
            if (pil == "3"):
                newAddress = (input("Masukkan First Name Baru :    "))
                param1 = "UPDATE barang SET address = {} WHERE id = {}".format(newAddress, self.id)
                query(param1)
                print("Berhasil!!")
                break
            if (pil == "4"):
                newEmail = (input("Masukkan First Name Baru :    "))
                param1 = "UPDATE barang SET email = {} WHERE id = {}".format(newEmail, self.id)
                query(param1)
                print("Berhasil!!")
                break
            if (pil == "5"):
                newPhoneNumber = (input("Masukkan First Name Baru :    "))
                param1 = "UPDATE barang SET phone_number = {} WHERE id = {}".format(newPhoneNumber, self.id)
                query(param1)
                print("Berhasil!!")
                break
            if(pil == "0"):
                menu(param, param1)

            else:
                clr()
                print("Pilihan Salah!\n")
                daftarOrang(costumers)
                self.ubah()
            

    def hapusOrang(self) :
        yakin = input("Apakah anda yakin ingin menghapus Orang ini (Y/N) ? :    ")
        if (yakin.upper() == "Y") :
            param1 = "DELETE FROM costumers WHERE id = {}".format(self.id)
            query(param1)
            print("Berhasil!!")
        elif (yakin.upper() == "N") :
            exit
        else :
            print("Input yang anda Masukkan SALAH!")









def menu(param, param1):
    items = query("SELECT * FROM barang ORDER BY " + param)
    costumers = query("SELECT * FROM costumers ORDER BY " + param1)
    clr()
    print("".rjust(39))
    print(" _______________________________________________________________________________________")
    print("|                                                     SELAMAT DATANG DI TOKO PANCING    |")
    print("|       1.  Admin                                                                       |")      
    print("|       2.  Daftar Barang                                                               |")      
    print("|       3.  Urutkan Barang                                                              |")      
    print("|       4.  Cari Barang                                                                 |")      
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
        print("|       1.  Kasir                                                                       |")      
        print("|       2.  Laporan Penjualan                                                           |")      
        print("|       3.  Data Pelanggan                                                              |")      
        print("|                                                                                       |")      
        print("|_______________________________________________________________________________________|")      
        print("|                                                                                       |")      
        print("|       4.  Lihat Daftar Barang                                                         |")      
        print("|       5.  Tambah Barang                                                               |")      
        print("|       6.  Hapus Barang                                                                |")      
        print("|       7.  Ubah Harga                                                                  |")      
        print("|       8.  Tambah Stok                                                                 |")      
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
            menu(param, param1)



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
            print("|    2.  Tambah Pelanggan                                                               |")      
            print("|    3.  Ubah Data Pelanggan                                                            |")   
            print("|    4.  Hapus Data Pelanggan                                                           |")   
            print("|                                                                                       |")   
            print("|                                                                                       |")       
            print("|_______________________________________________________________________________________|") 
            pil = input(" Pilih Menu >>  ")

            if (pil == "1"):
                clr()
                daftarOrang(costumers)
                input("\n\n\nTekan Enter Untuk Kembali ...")
                menu(param, param1)
            elif(pil == "2"):
                firstName = input("Masukkan Nama Depan :   ")
                lastName = input("Masukkan Nama Belakang :    ")
                print("Contoh Alamat: Jalan Ulin RT 10 Kel. Sebulu Ulu Kec. Sebulu  Kab. Kutai Kartanegara Kalimantan Timur 75552")
                address = input("Masukkan Alamat Lengkap :  ")
                email = input("Masukkan Email :   ")
                phoneNumber = int(input("Masukkan Nomor Handphone :    "))

                orang = Orang(None, firstName, lastName, address, email, phoneNumber)
                orang.tambahOrang()
                input("\n\n\nTekan Enter Untuk Kembali ...")
                menu(param, param1)

            elif(pil == "3"):
                clr()
                daftarOrang(costumers)

                pil = int(input("\nPilihlah Orang Yang Datanya Ingin anda ubah (ID) :      "))
                pil -= 1

                kwargs = {
                    "id": costumers[pil][0],
                    "first_name": costumers[pil][1],
                    "last_name": costumers[pil][2],
                    "address": costumers[pil][3],
                    "email": costumers[pil][4],
                    "phone_number": costumers[pil][5],
                    }

                orang = Orang(**kwargs)
                orang.ubah()
                input("\n\n\nTekan Enter Untuk Kembali ...")
                menu(param, param1)

            elif(pil == "4"):
                clr()
                daftarOrang(costumers)

                pil = int(input("\nPilihlah Orang Yang Ingin Anda Hapus (ID) :      "))
                pil -= 1

                kwargs = {
                    "id": costumers[pil][0],
                    "first_name": costumers[pil][1],
                    "last_name": costumers[pil][2],
                    "address": costumers[pil][3],
                    "email": costumers[pil][4],
                    "phone_number": costumers[pil][5],
                    }
                
                orang = Orang(**kwargs)
                orang.hapusOrang()
                input("\n\n\nTekan Enter Untuk Kembali ...")
                menu(param, param1)

        if (pil == "4") :
            clr()

            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param, param1)


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
            menu(param, param1)

        
        
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
            menu(param, param1)


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
            menu(param, param1)

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
            menu(param, param1)


        if (pil == "0"):
            print("Terima Kasih Telah Menggunakan Program Ini (●'◡'●)つ !!!")
            exit






    elif (pil == "2"):
        items = query("SELECT * FROM barang ORDER BY " + param)
        clr()
        print(" _______________________________________________________________________________________")
        print("|                                                                      Daftar Barang    |")          
        print("|       1.  Lihat Semua Barang                                                          |")      
        print("|       2.  Lihat Barang Tersedia                                                       |")      
        print("|       3.  Lihat Barang Yang Kehabisan STOK                                            |")      
        print("|       4.  Cari Barang                                                                 |")      
        print("|       5.  Urutkan Barang                                                              |")      
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
            menu(param, param1)
            
            
        if (pil == "2") :
            clr()

            stokTersedia = "SELECT * FROM barang WHERE stok != 0 ORDER BY " + param
            items = query(stokTersedia)
            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param, param1)


        if (pil == "3") :
            clr()

            stokKosong = "SELECT * FROM barang WHERE stok = 0 ORDER BY " + param
            items = query(stokKosong)
            daftarBarang(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param, param1)



        if (pil == "4") :
            clr()
            
            daftarBarang(items)
            cari(items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(param, param1)  


        if (pil == "5") :
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                                        Urut Barang    |")            
            print("|    1.  Urutkan Berdasarkan Jenis                                                      |")      
            print("|    2.  Urutkan Berdasarkan Brand                                                      |")      
            print("|    3.  Urutkan Berdasarkan Warna                                                      |")      
            print("|    4.  Urutkan Berdasarkan Varian                                                     |")      
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
            menu(param, param1)


        if (pil == "0"):
            menu(param, param1)





    if (pil == "3") :
        clr()
            
        daftarBarang(items)
        cari(items)
        input("\n\n\nTekan Enter Untuk Kembali ...")
        menu(param, param1)  


    if (pil == "4") :
        clr()
        print(" _______________________________________________________________________________________") 
        print("|                                                                        Urut Barang    |")            
        print("|    1.  Urutkan Berdasarkan Jenis                                                      |")      
        print("|    2.  Urutkan Berdasarkan Brand                                                      |")      
        print("|    3.  Urutkan Berdasarkan Warna                                                      |")      
        print("|    4.  Urutkan Berdasarkan Varian                                                     |")      
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
        menu(param, param1)


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
        menu(param, param1)

menu(param, param1)
