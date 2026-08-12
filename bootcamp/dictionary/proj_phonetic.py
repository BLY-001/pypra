#project generating codes from alphabet

alphabet = {}
with open('phonetic.csv') as f:
    content= f.read().splitlines()
    # print(content)
for letters in content[1:]:
    key, word = letters.split(',')
    alphabet[key] = word
# print(alphabet)

my_str = 'abcde'.upper()
print(my_str, end= '>>')
for item in my_str:
    alphabet[item]
print(alphabet[item], end='  ')