import random

l1 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]
l2 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]

n = 0 
# Random OI 
print("Frase Sendo gerada...")
while n < 10:
        join = random.choice(l1)
        join2 = random.choice(l1)
        toBring = join + join2 
        print(toBring)
        if toBring == "OI":
            break
        
        