import random 
sogl = 'qwrtpsdghjklxcvbnm'

glas = 'eyuioa'

numbers = '01234567890'

symbol = '@#%?!'

password = ""

for i in range(4):

    password += random.choice(sogl)

    password += random.choice(glas)

for i in range(2):

    password += random.choice(numbers)

password += random.choice(symbol)

print(password)
