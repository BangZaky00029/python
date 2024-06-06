from datetime import datetime

def atur_jadwal(kegiatan):
    # Urutkan daftar kegiatan berdasarkan waktu mulai
    kegiatan.sort(key=lambda x: datetime.strptime(x['waktu_mulai'], "%H:%M"))
    
    # Periksa setiap kegiatan dengan kegiatan berikutnya apakah ada tumpang tindih waktu
    for i in range(len(kegiatan) - 1):
        waktu_selesai_sekarang = datetime.strptime(kegiatan[i]['waktu_selesai'], "%H:%M")
        waktu_mulai_berikutnya = datetime.strptime(kegiatan[i + 1]['waktu_mulai'], "%H:%M")
        if waktu_selesai_sekarang > waktu_mulai_berikutnya:
            return f"Ada tumpang tindih waktu antara kegiatan '{kegiatan[i]['nama_kegiatan']}' dan '{kegiatan[i + 1]['nama_kegiatan']}'"
    
    # Jika tidak ada tumpang tindih, kembalikan jadwal yang sudah diurutkan
    return kegiatan

def tampilkan_jadwal(kegiatan):
    # Tampilkan kegiatan dalam format rapi
    for k in kegiatan:
        print("-" * 30)
        print(f"Nama Kegiatan: {k['nama_kegiatan']}")
        print(f"Waktu Mulai  : {k['waktu_mulai']}")
        print(f"Waktu Selesai: {k['waktu_selesai']}")
        print("-" * 30)

def masukkan_jadwal(kegiatan):
    while True:
        nama_kegiatan = input("Masukkan nama kegiatan (atau ketik 'selesai' untuk mengakhiri): ")
        if nama_kegiatan.lower() == 'selesai':
            break
        waktu_mulai = input("Masukkan waktu mulai (format HH:MM): ")
        waktu_selesai = input("Masukkan waktu selesai (format HH:MM): ")
        kegiatan.append({
            "nama_kegiatan": nama_kegiatan,
            "waktu_mulai": waktu_mulai,
            "waktu_selesai": waktu_selesai
        })
    return kegiatan

def tampilkan_tumpang_tindih(kegiatan):
    tumpang_tindih = []
    for i in range(len(kegiatan) - 1):
        waktu_selesai_sekarang = datetime.strptime(kegiatan[i]['waktu_selesai'], "%H:%M")
        waktu_mulai_berikutnya = datetime.strptime(kegiatan[i + 1]['waktu_mulai'], "%H:%M")
        if waktu_selesai_sekarang > waktu_mulai_berikutnya:
            tumpang_tindih.append((kegiatan[i]['nama_kegiatan'], kegiatan[i + 1]['nama_kegiatan']))
    if tumpang_tindih:
        print("Kegiatan-kegiatan ini tumpang tindih:")
        for kegiatan1, kegiatan2 in tumpang_tindih:
            print(f"- '{kegiatan1}' dan '{kegiatan2}'")
        return True
    else:
        print("Tidak ada tumpang tindih pada jadwal ini.")
        return False

def pilih_kegiatan(kegiatan):
    print("Berikut adalah kegiatan yang tersedia:")
    for i, k in enumerate(kegiatan):
        print(f"{i + 1}. {k['nama_kegiatan']}")
    while True:
        pilihan = input("Masukkan nomor kegiatan yang ingin diubah: ")
        if pilihan.isdigit() and 1 <= int(pilihan) <= len(kegiatan):
            return int(pilihan) - 1
        else:
            print("Masukan tidak valid. Harap masukkan nomor kegiatan yang sesuai.")

def tanya_lanjutkan_program():
    while True:
        jawaban = input("Apakah Anda ingin melanjutkan program? (yes/no): ").lower()
        if jawaban in ['yes', 'no']:
            return jawaban == 'yes'
        else:
            print("Masukan tidak valid. Harap masukkan 'yes' atau 'no'.")

