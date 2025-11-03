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

numk = [1,2,3,4,5,6,87]

print(numk[1:7]) # [2, 3, 4, 5, 6]

print(numk[::2]) # [1, 3, 5, 87]

'''


# METHODS

# HOW TO ADD DATA INTO LIST :

# Append
# Insert
# Extend

# 1.append(obj):
        # it adds the data at the end
'''
i = [11,222,33]
i.append(44) 
print(i)  # [11, 222, 33, 44]

'''

# 2.insert[index,obj]
        #  it add data at perticular index
'''
i = [11,22,33]
i.insert(3,44) #[11, 22, 33, 44]
i.insert(4,66) #[11, 22, 33, 44, 66]
i.insert(4,55) #[11, 22, 33, 44, 55, 66]
print(i)
'''

# 3.extend:
        #  it adds iterables to the perticular index (like adding list or dict , tuple , set , string)
        #  it only takes iterabls
''''''



