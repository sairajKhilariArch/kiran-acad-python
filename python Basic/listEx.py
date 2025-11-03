from typing import Any

numbers : list[int | list[Any]]= [11, 22, 33, [10, 20, 30, 40, [1, 2, 3, 4], 50, 60, 70], 44, 55, 66]

print(numbers)  # [11, 22, 33, [10, 20, 30, 40, [1, 2, 3, 4], 50, 60, 70], 44, 55, 66]

print(numbers[3][2]) # 30

print(numbers[-4][-2]) # 60

print(numbers[-4][-4][-4]) # 1
