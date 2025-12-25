# * Q1 WAP to take a user number and cal the sum of its odd number return list for odd and even number and return  total no of even and odd also return list and total even number and total odd number list


def Q1():
    odd_list = []
    even_list = []
    sum_odd = 0
    sum_even = 0
    a = eval(input("give me a number :"))

    for i in range(a):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    for i in odd_list:
        sum_odd = sum_odd + i

    for i in even_list:

        sum_even = sum_even + i
    print("sum of all odd numbers are :", sum_odd)
    print("sum of all even numbers are :", sum_even)
    print("list od odd number is:", odd_list)
    print("list od even number is:", even_list)


# Q1()


# * Q2 WAP to check if a given string  is a palindrome or not using loop...


def Q2():
    a = input("give me a string : ")
    b = ""

    if b == a:
        print("string is a palindrome")
    else:
        print("string is not a palindrome")


# Q2()


# * Q3 WAP to check if a given string is a palindrome or using loop


def Q3():
    a = input("give me a string : ")
    b = ""
    for char in a:
        b = char + b
    print(b)
    if b == a:
        print("string is a palindrome")
    else:
        print("string is not a palindrome")


# Q3()


# * Q4 WAP to find a frequently of each character in a string (how many times each char occurs) print a dict.....


def Q4():
    a = input("give me a string to cal char and their frequency :")
    b = {}
    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    print(b)


# Q4()

# * Q5 WAP  a program to check whether  a given number is prime  or not.


def Q5():
    a = int(input("give me a number :"))
    if a <=1 :
        print("is not a prime number")
        return
    elif a == 2 :
        print("is a prime number")
        return
    else:
        for i in range(2,a):
            if a % i ==0:
                print("is not a prime number")
                return
        print("is a prime number")
        return


# Q5()


# * Q6 write a program  to print all prime numbers  between 1  and n return list of a prime number



def Q6():
    a = int(input("give me a number :"))
    def is_prime(a):
        if a <=1 :
            flag = False
            return
        elif a == 2 :
            flag = True
            return
        else:
            for i in range(2,a):
                if a % i ==0:
                    flag = False
                    return
            flag = True
            return
    prime_list = []
    for i in range(1,a+1):
        if is_prime(i):
            prime_list.append(i)
    print("This are the prime numbers :",prime_list)
b

Q6()