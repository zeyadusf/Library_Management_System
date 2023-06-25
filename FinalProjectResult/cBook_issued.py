import sqlite3
from cBook_info import cBook_info
from cGeneral import cGeneral
from tkinter import messagebox

class cBook_issue:

    def __init__(self, dataBaseName):
        try:
            self.dataBaseName = dataBaseName
            # Create DB and Connection
            self.db = sqlite3.connect(f"{dataBaseName}")
            # Setting Up The Cursor
            self.cr = self.db.cursor() 
            # Create Object From Cgeneral Class
            self.generalClass = cGeneral(f"{dataBaseName}")
        except Exception as e:
            messagebox.showerror(
                "Connction Filed", f"Connection Failed with database.")
            print(
                f"{'='*20} \n > Error in class cBook_issue from Function '__init__' \n{e}\n{'='*20}")

    def CreateTableBook_issue(self):
        try:
            self.cr.execute(
                """Create Table IF NOT EXISTS `Book_issue` (
                    `book_id` INTEGER  NOT NULL,
                    `student_id` INTEGER NOT NULL,
                    `issue_date` date not null,
                    `return_date` date not null,
                    FOREIGN KEY(book_id) REFERENCES Book_info(book_id)
                )""")
            self.db.commit()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't Create  Book_issue. ")
            print(
                f"{'='*20} \n > Error in class cBook_issue from Function 'CreateTableBook_issue'\n{e} \n{'='*20}")

    def AddIssueBook(self,book_id,student_id):
        try:
            # Check if exist or not 
            book = cBook_info(self.dataBaseName)

            issueBook=book.SelectOneBook(book_id)

            if issueBook !=None  and issueBook[4] > 0 and self .SelectOneIssueBook(student_id)==None:
                self.cr.execute(
                f"insert into `Book_issue` values({book_id},{student_id},date('now'),date('now','+7 day'))")
                self.db.commit()  
                # update copies -1
                self.cr.execute(
                    f""" UPDATE `Book_info` SET book_copies=book_copies-1 WHERE book_id={book_id}""")
                self.db.commit()

                messagebox.showinfo(
                    "Succeeded", "Successfully added ")

            else:
                messagebox.showerror(
                    "Addition failed ", "this book does not exist or All copies are borrowed ,\n or The same student borrowed the same book")
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't add into  Book_issue. ")
            print(
                f"{'='*20} \n > Error in class cBook_issue from Function 'AddIssueBook'\n{e} \n{'='*20}")
        

    def ReturnIssueBook(self,book_id,student_id):
        try:
            if self.SelectOneIssueBook(book_id) != None:
                self.cr.execute(f"DELETE FROM `Book_issue` WHERE book_id ={book_id} AND student_id ={student_id}")
                self.db.commit()
                # update copies +1
                self.cr.execute(
                    f""" UPDATE `Book_info` SET book_copies=book_copies+1 WHERE book_id={book_id}""")
                self.db.commit()
            
                messagebox.showinfo(
                    "Succeeded", "The book was returned successfully")
            
            else:
                messagebox.showerror(
                    "Book Not Found", "There is no book or student with this ID to return")
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't Return  Book_issue. ")
            print(
                f"{'='*20} \n > Error in class cBook_issue from Function 'ReturnIssueBook'\n{e} \n{'='*20}")

    def SelectOneIssueBook(self,  book_id):
        self.cr.execute(
            f"SELECT * FROM `Book_issue` WHERE  book_id ={book_id}  ")
        return self.cr.fetchone()

    def SelectAllIssueBooks(self):
        return self.generalClass.SelectAll('Book_issue')
    
