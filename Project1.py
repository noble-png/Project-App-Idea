import json

class AbsensiKelas:
    def __init__(self):
        self.siswa = {}  

    def tambah_siswa(self, id_siswa, nama):
        if id_siswa in self.siswa:
            print(f"Siswa dengan ID {id_siswa} sudah terdaftar.")
        else:
            self.siswa[id_siswa] = {"nama": nama, "kehadiran": 0}
            print(f"Siswa {nama} berhasil ditambahkan.")

    def catat_kehadiran(self, id_siswa):
        if id_siswa in self.siswa:
            self.siswa[id_siswa]["kehadiran"] += 1
            print(f"Kehadiran {self.siswa[id_siswa]['nama']} berhasil dicatat.")
        else:
            print(f"Siswa dengan ID {id_siswa} tidak ditemukan.")

    def tampilkan_siswa(self):
        if self.siswa:
            print("\nDaftar Siswa:")
            for id_siswa, data in self.siswa.items():
                print(f"ID: {id_siswa}, Nama: {data['nama']}, Kehadiran: {data['kehadiran']}")
        else:
            print("Belum ada siswa yang terdaftar.")

    def laporan_kehadiran(self):
        if self.siswa:
            print("\nLaporan Kehadiran:")
            for id_siswa, data in self.siswa.items():
                print(f"{data['nama']} - Kehadiran: {data['kehadiran']} kali")
        else:
            print("Belum ada data kehadiran yang tercatat.")

    def simpan_data(self, nama_file):
        try:
            with open(nama_file, 'w') as file:
                json.dump(self.siswa, file)
            print(f"Data berhasil disimpan ke file {nama_file}.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan data: {e}")

    def muat_data(self, nama_file):
        try:
            with open(nama_file, 'r') as file:
                self.siswa = json.load(file)
            print(f"Data berhasil dimuat dari file {nama_file}.")
        except FileNotFoundError:
            print(f"File {nama_file} tidak ditemukan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat memuat data: {e}")


def menu():
    absensi = AbsensiKelas()
    while True:
        print("\n=== Sistem Absensi Kelas ===")
        print("1. Tambah Siswa")
        print("2. Catat Kehadiran")
        print("3. Tampilkan Daftar Siswa")
        print("4. Laporan Kehadiran")
        print("5. Simpan Data ke File")
        print("6. Muat Data dari File")
        print("0. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            id_siswa = input("Masukkan ID siswa: ")
            nama = input("Masukkan nama siswa: ")
            absensi.tambah_siswa(id_siswa, nama)
        elif pilihan == "2":
            id_siswa = input("Masukkan ID siswa: ")
            absensi.catat_kehadiran(id_siswa)
        elif pilihan == "3":
            absensi.tampilkan_siswa()
        elif pilihan == "4":
            absensi.laporan_kehadiran()
        elif pilihan == "5":
            nama_file = input("Masukkan nama file (contoh: absensi.json): ")
            absensi.simpan_data(nama_file)
        elif pilihan == "6":
            nama_file = input("Masukkan nama file (contoh: absensi.json): ")
            absensi.muat_data(nama_file)
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem absensi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
