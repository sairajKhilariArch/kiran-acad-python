
#* METHODS :

            #* NO. OF   paremeter require no. of arguments


            #!  methods takes parameter 
            #! .isalnum
            #! .isalpha()
            #! .index()
            #! .count()
            #! .remove()
            #! .startswith
            #! .endswith
            
name = "sairaj rajendra khilari"

print(type(name)) # ^ :<class 'str'>

print(name.index("j"))  # ^ : 5

print(name.count('a'))  # ^:5

print(name.count('a',0,-8))  #^ : 4

print(name.startswith('s'))  #^ : True

print(name.endswith('i'))  #^ : True

print(name.startswith('s',1,10)) #^ : False

print(name.endswith('i',2,5))  #^ : False

print(name.center(100,"-"))  #^ :output --------------------------------------sairaj rajendra khilari---------------------------------------

