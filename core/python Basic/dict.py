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

# Define types for clarity: outer -> department -> employee -> {str: str | int}
jbk: Dict[str, Dict[str, Dict[str, str | int]]] = {
    'faculty': {  # Fixed typo for better readability
        'f101': {'name': 'om', 'salary': 50000},  # Fixed spelling
        'f102': {'name': 'shanti', 'salary': 40000}
    },
    'operation': {
        'O101': {'name': 'sai', 'salary': 30000},
        'O102': {'name': 'sakshi', 'salary': 20000}
    }
}

print()
print(jbk.items())
print()
print(jbk.keys())
print()
print(jbk.values())
print()

# Update the name (use quotes for keys; update returns None, so print after)
jbk['operation']['O101'].update({'name': 'sa'})  # Or: .update(name='sa')
print(jbk['operation']['O101'])  # Shows updated: {'name': 'sa', 'salary': 30000}
print(jbk)


