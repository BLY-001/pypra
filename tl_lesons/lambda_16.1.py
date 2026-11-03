#ANONYMOUS FUNCTIONS (LAMBDA)
prices = [3.0, 4.0]

triple_list =list(map(lambda price: price * 3, prices)) 
print(triple_list)

triple = lambda x: x * 3
print(triple(5))

scale_syrup = lambda ml: ml/30.0
print(scale_syrup(60))

greet = lambda name: 'Hello,' + name
print(greet('Bob'))

#simple conditional statement can be used with lambda

sugar_level = 'High'

get_pump_count = lambda count: 4 if count == 'High' else 2
print(get_pump_count(sugar_level))

check_size = lambda ounces: 'large' if ounces >= 16 else 'small'
print(check_size(12))
print(check_size(16))
