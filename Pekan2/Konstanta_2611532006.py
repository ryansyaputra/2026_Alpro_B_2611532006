# Buat file dengan nama Konstanta_NIM.py
# program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI : Final = 3.14
print("pi: %f" % (PI))
jari_2006 = float(input('Masukkan nilai jari-jari:'))
luas_2006 = PI * jari_2006 * jari_2006
print("Luas lingkaran dengan jari-jari %.2f adalah %2f" % (jari_2006, luas_2006))
