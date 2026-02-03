class Person :
    
    def __init__(self,na,ad):
        self.name = na
        self.address = ad


class Student(Person) :
    
    def __init__(self, na, ad , rno ,ma):
        super().__init__(na, ad)
        self.Roll_no = rno
        self.marks = ma


class Scholership(Student):
    
    def __init__(self, na, ad, rno, ma):
        super().__init__(na, ad, rno, ma)
        
        
    
    def will_be_eligible(self):
        if self.marks >= 85 :
            return "you are eligible for the scholership"
        
        else :
            return "you are not eligible for the scholership"
        
    
    def student_details(self):
        
        data = f"""
        Student  Details
        -------------------------------------------
        Name        :     {self.name}
        Address     :     {self.address}
        Marks       :     {self.marks}
        Scholership :     {self.will_be_eligible()}
        """
        
        return data



hi = Scholership("sairaj", "pune" , 101 , 90)

print(hi.student_details())


hii = Scholership("sairaj", "pune" , 102 , 70)

print(hii.student_details())