# def create_greeting(name):
#     return f"Hello, {name}!"

# greeting = create_greeting("mosh")
# print(greeting)

# def add_numbers(a, b):
#     return a + b
# addition = add_numbers(5, 7)
# print(addition)

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# t = is_even(5)
# print(t)

# def get_even(numbers):
#     new_list = []
#     for number in numbers:
#         if number % 2 == 0:
#             new_list.append(number)
#     return new_list
            

# a = get_even([1,2,3,4,5,6])
# print(a)

# def calculate_tax(amount):
#     return amount * 0.1
# def get_final_price(price):
#     tax = calculate_tax(price)
#     return tax + price
# fina = get_final_price(100)
# print(fina)

# def cube(num):
#     return num ** 3

# def main():
#     num_list = [1,2,3,4]
#     for n in num_list:
#         print(cube(n))

# if __name__ == "__main__":
#     main()

# def get_user_age():
#     age = int(input("input your age: "))
#     return age

# def main():
#     age_in_5years = get_user_age() + 5
#     print(f"you will be {age_in_5years} in 5 years")

# main()

# def create_user_profile(username, score):
#     my_dict = {"name": username, "score": score}
#     return my_dict

# def main():
#     A = create_user_profile("sarah", 95)
#     print(f"the name of the user is {A["name"]} and the score of the user is {A["score"]}")

# main()

# def get_passing_students(students):
#     pass_student = []
#     for student in students:
#         if student["score"] >= 50:
#             pass_student.append(student["name"])
#     return pass_student

# def main():
#     test_list = [{"name": "nommy" , "score":45}, {"name": "alice" , "score":50},{"name": "phoden" , "score":70},]
#     a = get_passing_students(test_list)
#     print(a)

# main()

# def greet_user(name, greeting = "Hello"):
#     return f"{greeting},{name}"
# def main():
#     a = greet_user("AHMAD")
#     b = greet_user("AHMAD", "WELCOME")
#     print(a)
#     print(b)

# main()

# def divide_numbers(numerator, denominator):
#     if denominator == 0:
#         return "error message"
#     else:
#         return numerator/denominator

# def main():
#     sol = divide_numbers(10, 2)
#     itch = divide_numbers(10, 0)
#     print(sol)
#     print(itch)
    
# main()

# def analyze_numbers(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     my_dict = {"sum": total, "max":max(numbers), "min":min(numbers)}        
#     return my_dict

# def main():
#     a = [12, 45, 2, 89, 23]
#     b = analyze_numbers(a)
#     print(b)

# main()

def get_questions():
    quiz_data = [{"prompt": "what keyword is used to define a function in python?",
                 "choices":["1. function", "2. def", "3. define", "4. fun"],
                 "answer": "2"
                 },

                 {"prompt": "which data structure uses key-value pairs?",
                 "choices":["1. list", "2. tuple", "3. dictionary", "4. set"],
                 "answer": "3"
                 },

                 {"prompt": "what does the standard execution guard check?",
                 "choices":["1. __name__ == '__main__'", "2. __file__ == '__run__'", "3. main == True", "4.run == __start"],
                 "answer": "1"
                 }
                 ]
    return quiz_data

def ask_question(q):
    print(q["prompt"])
    for choice in q["choices"]:
        print(choice)
    my_answer = input("input your answer: ").strip()
    if my_answer == q["answer"]:
        return True
    return False

def run_quiz():
    q = get_questions() 
    score = 0
    for question in q:
        if ask_question(question) == True:
            score +=1
    return score

def main():
    score = run_quiz()
    print(f"your final score is {score}")

if __name__ == "__main__":
    main()
