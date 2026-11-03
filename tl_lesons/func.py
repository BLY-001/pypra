# def steam_milk():
#     temp = 65
#     print(f" milk steamed to {temp} degres")
#     return temp

# final_temp = steam_milk()
# print(final_temp)

# def test_scope():
#     secret_recipe = "vanilla syrup"
#     print(secret_recipe)

# print(secret_recipe)


count = 0 #GLOBAL VARIABLE
def increment():
    global count
    count += 1
    print(count)

increment()

