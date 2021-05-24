from os import system, name
from datetime import datetime
from matplotlib import pyplot as plt
import mysql.connector
import webbrowser
import getpass



conn = mysql.connector.connect( host="localhost", user="root", password="", database="toko-pancing" )

mycursor = conn.cursor()

# UNTUK MENAMPUNG ISI DARI DATABASE
items = []
login = False
NOW = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')



# import getpass
    # Supaya Password yang Kita ketik didalam CLI tidak terlihat (Contohnya seperti password didalam CLI Cisco Packet Tracer)

# mysql.connector.connect()
    # Menyiapkan koneksi , membuat sesi dengan server MySQL
    # Intinya Supaya Kode Kita bisa Tersambung ke Database SQL

# conn.cursor()
    # Mengizinkan kode Python untuk menjalankan perintah PostgreSQL dalam sesi database. Kursor dibuat oleh koneksi.
    # Intinya Supaya Code yang kita punya bisa menjalankan sintaks SQL.

# query()
    # Mengambil data dari dalam Database

# commit()
    # Menyimpan Perubahan kedalam Database

# mycursor.execute(query)
    # Mengeksekusi perintah yang ada di parameter
    # Misalnya User ingin mengambil semua data didalam database bisa dengan mengetik SELECT * FROM tabel





def signIn():
    global login
    u = ""
    p = ""
    try:
        while(len(p) == 0 or len(u) == 0):  
            u = input("Username :   ")
            p = getpass.getpass(prompt='Password :   ')
            if u.lower() == 'admin' and  p.lower() == 'admin':
                print('\n\nWelcome..!!!')
                login = True
                
            else:
                print(' Username atau Password anda salah..!!!')   
                input("\nKlik Enter Untuk Melanjutkan ... \n\n")
                u = "" 
                p = ""        
                continue
            
    except Exception as error:
        print('ERROR', error)
        input("Klik Enter Untuk Melanjutkan ... ")

def signOut():
    global login
    login = False



def clr():
   _ = system('clear') if name == 'posix' else system('cls')

def query(query):
    mycursor.execute(query)
    items = mycursor.fetchall()
    return items

def commit(param):
    mycursor.execute(param)
    conn.commit()


def back_to_menu():
    input("\n\n\nTekan Enter Untuk Kembali ...")
    menu(param)

def back_to_admin():
    input("\n\n\nTekan Enter Untuk Kembali ...")
    admin()



param = "harga"  
items = query("SELECT * FROM barang ORDER BY " + param)


costumers = query("SELECT * FROM costumers ORDER BY first_name")

terjual = query("SELECT * FROM terjual ORDER BY date")


# ==========================================================================================================================================================================================================================================================
def header():
    return (" ____________________________________________________________________________________________________________________________________________________\n" 
          + "|____ID_____|_______JENIS_______|__________BRAND__________|__________VARIAN__________|______WARNA______|______HARGA_______|___STOK___|____NO_SERI____|")
def footer():
    return ("⊥___________⊥___________________⊥_________________________⊥__________________________⊥_________________⊥__________________⊥__________⊥_______________⊥")


def header1():
    return (" __________________________________________________________________________________________________________________________________________________________________________________________\n" 
        +   "|__ID___|_____First Name_____|_____Last Name_____|_____________E-mail____________|_____Phone Number_____|_______________________________________Address____________________________________|")
def footer1():
    return ("⊥_______⊥____________________⊥___________________⊥_______________________________⊥______________________⊥__________________________________________________________________________________⊥")


def header2():
    return (" ____________________________________________________________________________________________________________________________________________________________________\n" 
         +  "|_________|_____JENIS______|________BRAND________|________VARIAN________|______WARNA______|______HARGA_______|_______MODAL______|__JUMLAH__|_________Tanggal_________|")
def footer2():
    return ("⊥_________⊥________________⊥_____________________⊥______________________⊥_________________⊥__________________⊥__________________⊥__________⊥_________________________⊥")

def header3():
    return (" ===============================================================================================================\n" +
            "                                                 TOKO  PANCING                                                \n"   +
            " ===============================================================================================================\n\n" +
            f" {NOW}\n\n" + 
            " |                                                            |  JUMLAH  |      HARGA       |      TOTAL       |")


# ==========================================================================================================================================================================================================================================================





