
def selectionSort(karyawan):
    for i in range(len(karyawan) - 1):
        posisi = i

        for j in range(i + 1, len(karyawan)):
            if karyawan[j][1] < karyawan[posisi][1]:
                posisi = j

        temp = karyawan[i]
        karyawan[i] = karyawan[posisi]
        karyawan[posisi] = temp


karyawan = [
    ["Andi", 3500000],
    ["Budi", 4500000],
    ["Citra", 3000000],
    ["Dina", 5000000],
    ["Eko", 4000000]
]

print("Data Karyawan Sebelum Diurutkan:")
for nama, gaji in karyawan:
    print(nama, "- Rp", format(gaji, ",").replace(",", "."))

selectionSort(karyawan)

print("\nData Karyawan Setelah Diurutkan (Selection Sort):")
for nama, gaji in karyawan:
    print(nama, "- Rp", format(gaji, ",").replace(",", "."))
