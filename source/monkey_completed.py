import random
import time 

l1 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l2 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]

l3 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]

l4 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l5 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l6 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
] 

l7 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l8 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l9= [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]

n = 0 
print("Frase Sendo gerada...")
time.sleep(1)
while n < 10:
        n += 1 
        if n >= 10:
            join = random.choice(l1)
            join2 = random.choice(l2)
            join3 = random.choice(l3)
            join4 = random.choice(l4)
            join5 = random.choice(l5)
            join6 = random.choice(l6)

            join9 = random.choice(l7)
            join7 = random.choice(l8)
            join8 = random.choice(l9)
            
            
            toBring = join + join2 + join3 
            toBring2 = join9 + join7 + join8
            print(toBring, toBring2)
            break
        
        