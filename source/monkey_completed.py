import random
import time 

l1 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
n = 0 
while n < 4000:
        n += 1 
        if n >= 10:
            letter = random.choice(l1) + random.choice(l1) 
            print(letter)
            break