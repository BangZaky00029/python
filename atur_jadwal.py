from datetime import datetime

# Mengubah string waktu menjadi objek datetime jika belum dikonversi
def convert_to_datetime(kegiatan):
    for k in kegiatan:
        if isinstance(k["waktu_mulai"], str):  # Hanya konversi jika masih berupa string
            k["waktu_mulai"] = datetime.strptime(k["waktu_mulai"], "%H:%M")
        if isinstance(k["waktu_selesai"], str):  # Hanya konversi jika masih berupa string
            k["waktu_selesai"] = datetime.strptime(k["waktu_selesai"], "%H:%M")
    return kegiatan

# Memeriksa tumpang tindih
def cek_tumpang_tindih(kegiatan):
    kegiatan = convert_to_datetime(kegiatan)
    # Mengurutkan kegiatan berdasarkan waktu mulai
    kegiatan.sort(key=lambda x: x["waktu_mulai"])
    
    tumpang_tindih = []
    
    for i in range(len(kegiatan) - 1):
        if kegiatan[i]["waktu_selesai"] > kegiatan[i + 1]["waktu_mulai"]:
            tumpang_tindih.append((i, i + 1))
    
    return tumpang_tindih

def cek_jadwal(kegiatan):
    tumpang_tindih = cek_tumpang_tindih(kegiatan)
    if tumpang_tindih:
        print("Ada tumpang tindih waktu antara kegiatan.")
        print("Kegiatan yang tumpang tindih:")
        idx = 1
        for idx_kegiatan1, idx_kegiatan2 in tumpang_tindih:
            kegiatan1 = kegiatan[idx_kegiatan1]
            kegiatan2 = kegiatan[idx_kegiatan2]
            print("=" * 30)
            print(f"{idx}. Nama Kegiatan  : {kegiatan1['nama_kegiatan']}")
            print(f"   Waktu Mulai    : {kegiatan1['waktu_mulai'].strftime('%H:%M')}")
            print(f"   Waktu Selesai  : {kegiatan1['waktu_selesai'].strftime('%H:%M')}")
            print("-" * 30)
            idx += 1
            print(f"{idx}. Nama Kegiatan  : {kegiatan2['nama_kegiatan']}")
            print(f"   Waktu Mulai    : {kegiatan2['waktu_mulai'].strftime('%H:%M')}")
            print(f"   Waktu Selesai  : {kegiatan2['waktu_selesai'].strftime('%H:%M')}")
            print("=" * 30)
            idx += 1
        while True:
            pilihan = input("Masukkan nomor indeks kegiatan yang ingin diubah (atau 'batal' untuk membatalkan): ")
            if pilihan.lower() == 'batal':
                return kegiatan
            elif pilihan.isdigit():
                idx_pilihan = int(pilihan)
                if idx_pilihan >= 1 and idx_pilihan <= len(tumpang_tindih) * 2:
                    idx_kegiatan = (idx_pilihan - 1) // 2
                    idx_kegiatan1, idx_kegiatan2 = tumpang_tindih[idx_kegiatan]
                    idx_kegiatan = idx_kegiatan1 if (idx_pilihan % 2) == 1 else idx_kegiatan2
                    print(f"Kegiatan yang ingin diubah: {kegiatan[idx_kegiatan]['nama_kegiatan']}")
                    waktu_mulai_baru = input("Masukkan waktu mulai baru (format HH:MM): ")
                    waktu_selesai_baru = input("Masukkan waktu selesai baru (format HH:MM): ")
                    kegiatan[idx_kegiatan]['waktu_mulai'] = datetime.strptime(waktu_mulai_baru, "%H:%M")
                    kegiatan[idx_kegiatan]['waktu_selesai'] = datetime.strptime(waktu_selesai_baru, "%H:%M")
                    # Memeriksa kembali jadwal setelah pembaruan
                    tumpang_tindih = cek_tumpang_tindih(kegiatan)
                    if not tumpang_tindih:
                        print("Jadwal telah diperbarui.")
                        return kegiatan
                    else:
                        print("Jadwal masih tumpang tindih setelah pembaruan. Silakan periksa kembali.")
                else:
                    print("Nomor indeks kegiatan tidak valid.")
            else:
                print("Input tidak valid.")
    else:
        print("Tidak ada kegiatan yang tumpang tindih.")
    return kegiatan

# Menampilkan seluruh jadwal
def tampilkan_seluruh_jadwal(kegiatan):
    for k in kegiatan:
        print("=" * 30)
        print(f"Nama Kegiatan: {k['nama_kegiatan']}")
        print(f"Waktu Mulai  : {k['waktu_mulai'].strftime('%H:%M')}")
        print(f"Waktu Selesai: {k['waktu_selesai'].strftime('%H:%M')}")
        print("-" * 30)
        
def main():
    kegiatan = [
        {"nama_kegiatan": "Makan Siang", "waktu_mulai": "12:00", "waktu_selesai": "13:30"},
        {"nama_kegiatan": "Belajar Python", "waktu_mulai": "08:00", "waktu_selesai": "13:00"},
        {"nama_kegiatan": "Olahraga", "waktu_mulai": "16:00", "waktu_selesai": "18:00"},
        {"nama_kegiatan": "Menonton Film", "waktu_mulai": "18:00", "waktu_selesai": "22:00"},
    ]

    # Mengonversi string waktu menjadi datetime sekali di awal
    kegiatan = convert_to_datetime(kegiatan)
    
    while True:
        print("\nMenu:")
        print("1. Tampilkan Seluruh Jadwal")
        print("2. Cek Jadwal")
        print("3. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tampilkan_seluruh_jadwal(kegiatan)
        elif pilihan == "2":
            kegiatan = cek_jadwal(kegiatan)
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")

if __name__ == "__main__":
    main()
