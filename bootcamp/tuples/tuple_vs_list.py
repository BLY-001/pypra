#TUPLE VS LISTS
 #1. TUPLES ARE FASTER AND MORE EFFICIENT THAN LISTS. you can save data that can never chaange inside a tuple i.e days of the week, coordinates of a gps point, letters of the alphabet,months of the year
#python uses "CONSTANT FOLDING" which means recognising and evaluating constant expression at compile time rather than run time
#tuples are more efficient when they contain immutable datas like string,int,tuple etc 


#2. Tuple are safer than lists. i.e tuples dont accidentaly get changed

#3. Tuples can be used as keys in dictionaries.

#4. Storage efficiency
import sys #this module was imported to get the size of the tuple and the list
l1 =[1, 2, 3, 4, 5, 6]
t1 =(1, 2, 3, 4, 5, 6)
print(f'list memory size: {sys.getsizeof(l1)}')
print(f'Tuple memory size: {sys.getsizeof(t1)}')