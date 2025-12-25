class employee:

    company_name = 'Blender'
    total_employee = 0
    bonuss_rate = 10
    max_leves = 5
    employee.total_employee += 1


    def __init__(self,eid,na,sal,dep,lev,pos):
        self.emp_id = eid
        self.name = na
        self.salary = sal
        self.department =dep
        self.no_leave = lev
        self.bonus_rate = employee.bonuss_rate
        self.position =pos
        

    def details(self):
        detail = f'''
        {employee.company_name}
        Employee ID = {self.emp_id}
        Employee Name = {self.name}
        Employee Salary = {self.salary}
        Employee Department = {self.department}
        Employee took {self.no_leave} leaves
        Employee position = {self.position}
        '''
        return detail

    @classmethod
    def Update_Bonus_rate_comp(cls,ra):
        bonus_rate = ra
        cls.bonuss_rate = bonus_rate
        return "boue rate is been updated to ",ra


    def Bonus_Apply(self,id):
        # bonus_rate = ra
        bonus_amount = ((self.bonus_rate  * self.salary ) /100)
        return "Bonus Applyed and the bonus this employee going to gate is",bonus_amount
    
    def Update_Bonus_rate_emp(self,ra):
        bonus_rate = ra
        self.bonus_rate = bonus_rate
        return "boue rate is been updated to ",ra

    def request_leave(self,no_l):
        new_leave_w = no_l
        leaves = self.no_leave
        if employee.max_leves <no_l:
            if leaves >= 12 :
                return "no leaves for this employee"
            else :
                self.no_leave = self.no_leave + new_leave_w
                return "employees leaves is granted"
        else:
            return 'you can not take this many leaves at the same time'
    

    def promote_employee_new_possition(self,npos):
        self.position = npos
        return "employees position is updated to ",npos

    def transfer_to_new_department(self,ndep):
        self.department = ndep
        return "employees department is changed to ",ndep

    def total_no_of_emp_in_company(cls):
        return "total no of company employee are",total_employee









e1 = employee(12,"sairaj",100000,"coder",1,"assit programmer")
e2 = employee(1,"sairaj",100000,"coder",1,"assit programmer")
e3 = employee(2,"sairaj",100000,"coder",1,"assit programmer")
e4 = employee(32,"sairaj",100000,"coder",1,"assit programmer")
print(e1.details())

print(e1.Update_Bonus_rate_emp(20))

print(e1.Bonus_Apply(12))
print()








