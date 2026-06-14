import random

result = []
letter = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P","Q", "R","S", "T", "U", "V","W", "X", "Y", "Z"
]

n = 0 
for _ in range(1000):
    attempts = 0

    while True:
        attempts += 1

        letter = random.choice(letter) + random.choice(letter)

        if letter.lower() == "ola":
            result.append(attempts)
            break
