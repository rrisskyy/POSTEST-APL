# Risky Kurniawan 2009106050

import os
from time import sleep


def clr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

num = [22, 12, 1, 8, 3, 2]
num2 = []







def tambah (pilTambah, num) : 
    if (pilTambah == "1") : 
        pilAddNum = input("Anda ingin menambahkan angka baru di akhir? (Y/N) :    ")
        if (pilAddNum.lower() == "y") :
            addNum = int(input("\nMasukkan angka yang ingin anda tambahkan :   "))
            num.append(addNum)
            print(num)
            print("\nOK\n\n\n")
            input("Klik Apapun untuk kembali ke Menu...")
            return num

        elif (pilAddNum.lower() == "n") :
            indexAddNum = int(input("Di index ke berapa anda ingin memasukkannya? :    "))
            addNum = int(input("\nMasukkan angka yang ingin anda tambahkan :   "))
            num.insert(indexAddNum, addNum)
            print(num)
            print("\nOK\n\n\n")
            input("Klik Apapun untuk kembali ke Menu...")
            return num

        else :
            print("Input yang anda Masukkan Salah!")
            sleep(2)
            tambah(pilTambah, num)

    elif (pilTambah == "2") :
            print("Masukkan Elemen List dan pisah dengan Spasi")
            addList = filter(None, input(">>   ").split(" "))
            addList = list(map(int, addList))   
            print("\nOK\n\n\n")
            input("Klik Apapun untuk kembali ke Menu...")
            return addList



def hapus(pilHapus, num) : 
    if (pilHapus == "1") :
        delNum = int(input("\nMasukkan angka yang ingin anda hapus :   "))
        num.remove(delNum)
        print(num)
        print("\nOK\n\n\n")
        input("Klik Apapun untuk kembali ke Menu...")
        return num



def update(num) : 
    indexUpdNum = int(input("Anda ingin Mengupdate Angka di index ke berapa? :   "))
    print("Anda memilih angka ", num[indexUpdNum])
    pilIndex = input("Apakah Anda yakin ingin Mengubahnya? (Y/N)       :     ")
    updNum = int(input("\n\nAnda ingin mengubahnya menjadi angka berapa? :   ")) if pilIndex.lower() == "y" else update(num, num2)
    num[indexUpdNum] = updNum
    print(num)
    print("\nOK\n\n\n")
    input("Klik Apapun untuk kembali ke Menu...")
    return num



def asc(num): 
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1] :
                num[j], num[j+1] = num[j+1], num[j]
    print(num)
    print("\nOK\n\n\n")
    input("Klik Apapun untuk kembali ke Menu...")
    return num



def desc(num): 
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] < num[j+1] :
                num[j], num[j+1] = num[j+1], num[j]
    print(num)
    print("\nOK\n\n\n")
    input("Klik Apapun untuk kembali ke Menu...")
    return num



def minimum(x): 
    min = x[0]

    for i in range(len(x)):
        if x[i] < min:
            min = x[i]

    return min



def maksimum(x): 
    max = x[0]

    for i in range(len(x)):
        if x[i] > max:
            max = x[i]

    return max







while(True) :
    clr()
    print("\n")
    if (len(num) == 0 and len(num2) == 0) :
        print(" ", "\n")
    elif (len(num) != 0 and len(num2) != 0) :
        print(" ", num, num2, "\n")
    elif (len(num) != 0) : 
        print(" ", num, "\n")
    elif (len(num2) != 0) :
        print(" ", num2, "\n")
    
    
    print("//=====================================================\\\\")
    print("||   1. Tambahkan Data                                 ||")      # ✔
    print("||   2. Hapus Data                                     ||")      # ✔
    print("||   3. Update Data                                    ||")      # ✔
    print("||   4. Urutkan Data                                   ||")      # ✔
    print("||   5. MIN                                            ||")      # ✔
    print("||   6. MAX                                            ||")      # ✔
    print("||   7. Banyaknya data didalam List                    ||")      
    print("||   8. Balik Urutan List                              ||")      
    print("||   9. Tambahkan Dua Buah List                        ||")      
    print("||   0. Exit                                           ||")      
    print("\\\\=====================================================//\n")

    pil = input("Pilih Menu >>  ")



