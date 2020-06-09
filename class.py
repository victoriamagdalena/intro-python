# class Mobil: 

#     def __init__(self, nama, brand, garansi, power, warna):
#         self.nama = nama
#         self.brand = brand
#         self.garansi = garansi
#         self.power = power
#         self.warna = warna

#     def info(self):
#         print(f'Mobil ini bernama {self.nama} memiliki merek {self.brand} bergaransi {self.garansi}. Memiliki power {self.power} dan berwarna {self.warna}.')

# mobil1 = Mobil('kijang', 'toyota', '2 tahun', '5000 cc', 'merah')
# mobil2 = Mobil('avanza', 'toyota', '2 tahun', '5000 cc', 'merah')

# print(mobil1.nama)
# print(mobil2.nama)
# mobil1.info()
# mobil2.info()

# nama = input('Masukkan nama: ')
# umur = int(input('Masukkan umur: '))
# agama = input('Masukkan agama: ')
# rumah = input('Masukkan tempat tinggal: ')
# sekolah = input('Masukkan sekolah: ')

# class Murid:
#     def __init__(self, nama, umur, rumah, agama, sekolah):
#         self.nama = nama
#         self.umur = umur
#         self.agama = agama
#         self.rumah = rumah
#         self.sekolah = sekolah

#     def info(self):
#         print(f'Murid bernama {self.nama} berumur {self.umur} merupakan seorang yang beragama {self.agama}. Tinggalnya di {self.rumah} dan bersekolah di {self.sekolah}.')

# murid1 = Murid('Vica', 17, 'kristen', 'gading', 'sanur')
# murid2 = Murid(nama, umur, agama, rumah, sekolah)
# murid1.info()
# murid2.info()

name = input('Flower name: ')
petals = int(input('Number of petals: '))
price = float(input('Price: '))

class Flower: 

    def __init__(self, name, petals, price):
        self.name = name 
        self.petals = petals
        self.price = price

    def info(self):
        return f'{self.name} which has {self.petals} petals is IDR {self.price}'

    def name(self, name2):
        self.name = name2

    def petals(self, petals2):
        self.petals = petals2
    
    def price(self, price2):
        self.petals = price2

    def return1(self, name2):
         return f'{self.name}'

    def return2(self, petals2):
         return f'{self.petals}'

    def return3(self, price2):
         return f'{self.price}'
    
    
flower1 = Flower(name, petals, price)
print(flower1.info())

print('---Edit flower---')
name2 = input('Flower name: ')
petals2 = int(input('Number of petals: '))
price2 = float(input('Price: '))

print('---Retrieve Flower---')
flower2 = Flower(name2, petals2, price2) 
print(flower2.return1(name2))
print(flower2.return2(petals2))
print(flower2.return3(price2))





