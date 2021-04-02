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
num1Sorted = False
num2Sorted = False





def tambah (num) :

    print("1. Tambahkan Elemen Baru")
    print("2. Tambahkan List Baru")

    pilTambah = input("Anda Ingin Menambahkan Apa? :    ")

    # Tambah Elemen
    if (pilTambah == "1") : 
        pilAddNum = input("Anda ingin menambahkan angka baru di akhir? (Y/N) :    ")
        if (pilAddNum.lower() == "y") :
            addNum = int(input("\n\nMasukkan angka yang ingin anda tambahkan :   "))
            num.append(addNum)
            main()

        elif (pilAddNum.lower() == "n") :
            indexAddNum = int(input("Di index ke berapa anda ingin memasukkannya? :    "))
            addNum = int(input("\n\nMasukkan angka yang ingin anda tambahkan :   "))
            num.insert(indexAddNum, addNum)
            main()

        else :
            print("Input yang anda Masukkan Salah!")
            sleep(2)
            clr()
            tambah(num, num2)

    # Tambah List
    elif (pilTambah == "2") :
        print("Masukkan Elemen List dan pisah dengan Spasi")
        addList = filter(None, input(">>   ").split(" "))
        addList = list(map(int, addList))   
        return addList

    else : 
        print("Input yang anda Masukkan Salah!")
        sleep(2)
        clr()
        tambah(num, num2)



def hapus(num, num2) : 
    if (len(num2) == 0) : 
        delNum = int(input("\n\nMasukkan angka yang ingin anda hapus :   "))
        num.remove(delNum)
        main()
    elif (len(num2) != 0) : 
        print("1 : ", num)
        print("2 : ", num2)
        listDelNum = input("Anda ingin Menghapus Elemen List 1 Atau List 2? :    ")
        if (listDelNum == "1") : 
            delNum = int(input("\n\nMasukkan angka yang ingin anda hapus :    "))
            num.remove(delNum)
            main()
        elif (listDelNum == "2") :
            delNum = int(input("\n\nMasukkan angka yang ingin anda hapus :    "))
            num2.remove(delNum)
            main()
        else :
            print("Input yang anda Masukkan Salah!")
            sleep(2)
            clr()
            hapus(num, num2)
        


def update(num, num2) : 
    if (len(num2) == 0) : 
        indexUpdNum = int(input("Anda ingin Mengupdate Angka di index ke berapa? :   "))
        print("Anda memilih angka ", num[indexUpdNum])
        pilIndex = input("Apakah Anda yakin ingin Mengubahnya? (Y/N)       :     ")
        updNum = int(input("\n\nAnda ingin mengubahnya menjadi angka berapa? :   ")) if pilIndex.lower() == "y" else update(num, num2)
        num[indexUpdNum] = updNum
        main()
    elif (len(num2) != 0) : 
        print("1 : ", num)
        print("2 : ", num2)
        listUpdNum = input("Anda ingin Mengubah List 1 Atau List 2? :   ")
        if (listUpdNum == "1") : 
            indexUpdNum = int(input("Anda ingin Mengupdate Angka di index ke berapa? :   "))
            print("Anda memilih angka ", num[indexUpdNum])
            pilIndex = input("Apakah Anda yakin ingin Mengubahnya? (Y/N)       :     ")
            updNum = int(input("\n\nAnda ingin mengubahnya menjadi angka berapa? :   ")) if pilIndex.lower() == "y" else update(num, num2)
            num[indexUpdNum] = updNum
            main()
        elif(listUpdNum == "2") :
            indexUpdNum = int(input("Anda ingin Mengupdate Angka di index ke berapa? :   "))
            print("Anda memilih angka ", num2[indexUpdNum])
            pilIndex = input("Apakah Anda yakin ingin Mengubahnya? (Y/N)       :     ")
            updNum = int(input("\n\nAnda ingin mengubahnya menjadi angka berapa? :   ")) if pilIndex.lower() == "y" else update(num, num2)
            num2[indexUpdNum] = updNum
            main()
        else :
            print("Input yang anda Masukkan Salah!")
            sleep(2)
            clr()
            update(num, num2)



