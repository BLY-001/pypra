#RECURSION when a fuction call itself to repeat smaller instances of the problem
#the anatomy of recursion 
def wash_mugs(stack_size):
    # 1. the base case(the stop switch)
    if stack_size == 0:
        print("All mugs are washed! drying hands")
        return #stop the function completely

    #2. recursive case (action + shrink)
    print(f"washing mug number{stack_size}...")
    #call ourselfs with one less mug
    wash_mugs(stack_size - 1)

wash_mugs(3)

def count_down(cups):
    if cups <= 0:
        print('Done!')
        return
    print('cup:' + str(cups))
    count_down(cups -1)
count_down(3)

#STEP 3 TRACING THE  CALL STACKS

stack_size = 3
total_water_ml = 0
def calculate_water(mugs):
    if mugs <= 0:
        return 0 #base case 0 mugs require 0ml
    #recursive case: 10ml for the current mug + water for the rest of the stack
    return 10 + calculate_water(mugs -1)

total_water_ml = calculate_water(stack_size)
print(total_water_ml)


def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs-1)
print(sum_stack(4))

#REAL-WORLD APPLICATION
# to write a search script to find a file named 'receipt.pdf' as in the example on tl nation
def search_folder(current_folder, target_file):
    #base case 1: if we find the file inside this folder, return it
    if target_file in current_folder.files:
        return current_folder.path_to(target_file)
    #recursive case: loop over any nested sub-folders
    for sub_folder in current_folder.sub_folder:
        path = search_folder(sub_folder, target_file) #recursive call
        if path is None:
            return path
    return None #Base case 2: folder is empty and has no sub-folders

