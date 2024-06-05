def atur_jadwal(kegiatan):
    # Urutkan daftar kegiatan berdasarkan waktu mulai
    kegiatan.sort(key=lambda x: x['waktu_mulai'])
    
    # Periksa setiap kegiatan dengan kegiatan berikutnya apakah ada tumpang tindih waktu
    for i in range(len(kegiatan) - 1):
        waktu_selesai_sekarang = kegiatan[i]['waktu_selesai']
        waktu_mulai_berikutnya = kegiatan[i + 1]['waktu_mulai']
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

def masukkan_jadwal():
    kegiatan = []
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

# Memasukkan jadwal dari pengguna
kegiatan = masukkan_jadwal()

# Mengatur jadwal dan menampilkannya
hasil_jadwal = atur_jadwal(kegiatan)
if isinstance(hasil_jadwal, list):
    tampilkan_jadwal(hasil_jadwal)
else:
    print(hasil_jadwal)