# TAMBAH DATA
    if(pil == "1") : 
        while(True) :
            print("\n\n     Tambah Data")
            print("//=====================================================\\\\")
            print("||   1. Tambahkan Elemen Baru                          ||")
            print("||   2. Tambahkan List Baru                            ||")
            print("\\\\=====================================================//\n")
            pilTambah = input("Anda Ingin Menambahkan Apa? (1 / 2) :    ")
            if (pilTambah == "1") : 
                if (len(num2) == 0) :
                    num = tambah(pilTambah, num)
                    break
                else : 
                    print("1 : ", num)
                    print("2 : ", num2)
                    listAddNum = input("Anda ingin Menambah Elemen List 1 Atau List 2? (1 / 2) :    ")    
                    if (listAddNum == "1") :
                        num = tambah(pilTambah, num)
                        break
                    elif (listAddNum == "2") :
                        num2 = tambah(pilTambah, num2)
                        break
                    else : 
                        print("Input yang anda Masukkan Salah!\n\n\n")
                        sleep(2)
                        continue
            elif (pilTambah == "2") :
                num2 = tambah(pilTambah, num2)
                break
            else : 
                print("Input yang anda Masukkan Salah!\n\n\n")
                sleep(2)
                continue



# HAPUS DATA
    if(pil == "2") : 
        while(True) :
            print("\n\n     Hapus Data")
            print("//=====================================================\\\\")
            print("||   1. Hapus Elemen List                              ||")
            print("||   2. Hapus List                                     ||")
            print("\\\\=====================================================//\n")
            pilHapus = input("Anda ingin Menghapus apa? :    ")

            if (pilHapus == "1") :
                if (len(num2) == 0) : 
                    num = hapus(pilHapus, num)
                    break
                else :
                    print("1 : ", num)
                    print("2 : ", num2)
                    listDelNum = input("Anda ingin Menghapus Elemen List 1 Atau List 2? (1 / 2) :    ")    
                    if (listDelNum == "1") :
                        num = hapus(pilHapus, num)
                        break
                    elif (listDelNum == "2") :
                        num = hapus(pilHapus, num2)
                        break
                    else : 
                        print("Input yang anda Masukkan Salah!\n\n\n")
                        sleep(2)
                        continue
            elif (pilHapus == "2") :    
                pilDel = input("Apakah anda yakin ? (Y/N): ")            
                if (pilDel.lower() == "y") :
                    if (len(num2) == 0) : 
                        num = []
                        print("LIST BERHASIL DIHAPUS!")
                        input("Klik Apapun untuk kembali ke Menu...")
                        break
                    else :
                        print("1 : ", num)
                        print("2 : ", num2)
                        listDelNum = input("Anda ingin Menghapus List 1 Atau List 2? (1 / 2) :    ")    
                        if (listDelNum == "1") :
                            num = []
                            print("LIST BERHASIL DIHAPUS!")
                            input("Klik Apapun untuk kembali ke Menu...")
                            break
                        elif (listDelNum == "2") :
                            num2 = []
                            print("LIST BERHASIL DIHAPUS!")
                            input("Klik Apapun untuk kembali ke Menu...")
                            break
                        else : 
                            print("Input yang anda Masukkan Salah!\n\n\n")
                            sleep(2)
                            continue
                else : 
                    break



# UPDATE DATA
    if(pil == "3") : 
        while(True) :
            if (len(num2) == 0) : 
                num = update(num)
                break
            else :
                print("1 : ", num)
                print("2 : ", num2)
                listUpd = input("Anda ingin Mengupdate Elemen List 1 Atau List 2? (1 / 2) :    ")    
                if (listUpd == "1") :
                    num = update(num)
                    break
                elif (listUpd == "2") :
                    num2 = update(num2)
                    break
                else : 
                    print("Input yang anda Masukkan Salah!\n\n\n")
                    sleep(2)
                    continue


    
# URUT DATA
    if(pil == "4") : 
        while(True) :
            print("\n\n     Mengurutkan Data")
            print("//=====================================================\\\\")
            print("||   1. Ascending                                      ||")
            print("||   2. Descending                                     ||")
            print("\\\\=====================================================//\n")
            pilUrut = input("Anda ingin Mengurutkan Secara Ascending Atau Descending (1 / 2) ? :   ")
            if(pilUrut == "1") :
                if (len(num2) == 0) : 
                    num = asc(num)
                    break
                else :
                    print("1 : ", num)
                    print("2 : ", num2)
                    listUrut = input("Anda ingin Mengurutkan Elemen List 1 Atau List 2? (1 / 2) :    ")    
                    if (listUrut == "1") :
                        num = asc(num)
                        break
                    elif (listUrut == "2") :
                        num = asc(num2)
                        break
                    else : 
                        print("Input yang anda Masukkan Salah!\n\n\n")
                        sleep(2)
                        continue

            elif(pilUrut == "2") :
                if (len(num2) == 0) : 
                    num = desc(num)
                    break
                else :
                    print("1 : ", num)
                    print("2 : ", num2)
                    listUrut = input("Anda ingin Mengurutkan Elemen List 1 Atau List 2? (1 / 2) :    ")    
                    if (listUrut == "1") :
                        num = desc(num)
                        break
                    elif (listUrut == "2") :
                        num = desc(num2)
                        break
                    else : 
                        print("Input yang anda Masukkan Salah!\n\n\n")
                        sleep(2)
                        continue



