'''
DICTIONARY :
            it is a comma seperated (key , value )-pair in a {}
            
            Syntax:
                    var = {k1:v1,k2:v2,k3:v3,k4:v4.....}
            
                square = {1:1,2:4,3:9,4:16,5:25.....}       
                print(type(square))   # <class='dict'>
            
            key:
                unique & ImMutable

            ex: 
                numbers {1:1,2:4,3:6,4:16,5:25,3:9}
                print(numbers)  #{1:1,2:4,3:6,4:16,5:25,3:9}
                
            values:
                dublicate & both-(mutable & ImMutable)
                
            ex:
                emp{1:'hello',2:'hello',3:{'name':'hello'}}
'''
from typing import Dict

# nested dict 
jbk = {
    'facuilty':{
        'f101':{'name':'om','salery':50000},
        'f102':{'name':'shanti','salery':40000}
                },
    'operation':{
        'O101':{'name':'sai','salery':30000},
        'O102':{'name':'sakshi','salery':20000}
                }
}

# jbk.clear()
print()
print(jbk.items())
print()
print(jbk.keys())
print()
print(jbk.values())
print()
print(jbk[operation][O101].update(name="sa"))
print(jbk)