#

# ? Q1 Accept string from console and display its data type as well as that string on console


def Q1():
    a = input("give me a string :")
    print(type(a))
    print(a)


# ? Q2 Accept string from terminal and display its  length on screen


def Q2():
    a = input("Enter one string: ")
    print("length of given string = ", len(a))


# ? Q3 Wap to check length of given string if length is more than 8 then valid string otherwise its invalid


def Q3():
    a = input("give me a string more than 8 character :")
    l = len(a)
    if l > 8:
        print("it is a valid string")
    else:
        print("it is not a valid string")


# ? Q4 Wap to check length of given string if length is more than 8 then valid string otherwise its invalid if that string contain white space then also it is invalid


def Q4():
    a = input("give me a string more than 8 character :")
    l = len(a)
    if l > 8:
        if " " in a:
            print("it is not a valid string")
        else:
            print("it is a valid string")
    else:
        print("it is not a valid string")


# ? Q5 Wap to check length of given string if length is more than 8 then valid string otherwise its invalid if that string contain white space then also it is invalid should contain a degit


def Q5():
    a = input("give me a string more than 8 character :")
    l = len(a)
    if l > 8:
        if " " in a:
            print("it is not a valid string")
        else:
            if a.isdigit():
                print("it is a valid string")
            else:
                print("it is not a valid string")
    else:
        print("it is not a valid string")


def Q5_ver2():
    a = input("give me a string more than 8 character :")
    if len(a) > 8 and " " not in a and a.isalnum():
        print("it is a valid string")
    else:
        print("it is not a valid string")


# ? Q6 Wap to check length of given string if length is more than 8 then valid string otherwise its invalid if that string contain white space then also it is invalid should contain a degit one capital char and special char


def Q6():
    a = input("Give me a string more than 8 characters: ")

    if len(a) > 8:

        if " " in a:
            print("It is not a valid string")
            return

        digit = False
        upper = False
        special = False

        for ch in a:
            if ch.isdigit():
                digit = True
            if ch.isupper():
                upper = True
            if ch in "!@#$%^&*()":
                special = True

        if digit and upper and special:
            print("password is valid")
        else:
            print("It is not a valid string")
    else:
        print("It is not a valid string")


Q6()
