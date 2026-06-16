import random

NUM_SENTENCES = 100_000
OUTPUT_FILE = "sentences.txt"

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
    """
    Generates a syllable following the pattern:
    Consonant + Vowel

    Example:
        ma, te, po
    """
    return random.choice(CONSONANTS) + random.choice(VOWELS)


def generate_ccv():
    """
    Generates a syllable following the pattern:
    Consonant Cluster + Vowel

    Example:
        bra, cri, plo
    """
    return random.choice(CONSONANT_CLUSTERS) + random.choice(VOWELS)


def generate_cvc():
    """
    Generates a syllable following the pattern:
    Consonant + Vowel + Consonant

    Example:
        mar, ton, bel
    """
    return (
        random.choice(CONSONANTS)
        + random.choice(VOWELS)
        + random.choice(CONSONANTS)
    )


def generate_cvv():
    """
    Generates a syllable following the pattern:
    Consonant + Vowel + Vowel

    Example:
        mai, bou, rei
    """
    return (
        random.choice(CONSONANTS)
        + random.choice(VOWELS)
        + random.choice(VOWELS)
    )


def generate_syllable():
    """
    Randomly selects one syllable pattern.
    """

    patterns = [
        generate_cv,
        generate_ccv,
        generate_cvc,
        generate_cvv
    ]

    return random.choice(patterns)()


def generate_word():
    """
    Generates a Portuguese-like word.

    Number of syllables:
        2 to 4
    """

    syllable_count = random.randint(2, 4)

    word = ""

    for _ in range(syllable_count):
        word += generate_syllable()

    return word

def generate_sentence():
    """
    Generates a sentence containing exactly 3 words.
    """

    return " ".join(
        generate_word()
        for _ in range(3)
    )

def generate_dataset(n):
    """
    Generates a list containing n sentences.
    """

    dataset = []

    for _ in range(n):
        dataset.append(generate_sentence())

    return dataset

def save_dataset(dataset, filename):
    """
    Saves the dataset to a text file.
    """

    with open(filename, "w", encoding="utf-8") as file:
        for sentence in dataset:
            file.write(sentence + "\n")

def print_statistics(dataset):
    """
    Displays dataset statistics.
    """

    print("=" * 50)
    print("INFINITE MONKEY DATASET")
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

    print("Generating dataset...")

    dataset = generate_dataset(NUM_SENTENCES)

    print("Saving dataset...")

    save_dataset(
        dataset,
        OUTPUT_FILE
    )

    print_statistics(dataset)

    print(f"\nDataset saved to: {OUTPUT_FILE}")
    print("Generated...")

if __name__ == "__main__":
    main()
