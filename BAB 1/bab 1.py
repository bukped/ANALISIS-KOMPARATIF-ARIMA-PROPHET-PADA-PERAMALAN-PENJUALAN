


#ini adalah sebuah komentar 
#ini adalah fungsi print
Print("Hello Salsabila Vebi Natasya ")

# penggunaan float
print(6.34)

#penggunaan string
print("Semoga Bisa Lulus")

#Penggunaan Complex 

print(9e)

#penggunaan Dictionary 
print({"Nama" : "Salsabila Vebi", 'umur':20})

#penggunaan integer
print(65)

#membuat variable
nama = "SALSABILA"

#mencetak variable 
print(nama)

#mengubah nilai dan tipe data dalam variable 
umur = 30
print(umur)
type(umur)
umur = "Tiga Puluh"
print(umur)
type(umur) #cek tipe data variable
namaDepan = "SALSABILA"
umur = 20
hobi = "Traveling"
print("Biodata\n", nama, "\n",umur , "\n", hobi)


#Operator Aritmatika 
#penjumlahan 
apel = 7
mangga = 3
buah = apel + mangga 
print(buah)

#Pengurangan 
hutang = 30000
bayar = 5000
sisa= hutang - bayar
print("sisa hutang adalah", sisa)

#perkalian 
panjang = 10
lebar = 15
luas = panjang * lebar
print(luas)

#pembagian
kue = 500
anak = 5
kuePerAnak = kue / anak
Print("Setiap anak akan mendapatkan kue sebanyak", kuePerAnak)

# pangkat 
bil3 = 9
bil4 = 11
hasil = bil3 ** bil4
print(hasil)


 # Kondisi if adalah kondisi yang akan dieksekusi oleh program jika
bernilai
benar atau TRUE
nilai = 9
# jika kondisi benar maka yang dieksekusi adalah perintah dibawahnya
if ( nilai > 7 ) :
print ( ” Selamat Anda Lulus ” )
# jika kondisi salah maka yang dieksekusi adalah perintah dibawah ini
if ( nilai > 10 ) :
print ( ” Selamat Anda Lulus ” )


# kondisi if else
if(nilai > 9): #jika kondisinya ini 
    print("selamat anda lulus") # maka yang diprint adalah ini 
else  #namun jika tidak
    print("maaf nilai anda tidak cukup ") # yang diprint adalah ini 


#contoh penggunaan kondisi elif 

hari = "Senin"
if(hari == "Selasa"):
 print("Saya Akan Kuliah")
elif(hari == "Rabu"):
    print("saya akan kuliah")
elif(hari == "Kamis"):
    print("saya Tidak akan kuliah")
elif(hari == "Jumat"):
    print("saya akan kuliah")
elif(hari == "Sabtu"):
    print("saya akan Libur")