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


#KONSTANTA DI PYTHON

PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"

#KONSTANTA DI DALAM MODULE

PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"

from constants import PI, GRAVITY, MAX_RETRY

print("Nilai PI:", PI)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)

#CONTOH PENGGUNAAN KONSTANTA 

TAX_RATE = 0.1  # 10% pajak

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)

# OPERATOR ARITMATIKA

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000


#OPERATOR PERBANDINGAN 

x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

# OPERATOR LOGIKA

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# OPERATOR PENUGASAN 

x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0

# OPERATOR KEANGGOTAAN (MEMBERSHIP)

buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True
print("pisang" not in buah) # True

# OPERATOR IDENTITAS

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True (b menunjuk objek yang sama dengan a)
print(a is c)     # False (c objek berbeda walau isinya sama)
print(a == c)     # True (nilai isinya sama)


# CONTROL FLOW (ALUR KENDALI)

# PERCABANGAN (IF, ELIF, ELSE)

nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B

# perulangan for

buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Output:
# apel
# jeruk
# mangga

# perulangan while

count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

# Output:
# Hitung: 0
# Hitung: 1
# Hitung: 2
# Hitung: 3
# Hitung: 4

#BREAK DAN CONTINUE

for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)

# Output:
# 1
# 2
# 4


#FUNCTION

def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()

#FUNCTION DENGAN PARAMETER

def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Siti")

#FUNCTION DENGAN RETRUN VALUE

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)


#DEFAULT PARAMETER

def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi")  # Menggunakan parameter
sapa_orang()        # Menggunakan default


#FUNCTION DENGAN BANYAK BANYAK ARGUMEN (*ARGS DAN **KWARGS)

# *args
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")


#LIST, TUPLE, DAN SET
# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])   # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)


# Membuat tuple
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1])   # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning"  # Error

# Tapi bisa diakses dengan loop
for w in warna:
    print(w)


# Membuat set
angka = {1, 2, 3, 3, 4, 5}

print(angka)  # {1, 2, 3, 4, 5} (duplikat otomatis hilang)

# Menambah elemen
angka.add(6)

# Menghapus elemen
angka.remove(2)

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)   # Union
print(ganjil & genap)   # Intersection
print(ganjil - genap)   # Difference


#DICTIONARY

# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

#MENGAKSES DATA
print(mahasiswa["nama"])    # Budi
print(mahasiswa.get("umur")) # 20

#MENAMBAH DAN MENGUBAH DATA
mahasiswa["angkatan"] = 2023   # Menambah data baru
mahasiswa["umur"] = 21         # Mengubah value umur

print(mahasiswa)

#MENHAPUS DATA

mahasiswa.pop("jurusan")   # Menghapus dengan key
del mahasiswa["nama"]      # Menghapus dengan del

print(mahasiswa)

#ITERASI DICITIONARY
for key, value in mahasiswa.items():
    print(key, ":", value)

#NESTED DICTIONARY
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi

#