# def greet():
#     print('hello, world!')
# greet()
# greet()
# greet()
# greet()

# def greet(name,time):
#     print(f'Hello, {name}! Good {time}.')
# greet('vica','evening')

# def greet(name,time):
#     print(f'Hello, {name}! Good {time}.')

# a = input('What is your name? ')
# b = input('Please enter the time of the day = ')

# greet(a,b)

radius = int(input('enter a radius: '))
length = int(input('enter a length: '))

def area(radius):
    return 3.14 * radius * radius 

def vol(area, length):
    vol = area * length 
    print(f'The volume of the silinder is {vol}')

vol(area(radius), length)