import re
from pathlib import Path

file_data = Path(__file__).with_name("data_dummy_100_mahasiswa.txt")
mahasiswa = []

with open(file_data, "r", encoding="utf-8") as file:
    for baris in file:
        hasil = re.match(
            r"\s*(\d+)\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s*$",
            baris
        )

        if hasil:
            nomor = int(hasil.group(1))
            nama = hasil.group(2).strip()
            basis_data = int(hasil.group(3))
            sistem_operasi = int(hasil.group(4))
            struktur_data = int(hasil.group(5))

            if 1 <= nomor <= 100:
                mahasiswa.append({
                    "nama": nama,
                    "basis_data": basis_data,
                    "sistem_operasi": sistem_operasi,
                    "struktur_data": struktur_data
                })


def bubble_sort(data, mata_kuliah):
    data = data.copy()

    for i in range(len(data) - 1):
        ditukar = False

        for j in range(len(data) - 1 - i):
            if data[j][mata_kuliah] < data[j + 1][mata_kuliah]:
                data[j], data[j + 1] = data[j + 1], data[j]
                ditukar = True

        if not ditukar:
            break

    return data


def tampilkan_lima_terbaik(mata_kuliah, nama_mk):
    hasil = bubble_sort(mahasiswa, mata_kuliah)

    print(f"\nTOP 5 MAHASISWA - {nama_mk}")
    print(f"{'No.':<5}{'Nama Mahasiswa':<30}{'Nilai':>8}")
    print("-" * 43)

    for i, orang in enumerate(hasil[:5], start=1):
        print(
            f"{i:<5}{orang['nama']:<30}"
            f"{orang[mata_kuliah]:>8}"
        )


print("Jumlah mahasiswa terbaca:", len(mahasiswa))

if len(mahasiswa) == 0:
    print("Data tidak terbaca. Periksa format file TXT.")
else:
    tampilkan_lima_terbaik("basis_data", "BASIS DATA")
    tampilkan_lima_terbaik("sistem_operasi", "SISTEM OPERASI")
    tampilkan_lima_terbaik("struktur_data", "STRUKTUR DATA")