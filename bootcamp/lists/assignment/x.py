# def solution(name, track):
#     return f'{name} is starting the {track} track'

# print(solution('yusuf', 3))

# def solution(name, cohort):
#     return f"name: {name}\n cohorts: {cohort}\n status: ready"
# print(solution('yusuf', 3))

# Write a function called `solution` that receives a student's name and three numbers.
# Return a four-line report in this exact format:
# Student: <name>
# Sum: <sum>
# Average: <average>
# Maximum: <maximum>
# Rules:
# - Add the three numbers to get the sum.
# - Divide the sum by 3 to get the average.
# - Round the average to 2 decimal places.
# - Find the largest number.
# - Return the final multi-line string.
# - Do not print.
# def solution(a, b, c, d):
#     return f"Student: {a}\nSum:{b + c + d}\nAverage: {((b + c + d)/2):.2f}\nMaximum: {max(b, c, d)}"

# print(solution('yusuf', 1, 2, 3))

def solution(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)

print(solution(10))

def solution(meters):
    Centimeters = float(meters) * 100
    Millimeters = float(meters) * 1000
    return f"Centimeters: {Centimeters}\nMillimeters: {Millimeters}"
print(solution(1))

def solution(kilogram):
    grams = kilogram * 1000
    pounds = kilogram * 2.20462
    return f"Kilograms:{kilogram}\nGrams:{grams}\nPounds{round(pounds, 2)}"

print(solution(1))