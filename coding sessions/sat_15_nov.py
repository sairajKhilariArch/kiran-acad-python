
'''
class student:

    def __init__(self,rno,na):
        self.name = na 
        self.roll_no = rno
        self.marks = {}

    def add_marks(self,no):
        for i in range(no):
            sub=input('enter subject name')
            marks = eval(input('enter your marks'))
            self.marks[sub] = marks

    def calculate_total(self):
        all_marks = self.marks.values()
        total_obt = sum(all_marks)
        return total_obt

    def calculate_percentage(self):
        obt = self.calculate_total()
        total = len(self.marks) * 100
        per = (obt/total)*100
        return per

    def get_result(self) :
        per =self.calculate_percentage()
        if per >= 40 :
            return 'fail'
        else:
            return 'pass'

    def display_details(self):
        pass


'''





# # ! employee ----------------------------------------------------------------------------------------------------------------------

# class Employee :

    

#     def __init__(self,eid,na,sal):
#         self.name = na
#         self.emp_id = eid
#         self.basic_salary = sal
        
#     def calculate_allowance(self) :
#         self.Hra =(( self.basic_salary * 20 )/100) 
#         self.Da = ((self.basic_salary * 10)/ 100)

#         return f'''done'''

#     def calculate_gross_sal(self):
#         self.gross_salary = self.basic_salary + self.Hra + self.Da 

#         return f'''done'''

#     def calculate_net_sal(self):
#         self.tax_sal = self.gross_salary *10 /100
#         self.net_sal = self.gross_salary - self.tax_sal

#         return '''done'''


#     def display_details(self):
#         detailss = f'''
        
#         Employee ID : {self.emp_id}

#         Employee Name : {self.name}

#         Employee salary : {self.basic_salary}

#         Employee Allowances :

#                         HRA of salary : {self.Hra}

#                         DA of salary : {self.Da}

#         Employee gross salary = {self.gross_salary}

#         Employee net salary = {self.net_sal}

#         Employee tax paid = {self.tax_sal}
        
#         '''

#         return detailss



# e1 = Employee(123,"sairaj",50000)


# e1.calculate_allowance()
# e1.calculate_gross_sal()
# e1.calculate_net_sal()

# print(e1.display_details())

# !---------------------------------------------------------------------------------------------------------------------------------





# ! Bank Account Management --------------------------------------------------------------------------------------------------------


# class BankAccount :
    

#     def __init__(self,an,hna,bal):
#         self.account_number = an
#         self.holder_name = hna
#         self.balance = bal

#     def Deposit_ammount(self,amo):
#         add_amo = amo
#         self.balance += add_amo

#         return 'done' 

#     def Withdrow_ammount(self,amo) :
#         wamo = amo
#         if wamo <= self.balance:
#             self.balance -= wamo
#             return 'withrow done'
#         else :
#             return 'insufficientt Balance'

#     def current_balance(self):
#         return f'current balance in the account is ',{self.balance}


#     def account_details(self) :
#         detail = f'''
#         ---------------------------Account Detail------------------------------------
#         Account Number : {self.account_number}
#         Account Holder Name : {self.holder_name}
#         Account Balance : {self.balance}
#         '''
#         return detail



# ah1 = BankAccount(10001,'sairaJ khilari',50000)

# print(ah1.Deposit_ammount(50000))

# print(ah1.Withdrow_ammount(205000))

# print(ah1.account_details())




# !------------------------------------------------------------------------------------------------------------



# ! Library Management System ---------------------------------------------------------------------------------




