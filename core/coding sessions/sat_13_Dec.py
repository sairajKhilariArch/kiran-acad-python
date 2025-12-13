# 
# * Loop : 1.for    2.while   

# ? Write a program to print 1 to 10 number
# ? write a program to print 1 to 30 number increment by 3
# ? write a program to print 10 to 1 number


# ? for loop

def q_1_for():
    print("Write a program  to print 1 to 10 number")
    for i in range(1,11,1):
        print(i,end=" ")
    print()
    print("write a program to print 1 to 30 number increment by 3")
    for i in range(1,31,3):
        print(i,end=" ")
    print()
    print("write a program to print 10 to 1 number")
    for i in range(11,1,-1):
        print(i,end=" ")
    print()


# q_1_for()

# ? while loop

def q_1_while():
    print("Write a program  to perint 1 to 10 number")
    i =1
    while i<11:
        print(i,end=" ")
        i+=1
    print()
    print("write a program to print 1 to 30 number increment by 3")
    while i <30:
        print(i,end=" ")
        i+=3
    print()
    print("write a program to print 10 to 1 number")
    while i <11:
        print(i,end=" ")
        i-=1
    print()


# q_1_while()


# ? Q2

# ? from user range
def Q2_for_from_user():
    a = int(input("give me a number "))
    b = int(input("give me a another number "))
    for i in range(a,b+1):
        print(i,end=" ")
    print()

def Q2_while_from_user():
    a = int(input("give me a number "))
    b = int(input("give me a another number "))

    while a<b+1:
        print(a)
        a+=1
    print()
    



# ? 3. WAP to print  sum of  1 to 10 numbers:

def Q3_for_range():
    a = 0
    for i in range(1,11):
        a = a + i
    print(a)


def Q3_while_range():
    a = 0
    i=0
    while i<11:
        a = a + i
        i+=1
    print(a)
    




# ? 4. WAP to print sum of number take range by user:

def Q4_for_range_user():
    a = int(input("give me a number "))
    b = int(input("give me a another number "))
    x = 0
    for i in range(a,b+1,1):
        x = x+i
    print(x)

def Q4_while_range_user():
    a = int(input("give me a number "))
    b = int(input("give me a another number "))
    x = 0
    while a <= b :
        x+=a
        a+=1
    print(x)
    

# ? 5. WAP to print sum of even number from 1 to 10 number:

def Q5_for_range():
    a = 0
    for i in range(1,11):
        if i % 2 == 0:
            a = a + i
    print(a)

def Q5_while_range():
    a = 0
    i = 0
    while i<11:
        if i % 2 == 0:
            a = a + i
        i+=1
    print(a)
    




# ?6. WAP to cal sum of all numbers only devi by 3 and 4:


def Q6_sum():
    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a = 0
    for i in l:
        if i%3==0 & i%4==0:
            a = a+i
    print(a)



# ? 7. WAP to cal total obtain marks:

def Q7_sum():
    l = {'math':78,'science':67,'his':90,'hindi':94,'marathi':85}
    a = 0
    for i in l.values():
        a = a+i
    print(a)
    
    



# ? 8. WAP to cal total obtain percentage:

def Q8_sum():
    l = {'math':78,'science':67,'his':90,'hindi':94,'marathi':85}
    a = 0
    b = 0
    for i in l.values():
        a = a+i
        b = b=1
    c = b * 100
    per = (a / c) * 100
    print(per)
    
    


# ? 9. WAP to print dic of selling price

def Q9_dict():
    product_mrp = {'laptop':60000,'mobile':20000,'tv':40000}
    product_sel = {}
    for i,j in product_mrp.items():
        k = j * 15 / 100
        j = j-k
        product_sel[i] = j
    print(product_sel)



