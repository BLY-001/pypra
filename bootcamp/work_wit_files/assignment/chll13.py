# Challenge #13
# Continue the previous challenge and find the 3 most frequently used letters in all English Words.
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)

#  Challenge #11
# # Consider this dictionary file.
# # Write a Python script that finds the number of occurrences of each letter of the alphabet
# # in all the words of the dictionary. Make a distinction between lower and uppercase letters.
# # You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear
# # in all the words in the dictionary.
# # Which is the most frequently used letter in English words? But the least frequently used one?

with open('American_english.txt', 'r')as f:
    content = [line.strip().lower() for line in f if line.strip()]
    letter = {}
    for lines in content:
        for alp in lines:
            letter[alp] = letter.get(alp, 0) + 1
    is_sorted = sorted(letter.items(), key=lambda item:item[1], reverse=True)
    print(is_sorted[:3])