# ==========================================================================================================================================================================================================================================================
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
    a += str(item[i][7]).ljust(7)  + "|".ljust(7)
    a += str(item[i][0]).ljust(9)  + "|".ljust(3)
    return a


  

def spacing1 (item, i):
    a = ''
    if i < 9 :
        a = "|".ljust(2) + "[" + str(i+1) + "] ".ljust(4) + "|".ljust(3)
    if i >= 9:
        a = "|".ljust(2) + "[" + str(i+1) + "] ".ljust(3) + "|".ljust(3)
    a += str(item[i][1]).ljust(18) + "|".ljust(3)
    a += str(item[i][2]).ljust(17) + "|".ljust(3)
    a += str(item[i][4]).ljust(29) + "|".ljust(3)
    a += str(item[i][5]).ljust(20) + "|".ljust(3)
    a += str(item[i][3]).ljust(80) + "|".ljust(4)
    return a



def spacing2 (item, i):
    a = ''
    if i < 9 :
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(5) + "|".ljust(3)
    if i >= 9:
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(4) + "|".ljust(3)
    if i >= 99:
        a = "|".ljust(3) + "[" + str(i+1) + "] ".ljust(3) + "|".ljust(3)
    a += str(item[i][1]).ljust(14) + "|".ljust(3)
    a += str(item[i][2]).ljust(19) + "|".ljust(3)
    a += str(item[i][3]).ljust(20) + "|".ljust(3)
    a += str(item[i][4]).ljust(15) + "|".ljust(3) + "Rp. "
    a += str(item[i][5]).ljust(12) + "|".ljust(3) + "Rp. "
    a += str(item[i][6]).ljust(12) + "|".ljust(5)
    a += str(item[i][7]).ljust(6)  + "|".ljust(3)
    a += str(item[i][8]).ljust(23)  + "|".ljust(3)
    return a


def spacing3 (item, i):
    a = ' |'.ljust(3)
    a += str(item[i][0]).ljust(14) + " ".ljust(3)
    a += str(item[i][1]).ljust(19) + " ".ljust(3)
    a += str(item[i][2]).ljust(20) + "|".ljust(5) 
    a += str(item[i][4]).ljust(6)  + "|".ljust(3) + "Rp. "
    a += str(item[i][5]).ljust(12) + "|".ljust(3) + "Rp. "
    a += str(item[i][3]).ljust(12) + "|".ljust(3)
    return a

# ==========================================================================================================================================================================================================================================================




# PRINT DAFTAR BARANG
# ==========================================================================================================================================================================================================================================================
def daftarBarang(items):
    print(header())
    for i in range(len(items)) :
        print(spacing(items, i))
    print(footer())

def daftarBarang1(items):
    print("\nHistory Penjualan : \n")
    print(header2())
    for i in range(len(items)) :
        print(spacing2(items, i))
    print(footer2())

def daftarBarang2(items):
    print("\nStruk : \n")
    print(header3())
    for i in range(len(items)) :
        print(spacing3(items, i))

def daftarOrang(items):
    print(header1())
    for i in range(len(items)) :
        print(spacing1(items, i))
    print(footer1())        

# ==========================================================================================================================================================================================================================================================




# BARANG SQL
# ==========================================================================================================================================================================================================================================================
def tambahBarang(id, jenis, brand, varian, warna, harga, modal, stok) :
    param = "INSERT INTO `barang` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `modal`,`stok`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" % (id, jenis, brand, varian, warna, harga, modal, stok)
    commit(param)  
    print("Berhasil!!")

def tambahStok(stok, id) :
    stokBaru = int(input("Masukkan Jumlah Stok :    "))
    stokBaru += stok
    param = f"UPDATE `barang` SET `stok` = {stokBaru} WHERE id = {id}"
    commit(param)
    print("Berhasil!!")

def ubahHargaBarang(id) : 
    hargaBaru = int(input("Masukkan Harga Baru :     "))
    param = "UPDATE barang SET harga = {} WHERE id = {}".format(hargaBaru, id)
    commit(param)
    print("Berhasil!!")

def hapusBarang(id) :
    yakin = input("Apakah anda yakin ingin menghapus item ini (Y/N) ? :    ")
    if (yakin.upper() == "Y") :
        param = "DELETE FROM barang WHERE id = {}".format(id)
        commit(param)
        print("Berhasil!!")
    elif (yakin.upper() == "N") :
        exit
    else :
        print("Input yang anda Masukkan SALAH!")



