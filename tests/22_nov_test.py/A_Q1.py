# * create a fun prime or not
input_user = eval(input("give me a number to check prime is or not: "))


def is_prime(a):
    primee = ""
    for i in range(2, a):
        if (a % i == 0) & (a % a == 0):
            primee = "false"

        else:
            primee = "true"

    if primee == "true":
        print("number is prime")
    else:
        print("number is not print")


is_prime(input_user)
