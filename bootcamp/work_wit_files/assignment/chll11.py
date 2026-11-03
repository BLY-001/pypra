# Challenge #11
# Consider this dictionary file.
# Write a Python script that finds the number of occurrences of each letter of the alphabet
# in all the words of the dictionary. Make a distinction between lower and uppercase letters.
# You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear
# in all the words in the dictionary.
# Which is the most frequently used letter in English words? But the least frequently used one?

with open('American_english.txt', 'r') as file:
    content = [line.strip() for line in file if line.strip()]
    letter = {}
    for alpha in content:
        for a in alpha:
            letter[a] = letter.get(a, 0) + 1
    max_letter = max(letter, key= letter.get)
    print(f"most frequent: {max_letter} with {letter[max_letter]}")
    min_letter = min(letter, key= letter.get)
    print(f"minimum frequent letter: {min_letter} with {letter[min_letter]}")            