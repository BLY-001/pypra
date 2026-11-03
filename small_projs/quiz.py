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

def get_high_score():
    initial_high = 2
    return initial_high

def main():
    score = run_quiz()
    if score > get_high_score():
        print(f"new high score is {score}")
    print(f"your final score is {score}")

if __name__ == "__main__":
    main()
