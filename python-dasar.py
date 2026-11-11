print("Hello, World!")



# KOMENTAR DI PYTHON

#  komentar satu baris

"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""


# INDENTASI DI PYTHON

if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")


#INPUT DAN OUTPUT DASAR

nama = input("Masukkan nama Anda: ")
print("Halo,", nama)


# STRUKTUR PROGRAM DENGAN FUNGSI

def main():
    print("Hello dari fungsi main!")

if __name__ == "__main__":
    main()


#TIPE DATA DASAR DI PYTHON

#1. Integer (bilangan bulat)

umur = 25
print(type(umur))  # <class 'int'>

#2. Float (bilangan desimal)

tinggi = 175.5
print(type(tinggi))  # <class 'float'>

#3. String (teks)

nama = "Alice"
print(type(nama))  # <class 'str'>

#4. Boolean (benar/salah)

is_student = True
print(type(is_student))  # <class 'bool'>

#5. List (daftar)

buah = ["apel", "pisang", "ceri"]
print(type(buah))  # <class 'list'>

#6. Tuple (tuple)

koordinat = (10, 20)
print(type(koordinat))  # <class 'tuple'>

#7. Dictionary (kamus)

mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}
print(type(mahasiswa))  # <class 'dict'>

#8. Set (himpunan)

angka = {1, 2, 3, 3, 4}
print(angka)  # {1, 2, 3, 4}
print(type(angka))  # <class 'set'>


#KONVERSI TIPE DATA

x = 10       # int
y = float(x) # konversi ke float
z = str(x)   # konversi ke string

print(y, type(y))  # 10.0 <class 'float'>
print(z, type(z))  # "10" <class 'str'>


#MEMBUBAT VARIABEL DI PYTHON

nama = "Nurhadi"
umur = 16
tinggi = 172
is_active = True

print(nama)
print(umur)
print(tinggi)
print(is_active)

#MENGECEK TIPE DATA VARIABEL

print(type(nama))      # <class 'str'>
print(type(umur))      # <class 'int'>
print(type(tinggi))    # <class 'int'>

# MENGHAPUS VARIABEL
x = 10 
print(x)

 del x 
# print(x)  error karena variable sudah di hapus
