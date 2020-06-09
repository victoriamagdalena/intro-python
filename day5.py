print('Biodata Murid')
biodata = {}
murid = []

while True: 
    biodata = {}
    nama = input('Siapakah nama Anda: ')
    umur = int(input('Berapakah umur Anda: '))
    rumah = input('Dimanakah anda tinggal? ')
    
    biodata['Nama: '] = nama
    biodata['Umur: '] = umur
    biodata['Tempat tinggal: '] = rumah
    murid.append(biodata)

    tambahan = input('Apakah anda masih mau mengisi biodata? (y/n): ')
    if tambahan == 'y': 
        continue
    else: 
        break

for biodata in murid:
    for key,value in biodata.items():
        print(f'{key} {value}')


print('Rock, Paper, Scissor Game')
while True: 
    import random 
    choice = ['Rock', 'Paper', 'Scissor']
    number = random.randint(0,2)
    answer = choice[number]
    guess = input('Rock, Paper, Scissor? ')

    if guess == 'Paper' and answer == 'Paper': 
        print('Tie!')
    elif guess == 'Paper' and answer == 'Rock': 
        print('You win! Paper covers Rock')
    elif guess == 'Paper' and answer == 'Scissor':
        print("You lose! Paper can't covers Scissor") 
    elif guess == 'Rock' and answer == 'Rock':
        print('Tie!')
    elif guess == 'Rock' and answer == 'Scissor':
        print("You win! Rock covers Scissor")
    elif guess == 'Rock' and answer == 'Paper':
        print("You lose!' Paper can't covers Rock")
    elif guess == 'Scissor' and answer == 'Scissor':
        print('Tie!')
    elif guess == 'Scissor' and answer == 'Paper':
        print("You win! Scissor cover Paper")
    elif guess == 'Scissor' and answer == 'Rock':
        print("You lose! Scissor can't cover Paper")




