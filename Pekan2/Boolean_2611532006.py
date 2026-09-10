#Buat file dengan nama Boolean_NIM.py
#Nama variabel ditambah 4 digit nim terakhir contoh: milai_1234
#Deklarasi variabel dengan tipe data boolean
is_lulus_2006 = True
is_cumlaude_2006 = True

#Menggunakan Boolean
nilai_2006 = 85
batas_lulus_2006 = 75

#menentukan nilai boolean dari kondisi
status_kelulusan_2006 = nilai_2006 >= batas_lulus_2006 #hasilnya akan true

print("=== Check kelulusan ===")
print("Nilai:",nilai_2006 )
print("Apakah lulus?:", status_kelulusan_2006)
if is_lulus_2006 and is_cumlaude_2006:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")