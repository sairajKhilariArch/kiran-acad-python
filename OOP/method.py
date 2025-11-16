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



'''


class Student:
    #? class attributes
    institute = "The kiran Academy"
    course = "Data Science"
    course_fees = 40000
    trainer = "Vaibhav Patil"

    def __init__(self,nm,ag,bn):
        #? instanse attributes
        self.name = nm
        self.age = ag
        self.marks = {}
        self.batch_no = bn
        self.post_fees = {'t_fees' : 0,'r_fees' : 0,'p_fees':0}


    def details(self) :
        detail = f'''
        {Student.institute}
        NAME :{self.name}
        AGE :{self.age}
        Batch Number :{self.batch_no}
        Course :{Student.course}
        Trainer no :{Student.trainer}
        total fees: {self.post_fees['t_fees']},
        remaining fees: {self.post_fees['r_fees']}, 
        paid fees: {self.post_fees['p_fees']}
        
            '''
        return detail



    def cal_total_fees(self,dis):
        dp = Student.course_fees*dis/100
        tfees = Student.course_fees-dp
        self.post_fees[tfees] = tfees
        print('Total fees after dis:',tfees)
        pfees = eval(input("What Amount of Sum Fees You Would Like To Pay :"))
        self.post_fees['p_fees'] = pfees
        rfees = tfees - pfees
        self.post_fees['r_fees'] = rfees
        
        return (f"For the {dis}% Discount on course fee and \n you have paid {pfees} rupees \n of which your Total remaining fees are {rfees}")
    
    
    @classmethod
    def update_course_fees(clself,amount) :
        clself.course_fees = amount
        
        return 'Done :New fee amount has been updated'
        
    
    def change_batch(self,n_batch_no) :
        print('Your batch is  changing......')
        self.batch_no = n_batch_no
        
        return 'Done :Your batch has been changed'
    
    
    def update_new_test_marks(self,tname,tmarks) :
        print('Your new test and new marks are being added......')
        
        self.marks[tname] = tmarks
        
        return 'Done: Your new test and new marks have been added'
    
    def test_persentage(self) :
        marks = list(self.marks.values())
        smarks =sum(marks)
        lmarks = len(marks)
        per = (smarks * lmarks)/100
        self.persentage = per
        
        return 'Persentage of all the tests are ', per
    
    
    def pass_or_fail(self):
        per = self.persentage
        if per >= 75 :
            return 'you are pass with flying persentage'
        elif per>=35 :
            return 'you are pass'
        else :
            return 'you are fail'








s1 = Student('ajay',23,9352)
s2 = Student('vijay',12,5522)




s1.update_new_test_marks("Data Structures", 92)
s1.update_new_test_marks("Algorithms", 88)
s1.update_new_test_marks("Object-Oriented Programming", 95)
s1.update_new_test_marks("Database Design", 85)
s1.update_new_test_marks("Web Development", 90)
s1.update_new_test_marks("System Design", 87)
s1.update_new_test_marks("Operating Systems", 83)
s1.update_new_test_marks("Computer Networks", 86)
s1.update_new_test_marks("Software Testing", 91)
s1.update_new_test_marks("API Development", 94)


print(s1.test_persentage())


print(s1.pass_or_fail())




# print(s1.change_batch(1010))

# print(s1.update_course_fees(10000))


# print(s1.cal_total_fees(10))


# print(s1.details())   
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




