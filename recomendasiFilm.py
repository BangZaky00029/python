def rekomendasikan_film(genre_favorit, daftar_film):
    # Filter daftar film berdasarkan genre favorit
    film_terfilter = [film for film in daftar_film if film['genre'].lower() == genre_favorit.lower()]
    
    # Urutkan film yang terfilter berdasarkan popularitas (misalnya berdasarkan urutan di daftar_film)
    film_terfilter.sort(key=lambda x: daftar_film.index(x))
    
    # Pilih 3 film teratas dari daftar yang diurutkan
    rekomendasi = film_terfilter[:3]
    
    return rekomendasi

def tampilkan_rekomendasi(film_rekomendasi):
    # Tampilkan film rekomendasi dalam format rapi
    if not film_rekomendasi:
        print("Tidak ada film yang sesuai dengan genre favorit Anda.")
    else:
        for film in film_rekomendasi:
            print(f"Judul Film: {film['judul_film']}")
            print(f"Genre     : {film['genre']}")
            print("-" * 30)

def masukkan_film():
    daftar_film = []
    while True:
        judul_film = input("Masukkan judul film (atau ketik 'selesai' untuk mengakhiri): ")
        if judul_film.lower() == 'selesai':
            break
        genre = input("Masukkan genre film: ")
        daftar_film.append({
            "judul_film": judul_film,
            "genre": genre
        })
    return daftar_film

def inputGenreFavorit(daftar_film):
    genre_favorit = ""
    genre_list = [film['genre'].lower() for film in daftar_film]
    while True:
        favorit = input("Masukkan Genre favoritmu (atau ketik 'selesai' untuk mengakhiri) : ").lower()
        if favorit == 'selesai':
            break
        elif favorit in genre_list:
            genre_favorit = favorit
            break
        else:
            print("Genre yang Anda maksud tidak tersedia.")
    return genre_favorit

# Memasukkan daftar film dari pengguna
daftar_film = masukkan_film()

# Memasukkan genre favorit dari pengguna
genre_favorit = inputGenreFavorit(daftar_film)

# Mendapatkan rekomendasi film
film_rekomendasi = rekomendasikan_film(genre_favorit, daftar_film)

# Menampilkan rekomendasi film
tampilkan_rekomendasi(film_rekomendasi)
