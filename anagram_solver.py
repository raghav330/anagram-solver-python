from collections import Counter
import sys
import time

with open('words.txt', 'r') as f:
    dictionary = f.read()

dictionary = [x.lower() for x in dictionary.split('\n')]


def return_anagrams(letters: str) -> list:
    """
    This returns all length anagrams from the input string.

    :param: a string of alphabets
    :return: a list of anagrams

    :example:
    $ python3 anagram_solver.py dive
    >> ['de', 'ed', 'id', 'di', 'ie', 'vei', 'div', 'vie', 'die', 'dev', 'ide',
        'dive']
        Number of anagrams: 12
        Time Taken: 0.32 seconds
    """

    global dictionary

    assert isinstance(letters,
                      str), 'Scrambled letters should only be of type string.'

    letters = letters.lower()

    letters_count = Counter(letters)

    anagrams = set()
    for word in dictionary:
        # Check if all the unique letters in word are in the
        # scrambled letters
        if not set(word) - set(letters):
            check_word = set()
            # Check if the count of each letter is less than or equal
            # to the count of that letter in scrambled letter input
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check_word.add(k)
            # Check if check_words is exactly equal to the unique letters
            # in the word of dictionary
            if check_word == set(word):
                anagrams.add(word)

    # Sort the anagrams by length
    anagrams = sorted(list(anagrams), key=lambda x: len(x))

    # Remove the empty string and one length alphabets
    anagrams = anagrams[1 + len(letters):]

    return anagrams


if __name__ == '__main__':
    start = time.time()
    test_anagrams = return_anagrams(sys.argv[1])
    stop = time.time()

    print(test_anagrams)
    print(f"Number of anagrams: {len(test_anagrams)}")
    print(f"Time Taken: {round(stop - start, 2)} seconds")