# MIN
    if(pil == "5") : 
        while(True) :
            if (len(num2) == 0) : 
                min = minimum(num)
                print("Angka Terkecil adalah : ", min, "\n\n\n")
                input("Klik Apapun untuk kembali ke Menu...")
                break
            else :
                print("1 : ", num)
                print("2 : ", num2)
                listMin = input("Anda ingin Mencari Nilai Terkecil List 1 Atau List 2? (1 / 2) :    ")    
                if (listMin == "1") :
                    min = minimum(num)
                    print("Angka Terkecil adalah : ", min, "\n\n\n")
                    input("Klik Apapun untuk kembali ke Menu...")
                
                    break
                elif (listMin == "2") :
                    min = minimum(num2)
                    print("Angka Terkecil adalah : ", min, "\n\n\n")
                    input("Klik Apapun untuk kembali ke Menu...")
                
                    break
                else : 
                    print("Input yang anda Masukkan Salah!\n\n\n")
                    sleep(2)
                    continue



# MAX
    if(pil == "6") : 
        while(True) :
            if (len(num2) == 0) : 
                max = maksimum(num)
                print("Angka Terbesar adalah : ", max, "\n\n\n")
                input("Klik Apapun untuk kembali ke Menu...")
                break
            else :
                print("1 : ", num)
                print("2 : ", num2)
                listMax = input("Anda ingin Mencari Nilai Terbesar List 1 Atau List 2? (1 / 2) :    ")    
                if (listMax == "1") :
                    max = maksimum(num)
                    print("Angka Terbesar adalah : ", max, "\n\n\n")
                    input("Klik Apapun untuk kembali ke Menu...")
    
                    break
                elif (listMax == "2") :
                    max = maksimum(num2)
                    print("Angka Terbesar adalah : ", max, "\n\n\n")
                    input("Klik Apapun untuk kembali ke Menu...")
    
                    break
                else : 
                    print("Input yang anda Masukkan Salah!\n\n\n")
                    sleep(2)
                    continue



#COUNT DATA
    if (pil == "7") : 
        while(True) :
            if (len(num2) == 0) : 
                print("Banyaknya data di dalam List adalah :  ", len(num))
                input("Klik Apapun untuk kembali ke Menu...")
                break
            else :
                print("//=====================================================\\\\")
                print("||   List")
                print("||   1. ", num)
                print("||   2. ", num2)
                print("\\\\=====================================================//\n")
                print("//=====================================================\\\\")
                print("||   Banyak Data List")
                print("||   1. ", len(num))
                print("||   2. ", len(num2))
                print("\\\\=====================================================//\n")
                input("Klik Apapun untuk kembali ke Menu...")
                break



# REVERSE DATA
    if (pil == "8") : 
        while(True) :
            if (len(num2) == 0) : 
                num.reverse()
                print("\nList Akan Menjadi Seperti Ini :   ", num)
                input("Klik Apapun untuk kembali ke Menu...")
                break
            else :
                print("//=====================================================\\\\")
                print("||   List Akan Menjadi Seperti ini : ")
                num.reverse()
                print("||   1. ", num)
                num2.reverse()
                print("||   2. ", num2)
                print("\\\\=====================================================//\n")
                input("Klik Apapun untuk kembali ke Menu...")
                break



# EXTEND DATA
    if (pil == "9") : 
        while(True) :
            if (len(num2) == 0) : 
                num.reverse()
                print("Tidak ada list Kedua untuk di Extend, Silakan Tambah Dahulu List nya!")
                input("Klik Apapun untuk kembali ke Menu...")
                break
            else :
                print("//=====================================================\\\\")
                print("||   List Akan Menjadi Seperti Ini : ")
                num.extend(num2)
                print("||   ", num)
                print("\\\\=====================================================//\n")
                input("Klik Apapun untuk kembali ke Menu...")
                num2 = []
                break



# EXIT
    if (pil == "0") :
        print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI!")
        input("Klik Apapun untuk Keluar Aplikasi!!!")
        break
