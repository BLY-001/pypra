company_score = 500
def take_name(name):
    employee_perfomance = 50
    def take_additional_performance(score):
        nonlocal employee_perfomance
        adding = sum_up()
        employee_perfomance += score
        return f"performance of {name} is {employee_perfomance}"
    def sum_up():
        global company_score
        company_score += employee_perfomance
    return take_additional_performance


first = take_name("Saliu")
print(first(20))
print(first(30))
