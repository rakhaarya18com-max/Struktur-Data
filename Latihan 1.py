def tukar(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]


def bubble(listku):
    perubahan = True
    sesi = len(listku)

    while sesi > 1 and perubahan:
        perubahan = False
        j = 1

        while j < sesi:
            if listku[j] < listku[j - 1]:
                perubahan = True
                tukar(listku, j, j - 1)
            j += 1

        print(listku)

        if not perubahan:
            print("hasil akhir = %s" % str(listku))

        sesi -= 1


print("========== Bubble Sort ==========")

panjang = int(input("Masukkan jumlah data: "))
mylist = []

for i in range(panjang):
    angka = int(input("Masukkan data ke-%d: " % (i + 1)))
    mylist.append(angka)

print("Sebelum Bubble Sort")
print(mylist)

print("Setelah Bubble Sort")
bubble(mylist)
