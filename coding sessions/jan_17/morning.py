
# ? WAP to calculate the words froom the file


def Q1():
    f = open("hello.txt",'r')

    data = f.read()
    print(len(data.split()))

# Q1()


# ?Q2: WAP to in a file a word repeated how many times

def Q2():
    
    file = input("what is the file name you want to open")
    word = input("what is the word you want to find")
    f = open(file,'r')
    a = 0
    for line in f:
        list1 = line.split()
        for wd in list1:
            if word.lower() ==wd.lower():
                count = count + 1
    return count
    


# Q2()


# ? Q3 customer no txt file name number

def Q3():
    file = "customer.txt"
    f = open(file, 'r')

    results = []

    for line in f:
        list1 = line.split()
        hi = list1[-1]  

        isnumber = hi.isnumeric()  
        length = len(hi)          

        match (isnumber, length):
            case (True, 10):
                ppo = "good"
            case (False, 10):
                ppo = f"contact no does not contain only numbers {hi}"
            case (True, _):
                ppo = f"invalid length {hi}"
            case (False, _):
                ppo = f"invalid number and invalid length {hi}"
            case _:
                ppo = "invalid"

        results.append(ppo)

    return "\n".join(results) 


# Q3()




# ? total sum of the sales value 

def Q4():
    
    file = "sales.txt"
    f = open(file, 'r')
    total = 0
    for line in f:
        list1 = line.split()
        hi = list1[-1]
        price = hi.replace("₹", "").replace(",","")
        price = int(price)
        total = total + price
    return f"₹{total}"

Q4()

