def urut(num, num2) : 
    global num1Sorted,num2Sorted
    ascSortedList = []
    descSortedList = []
    
    print("1. Ascending")
    print("2. Descending")
    pilUrut = input("Anda ingin Mengurutkan Secara Ascending Atau Descending (1 / 2) ? :   ")
    if (pilUrut == "1") :
        if (len(num2) == 0) : 
            while num:
                min = num[0]  
                for x in num: 
                    if x < min:
                        min = x
                ascSortedList.append(min)
                num.remove(min)  
            num1Sorted = True
            return ascSortedList
        elif (len(num2) != 0) :     
            print("1 : ", num)
            print("2 : ", num2)
            listUrutNum = input("Anda ingin Mengurutkan List 1 Atau List 2? :   ")
            if (listUrutNum == "1") :
                while num:
                    min = num[0]  
                    for x in num: 
                        if x < min:
                            min = x
                    ascSortedList.append(min)
                    num.remove(min)  
                num1Sorted = True
                return ascSortedList

            elif (listUrutNum == "2") :
                while num2:
                    min = num2[0]  
                    for x in num2: 
                        if x < min:
                            min = x
                    ascSortedList.append(min)
                    num2.remove(min)  
                num2Sorted = True
                return ascSortedList


    if (pilUrut == "2") : 
            if (len(num2) == 0) : 
                while num:
                    max = num[0]  
                    for x in num: 
                        if x > max:
                            max = x
                    descSortedList.append(max)
                    num.remove(max)  
                numSorted = True
                return descSortedList
            elif (len(num2) != 0) :     
                print("1 : ", num)
                print("2 : ", num2)
                listUrutNum = input("Anda ingin Mengurutkan List 1 Atau List 2? :   ")
                if (listUrutNum == "1") :
                    while num:
                        max = num[0]  
                        for x in num: 
                            if x > max:
                                max = x
                        descSortedList.append(max)
                        num.remove(max)  
                    numSorted = True
                    return descSortedList

                elif (listUrutNum == "2") :
                    while num2:
                        max = num2[0]  
                        for x in num2: 
                            if x > max:
                                max = x
                        descSortedList.append(max)
                        num2.remove(max)  
                    num2Sorted = True
                    return descSortedList


def minEl(num, num2) :
    current_min = list[0]  # Start by assuming the first number is smallest
    for num in list:       # Loop through each number in the list
        if num < current_min:
            current_min = num  # Update current_min if current number is less
    return current_min






def main() : 
    global num, num2
    clr()
    print("\n")
    if (len(num2) == 0) : 
        print(" ", num, "\n")
    if (len(num2) != 0) :
        print(" ", num, num2, "\n")
    print("//=====================================================\\\\")
    print("||   1. Tambahkan Data                                 ||")
    print("||   2. Hapus Data                                     ||")
    print("||   3. Update Data                                    ||")
    print("||   4. Urutkan Data                                   ||")
    print("||   5. MIN                                            ||")
    print("||   6. MAX                                            ||")
    print("||   7. Banyaknya Angka didalam List                   ||")
    print("||   8. Balik Urutan List                              ||")
    print("||   9. Tambahkan Dua Buah List                        ||")
    print("||   0. Exit                                           ||")
    print("\\\\=====================================================//\n")

    pil = input("Pilih Menu >>  ")

    if(pil == "1") : 
        print("1. Tambahkan Elemen Baru")
        print("2. Tambahkan List Baru")

        pilTambah = input("Anda Ingin Menambahkan Apa? :    ")




        num2 = tambah(num)
        main()
    if(pil == "2") : 
        hapus(num, num2)
    if(pil == "3") : 
        update(num, num2)
    if(pil == "4") : 
        sorted = urut(num, num2)
        if (num1Sorted == True) :
            num = sorted
        elif (num2Sorted == True) :
            num2 = sorted
        main()
    if(pil == "5") : 
        minEl(num, num2)
    # if(pil == "6") : 
    #     max(num, num2)
    # if(pil == "7") : 
    #     count(num, num2)
    # if(pil == "8") : 
    #     balik(num, num2)



main()