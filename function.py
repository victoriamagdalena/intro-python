# def f(x,y):
#     print('Hasilnya', x+y+6)

# angka = int(input('Masukkan angka: '))
# angka2 = int(input('Masukkan angka2: '))

# f(angka, angka2) 

# def tambah(x,y):
#     return x+y

# def kali(x,y):
#     print('Hasilnya', x*y)

# x = int(input('Masukkan angka: '))
# y = int(input('Masukkan angka2: '))

# hasil = tambah(x,y)
# angka3 = int(input('Masukkan angka3: '))

# kali(hasil, angka3)

# hasil = f(angka, angka2)
# print(hasil)

def luaspp(panjang,lebar):
    return panjang*lebar

def vol_balok(luas, tinggi): 
    print('Volume balok', luas * tinggi)

panjang = int(input('Masukkan panjang: '))
lebar = int(input('Masukkan lebar: '))
tinggi = int(input('Masukkan tinggi: '))

vol_balok(luaspp(panjang,lebar), tinggi)