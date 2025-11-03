import string
def count_word_occurrences(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()

    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def main():
    sentence = input("Enter a sentence: ")
    word_counts = count_word_occurrences(sentence)
    print("Word occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
if __name__ == "__main__":
    main()
