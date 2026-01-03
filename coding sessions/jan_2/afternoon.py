



class Employee:
    
    def __init__(self,empid,name,basic_salary):
        self.empid = empid
        self.name = name
        self.basic_salary = basic_salary
        
        
    def calculate_allowances(self):
        HRA = (self.basic_salary*20/100)
        DA = (self.basic_salary*10/100)
        return HRA,DA

    def calculate_gross_salary(self):
        HRA,DA = self.calculate_allowances()
        Gross_Salary = self.basic_salary + HRA + DA
        return Gross_Salary

    def calculate_net_salary(self):
        Gross = self.calculate_gross_salary() 
        tax_10per = Gross * 10 / 100
        Net_Salary = Gross - tax_10per
        
        return Net_Salary

    def display_payslip(self):
        HRa,Da = self.calculate_allowances()
        data = f"""
    NAME            : {self.name}
    ID              : {self.empid}
    Salary          : {self.basic_salary}
    HRA             : {HRa}
    DA              : {Da}
    Gross Salary    : {self.calculate_gross_salary()}
    Net Salary      : {self.calculate_net_salary()}
    """
        print(data)
    

# emp1 = Employee(567,"asdf",100)
# emp1.display_payslip()





class BankAccount:
    Bank_Name = "Bank of India"
    IFSC_COde = "123456780987"
    Bank_Address = "pune"
    
    def __init__(self,Account_number,Holder_name,Balance):
        self.Account_number = Account_number
        self.Holder_name = Holder_name
        self.Balance = Balance
    
    
    
    def Deposit(self):
        bal = int(input("how much Balance you want to add :"))
        self.Balance += bal
        print("your balance has been added...")
        
        
        
    def withdrew(self):
        bal = int(input("how much Balance you want to Withdraw :"))
        if bal< self.Balance :
            self.Balance -= bal
            print(f"Withdraw is successful with {bal} Amount is been deducted...")
        else:
            print("insufficient BAlance present in the Account ")
        
        
    def check_balance(self):
        print(f"Balance in your Account is {self.Balance}")
    
    def display_account(self):
        data = f"""
    NAME            : {self.Holder_name}
    Account Number  : {self.Account_number}
    Balance         : {self.Balance}
    """
        print(data)
    
    def display_bank_details(cls):
        data = f"""
    Bank Name       : {cls.Bank_Name}
    Bank IFSC code  : {cls.IFSC_COde}
    Bank Address    : {cls.Bank_Address}
    """
        print(data)

    
cus1 = BankAccount(123,"dfg",100000)

cus1.Deposit()

cus1.withdrew()

cus1.check_balance()


cus1.display_account()
cus1.display_bank_details()