def pilih_tampilan_jadwal():
    print("Pilih opsi tampilan jadwal:")
    print("1. Tampilkan seluruh jadwal yang sudah dibuat")
    print("2. Tampilkan jadwal yang tumpang tindih")
    while True:
        pilihan = input("Masukkan nomor pilihan Anda: ")
        if pilihan.isdigit() and 1 <= int(pilihan) <= 2:
            return int(pilihan)
        else:
            print("Masukan tidak valid. Harap masukkan 1 atau 2.")

def edit_jadwal(kegiatan):
    indeks_kegiatan = pilih_kegiatan(kegiatan)
    waktu_mulai_baru = input("Masukkan waktu mulai baru (format HH:MM): ")
    waktu_selesai_baru = input("Masukkan waktu selesai baru (format HH:MM): ")
    kegiatan[indeks_kegiatan]['waktu_mulai'] = waktu_mulai_baru
    kegiatan[indeks_kegiatan]['waktu_selesai'] = waktu_selesai_baru
    return kegiatan

def hapus_jadwal(kegiatan):
    print("Masukkan kegiatan yang mau dihapus dari jadwal yang tersedia:")
    indeks_kegiatan = pilih_kegiatan(kegiatan)
    kegiatan_dihapus = kegiatan.pop(indeks_kegiatan)
    print(f"Detail kegiatan yang sudah dihapus:")
    print("-" * 30)
    print(f"Nama Kegiatan: {kegiatan_dihapus['nama_kegiatan']}")
    print(f"Waktu Mulai  : {kegiatan_dihapus['waktu_mulai']}")
    print(f"Waktu Selesai: {kegiatan_dihapus['waktu_selesai']}")
    print("-" * 30)
    print(f"Kegiatan '{kegiatan_dihapus['nama_kegiatan']}' sudah dihapus.")
    return kegiatan


def menu_utama():
    print("Pilih opsi:")
    print("1. Tambahkan Jadwal")
    print("2. Edit Jadwal")
    print("3. Hapus Jadwal")
    print("4. Tampilkan seluruh jadwal")
    print("5. Cek Jadwal yang tumpang tindih")
    while True:
        pilihan = input("Masukkan nomor pilihan Anda: ")
        if pilihan.isdigit() and 1 <= int(pilihan) <= 5:
            return int(pilihan)
        else:
            print("Masukan tidak valid. Harap masukkan nomor antara 1 dan 5.")

# Loop utama program
kegiatan = []

while True:
    pilihan = menu_utama()
    
    if pilihan == 1:  # Tambahkan Jadwal
        kegiatan = masukkan_jadwal(kegiatan)
    elif pilihan == 2:  # Edit Jadwal
        kegiatan = edit_jadwal(kegiatan)
    elif pilihan == 3:  # Hapus Jadwal
        kegiatan = hapus_jadwal(kegiatan)
    elif pilihan == 4:  # Tampilkan seluruh jadwal
        if kegiatan:
            tampilkan_jadwal(kegiatan)
        else:
            print("Tidak ada jadwal yang tersedia.")
    elif pilihan == 5:  # Cek Jadwal yang tumpang tindih
        if kegiatan:
            if tampilkan_tumpang_tindih(kegiatan):
                while True:
                    lanjutkan = input("Apakah Anda ingin mengedit jadwal yang tumpang tindih? (yes/no): ").lower()
                    if lanjutkan == 'yes':
                        kegiatan = edit_jadwal(kegiatan)
                        if not tampilkan_tumpang_tindih(kegiatan):
                            break
                    elif lanjutkan == 'no':
                        print("Jadwal Anda tumpang tindih harap segera untuk diperbaharui.")
                    else:
                        print("Masukan tidak valid. Harap masukkan 'yes' atau 'no'.")
            else:
                print("Jadwal yang tumpang tindih tidak ditemukan.")
        else:
            print("Tidak ada jadwal yang tersedia.")

    # Tanyakan kepada pengguna apakah ingin melanjutkan program
    if tanya_lanjutkan_program():
        print("Program akan dimulai ulang.")
    else:
        print("Program selesai.")
        break
