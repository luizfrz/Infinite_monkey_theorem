import random

l1 = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

for _ in range(1000):
    attempts = 0

    while True:
        attempts += 1

        letters = random.choice(l1) + random.choice(l1) + random.choice(l1)  

        if letters.lower() == "ola":
            print("A probabilidade de gerar OLA em uma tentativa é: ",attempts)
            break

