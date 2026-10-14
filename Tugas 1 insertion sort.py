
from pathlib import Path

FOLDER = Path(__file__).resolve().parent


# Membaca data pegawai
def baca_pegawai():
    pegawai = []

    with open(FOLDER / "pegawai.txt", "r", encoding="utf-8") as file:
        next(file)

        for baris in file:
            id_, nama, departemen, jabatan, gaji = (
                baris.strip().split("|")
            )

            pegawai.append({
                "id": id_,
                "nama": nama,
                "departemen": departemen,
                "jabatan": jabatan,
                "gaji": int(gaji)
            })

    return pegawai


# Insertion Sort: gaji terkecil ke terbesar
def insertion_sort(data):
    hasil = data.copy()

    for i in range(1, len(hasil)):
        kunci = hasil[i]
        j = i - 1

        while j >= 0 and hasil[j]["gaji"] > kunci["gaji"]:
            hasil[j + 1] = hasil[j]
            j -= 1

        hasil[j + 1] = kunci

    return hasil


# Menampilkan data pegawai
def tampilkan(data):
    print("\n=== HASIL INSERTION SORT ===")
    print("Urutan gaji terkecil ke terbesar\n")

    for p in data:
        gaji = "Rp" + f'{p["gaji"]:,}'.replace(",", ".")
        print(
            f'{p["id"]} | {p["nama"]:<25} | '
            f'{p["jabatan"]:<15} | {gaji}'
        )


def main():
    pegawai = baca_pegawai()
    hasil = insertion_sort(pegawai)
    tampilkan(hasil)


if __name__ == "__main__":
    main()
