# print("Welcome to simple calculator!")

# tries = 0 

# while tries != 3:
#     num1 = int(input('Enter your first number = '))
#     num2 = int(input('Enter your second number = '))
#     calculate = input('Choose one type of calculation, 1(+) 2(-) 3(*) 4(/) 5(^) = ')
#     if calculate == "1":
#         answer = num1 + num2
#         print (f'{num1} + {num2} = {answer}')
#     elif calculate == "2":
#         answer = num1 - num2
#         print (f'{num1} - {num2} = {answer}')
#     elif calculate == "3":
#         answer = num1 * num2
#         print (f'{num1} * {num2} = {answer}')
#     elif calculate == "4":
#         answer = num1 / num2
#         print (f'{num1} / {num2} = {answer}')
#     elif calculate == "5":
#         answer = num1 ** num2
#         print (f'{num1} ^ {num2} = {answer}')
#     else: 
#         print('You can only choose calculation no. 1,2,3,4, or 5.')
#     tries += 1

print("Welcome to simple calculator!")

num1 = int(input('Enter your first number = '))
num2 = int(input('Enter your second number = '))
calculate = input('Choose one type of calculation, 1(+) 2(-) 3(*) 4(/) 5(^) = ')

def tambah(num1,num2):
    print('The answer is', num1+num2)

def kurang(num1,num2):
    print('The answer is', num1-num2)

def kali(num1,num2):
    print('The answer is', num1*num2)

def bagi(num1,num2):
    print('The answer is', num1/num2)

def pangkat(num1,num2):
    print('The answer is', num1**num2)

if calculate == "1":
    tambah(num1,num2)
elif calculate == "2":
    kurang(num1,num2)
elif calculate == "3":
    kali(num1,num2)
elif calculate == "4":
    bagi(num1,num2)
elif calculate == "5":
    pangkat(num1,num2)
else: 
    print('You can only choose calculation no. 1,2,3,4, or 5.')

