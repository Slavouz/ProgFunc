# Sistem penilaian mahasiswa

# Tambahkan fungsi untuk menghitung nilai akhir

# Tambahkan fungsi untuk menghitung semua nilai akhir


# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        for k in nilai_akhir:
            print(k + ":", nilai_akhir[k])


# Program utama
def main():
    data_mahasiswa = [
        {"Nama": "Bagas", "UTS": 80, "UAS": 90},
        {"Nama": "Satrya", "UTS": 75, "UAS": 80},
        {"Nama": "Yoga", "UTS": 70, "UAS": 75},
    ]

    data_nilai_akhir = {}

    for data in data_mahasiswa:
        nama = data["Nama"]
        uts = data["UTS"]
        uas = data["UAS"]
        nilai_akhir = (uts + uas) / 2
        data_nilai_akhir[nama] = {"Nama": nama, "Nilai Akhir": nilai_akhir}

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
