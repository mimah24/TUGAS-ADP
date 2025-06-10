# Nama file untuk menyimpan data
nama_file = 'data_keuangan.txt'

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n===== APLIKASI CATAT KEUANGAN ANAK KOST =====")
    print("1. Tambah Data Keuangan")
    print("2. Hapus Data Keuangan")
    print("3. Tampilkan Semua Data")
    print("4. Keluar")
    print("============================================")

# Fungsi untuk menambahkan data
def tambah_data():
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan: ")
    jumlah = input("Masukkan jumlah uang: ")
    tipe = input("Tipe (pemasukan/pengeluaran): ").lower()

    file = open(nama_file, 'a')
    file.write(tanggal + "|" + keterangan + "|" + jumlah + "|" + tipe + "\n")
    file.close()

    print("Data berhasil ditambahkan!")

# Fungsi untuk menampilkan semua data
def tampilkan_data():
    file = open(nama_file, 'r')
    data = file.readlines()
    file.close()

    if len(data) == 0:
        print("Belum ada data keuangan.")
    else:
        print("\n===== DATA KEUANGAN =====")
        for i in range(len(data)):
            bagian = data[i].strip().split("|")
            print("ID: " + str(i+1))
            print("  Tanggal    : " + bagian[0])
            print("  Keterangan : " + bagian[1])
            print("  Jumlah     : Rp" + bagian[2])
            print("  Tipe       : " + bagian[3])
            print("-----------------------------")

# Fungsi untuk menghapus data
def hapus_data():
    tampilkan_data()
    id_hapus = int(input("Masukkan ID data yang ingin dihapus: "))

    file = open(nama_file, 'r')
    data = file.readlines()
    file.close()

    del data[id_hapus-1]

    file = open(nama_file, 'w')
    file.writelines(data)
    file.close()

    print("Data berhasil dihapus!")

# Program utama
def menu():
    while True:
        show_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            hapus_data()
        elif pilihan == '3':
            tampilkan_data()
        elif pilihan == '4':
            print("Terima kasih sudah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()
