# Challenge #12
# Write a Python script that displays a number with a comma (,) as the thousands separator (US and UK format) and with a period(.) as the thousands separator (EU format).
# Sample input number: 1234567
# Expected Result: 1,234,567 and 1.234.567

# print(help(str.join))

number = 1234567
us = f"{number:,}"
print(f'this is a format for the {us} us number')
uk = us.replace(',', '.')
print(f"this is the format for {uk} uk number")
