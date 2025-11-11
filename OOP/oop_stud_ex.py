class Students:
    #class attributes
    institute='The Kiran Academy'
    branch='Karve Nager'
    course='Data Science'
    course_fees=40000
    trainer='Vaibhav Patil'
    def __init__(self,nm,bn):
        #instance attributes
        self.name=nm
        self.fees={'tfees':30000,'pfees':0,'rfees':0}
        self.batch_no=bn
        self.marks={}
    def details(self):
        data=f'''
            {Students.institute}

            Name : {self.name}
            Batch Number: {self.batch_no}
            Course : {Students.course}
            Total Fees : {self.fees['tfees']}
            Paid Fees  : {self.fees['pfees']}
            Remaining Fees  : {self.fees['rfees']}
            '''
        
        return data
    
    def cal_total_fees(self,dis):
        dp=Students.course_fees*dis/100
        tfees=Students.course_fees-dp
        self.fees['tfees']=tfees
        print('Total fees after dis:',tfees)
        pfees=eval(input("enter fees amount: "))
        self.fees['pfees']= pfees
        rfees=tfees-pfees
        self.fees['rfees']=rfees
        return f'''
            Total : {tfees}
            Paid  : {pfees}
            Remaining : {rfees}
            '''
    
    @classmethod
    def update_course_fees(cls,new_fees):
        cls.course_fees=new_fees
        return 'done'
    
    def change_batch(self,bno):
        self.batch_no=bno
        return 'done'
    

    def add_test_marks(self,test_name,marks):
        self.marks[test_name]=marks
        return 'done'


    def cal_per(self):
        all_marks=self.marks.values()
        obt=sum(all_marks)
        total=len(self.marks)*100
        per=(obt/total)*100
        return per
    
    def final_result(self):
        per=self.cal_per()
        if per >=40:
            return 'pass'
        else:
            return 'fail'
    
    

    
s1=Students('pritam',1290)
s2=Students('pavan',1293)
s3=Students('ajay',1290)
print(s1.add_test_marks('test1',89))
print(s1.add_test_marks('test2',79))
print(s1.add_test_marks('test3',99))
print(s1.cal_per())
print(s1.final_result())



    
    
    
