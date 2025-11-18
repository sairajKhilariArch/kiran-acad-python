
# ? POLYMORPHISM :
                    # ? Polymorphism is a core concept in OOP that allows methods to do different things based on the object it is acting upon. 
                    
                    # ? It allows methods to be used interchangeably, even if they belong to different classes.
                    
                    # ! Example of Polymorphism with Method Overriding :
                    
                    
                    # * example:
                    
''' 
                    class Book :
                        def __init__(self,nm,pg):
                            self.name = nm
                            self.pages = pg
                            
                        def __add__(self,others):
                            total = self.pages+others.pages
                            
                            return f'total numbers of pages{total}'
                        
                    b1 = Book('bb11',500)
                    b2 = Book('bb22',500)

                    print(b1+b2) # ^ total numbers of pages1000
                    print(b1.__add__(b2)) # ^ total numbers of pages1000
                    
                    
                    
                    '''
                    
                    

# class hotel :
    
#     def __init__(self,nm,rt ):
#         self.name = nm
#         self.rent = rt 
        
        
#     def __gt__(self,other) :
        
        
#         return grater
        
        
# h1 = hotel('h11',2000)
# h2 = hotel('h2',20000)


# print(h1.__gt__(h2)) 

 
                    






# ? Method Overloading:
                        # ? overloading a method with same method 
                        # ? but in python method overloading is not allowed
                        
                        # ^ it will run the resent one (last return ) same method previous return methods will be deleated 
                        
                        
                        
                        # * Example:
                        
                        
                 
# class Student :
    
#     def __init__(self,nm):
#         self.name = nm
 

#     def __init__(self,nm,rt,id ):
#         self.name = nm
#         self.rent = rt   
#         self.id = id

#     def __init__(self,nm,rt ):
#         self.name = nm
#         self.rent = rt    


# s1 = Student('svsfbbd',520) #^ here it too 2 argument as the last or say most recent one method was writtten with not 1 no 3 but 2 parameters 








