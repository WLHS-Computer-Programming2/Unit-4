'''
Name: Brandon Smith
Date: 2/26/24
Topic: Unit 4 - lists, tuples, list methods
'''

my_list = ["taco","salad","pot roast","cake"]

for item in my_list:
    print(item)

# tuples in lists and lists in tuples

#                   0      1     2       3
#                  0 1    0 1   0 1    0   1        
list_of_points = [(1,2),(-4,5),(7,4),(12,-12)]
print(list_of_points[1]) # (-4,5)
print(list_of_points[1][1]) # gives 5, the y coordinate of the point at index 1
# list_of_points[1][1] = -5 this is invalid
list_of_points[1] = (-4,-5)
print(list_of_points)

tuple_of_lists = ([1,2],[3,4],[5,6])
print(tuple_of_lists[0][1]) # 2
print(tuple_of_lists[0])
# tuple_of_lists[0] = [-1,-2] invalid
tuple_of_lists[0][0] = -1
print(tuple_of_lists)
big_tuple = ([1,2,3,4,5],[6,7,8])
print(big_tuple[0][2:])