import random

NUM_SENTENCES = 100

VOWELS = ["a", "e", "i", "o", "u"]

CONSONANTS = [
    "b", "c", "d", "f", "g",
    "j", "l", "m", "n", "p",
    "r", "s", "t", "v"
]

CONSONANT_CLUSTERS = [
    "br", "cr", "dr", "fr",
    "gr", "pr", "tr",
    "bl", "cl", "pl"
]

def generate_cv():
   
    return random.choice(CONSONANTS) + random.choice(VOWELS)


def generate_ccv():
   
    return random.choice(CONSONANT_CLUSTERS) + random.choice(VOWELS)

def generate_cvc():
  
    return (
        random.choice(CONSONANTS)
        + random.choice(VOWELS)
        + random.choice(CONSONANTS)
    )


def generate_cvv():
  
    return (
        random.choice(CONSONANTS)
        + random.choice(VOWELS)
        + random.choice(VOWELS)
    )


def generate_syllable():
    patterns = [
        generate_cv,
        generate_ccv,
        generate_cvc,
        generate_cvv
    ]

    return random.choice(patterns)()


def generate_word():
  
    syllable_count = random.randint(2, 4)

    word = ""

    for _ in range(syllable_count):
        word += generate_syllable()

    return word

def generate_sentence():
  
    
    return " ".join(
        generate_word()
        for _ in range(3)
    )

def generate_dataset(n):

    dataset = []

    for _ in range(n):
        dataset.append(generate_sentence())

    return dataset
def print_statistics(dataset):
    print("=" * 50)
    
    print("=" * 50)

    print(f"Total sentences: {len(dataset)}")

    total_words = sum(
        len(sentence.split())
        for sentence in dataset
    )

    print(f"Total words: {total_words}")

    average_words = total_words / len(dataset)

    print(f"Average words per sentence: {average_words:.2f}")

    print("\nSample sentences:\n")

    for sentence in dataset[:10]:
        print(sentence)

def main():

    print("Generated...")

if __name__ == "__main__":
    main()

def main():

    dataset = generate_dataset(NUM_SENTENCES)

    print_statistics(dataset)


if __name__ == "__main__":
    main()
