import random
answer = random.randint(1,11)
print('Tebak angka 1-10')
tebakan = ""
while tebakan != answer:
    tebakan = int(input('Masukkan angka tebakan: '))
    if tebakan < answer: 
        print('Kekecilan')
    elif tebakan > answer:
        print('Kebesaran')        
print('Selamat!')