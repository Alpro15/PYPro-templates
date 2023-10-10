import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passw = ""
longness = int(input('Uzunluk' + '\n'))

for i in range(longness):
    passw += random.choice(characters)
    print(passw)
