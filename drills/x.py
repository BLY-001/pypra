# def division_details(a, b):
#     return {
#         "true_division": round(a/b, 2),
#         "floor_division": a//b,
#         "remainder": a%b
#     }

# print(division_details(4, 2))


# EligibilityLogic
# Instructions
# Implement eligibility_logic(score, attendance, completed_drill). 
# Return "Eligible" only when score is greater than or equal to 70, 
# attendance is greater than or equal to 80, and completed_drill is True. Otherwise return "Not eligible".

# def eligibility_logic(score, attendance, completed_drill):
#     if score >= 70 and attendance >= 80 and completed_drill:
#         return "Eligible"
#     else:
#         return "Not eligible"

# print(eligibility_logic(70, 7, True))




# SafeCalculator
# Instructions
# Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. 
# Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator".
# If the operator is "/" or "%" and b is 0, 
# return "Cannot divide by zero". Round division results to 2 decimal places.

def safe_calculator(a, operator, b):
    if operator not in ("+", "-", "*", "/", "%", "**"):
        return "Invalid operator"
    if operator in ("/", "%") and b == 0:
        return "Cannot divide by zero"
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a ** b

print(safe_calculator(2, '%', 2))

