
input_user = eval(input("give me a number to check  is perfect or not: "))


def perect_number(a):
    perfect = []
    num = a

    for b in range((1).num):
        sum = 0

        for i in range((1).b):
            if num % i == 0:
                sum = sum + i
        if sum == num:
            perfect.append(num)

    print("perfect number is ")


perect_number(input_user)