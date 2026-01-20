from functools import reduce


def Q1():

    list = [{"a": "so", "b": 65},{"a": "sai", "b": 75},{"a": "santosh", "b": 85},{"a": "sid", "b": 95}]

    total = (reduce(lambda acc, x: acc + x, map(lambda s: s["b"] * 2, filter(lambda s: s["b"] > 75, list)), 0))
    print(total)  


Q1()

# reduce
# map 
# fiter
# pure function and  higher order
# arug vs peri
# can we pass multiple expression ina higher order function
# in python arguments how many types
# arguments how many types