# Challenge #12
# Change the solution from the previous challenge so that the script considers
# all letters lowercase (it makes no distinction between lower and uppercase letters).

with open('American_english.txt', 'r') as file:
    content = [line.strip().lower() for line in file if line.strip()]
    letter = {}
    for alpha in content:
        for a in alpha:
            letter[a] = letter.get(a, 0) + 1
    max_letter = max(letter, key= letter.get)
    print(f"most frequent: {max_letter} with {letter[max_letter]}")
    min_letter = min(letter, key= letter.get)
    print(f"minimum frequent letter: {min_letter} with {letter[min_letter]}")            