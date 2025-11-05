# lambda :
            
'''
print((lambda n1 , n2  : n1 + n2)(10,20))
'''

# this is a normal function of making
# name into fullname 
'''
def fullname(fn,mn,ln):
    fname = f'{fn} {mn} {ln}'
    return fname
print(fullname('jay' ,'prakash', 'shankar'))
'''

# this is  a LAMBDA function for making name into fullname  
'''
print((lambda fn,mn,ln : f'{fn} {mn} {ln}')('jay' ,'prakash', 'shankar'))
'''


# create a function for square only
'''
print((lambda a:a*a)(2))
'''


# make a calculater function using lambda :
'''
calculater = (lambda num1 ,num2:(num1+num2 , num1-num2 ,num1*num2 , num1/num2, num1%num2))
add,sub,mul,div,reminder = calculater(5,5)
print(add)
'''



# FILTER:
            # filter takes two argument
                # 1.function
                # 2.iterables


# so at the function we can make lambda function to make it small and redable

# eg with normal function
'''
numbers = [23, 87, 45, 12, 34, 59, 76, 8, 51, 29]

def gt(aaa):
    if aaa > 50:
        return True
    else:
        return False

print(list(filter(gt,numbers)))
'''

# eg with lambda function

numbers = [23, 87, 45, 12, 34, 59, 76, 8, 51, 29]
print(list(filter(lambda aaa :aaa > 50 ,numbers)))