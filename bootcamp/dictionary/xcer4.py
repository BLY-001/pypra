visits = {
    'Monday': 5000,
    'Tuesday': 3000,
    'Wednessday': 4000,
    'Thursday': 4500,
    'Friday': 5000,
    'Saturday': 2000,
    'Sunday': 1500
}

total_visit = sum(visits.values())
print(total_visit)

percentage = {k:v/(sum(visits.values())) * 100 for k,v in visits.items()}
print(percentage)
