# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt')

# ninja_belts = {}

# while True:
#     ninja_name = input('enter a ninja name: ')
#     ninja_belt = input('enter a belt colour: ')
#     ninja_belts[ninja_name] = ninja_belt 

#     another = input('add another? (y/n)')
#     if another == 'y':
#         continue 
#     else:
#         break 

orang = {'nama' : 'Vica', 'umur' : 17}
# print(orang['nama'])

# for key in orang.keys():
#     print(key)

# for value in orang.values():
#     print(value)

# for key,value in orang.items():
#     print(key,value)

# nama = ['Vica','Lola']
# print(nama[0])

# orang['nama']='Bernard'
# print(orang['nama'])

# nama = input('Masukkan nama anda: ')
# umur = int(input('Masukkan umur anda: '))

# orang['nama']=nama
# orang['umur']=umur

# for key,value in orang.items():
#     print(f' {key} {value}')

orang = {}

nama = input('Masukkan nama anda: ')
umur = int(input('Masukkan umur anda: '))
hobi = input('Masukkan hobi anda: ')
tinggi = int(input('Masukkan tinggi anda: '))

orang['Nama'] = nama
orang['Umur'] = umur
orang['Hobi'] = hobi
orang['Tinggi'] = tinggi

for key,value in orang.items():
    if key == 'Tinggi':
        print(f'{key} {value} cm')
    else:
        print(f'{key} {value}')

# print
# for key,value in orang.items():
#     print

# list of dictionaries
# persons = [{'nama': 'Enryl', 'umur':15}, {'nama':'Bernard','umur':17}]

# for person in persons:
#     for key,value in person.items():
#         print(f'{key} {value}')
