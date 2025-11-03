# list

#  list is a comma seperated elements whitin []
            # SYNTAX :
                    # var = [e1,e2,e3,...]

'''
examples:

num = 10
numbers = [2,4,6,8,10]
print(type(numbers)) #<class 'list'>

name = 'pavan'
students = ["rajesh","kunal","om","prakash"]
print(type(students)) #<class 'list'>

'''


# it is ordered , Mutable , Heterogeneous , collection of elemens  where dublicates are allowed .....

# all the fundamental data type are IMMUTABLE   

# Heterogeneous MEANS :   DIfferent type of datatype

# list allow different type of data type  and data 

#  dublicates are allowed

# 1.indexing:::
'''
listt = [1,2,3,4,5,6]
print("index value of 1 in listt :",listt[1])

students = ['jauy','ajay','vijay',"jay"]
print("index value of -1 in students :",listt[-1])
'''

# 2.slicing:
'''
var[Start_index : End_index : Step_index]

StartIndex => value which slicing start from 
EndIndex => value which slicing end to 
stepValue =>
        forward => + valueStep
        reverce => - valueStep
'''

numk = [1,2,3,4,5,6,87]
print(numk[1:7]) # [2, 3, 4, 5, 6]
print(numk[::2]) # [1, 3, 5, 87]

