'''
Name: Brandon Smith
Date: 2/22/24
Topic: Unit 4 - lists, tuples, list methods
'''

# Lists
for i in range(1,11,2):
    print(i,end=" ")

odd_nums = list(range(1,11,2))
print(odd_nums)
# a list is a collection of items in Python 
# that can change during the program
even_nums = [2,4,6,8,10,"two","four","six","eight","ten"]
print(even_nums)

perfect_squares = []
# List methods
# append - adds an item to the end of a list
perfect_squares.append(1)
print(perfect_squares)
# write a loop that fills the perfect squares
# list with the squares from 1 to 144
for i in range(2,13):
    perfect_squares.append(i**2)
print(perfect_squares)

# quick way with list comprehensions
new_perfect_squares = [num**2 for num in range(1,13)]
print(new_perfect_squares)

# more methods
# min(), max(), sum()
print(min(new_perfect_squares))
print(max(new_perfect_squares))
print(sum(new_perfect_squares))

# make list of the numbers from 1 to 1,000,000
# use min() and max() to make sure the list is valid
# then see how long it takes Python to sum the list
# and print the sum
import time
# accessing items in a a list and slicing
big_list = [num for num in range(1,1_000_001)]
print(min(big_list))
print(max(big_list))
start = time.time()
print(sum(big_list))
end = time.time()
print(f"Time elapsed: {end-start:.5f} seconds")

print(big_list[0]) # first item
print(big_list[-1]) # last item
print(big_list[0:101]) # first 100 numbers
print(big_list[0:11:2])

my_fav_foods = ["chicken","hot dogs", "nuggies", "fries","chicken fried steak"]
your_fav_foods = my_fav_foods[:]
my_fav_foods.append("apple pie")
print(my_fav_foods)
print(your_fav_foods)
my_fav_foods.pop(0) # pop returns the value you popped
print(my_fav_foods)
try:
    my_fav_foods.remove("carrots") # remove returns None
except ValueError:
    print("Not in list")

# Tuple
    
my_tuple = (1,2,3,4)
print(my_tuple)
print(my_tuple[2])
# my_tuple[3] = 5 this is not valid

my_fav_foods[0] = "beef"
my_tuple = (my_tuple[0],)
print(my_tuple)




