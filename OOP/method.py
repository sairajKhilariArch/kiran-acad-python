'''
# * Methods :
                # ? methods are ruuable block of code which are present in class

                # ? there are 3 type of methods in class(oop)

                    # ^ 1.instance method

                    # ^ 2.class method

                    # ^ 3.static method

# * 1.Instance Method:
                        # ! object level => Instance attributes
                        # ! self
                        # ! object refrence


# * 2.Class Method:
                        # ! Class Level => Class Attributes
                        # ! Class
                        # ^ @classmethod
                        # ! object refrence or class name

# * 3.Static Method:
                        # ! Local Attribute
                        # ! no refrence
                        # ^ @staticmethod
                        # ! object refrence or class name

hhbb  fff

'''


class Student:
    #? class attributes
    institute = "The kiran Academy"
    course = "Data Science"
    fees = 40000
    trainer = "Vaibhav Patil"

    def __init__(self,nm,ag,bn):
        #? instanse attributes
        self.name = nm
        self.age = ag
        self.marks = {}
        self.batch_no = bn
        self.post_fees = {'t_fee' : 0,'r_fees' : 0,'p_fees':0}


    def details(self) :
        detail = f'''
        {Student.institute}
        NAME :{self.name}
        AGE :{self.age}
        Batch Number :{self.batch_no}
        Course :{Student.course}
        Trainer no :{Student.trainer}
        total fees: {self.post_fees['t_fee']},
        remaining fees: {self.post_fees['r_fees']}, 
        paid fees: {self.post_fees['p_fees']}
        
            '''
        return detail



        def cal_total_fees(self,dis):
            dp = Student.fees*dis/100
            tfees = Student.fees-dp
            self.post_fees['t_fee'] =tfees
            print('total fees after dis:',tfees)
            postfees =eval(input("enter fees amount : "))
            self.post_fees['p_fees'] = postfees
            r







s1 = Student('ajay',23,9352)
s2 = Student('vijay',12,5522)
print(s1.details())   
''' 
# &        The kiran Academy
# &        NAME :ajay
# &        AGE :23
# &        Batch Number :9352
# &        Course :Data Science
# &        Trainer no :Vaibhav Patil
# &        total fees: 0,
# &        remaining fees: 0, 
# &        paid fees: 0

'''