def sequentialSearch(items, x):
    clr()
    equalItems = []
    for i in range(0, len(items)):
        for j in range(0, len(items[i])):            
            if (items[i][j] == x):
                equalItems.append(items[i])
    daftarBarang(equalItems)
    return -1  
    


def orderby(keyword, item):
    global items
    print("[1] Ascending")
    print("[2] Descending")
    a = input("Pilih Menu :    ")
    if a == "1": a = "ASC"
    elif a == "2": a = "DESC"
    param = f"SELECT * FROM barang ORDER BY {keyword} {a}"
    item = query(param)
    items = item
    daftarBarang(items)
    return keyword

# ==========================================================================================================================================================================================================================================================



# ORANG SQL
# ==========================================================================================================================================================================================================================================================
def tambahOrang(id, first_name, last_name, address, email, phone_number) :
    param = "INSERT INTO costumers (id, first_name, last_name, address, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)" % (id, first_name, last_name, address, email, phone_number)
    commit(param)
    print("Berhasil!!")

def ubah(id, first_name, last_name, address, email, phone_number) : 
    while(True):
        print("\nAnda ingin mengubah Apa    ?\n\n")
        print(f"1). Nama Depan    :  {first_name}  ")
        print(f"2). Nama Belakang :  {last_name}  ")
        print(f"3). Alamat Rumah  :  {address}  ")
        print(f"4). Email         :  {email}  ")
        print(f"5). Nomor Telepon :  {phone_number}  ")
        print("\n\n\n0). Kembali Ke Menu     ")
        pil = ''
        try:
            while(pil == '' and pil.isdigit() == False):
                pil = input("\n\nPilih Menu :    ")
                if (pil == ''):
                    print("Tidak Boleh Kosong!")

            if (pil == "1"):
                newFirstName = ''
                while (newFirstName == ''):
                    newFirstName = (input("Masukkan Nama Depan Baru :    "))
                    if (newFirstName == ''):
                        print("Nama Depan tidak boleh kosong")
                
                param = "UPDATE costumers SET first_name = %s WHERE id = %s" % (newFirstName, id)
                commit(param)
                print("Berhasil!!")
                break

            elif (pil == "2"):
                newLastName = ''
                while (newLastName == ''):
                    newLastName = input("Masukkan Last Name Baru :    ")
                    if (newLastName == ''):
                        print("Nama Belakang tidak boleh kosong")
                
                param = "UPDATE costumers SET last_name = %s WHERE id = %s"
                val = (newLastName, id)
                commit(param)
                print("Berhasil!!")
                break

            elif (pil == "3"):
                newAddress = ''
                while (newAddress == ''):
                    newAddress = input("Masukkan Address Baru :    ")
                    if (newAddress == ''):
                        print("Alamat tidak boleh kosong")
                
                param = "UPDATE costumers SET address = %s WHERE id = %s" % (newAddress, id)
                commit(param)
                print("Berhasil!!")
                break
            elif (pil == "4"):
                newEmail = ''
                while (newEmail == ''):
                    newEmail = input("Masukkan Email Baru :    ")
                    if (newEmail == ''):
                        print("Email tidak boleh kosong")
                
                param = "UPDATE costumers SET email = %s WHERE id = %s" % (newEmail, id)
                commit(param)
                print("Berhasil!!")
                break

            elif (pil == "5"):
                newPhoneNumber = ''
                while (newPhoneNumber == ''):
                    newPhoneNumber = input("Masukkan Nomor Handphone Baru :    ")
                    if (newPhoneNumber == ''):
                        print("Alamat tidak boleh kosong")
                
                param = "UPDATE costumers SET phone_number = %s WHERE id = %s" % (newPhoneNumber, id)
                commit(param)
                print("Berhasil!!")
                break
            elif(pil == "0"):
                break

            else:
                clr()
                print("Pilihan Salah!\n")
                daftarOrang(costumers)
                ubah()
        except TypeError:
            input("Pilihlah Menu Dari 1 - 5!!, Tekan Enter Untuk Melanjutkan!")
            continue

        

