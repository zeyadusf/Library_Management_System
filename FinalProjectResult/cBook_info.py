import sqlite3
from tkinter import messagebox
from cGeneral import cGeneral


class cBook_info :

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
                f"{'='*20} \n > Error in class cBook_info from Function '__init__' \n{e}\n{'='*20}")

    def CreateTableBook_info(self):
        try:
            self.cr.execute(""" CREATE TABLE IF NOT EXISTS `Book_info`(
                `book_id` INTEGER  PRIMARY KEY ,
                `book_title` TEXT NOT NULL,
                `book_author` TEXT NOT NULL,
                `book_genre` TEXT NOT NULL,
                `book_copies` INTEGER NOT NULL,
                `book_location` TEXT NOT NULL)""")
            self.db.commit()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't Create  Book_info. ")
            print(
                f"{'='*20} \n > Error in class cBook_info from Function 'CreateTableBook_info'\n{e} \n{'='*20}")


    def InsertIntoBook_info(self,id,title,author,gener,copies,location):
        try :
            NumOfCopies=self.generalClass.GetNumOf_book(id) 
            if  NumOfCopies != None:
                NewNumOfCopies = NumOfCopies[0]+copies
                cBook_info.UpdateIntoBook_info(self,id, title, author, gener, NewNumOfCopies, location)

            else:
                self.cr.execute(f""" INSERT INTO `Book_info` (book_id, book_title ,book_author ,book_genre ,book_copies,book_location)
                    VALUES ({id}, '{title}','{author}','{gener}',{copies},'{location}')""")
                self.db.commit()
                messagebox.showinfo("Succeeded", "Successfully added ")
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't add a book. ")
            print(
                f"{'='*20} \n > Error in class cBook_info from Function 'UpdateIntoBook_info' \n{e}\n{'='*20}")


    def UpdateIntoBook_info(self, id, title, author, gener, copies, location):
        try:

            self.cr.execute(
                f""" UPDATE `Book_info` SET book_title='{title}',book_author='{author}',book_genre='{gener}',book_copies={copies} , book_location='{location}' WHERE book_id={id}""")
            self.db.commit()
            messagebox.showinfo("Succeeded", "Successfully update ")

        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database , You can't Update a book. ")
            print(
                f"{'='*20} \n > Error in class cBook_info from Function 'UpdateIntoBook_info' \n{e}\n{'='*20}")


    def DeleteBook(self,id):
        checkDlelete =self.generalClass.DeletePK_isInt('Book_info','book_id',id)
    
        if  checkDlelete:
            messagebox.showinfo("Delete succeeded", " deleted")
        else:
            messagebox.showerror("Delete  failed","book not found")

    def SelectOneBook(self, id): return self.generalClass.SelectOnePK_isInt('Book_info', 'book_id', id)

    def SelectAllBooks(self): return self.generalClass.SelectAll('Book_info')

# =============================================================================
    def GetSumofBooks(self):
        self.cr.execute("SELECT SUM(book_copies) FROM Book_info")
        return self.cr.fetchone()
# 