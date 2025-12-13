input_user = eval(input("give me a number to"))

def piramid(a):
    j = 1
    p = a
    for i in range(a):
        print(" "*p,"*"*j)
        j+=1
        p-=1

piramid(input_user)

git config --global user.email "sairajkhilari191918110+github1@gmail.com"
git config --global user.name "sairajKhilariArch"