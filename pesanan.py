# print('Pesan apa aja mbak?')
# print('Mbak sudah pesan')

# pesanan_1 = ['es teh manis','nasi pecel','sambal bawang']
# for n in range(len(pesanan_1)):
#     print(n+1, pesanan_1[n])

# tambahan = input('Ada tambahan mbak? (y/n)')
# while tambahan == 'y':
#     pesanan_2 = input('Mau tambah apa mbak? ')
#     tambahan = input('Ada tambahan mbak? (y/n)')
# print('Saya ulang pesanannya ya')

pesanan = {}
daftar = []

while True:
    pesanan = {}
    tambah = input('Mau pesan apa? ')

    pesanan['tambahan'] = tambah
    daftar.append(pesanan)
    
    tambahan = input('Ada tambahan mbak? (y/n) ')
    if tambahan == 'y':
        continue
    elif tambahan == 'n':
        break

for pesanan in daftar: 
    for key,value in pesanan.items():
        for n in range(len(pesanan)):
            print (n+1, value)




