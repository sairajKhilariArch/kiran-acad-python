input_user = eval(input("give me a number to"))

def piramid(a):
    j = a
    for i in range(a):
        print("*"*j)
        j-=1

piramid(input_user)

