
# * ENCAPSULATION:

                    # ? Encapsulation is a process which bundling (wrapping) and store the data and methods in a class in a protrected format that other that the same class no one can acess the veriable which is protected 
                    
                    # ? restracting certain part of the data
                    
                    
                    # ? to protect the veriable '__'is used  


















class Counter :
    
    def __init__(self):
        self.__count = 0
        
    def inc(self):
        self.__count += 1
        
    def dec(self):
        self.__count -= 1
        
    def tcount(self):
        return f'total count is {self.__count}'
    
    
z = Counter()

z.inc()

z.inc()

z.inc()

z.inc()

z.inc()

z.inc()

z.dec()

𝗽𝗿𝗶𝗻𝘁(𝘇.tcount())





# * SETTER :
            # ? set the value of the private attribute
            
            
#  * GETTER :
            # ? get the  value of private attribute
            
            



class Student:
    
    def __init__(self,na,ag):
        self.__name = na
        self.__age = ag
        
        
    def name(self):
        return {self.__name}
    
    def age(self):
        return {self.__age}
    
    
    def set_name(self,sna):
        if isinstance(sna,str) and sna.isalpha():
            self.__name =sna
        else :
            print("invalid name")
            
    def set_age(self,sag) :
        if isinstance(sag,int) and sag>0 and sag<100 :
            pass
        
