import sqlite3
from tkinter import messagebox


class cGeneral:

    def __init__(self, nameOfDataBase):
        """ Constractor used to connect to database and take name of database  as input"""
        try:
            self.db = sqlite3.connect(f"{nameOfDataBase}")
            self.cr = self.db.cursor()
        except Exception as e:
            messagebox.showerror(
                "Connction Filed", f"Connection Failed with database.\n\t\t{e}")

    def DeletePK_isString(self, table, PK, PkValue):
        """ Delete function used to delete any 'Row ' in any table in database and take input (name of table , primary key ,value of primary key) """
        try:
            mydata = self.SelectOnePK_isString(table, PK, PkValue)
            if mydata != None:
                self.cr.execute(
                    f"Delete FROM `{table}` WHERE {PK}='{PkValue}'")
                self.db.commit()
                return True  # return >> to check in gui deleted done or not
            else:
                return False  # return >> to check in gui deleted done or not
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e}")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'DeletePK_isInt' \n{'='*20}")

    def DeletePK_isInt(self, table, PK, PkValue):
        """ Delete function used to delete any ' ' in any table in database and take input (name of table , primary key ,value of primary key) """
        try:
            mydata = self.SelectOnePK_isInt(table, PK, PkValue)
            if mydata != None:
                self.cr.execute(
                    f"Delete FROM `{table}` WHERE {PK}={PkValue}")
                self.db.commit()

                return True  # return >> to check in gui deleted done or not
            else:
                return False  # return >> to check in gui deleted done or not
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e}")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'DeletePK_isInt' \n{'='*20}")

    def SelectOnePK_isString(self, table, PK, PkValue):
        """ select function used to select any row in any table in database and take input (name of table , primary key(text) ,value of primary key) """
        try:
            self.cr.execute(f"SELECT * FROM `{table}` WHERE {PK}='{PkValue}' ")
            return self.cr.fetchone()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e}")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'SelectOnePK_isString' \n{'='*20}")

    def SelectOnePK_isInt(self, table, PK, PkValue):
        """ select function used to select any row in any table in database and take input (name of table , primary key(int) ,value of primary key) """
        try:
            self.cr.execute(f"SELECT * FROM `{table}` WHERE {PK}={PkValue} ")
            return self.cr.fetchone()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e} ")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'SelectOnePK_isInt' \n{'='*20}")

    def SelectAll(self, table):
        try:
            self.cr.execute(f"SELECT * FROM `{table}`")
            return self.cr.fetchall()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e} ")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'SelectAll' \n{'='*20}")

    def GetNumOf_book(self, id):
        try:
            self.cr.execute(
                f"SELECT `book_copies` FROM `Book_info` WHERE `book_id`={id}")
            return self.cr.fetchone()
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e} ")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function 'GetnumOf_book' \n{'='*20}")

    def __del__(self):

        try:
        
            self.db.commit()
            self.db.close()
            print("close Connection 'Cgeneral Class'")
        except Exception as e:
            messagebox.showerror(
                "DataBase Error", f"Error in database .\n\t\t{e} ")
            print(
                f"{'='*20} \n > Error in class cGeneral from Function '__del__' \n{'='*20}")
