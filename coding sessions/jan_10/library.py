
class Library:
    L_NAME = "THE KIRAN ACADEMY"
    L_OWNER = "KIRAN SIR"

    
    def __init__(self,br):
        self.Branch = br
        self.Books ={}
        self.Members = {}
        
    
    def book_add(self,bname,bcount):
        if bname in self.Books:
            self.Books[bname] += bcount
            return "done"
        else :
            self.Books[bname] = bcount
            return "done"
        
        
        
    def book_remove(self):
        stats = input('you want to Remove the Books or less the count of the book \n "R" for remove "C" for count "E" for exit:').upper()
        
        while stats not in ('R', 'C', 'E'):
            stats = input("Type R to remove, C to count, E to exit: ").upper()

        if stats in ('R', 'C'):
            book_name = input("Book name")
            if book_name in self.Books:
                if stats =='R':
                    del self.Books[book_name]
                    return "done"
                elif stats =='C':
                    book_count = int(input("what is the count"))
                    self.Books[book_name]-=book_count
                    return "done"
            else:
                return "Book is not in the library"
        elif stats == 'E':
            return "exited"
        else:
            print("incorrect character retype")
            return self.book_remove()
    
    
    
    
    def book_issue(self):
        print("------------------------------ ")
        print("Book Issue ")
        print("------------------------------ ")
        id = input("What is your ID: ")
        book = input("What book do you want: ")

        if id not in self.Members:
            print("You are not a member.")
            stats = input("Add member? (Y/N/E): ").upper()

            while stats not in ('Y', 'N', 'E'):
                stats = input("Type Y to add, N to cancel, E to exit: ").upper()

            if stats == 'E':
                return "Exited."
            elif stats == 'Y':
                self.Add_Member()
                print("------------------------------ ")
                print("Book Issue ")
                print("------------------------------ ")
                return self.book_issue()
            else:
                return "Book not issued."

        if book not in self.Books:
            return "Book not in library."

        if self.Books[book] == 0:
            return "Book not available."

        self.Books[book] -= 1
        self.Members[id].append(book)
        return "Book issued successfully."

    
    
    
    def Add_Member(self):
        ID = input("ID you want to Give :")
        if ID not in self.Members:
            name = input("Name of the Member:")
            self.Members[ID] = name
            return f"Member is been Added \n--------------------------\n {ID} :  {name}"
        else :
            return "member ID is already Present in the Library"
    
    
    
    
    
    

karve = Library("karve")

# print(karve.book_remove())
print(karve.book_issue())

# print(karve.Add_Member())

