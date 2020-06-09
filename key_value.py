print('Key and Value Dictionary')
print('===========================================')

dictionary = {}

n = 0
while n != 3:
    key = input('Masukkan key yang ingin ditambahkan: ')
    value = input('Masukkan value yang ingin ditambahkan: ')
    print('===========================================')
    dictionary[key] = value
    n += 1

for key,value in dictionary.items():
        print(f'{key} : {value}')

