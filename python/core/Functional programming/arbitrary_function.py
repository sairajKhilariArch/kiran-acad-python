
# * arbitrary function:
#               ! Arbitrary arguments let a function take any number of values without knowing the count in advance.
#               & It means a function can accept any number of arguments.

#               ? You don’t know beforehand how many values the user will pass.

#               ^ Eg: def func(*args):
#                ^        print(args)


# * Arbitrary arguments : (*args)
#               & converts it selfs into tuple
def add(*args):
    return sum(args)

print(add(1, 2)) # ^ 3
print(add(1, 2, 3, 4, 5)) # ^ 15

#             ? args becomes a tuple: (1,2) or (1,2,3,4,5)


# * Arbitrary keyword arguments :(**kwargs)
#               ! Accept any number of named arguments.
#               & converts it selfs into dict 
#               ^ Eg:
#               ^ def func(**kwargs):
#               ^     print(kwargs)

def show(**kwargs):
    print(kwargs)

show(name="Sairaj", age=20) # ^ {'name': 'Sairaj', 'age': 20}
show(country="India", skill="Python") # ^ {'country': 'India', 'skill': 'Python'}


# * Arbitrary function:
#                ? There is no special thing called an “arbitrary function” in Python.
#                ? What people mean is:
#                & A function that uses arbitrary arguments (*args or **kwargs).
#                ! So “arbitrary function” = “function with variable-length arguments”.


# * DIfference:
#               !| Feature                        | Meaning                    | Symbol     |
#               ?| ------------------------------ | -------------------------- | ---------- |
#               &| Arbitrary positional arguments | Any number of values       | `*args`    |
#               &| Arbitrary keyword arguments    | Any number of named values | `**kwargs` |



# * Mixing normal + arbitrary

def demo(a, b, *args, **kwargs):
    print(a, b) # ^ 1,2
    print(args) # ^ (3,4)
    print(kwargs) # ^ {'x': 10, 'y': 20}

demo(1, 2, 3, 4, x=10, y=20)


# * Order rule:
#               ? Normal → *args → **kwargs
#               ? This order is mandatory.
#               ^ def func(normal, *args, **kwargs):
#               ^     pass


# * Final simple explanation:

#               !| Term                | Meaning                               |
#               ?| ------------------- | ------------------------------------- |
#               &| Arbitrary arguments | Unknown number of inputs              |
#               &| `*args`             | Many positional arguments             |
#               &| `**kwargs`          | Many named arguments                  |
#               &| Arbitrary function  | Function that accepts variable inputs |