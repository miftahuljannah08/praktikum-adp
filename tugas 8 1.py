data_film={
    "judul":"rumah masa depan",
    "penulis_skenario" : "ali shahab",
    "sutradara":"danial rifki ",
    "tahun_rilis":"2023"
}
for key,value in data_film.items():
    print(f"{key:<14}:{value}")

def tambah_data_film(judul,penulis_skenario,sutradara,tahun_rilis):
    with open("database_data_film.txt","a")as file:
        file.write(f"{judul},{penulis_skenario},{sutradara},{tahun_rilis}\n")
    print("data film berhasil ditambahkan")

def hapus_data_film(judul):
    with open("database_data_film.txt","r") as file:
        lines=file.readlines()
    with open("database_data_film.txt","w") as file:
        for line in lines:
            if line.split(",")[0]!=judul:
                file.write(line)
    print("data film berhasil dihapus")

def edit_data_film(judul,penulis_skenario,sutradara,tahun_rilis):
    with open("database_data_film.txt", "r") as file:
        lines = file.readlines()
    with open("database_data_film.txt", "w") as file:
        for line in lines:
            if line.split(",")[0] == judul:
                file.write(f"{judul},{penulis_skenario},{sutradara},{tahun_rilis}\n")
            else:
                file.write(line)
    print("Data film berhasil diubah.")

def tampilkan_semua_data_film():
    with open("database_data_film.txt", "r") as file:
        data_film = file.readlines()
    if  data_film:
        print("Data film:")
        for data in data_film:
            print(data.strip())
    else:
        print("Database film kosong.")

while True:   
    print("\nMenu:")
    print("1.tambah data film")
    print("2.hapus data film")
    print("3.edit data film")
    print("4.tampilkan data film")
    print("5.keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        judul = input("Masukkan judul film: ")
        penulis_skenario = input("Masukkan penulis skenario: ")
        sutradara = input("Masukkan nama sutradara: ")
        tahun_rilis = input("Masukkan tahun rilis film: ")
        tambah_data_film(judul,penulis_skenario,sutradara,tahun_rilis)
    elif pilihan == "2":
        judul = input("Masukkan judul film yang akan dihapus: ")
        hapus_data_film(judul)
    elif pilihan == "3":
        judul = input("Masukkan judul film: ")
        penulis_skenario = input("Masukkan penulis skenario: ")
        sutradara = input("Masukkan nama sutradara: ")
        tahun_rilis = input("Masukkan tahun rilis film: ")
        edit_data_film(judul,penulis_skenario,sutradara,tahun_rilis)
    elif pilihan == "4":
        tampilkan_semua_data_film()
    elif pilihan == "5":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")




    
    
  

