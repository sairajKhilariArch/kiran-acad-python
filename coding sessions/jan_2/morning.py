
#  ! arbitrary arguments:
#               & takes many arguments in a function/method
#               ? used when we dont know how many arguments are present..to be obtain by user


def Q_Percentage(*args,total_marks):
    per = obtain_marks/total_marks * 100
    print(per)




# Q_Percentage(2,10)



class Student:
    
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}
        
    def add_marks(self):
        mar = int(input("how many subjects are their : "))
        for i in range(mar):
            sub = input(f"Enter subject {i+1} name:")
            mark = int(input("Enter mark:"))
            
            self.marks[sub] = mark
        print("marks added...")
    
    def calculate_total(self):
        # return sum(self.marks.values())
        mark = self.marks.values()
        total = sum(mark)
        return total
        
    def calculate_percentage(self):
        # total_mark = sum(self.marks.values())
        # total_sub = len(self.marks) * 100
        # return (total_mark / total_sub) * 100
        
        mark = self.marks.values()
        total_mark = sum(mark)
        total_sub = len(mark) * 100
        per =  total_mark/total_sub  * 100
        print(per)
        return per
    
    def ss(self):
        result = ""
        for sub, mark in self.marks.items():
            result += f"{sub:15} {mark}\n"
        return result
    
    
    def display_details(self):
        mar = self.calculate_total()
        per = self.calculate_percentage()
        
        detail = f"""
        NAME       : {self.name}
        Roll no.   : {self.roll_no}
        MARKS      : {mar}
        PERCENTAGE : {per}
        subjects      marks
        --------------------
        {self.ss()}
        """
        print(detail)

s1 = Student(101,"sairaj")
s1.add_marks()
s1.display_details()
# s1.ss()
# s1.calculate_total()
# s1.calculate_percentage()