def hapusOrang(id) :
    while (True):
        yakin = input("Apakah anda yakin ingin menghapus Orang ini (Y/N) ? :    ")
        if (yakin.upper() == "Y") :
            param1 = "DELETE FROM costumers WHERE id = {}".format(id)
            commit(param1)
            print("Berhasil!!")
            break
        elif (yakin.upper() == "N") :
            break    
        else :
            print("Input yang anda Masukkan SALAH!")

# ==========================================================================================================================================================================================================================================================


    
# SORTING
# ==========================================================================================================================================================================================================================================================
def ascBubbleSort(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
def descMergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		descMergeSort(L)
		descMergeSort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i][3] < R[j][3]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
    

# ==========================================================================================================================================================================================================================================================

# PEMBAYARAN
def pembayaran(id, jenis, brand, varian, warna, harga, stok, totalHarga, count):
    result = query(f"SELECT * FROM barang WHERE `id` = {id}")
    harga = result[0][5] * count
    modal = result[0][6] * count
    totalHarga += harga
    print("Harga Barang  =  ", result[0][5], " x ", count, "  =  ", harga)
    
    param = "INSERT INTO `terjual` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `modal`, `jumlah`, `date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (None, jenis, brand, varian, warna, harga, modal, count, NOW)
    commit(param)

    return totalHarga



# ==========================================================================================================================================================================================================================================================


