from collections import Counter
import sys
import time

with open('words.txt', 'r') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]


def return_anagrams(letters: str) -> list:

    global dictionary

    assert isinstance(letters,
                      str), 'Scrambled letters should only be of type string.'

    letters = letters.lower()

    anagrams = set()
    for word in dictionary:
        # if letters in word are in the scrambled letters
        if not set(word) - set(letters):
            check_word = set()
            for w in set(word):
                if Counter(word)[w] <= Counter(letters)[w]:
                    check_word.add(w)
            if check_word == set(word):
                anagrams.add(word)

    return sorted(list(anagrams), key=lambda x: len(x))


if __name__ == '__main__':
    start = time.time()
    test_anagrams = return_anagrams(sys.argv[1])
    print(test_anagrams)
    stop = time.time()
    print(f"Number of anagrams: {len(test_anagrams)}")
    print(f"Time Taken: {round(stop - start, 2)} seconds")
