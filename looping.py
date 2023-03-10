# membuat dictionary kosong
orang = []

# menerima input dari user dan menambahkan ke dalam dictionary
for i in range(3):
    nama = input(f"Masukkan nama orang ke-{i+1}: ")
    nik = int(input(f"Masukkan NIK orang ke-{i+1}: "))
    jenis_kelamin = input(f"Masukkan jenis kelamin orang ke-{i+1} (male/female): ")
    tanggal_lahir = input(f"Masukkan tanggal lahir orang ke-{i+1} (format: YYYY-MM-DD): ")
    
    # membuat dictionary untuk setiap orang
    data_orang = {
        'nama': nama,
        'nik': nik,
        'jenis_kelamin': jenis_kelamin,
        'tanggal_lahir': tanggal_lahir
    }
    
    # menambahkan dictionary orang ke dalam list orang
    orang.append(data_orang)

# print hasil
print(orang)