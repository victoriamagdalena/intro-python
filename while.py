username = "vica"
password = "123"

username_guess = input('Masukkan username = ')
password_guess = input('Masukkan password = ')

while username_guess != username or password_guess != password:
    print('Coba lagi')
    username_guess = input('Masukkan username = ')
    password_guess = input('Masukkan password = ')
print('Berhasil')

# username = 'vica'
# password = '123'
# tries = 0 

# while tries != 3:
#     username_guess = input('Masukkan username = ')
#     password_guess = input('Masukkan password = ')
#     if username_guess == username and password_guess == password:
#         print('Berhasil')
#         break
#     print('Coba lagi')
#     tries +=1
    