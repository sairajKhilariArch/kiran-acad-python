
# * Exception Handeling :
                        # ? It is a try catch block which run for the code which it is written for if it (code) fails to run....
                        
                        #^ try:
                            # & risky code
                        # ^except:
                            # &code to handle exception
                        # ^else:
                            # & if no exp
                        #^ finally:
                            # & always ex.
                        
                        
'''                        
                        
# ? Eg: for how it's done

n1 = int(input("give me a integer")) 
n2 = int(input("GIVE ME A INTEGER"))

try:
    div = n1/n2
    print(div)
except:
    print("only integer and no 0 as input")
    
print("coding...")

'''

'''
# ? Eg: for multiple exception

n1 = int(input("give me a integer")) 
n2 = int(input("GIVE ME A INTEGER"))

try:
    div = n1/n2
    print(div)
except ZeroDivisionError:
    print("only integer and no 0 as input")

except NameError:
    print("incorrect variable name")
    
print("coding...")

'''

'''

# ? Eg: for full fledge try except else finally block

n1 = int(input("give me a integer")) 
n2 = int(input("GIVE ME A INTEGER"))

try:
    div = n1/n2
    sum = n1/n2
    mult = n1/n2
    sub = n1/n2
except ZeroDivisionError:
    print("only integer and no 0 as input")

except NameError:
    print("incorrect variable name")
finally:

    print(sub)
    print(mult)
    print(sum)
print("coding...")

'''

'''
# ? Eg: raise excepion handling

age = int(input("your age :"))

if age < 0:
    raise ValueError
print("my age is ",age)
print("coding.........")

'''














