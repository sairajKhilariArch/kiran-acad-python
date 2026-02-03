from functools import reduce

def Q1():
    list = [12,234,346,76,256,334,66,200,100]
    
    a = reduce(
        lambda a, x: a + x, 
        map(
            lambda s: (s-(s * 25/100)), 
            filter(
                lambda s: s > 100, list
                )
            ),0
        )

    print(a)  

Q1()


positonal argument

first calss function

function composition 

clouser


