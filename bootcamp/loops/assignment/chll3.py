# Challenge #3
# Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
# Input str: Hello Everybody!
# Output: 5

m_input = input("input anything here: ").lower()
n = 0
vowel = "aeiou"
for x in m_input:
    if x in vowel:
        n += 1
print(f"the count is {n}")