def admin():
    signOut()
    items = query("SELECT * FROM barang ORDER BY " + param)
    costumers = query("SELECT * FROM costumers ORDER BY first_name")
    terjual = query("SELECT * FROM terjual ORDER BY date")

    pil = ''
    allMenu = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while(pil not in allMenu): 
        clr()
        print(" _______________________________________________________________________________________")
        print("|                                                                          Menu Kasir   |")      
        print("|  Hai Admin...                                                                         |")
        print("|                                                                                       |")      
        print("|       1.  Kasir                                                                       |")      # ✔
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
        print("|       9.  Urutkan Barang                                                              |")      
        print("|                                                                                       |")      
        print("|       0.  Kembali                                                                     |")
        print("|                                                                                       |")      
        print("|                                                                                       |")    
        print("|_______________________________________________________________________________________|") 
        pil = input(" Pilih Menu >>  ")


        if (pil == "1"):
            while(True): 
                try:
                    clr()
                    daftarBeli = []
                    stokTersedia = "SELECT * FROM barang WHERE stok != 0 ORDER BY " + param
                    items = query(stokTersedia)
                    daftarBarang(items)
                    totalHarga = 0

                    print("\nMasukkan Barang Yang Dibeli : ")
                    # print("Masukkan Angka 0 Jika Semua Barang Yang dibeli sudah dimasukkan")
                    _run = True
                    while(_run):
                        try:
                            pil = int(input("\nMasukkan ID Barang  >>>        "))
                            pil -= 1
                            count = int(input("Berapa Buah? :   "))
                            
                            kwargs = {
                                "id": items[pil][0],
                                "jenis": items[pil][1],
                                "brand": items[pil][2],
                                "varian": items[pil][3],
                                "warna": items[pil][4],
                                "harga": items[pil][5],
                                "stok": items[pil][7],
                                "totalHarga": totalHarga,
                                "count": count
                                }
                            
                            daftarBeli.append((kwargs["jenis"], kwargs["brand"], kwargs["varian"], kwargs["harga"] * kwargs["count"], kwargs["count"], kwargs["harga"]))
                            newStok = kwargs["stok"] - kwargs["count"]
                            if (kwargs["stok"] < kwargs["count"]) :
                                beli = input(f"Barang yang tersedia tidak cukup, Maukah anda membeli sebanyak {kwargs['stok']} (Y/N) ?")
                                if beli.upper() == "Y":
                                    newStok = kwargs["stok"]
                                elif beli.upper() == "N":
                                    daftarBeli.pop()
                                    continue
                                    
                        except ValueError:
                            input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                            continue
                        
                        updatingStok = f'UPDATE barang SET stok = {newStok} WHERE id = {kwargs["id"]}'
                        commit(updatingStok)
                        totalHarga = pembayaran(**kwargs)  
                        _run2 = True
                        while(_run2):
                            ulang = input("Apakah Anda ingin membeli yang lain? (Y/N) : ")
                            if (ulang.upper() == "Y"):
                                _run2 = False
                            elif(ulang.upper() == "N"):
                                print(f"\n\nTotal Harga : Rp. {totalHarga}\n")
                                while (True):
                                    try:
                                        uang = int(input("Berapa Uang Yang Dibayarkan:   Rp. ")) 
                                        result = uang - totalHarga
                                        if (result < 0):
                                            print("Uang Yang Dibayarkan Tidak Cukup Mohon Tambah Lagi!")
                                            print(f"Uang Kurang {abs(result)}")
                                            continue
                                        else: 
                                            _run = False
                                            _run2 = False
                                            break
                                    except ValueError:
                                        input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                                        continue
                            else: 
                                print("Input anda salah!")
                                continue

                    print("\n\nUrutkan Struk dari Harga Tertinggi atau Terendah? ")
                    print("[1] Tertinggi")
                    print("[2] Terendah ")
                    while(True):
                        pil = input("Pilih Menu :    ")
                        if (pil == "1") : ascBubbleSort(daftarBeli)    
                        elif (pil == "2") : descMergeSort(daftarBeli)   
                        else : continue 
                        clr()
                        daftarBarang2(daftarBeli)        
                        print("  _____________________________________________________________________________________________________________\n")
                        
                        print(f"                                                                                     Total Harga : Rp. {totalHarga}")
                        print(f"                                                                            Uang Yang Dibayarkan : Rp. {uang}")
                        if (result == 0):
                            print(f"                                                                                   Uang Yang Dibayarkan Pas")
                        elif (result > 0):
                            print(f"                                                                                       Kembalian : Rp. {result}\n")
                        break

                    totalHarga = 0  
                    break
                except ValueError:
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
            
            back_to_admin()         
                                
                    



        elif (pil == "2") :
            pil = ''
            allMenu = ['1', '2', '3']
            while(pil not in allMenu):
                clr()
                print(" _______________________________________________________________________________________") 
                print("|                                                        Laporan Penjualan Bulan ini    |")             
                print("|    1.  Lihat Grafik Penjualan Bulan Ini                                               |")      
                print("|    2.  Lihat History Penjualan                                                        |")     
                print("|    3.  Hapus History Penjualan                                                        |")      
                print("|                                                                                       |") 
                print("|       0.  Kembali                                                                     |")  
                print("|                                                                                       |")    
                print("|_______________________________________________________________________________________|") 
                pil = input(" Pilih Menu >>  ")
                
                if (pil == "1"):
                    try:
                        mycursor.execute("SELECT SUM(harga) FROM terjual")
                        untung = mycursor.fetchone()[0]
                        mycursor.execute("SELECT SUM(modal) FROM terjual")
                        modal = mycursor.fetchone()[0]
                        
                        fig = plt.figure("Keuntungan Bulan Ini")

                        x = []
                        y = []
                        mycursor.execute("SELECT jenis, SUM(harga - modal) FROM terjual GROUP BY jenis")
                        group = mycursor.fetchall()

                        for i in range(len(group)):
                            x.append(group[i][0])
                            y.append(group[i][1])
                        plt.bar(x,y, color = ['#15FA00'])
                        plt.title(f'Keuntungan Bulan Ini: Rp. {untung - modal}')
                        plt.show()
                        back_to_admin()
                    except TypeError:
                        print("Tidak ada Penjualan Bulan ini!")
                        back_to_admin()

                elif (pil == "2"):
                    clr()
                    daftarBarang1(terjual)
                    back_to_admin()
                    
                elif (pil == "3"):
                    while (True):
                        yakin = input("Apakah anda yakin ingin menghapus History (Y/N) ? :    ")
                        if (yakin.upper() == "Y") :
                            param1 = "DELETE FROM terjual"
                            commit(param1)
                            print("Berhasil!!")
                            break
                        elif (yakin.upper() == "N") :
                            break    
                        else :
                            print("Input yang anda Masukkan SALAH!")
                    clr()
                    
                    back_to_admin()
                    
                elif (pil == "0"):
                    back_to_admin()

                else: 
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
                
        elif (pil == "3") :
            pil = ''
            allMenu = ['1', '2', '3', '4']
            while(pil not in allMenu):
                clr()
                print(" _______________________________________________________________________________________") 
                print("|                                                                     Data Pelanggan    |")             
                print("|    1.  Lihat Data Pelanggan                                                           |")      
                print("|    2.  Tambah Pelanggan                                                               |")      
                print("|    3.  Ubah Data Pelanggan                                                            |")   
                print("|    4.  Hapus Data Pelanggan                                                           |")   
                print("|                                                                                       |")   
                print("|       0.  Kembali                                                                     |")   
                print("|                                                                                       |")   
                print("|                                                                                       |")       
                print("|_______________________________________________________________________________________|") 
                pil = input(" Pilih Menu >>  ")

                if (pil == "1"):
                    clr()
                    daftarOrang(costumers)
                    back_to_admin()

                elif(pil == "2"):
                    print("\n\nTambah Pelanggan\n\n")
                    
                    firstName = ''
                    lastName = ''
                    address = ''
                    email = ''
                    phoneNumber = ''


                    while (firstName == ''):
                        firstName = input("Masukkan Nama Depan :   ")
                        if (firstName == ''):
                            print("Nama Depan tidak boleh kosong")
                    
                    while (lastName == ''):
                        lastName = input("Masukkan Nama Belakang :    ")
                        if (lastName == ''):
                            print("Nama Belakang tidak boleh kosong")
                    
                    while (address == ''):
                        print("Contoh Alamat: Jalan Ulin RT 10 Kel. Sebulu Ulu Kec. Sebulu  Kab. Kutai Kartanegara Kalimantan Timur 75552")
                        address = input("Masukkan Alamat Lengkap :  ")
                        if (address == ''):
                            print("Alamat tidak boleh kosong")
                    
                    while (email == ''):
                        email = input("Masukkan Email :   ")
                        if (email == ''):
                            print("Email tidak boleh kosong")
                    
                    while (phoneNumber == ''):
                        phoneNumber = input("Masukkan Nomor Handphone :    ")
                        if (phoneNumber == ''):
                            print("Nomor Telepon tidak boleh kosong")

                    tambahOrang(None, firstName, lastName, address, email, phoneNumber)
                    back_to_admin()


                elif(pil == "3"):
                    while(True):
                        try:
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

                            ubah(**kwargs)
                            break

                        except ValueError:
                            input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                            continue
                        except IndexError:
                            input("Mohon Maaf, Orang yang ingin diubahh tidak ada di data!\n\n")
                            continue
                    back_to_admin()

                elif(pil == "4"):
                    while(True):
                        try:
                            clr()
                            daftarOrang(costumers)

                            pil = int(input("\nPilihlah Orang Yang Ingin Anda Hapus (ID) :      "))
                            pil -= 1
                            
                            id = costumers[pil][0]
                            
                            hapusOrang(id)
                            break
                        except ValueError:
                            input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                            continue
                        except IndexError:
                            input("Mohon Maaf, Orang yang ingin dihapus tidak ada di data!\n\n")
                            continue
                    back_to_admin()

                elif (pil == "0"):
                    back_to_admin()

                else: 
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
                


        elif (pil == "4") :
            clr()
            daftarBarang(items)
            back_to_admin()


        elif (pil == "5") :
            jenis = ''
            brand = ''
            varian = ''
            warna = ''
            harga = ''
            modal = ''
            stok = ''
            while(jenis == ''):
                jenis = input("Masukkan Jenis Barang :   ")
                if (jenis == ''):
                    print("Jenis Tidak Boleh Kosong!")
            while(brand == ''):
                brand = input("Masukkan Merk Barang :    ")
                if (brand == ''):
                    print("Brand Tidak Boleh Kosong!")
            while(varian == ''):
                varian = input("Masukkan Varian Barang :  ")
                if (varian == ''):
                    print("Varian Tidak Boleh Kosong!")
            while(warna == ''):
                warna = input("Masukkan Warna Barang :   ")
                if (warna == ''):
                    print("Warna Tidak Boleh Kosong!")
            while(harga == ''):
                try:
                    harga = int(input("Masukkan Harga Barang :   "))
                    if (harga == ''):
                        print("Harga Tidak Boleh Kosong!")
                except ValueError:
                    input("Harga Harus Berupa Angka!")
                    continue
            while(modal == ''):
                try:
                    modal = int(input("Masukkan Harga Modal :   "))
                    if (modal == ''):
                        print("Modal Tidak Boleh Kosong!")
                except ValueError:
                    input("Modal Harus Berupa Angka!")
                    continue
            while(stok == ''):
                try:
                    stok = int(input("Masukkan Stok Barang :    "))
                    if (stok == ''):
                        print("Stok Tidak Boleh Kosong!")
                except ValueError:
                    input("Stok Harus Berupa Angka!")
                    continue

            
        
            tambahBarang(None, jenis, brand, varian, warna, harga, modal, stok)
            back_to_admin()

        
        
        elif (pil == "6") :
            clr()
            daftarBarang(items)

            while(True):
                try:
                    pil = int(input("\nPilihlah Barang Yang Ingin Anda Hapus (ID) :      "))
                    pil -= 1    
                    id = items[pil][0]
                    
                    hapusBarang(id)
                    break

                except ValueError:
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
                except IndexError:
                    input("Mohon Maaf, Barang yang ingin dihapus tidak ada di data!\n\n")
                    continue
            back_to_admin()        

        elif (pil == "7") :
            clr()
            daftarBarang(items)

            while(True):
                try:
                    pil = int(input("\nPilihlah Barang Yang Ingin Anda Ubah (ID) :      "))
                    pil -= 1    
                    id = items[pil][0]

                    ubahHargaBarang(id)
                    break
                    
                except ValueError:
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
                except IndexError:
                    input("Mohon Maaf, Barang yang ingin diubah tidak ada di data!\n\n")
                    continue
            back_to_admin()        
            

        elif (pil == "8") :
            clr()
            daftarBarang(items)

            while(True):
                try:
                    pil = int(input("\nPilihlah Barang Yang Ingin Anda Tambah Stoknya (ID) :      "))
                    pil -= 1    
                    id = items[pil][0]
                    stok = items[pil][7]
                    tambahStok(stok, id)
                    break
                    
                    
                except ValueError:
                    input("Input anda Salah, Tekan Enter untuk melanjutkan!")
                    continue
                except IndexError:
                    input("Mohon Maaf, Barang yang ingin diubah tidak ada di data!\n\n")
                    continue
            back_to_admin()      


        elif (pil == "9") :
            clr()
            print(" _______________________________________________________________________________________") 
            print("|                                                                        Urut Barang    |")            
            print("|    1.  Urutkan Berdasarkan Jenis                                                      |")      
            print("|    2.  Urutkan Berdasarkan Brand                                                      |")      
            print("|    3.  Urutkan Berdasarkan Warna                                                      |")      
            print("|    4.  Urutkan Berdasarkan Varian                                                     |")      
            print("|    5.  Urutkan Berdasarkan Harga                                                      |")           
            print("|                                                                                       |")   
            print("|       0.  Kembali                                                                     |")    
            print("|                                                                                       |") 
            print("|_______________________________________________________________________________________|") 

            while(True):
                pilUrut = input("\n\tAnda ingin Mengurutkan Berdasarkan : ")    
                
                if (pilUrut == "1"):
                    pilUrut = "Jenis"
                    break
                elif (pilUrut == "2"):
                    pilUrut = "Brand"
                    break
                elif (pilUrut == "3"): 
                    pilUrut = "Warna"
                    break
                elif (pilUrut == "4"): 
                    pilUrut = "Varian"
                    break
                elif (pilUrut == "5"): 
                    pilUrut = "Harga"
                    break
                elif (pilUrut == "0"):
                    back_to_admin()
                else: 
                    print("Input anda Salah, Masukkan Ulang!")
                    continue

            key = orderby(pilUrut.lower(), items)
            input("\n\n\nTekan Enter Untuk Kembali ...")
            menu(key)
        elif (pil == "0") :
            menu(param)

        else : 
            input("Input anda Salah, Tekan Enter untuk melanjutkan!")
        












