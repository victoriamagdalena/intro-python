print('--Tube Calculator--')

ajak = input('Mau menggunakan calculator (y/n)? ')
if ajak == 'y':
    jari_jari = int(input('Masukkan jari-jari tabung: '))
    tinggi = float(input('Masukkan tinggi tabung: '))

    print('1 Hitung luas lingkaran alas')
    print('2 Hitung volume tabung')
    pilih = input('Apa yang ingin dihitung? ')
    
    def luas(jari):
        return jari * jari * 3.14

    if pilih == '1': 
        luas = jari_jari * jari_jari * 3.14
        print(f'Luas lingkaran alas {luas}')

    elif pilih == '2':
        voltabung = luas(jari_jari) * tinggi
        print(f'Volume tabung {voltabung}')

    while True: 
        ajak2 = input('Apakah masih ingin menggunakan kalkulator? (y/n) ')

        if ajak2 == 'y':
            jari_jari = int(input('Masukkan jari-jari tabung: '))
            tinggi = float(input('Masukkan tinggi tabung: '))
            
            print('1 Hitung luas lingkaran alas')
            print('2 Hitung volume tabung')
            pilih = input('Apa yang ingin dihitung? ')

            def luas(jari):
                return jari * jari * 3.14

            if pilih == '1': 
                luas = jari_jari * jari_jari * 3.14
                print(f'Luas lingkaran alas {luas}')

            elif pilih == '2':
                voltabung = luas(jari_jari) * tinggi
                print(f'Volume tabung {voltabung}')

        elif ajak2 == 'n':
            print('--Usage History--')
            break

    class Tabung:

        def __init__(self, jari_jari, tinggi, luas, voltabung):
            self.radius = jari_jari
            self.tinggi = tinggi
            self.luasling = luas
            self.volume = voltabung
            
        def info(self):
            if pilih == '1':
                print(f'Radius Tabung {self.radius}, Tinggi {self.tinggi}, Luas Lingkaran Alas {self.luasling}')
            elif pilih == '2':
                print(f'Radius Tabung {self.radius}, Tinggi {self.tinggi}, Volume Tabung {self.volume}')

    tabung1 = Tabung(jari_jari, tinggi, luas, voltabung)
    print(tabung1.info())

elif ajak == 'n':
    print('--Usage History--')
    






    