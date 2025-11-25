


# 
# * new_list = [exp for var in iterable]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [num**2 for num in l]
print(square)







results = {"sairaj":10,"soham":20,"ankit":30,"yash":40,"dhruv":50}
# create a list of name students

students = [name for name in results]
print(students)

# create a list of name of passed students
# new = [exp for loop if condition]

passed = [name for name in results if results[name]>=40 ]
print(passed)


# new = [e1 if cond else e2 for loop]

# data = [ if results[name]>=40 else name.lower() for name in results]
# print(data)



l = [11,22,33,44,55]

liter_obj = iter(l)
num = 199

def check(obj):
    list_of_attribute = dir(obj)
    if '__iter__' in list_of_attribute and '__next__' in list_of_attribute :
        return "iterator"
    elif '__iter__' in list_of_attribute:
        return "iterable"
    else:
        return 'nothing'
    
print(check(num))