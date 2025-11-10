#  ATTRIBITES:
                # ATTRIBUTES are the data members and variables associateds the class or an object

                # attributes means veriables

                #  attributes store properties of the class or object

                # their are various type of attributes:
                    # ? 1.instance attributes

                    # 2.class attributes

                    # 3.local attributes



class Student :

    def __init__(self,na,ag,ci):
        self.age = ag
        self.name = na
        self.city = ci


st_1 = Student("sairaj",52,"pune")

print(st_1.age)