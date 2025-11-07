# map :
        # map is also like a  filter 
        # but filter returns if it is a true or false 
        # but map returns the element 

'''
students = ['kunal','vishal','sai','sunil']
print(list(map(lambda name : name.upper(),students)))
'''


'''
numbers = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
print(list(map(lambda number : number+5 ,numbers)))
'''
'''
numbers = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
print(list(map(lambda number : number**2 ,numbers)))
'''

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(dict(map(lambda number : (number,number*number) ,numbers)))


emp = {'kunal':5200,'vishal':8520,'sai':7410,'sunil':6305}
print(dict(map(lambda t : (t[0],t[1]+5000) ,emp.items() )))