def menu(param):
    items = query("SELECT * FROM barang ORDER BY " + param)
    costumers = query("SELECT * FROM costumers ORDER BY first_name")
    terjual = query("SELECT * FROM terjual ORDER BY date")
    clr()

    print("".rjust(39))
    print(" _______________________________________________________________________________________")
    print("|                                                     SELAMAT DATANG DI TOKO PANCING    |")
    print("|       1.  Admin                                                                       |")      
    print("|       2.  Lihat Daftar Barang                                                         |")      
    print("|       3.  Urutkan Barang                                                              |")      
    print("|       4.  Cari Barang                                                                 |")         
    print("|       5.  Hubungi Admin                                                               |")         
    print("|                                                                                       |")   
    print("|       0.  Exit                                                                        |")
    print("|                                                                                       |")   
    print("|                                                                                       |")    
    print("|_______________________________________________________________________________________|")    

    pil = input(" Pilih Menu >>  ")

    if (pil == "1" and login == False):
        signIn()
    if (pil == "1" and login == True):
        admin()
        
        






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
            back_to_menu()
            
            
        elif (pil == "2") :
            clr()

            stokTersedia = "SELECT * FROM barang WHERE stok != 0 ORDER BY " + param
            items = query(stokTersedia)
            daftarBarang(items)
            back_to_menu()


        elif (pil == "3") :
            clr()

            stokKosong = "SELECT * FROM barang WHERE stok = 0 ORDER BY " + param
            items = query(stokKosong)
            daftarBarang(items)
            back_to_menu()



        elif (pil == "4") :
            clr()            
            daftarBarang(items)
            while(True): 
                keyword = input("\n\nKetikkan Sesuatu Untuk Mencari :     ") 
                if (keyword == ""):
                    print("Tidak Boleh Kosong!")
                    continue
                else: break  
            sequentialSearch(items, keyword.title())
            back_to_menu() 


        elif (pil == "5") :
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
            
            while(True):
                pilCari = input("\n\tAnda ingin Mengurutkan Berdasarkan : ")    
                
                if (pilCari == "1"):
                    pilCari = "Jenis"
                    break
                elif (pilCari == "2"):
                    pilCari = "Brand"
                    break
                elif (pilCari == "3"): 
                    pilCari = "Warna"
                    break
                elif (pilCari == "4"): 
                    pilCari = "Varian"
                    break
                elif (pilCari == "5"): 
                    pilCari = "Harga"
                    break
                else: 
                    print("Input anda Salah, Masukkan Ulang!")
                    continue
            orderby(pilCari.lower(), items)
            back_to_menu()



        elif (pil == "0"):
            menu(param)

    elif (pil == "3") :
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

        while(True):
            pilCari = input("\n\tAnda ingin Mengurutkan Berdasarkan : ")    
            
            if (pilCari == "1"):
                pilCari = "Jenis"
                break
            elif (pilCari == "2"):
                pilCari = "Brand"
                break
            elif (pilCari == "3"): 
                pilCari = "Warna"
                break
            elif (pilCari == "4"): 
                pilCari = "Varian"
                break
            elif (pilCari == "5"): 
                pilCari = "Harga"
                break
            else: 
                print("Input anda Salah, Masukkan Ulang!")
                continue

        orderby(pilCari.lower(), items)
        back_to_menu()



    elif (pil == "4") :
        clr()            
        daftarBarang(items)
        while(True): 
                keyword = input("\n\nKetikkan Sesuatu Untuk Mencari :     ") 
                if (keyword == ""):
                    print("Tidak Boleh Kosong!")
                    continue
                else: break
        sequentialSearch(items, keyword.title())
        back_to_menu() 

    elif (pil == "5") :
        clr()
        _run = True
        while(_run):
            print("""

            Daftar Kontak Admin

            1.  Yanuar Satria Gotama  (2009106013)    ||    +62 812-4074-1502    ||
            2.  Daffa Putra Mahardika (2009106036)    ||    +62 822 5126-6939    ||
            3.  Risky Kurniawan       (2009106050)    ||    +62 821 5831-7722    ||
            
            
            0.  Kembali

            """)
            pil = input("\n\nHubungi Kontak  >>  ")
            if pil == "1": 
                webbrowser.open('https://wa.me/6281240741502')
                _run = False
                menu(param)

            elif pil == "2": 
                webbrowser.open('https://wa.me/6282251266939')
                _run = False
                menu(param)
            elif pil == "3": 
                webbrowser.open('https://wa.me/6282158317722')
                _run = False
                menu(param)
            elif pil == "0": 
                back_to_menu()
            else : 
                print("\n\nInput anda salah!")
                input("Tekan Enter Untuk Melanjutkan...")
                clr()
            
        

    elif (pil == "0"):
        print( "\n"*5 + "Terima Kasih Telah Menggunakan Program Ini (●'◡'●)つ !!!" + "\n"*10)
        exit
    
    else :
        menu(param)


menu(param)
