print('PAYMENT COMPUTATION FOR EMPLOYEES')
print('---------------------------------')

hours = int(input('Enter hours: '))
rate = int(input('Enter rate: '))

def pay(hours,rate):
    if hours <= 10: 
        pay = hours*rate
        print(f'Pay: {pay}')
    elif hours > 10: 
        bonus = hours*rate + 200
        print(f'Pay: {bonus}')

pay(hours,rate)