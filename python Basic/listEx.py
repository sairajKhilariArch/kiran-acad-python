'''
from typing import list

numbers : list[int | list[Any]]= [11, 22, 33, [10, 20, 30, 40, [1, 2, 3, 4], 50, 60, 70], 44, 55, 66]

print(numbers)  # [11, 22, 33, [10, 20, 30, 40, [1, 2, 3, 4], 50, 60, 70], 44, 55, 66]

print(numbers[3][2]) # 30

print(numbers[-4][-2]) # 60

print(numbers[-4][-4][-4]) # 1

'''

#  methods

'''
# example 01

numbers = [10,30,40,[11,22,33,[1,2,3,4,6],55,66,77],50,60,70]
print(numbers) # [10, 30, 40, [11, 22, 33, [1, 2, 3, 4, 6], 55, 66, 77], 50, 60, 70]

# 70>80
numbers.insert(7,80)
print(numbers) #[10, 30, 40, [11, 22, 33, [1, 2, 3, 4, 6], 55, 66, 77], 50, 60, 70, 80]

# 10>20
numbers.insert(1,20)
print(numbers) # [10, 20, 30, 40, [11, 22, 33, [1, 2, 3, 4, 6], 55, 66, 77], 50, 60, 70, 80]

# 77>88
numbers[4].append(88)
print(numbers) # [10, 20, 30, 40, [11, 22, 33, [1, 2, 3, 4, 6], 55, 66, 77, 88], 50, 60, 70, 80]

# 44 < 55
numbers[4].insert(3,44)
print(numbers) # [10, 20, 30, 40, [11, 22, 33, 44, [1, 2, 3, 4, 6], 55, 66, 77, 88], 50, 60, 70, 80]

# 4 > 5
numbers[4][4].insert(4,5)
print(numbers) # [10, 20, 30, 40, [11, 22, 33, 44, [1, 2, 3, 4, 5, 6], 55, 66, 77, 88], 50, 60, 70, 80]

# 6 > 7
numbers[4][4].append(7)
print(numbers) #  [10, 20, 30, 40, [11, 22, 33, 44, [1, 2, 3, 4, 5, 6, 7], 55, 66, 77, 88], 50, 60, 70, 80]

# 7 >8,9,10
a = [8,9,10]
numbers[4][4].extend(a)
# or
# numbers[4][4].extend([8,9,10])
print(numbers) # [10, 20, 30, 40, [11, 22, 33, 44, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55, 66, 77, 88], 50, 60, 70, 80]


'''

# example 02

students = ['ram','kunal',['arun',['vijay','om'],'jayesh'],'kiran']
print(students)


# kiran > roshan
students.append('roshan')
print(students) #['ram', 'kunal', ['arun', ['vijay', 'om'], 'jayesh'], 'kiran', 'roshan']

# ram > sham
students.insert(1,'sham')
print(students) # ['ram', 'sham', 'kunal', ['arun', ['vijay', 'om'], 'jayesh'], 'kiran', 'roshan']

# jayesh > yash
students[3].append('yash')
print(students) # ['ram', 'sham', 'kunal', ['arun', ['vijay', 'om'], 'jayesh', 'yash'], 'kiran', 'roshan']

# arun > varun
students[3].insert(1,'varun')
print(students) # ['ram', 'sham', 'kunal', ['arun', 'varun', ['vijay', 'om'], 'jayesh', 'yash'], 'kiran', 'roshan']

# om > sai
students[3][2].append('sai')
print(students) # ['ram', 'sham', 'kunal', ['arun', 'varun', ['vijay', 'om', 'sai'], 'jayesh', 'yash'], 'kiran', 'roshan']