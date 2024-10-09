#!/usr/bin/env python3

def count_words_efficient(file_path):
    with open(file_path, 'r') as file:
        return sum(len(line.strip().split()) for line in file)

def count_words(file_path):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            word_count += len(line.strip().split())
    return word_count

# print(count_words('resources/TheGreatGatsby.txt'))
print(count_words('resources/dracula.txt'))
print(count_words_efficient('resources/dracula.txt'))

def word_has_vowels_efficient(word):
    word = word.lower()
    return any(vowel in word for vowel in 'aeiou')

def word_has_vowels(word):
    for l in word.lower():
        if l in 'aeiou':
            return True
    return False

print(word_has_vowels('Hello'))
print(word_has_vowels('crypt'))
print(word_has_vowels_efficient('Hello'))
print(word_has_vowels_efficient('crypt'))

def letter_positions(word, letter):
    letter = letter.lower()
    i = 0
    result = ''
    for l in word.lower():
        if l == letter:
            result += str(i) + ','
        i += 1
    return result.removesuffix(',').split(',')

def letter_positions_efficient(word, letter):
    letter = letter.lower()
    return [i for i, l in enumerate(word.lower()) if l == letter]

print(letter_positions_efficient('PARTNERSHIPS', 'R'))
print(letter_positions('PARTNERSHIPS', 'R'))

from doctest import run_docstring_examples

def run_doctests(func):
    run_docstring_examples(func, globals(), name=func.__name__)

def has_letter(word, char):
    """Checks if a word uses the letter char.

    >>> has_letter('banana', 'a')
    True
    >>> has_letter('stuff', 'x')
    False
    """
    for letter in word:
        if letter.lower() == char.lower():
            return True
    return False

# run_doctests(has_letter)

def is_palindromic(word):
    w_len = len(word)
    s = 0
    e = w_len - 1
    while s < e:
        if word[s] != word[e]:
            return False
        s += 1
        e -= 1
    return True

print(is_palindromic('civic'))
print(is_palindromic('noon'))
print(is_palindromic('nosaon'))

def count_by_length(file_path, n):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            word_count += sum(1 for word in line.strip().split() if len(word) == n)
    return word_count

print(count_by_length('resources/TheGreatGatsby.txt', 4))

def find_words_with_pattern(file_path, pattern):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            word_count += sum(1 for word in line.strip().split() if pattern in word)
    return word_count

print(find_words_with_pattern('resources/TheGreatGatsby.txt', 'bac'))
