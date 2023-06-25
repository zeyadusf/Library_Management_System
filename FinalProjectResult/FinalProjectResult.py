import string
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import sqlite3
from cBook_info import cBook_info
from cBook_issued import cBook_issue

# define photes to use
img1 = "book_house_dinkytown_copy.jpg"
img2 = "image2.jpg"
img3 = "image3.jpg"

class main_lb(Tk):
    def __init__(self):
        self.wind1 = Tk()
        self.wind1.title("Library Management System ")
        self.wind1.state("zoomed")  # to full screen
        self.ph1 = self.photos(img1)

        # ===================
        self.nameOfDatabase = 'library.db'
        self.db = sqlite3.connect(self.nameOfDatabase)
        self.cr = self.db.cursor()

        self.info = cBook_info(self.nameOfDatabase)
        self.BookIssue = cBook_issue(self.nameOfDatabase)

        self.info.CreateTableBook_info()
        self.BookIssue.CreateTableBook_issue()
        # ===================
        l1 = Button(self.ph1, text="BOOK DATA", fg="white", bg="black",
                    font="Papyrus 22 bold", borderwidth=0, command=self.book)
        l1.place(x=200, y=500)
        l1 = Button(self.ph1, text="STUDENT DATA", fg="white", bg="black",
                    font="Papyrus 22 bold", borderwidth=0, command=self.student)
        l1.place(x=900, y=500)
        self.wind1.mainloop()

    # ================================db================================

    # ----------------------Book Info--------------------------------------------------
    def AddBook_db(self):
        if self.a_id.get() and self.a_title.get() and self.a_title.get() and self.a_author.get() and self.a_genre.get() and self.a_copies.get() and  self.a_loc.get()  !="":  
            if self.a_id.get() > 0:
                self.info.InsertIntoBook_info(self.a_id.get(), self.a_title.get(), self.a_author.get(), self.a_genre.get(),
                                      self.a_copies.get(), self.a_loc.get())
            else :
                messagebox.showerror("ID Error", "It must be greater than 0")

        else:
            messagebox.showerror("Input Error", "Fill in data is required")

    def UpdateBook_db(self):
        if self.a_id.get() and self.a_title.get() and self.a_title.get() and self.a_author.get() and self.a_genre.get() and self.a_copies.get() and self.a_loc.get() != "":
            if self.a_id.get() > 0:
                self.info.UpdateIntoBook_info(self.a_id.get(), self.a_title.get(), self.a_author.get(), self.a_genre.get(),
                                      self.a_copies.get(), self.a_loc.get())
            else:
                messagebox.showerror("ID Error", "It must be greater than 0")

        else:
            messagebox.showerror("Input Error", "Fill in data is required")


    def DeleteBook_db(self):
        self.info.DeleteBook(self.a_id.get())

    # -----------------Book Issue---------------------------------------

    def IssueBook_db(self):
        if self.a_id.get() and self.a_student.get() !="":
            self.BookIssue.AddIssueBook(self.a_id.get(), self.a_student.get())
        else:
            messagebox.showerror("Input Error", "Fill in data is required")
    def ReturnBook_db(self):
        if self.a_id.get() and self.a_student.get() != "":
            self.BookIssue.ReturnIssueBook(self.a_id.get(), self.a_student.get())
        else:
            messagebox.showerror("Input Error", "Fill in data is required")
    # ================================================
    # ---------photos function ----------

    def photos(self, images):
        w = self.wind1.winfo_screenwidth()
        h = self.wind1.winfo_screenheight()
        photo = Image.open(images)
        photo1 = photo.resize((w, h), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(photo1)

        self.cnv = Canvas(self.wind1, width='%d' % w, height='%d' % h)
        self.cnv.grid(column=0, row=0)
        self.cnv.grid_propagate(0)
        self.cnv.create_image(0, 0, anchor=NW, image=photo2)
        self.cnv.image = photo2
        return self.cnv

    # -------use in back btn---------
    def rm(self):
        self.f1.destroy()

    # --------use in main page btn----------
    def mainmenu(self):
        self.wind1.destroy()
        ph1 = main_lb()

    # -----------book data---------------
    def book(self):
        self.ph1.destroy()
        self.ph1 = self.photos(img2)
        btn1 = Button(self.ph1, text="Add Books", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10, command=self.addbook)
        btn1.place(x=12, y=100)
        btn2 = Button(self.ph1, text="Search Books", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10, command=self.search)
        btn2.place(x=12, y=200)
        btn3 = Button(self.ph1, text="All Books", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10, command=self.all_book)
        btn3.place(x=12, y=300)

        btn4 = Button(self.ph1, text="Main Page", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10, command=self.mainmenu)
        btn4.place(x=12, y=550)

        btn5 = Button(self.ph1, text="Delete Book", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10,command=self.deletebook)
        btn5.place(x=1100, y=200)
        btn6 = Button(self.ph1, text="Update Book", bg="black", fg="white",
                      font="Papyrus 22 bold", width=15, padx=10,command=self.updatebook )
        btn6.place(x=1100, y=100)

    def addbook(self):
        self.a_id = IntVar()  # book id
        # self.a_id.get()
        self.a_title = StringVar()
        self.a_author = StringVar()
        self.a_genre = StringVar()
        self.a_copies = IntVar()
        self.a_loc = StringVar()

        # -------frame for books info ------------
        self.f1 = Frame(self.ph1, height=500, width=650, bg='black')
        self.f1.place(x=400, y=100)
        # book id-------
        lb_id = Label(self.f1, text="Book ID : ",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_id.place(x=50, y=45)
        e1 = Entry(self.f1, textvariable=self.a_id, width=45, bg="white")
        e1.place(x=160, y=50)
        # book_title-------
        lb_title = Label(self.f1, text="Book Title :",
                         font="Papyrus 12 bold", fg="white", bg="black")
        lb_title.place(x=40, y=95)
        e2 = Entry(self.f1, textvariable=self.a_title, width=45, bg="white")
        e2.place(x=160, y=103)
        # book author--------
        lb_au = Label(self.f1, text="Book Author :",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_au.place(x=30, y=145)
        e3 = Entry(self.f1, textvariable=self.a_author, width=45, bg="white")
        e3.place(x=160, y=150)
        # book genre--------
        lb_ge = Label(self.f1, text="Book Genre :",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_ge.place(x=35, y=194)
        e4 = Entry(self.f1, textvariable=self.a_genre, width=45, bg="white")
        e4.place(x=160, y=200)
        # book copies--------
        lb_copy = Label(self.f1, text="Book Copies : ",
                        font="Papyrus 12 bold", fg="white", bg="black")
        lb_copy.place(x=30, y=242)
        e5 = Entry(self.f1, textvariable=self.a_copies, width=45, bg="white")
        e5.place(x=160, y=250)
        # book location--------
        lb_loc = Label(self.f1, text="Book Location :",
                       font="Papyrus 12 bold", fg="white", bg="black")
        lb_loc.place(x=25, y=290)
        e6 = Entry(self.f1, textvariable=self.a_loc, width=45, bg="white")
        e6.place(x=162, y=300)

        btn_add2 = Button(self.f1, text="Add", fg="black", bg="purple",
                          width=15, font="Papyrus 10 bold", command=self.AddBook_db)  # Done
        btn_add2.place(x=130, y=400)
        btn_back = Button(self.f1, text="Back", fg="black", bg="purple",
                          width=15, font="Papyrus 10 bold", command=self.rm)
        btn_back.place(x=340, y=400)

    def updatebook(self):
        self.a_id = IntVar()  # book id
        # self.a_id.get()
        self.a_title = StringVar()

        self.a_author = StringVar()
        self.a_genre = StringVar()
        self.a_copies = IntVar()
        self.a_loc = StringVar()
        # -------frame for books info ------------
        self.f1 = Frame(self.ph1, height=500, width=650, bg='black')
        self.f1.place(x=400, y=100)
        # book id-------
        lb_id = Label(self.f1, text="Book ID : ",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_id.place(x=50, y=45)
        e1 = Entry(self.f1, textvariable=self.a_id, width=45, bg="white")
        e1.place(x=160, y=50)
        # book_title-------
        lb_title = Label(self.f1, text="Book Title :",
                         font="Papyrus 12 bold", fg="white", bg="black")
        lb_title.place(x=40, y=95)
        e2 = Entry(self.f1, textvariable=self.a_title, width=45, bg="white")
        e2.place(x=160, y=103)
        # book author--------
        lb_au = Label(self.f1, text="Book Author :",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_au.place(x=30, y=145)
        e3 = Entry(self.f1, textvariable=self.a_author, width=45, bg="white")
        e3.place(x=160, y=150)
        # book genre--------
        lb_ge = Label(self.f1, text="Book Genre :",
                      font="Papyrus 12 bold", fg="white", bg="black")
        lb_ge.place(x=35, y=194)
        e4 = Entry(self.f1, textvariable=self.a_genre, width=45, bg="white")
        e4.place(x=160, y=200)
        # book copies--------
        lb_copy = Label(self.f1, text="Book Copies : ",
                        font="Papyrus 12 bold", fg="white", bg="black")
        lb_copy.place(x=30, y=242)
        e5 = Entry(self.f1, textvariable=self.a_copies, width=45, bg="white")
        e5.place(x=160, y=250)
        # book location--------
        lb_loc = Label(self.f1, text="Book Location :",
                       font="Papyrus 12 bold", fg="white", bg="black")
        lb_loc.place(x=25, y=290)
        e6 = Entry(self.f1, textvariable=self.a_loc, width=45, bg="white")
        e6.place(x=162, y=300)

        btn_update= Button(self.f1, text="Update", fg="black", bg="purple",
                          width=15, font="Papyrus 10 bold", command=self.UpdateBook_db)  # Done
        btn_update.place(x=130, y=400)
        btn_back = Button(self.f1, text="Back", fg="black", bg="purple",
                          width=15, font="Papyrus 10 bold", command=self.rm)
        btn_back.place(x=340, y=400)

    def search(self):

        self.a_id = IntVar()
        self.f1 = Frame(self.ph1, height=500, width=650, bg='black')
        self.f1.place(x=400, y=100)
        l1 = Label(self.f1, text='Book ID : ', font=(
            'Papyrus 10 bold'), bd=2, fg='white', bg='black')
        l1.place(x=160, y=40)
        e1 = Entry(self.f1, width=25, bd=5, bg='white',
                   fg='black', textvariable=self.a_id)
        e1.place(x=260, y=40)
        b1 = Button(self.f1, text='Search', bg='purple', fg="black", font='Papyrus 10 bold',width=9, bd=2, command=self.search1)  # <<<<<<<
        b1.place(x=170, y=200)
        b2 = Button(self.f1, text='Back', bg='purple', fg="black",
                    font='Papyrus 10 bold', width=10, bd=2, command=self.rm)
        b2.place(x=350, y=200)

    def deletebook(self):

        self.a_id = IntVar()
        self.f1 = Frame(self.ph1, height=500, width=650, bg='black')
        self.f1.place(x=400, y=100)
        l1 = Label(self.f1, text='Book ID : ', font=(
            'Papyrus 10 bold'), bd=2, fg='white', bg='black')
        l1.place(x=160, y=40)
        e1 = Entry(self.f1, width=25, bd=5, bg='white',
                   fg='black', textvariable=self.a_id)
        e1.place(x=260, y=40)
        b1 = Button(self.f1, text='Delete', bg='purple', fg="black", font='Papyrus 10 bold',width=9, bd=2, command=self.DeleteBook_db)  # <<<<<<<
        b1.place(x=170, y=200)
        b2 = Button(self.f1, text='Back', bg='purple', fg="black",
                    font='Papyrus 10 bold', width=10, bd=2, command=self.rm)
        b2.place(x=350, y=200)

    def create_tree(self, plc, lists):
        self.tree = ttk.Treeview(
            plc, height=13, column=(lists), show='headings')
        n = 0
        while n is not len(lists):
            self.tree.heading("#" + str(n + 1), text=lists[n])
            self.tree.column("" + lists[n], width=100)
            n = n + 1
        return self.tree

    def all_book(self):
        self.f1 = Frame(self.ph1, bg="black", height=500, width=650)
        self.f1.place(x=400, y=100)
        self.lists = ("BOOK ID", "TITLE", "AUTHOR",
                      "GENRE", "COPIES", "LOCATION")
        self.trees = self.create_tree(self.f1, self.lists)
        self.trees.place(x=25, y=80)

        btn_back = Button(self.f1, text="Back", fg="black", bg="purple",
                          font='Papyrus 10 bold', width=10, command=self.rm)
        btn_back.place(x=250, y=400)
        c = self.db.execute("select* from book_info")
        g = c.fetchall()
        if len(g) !=0:
            for row in g:
                self.trees.insert('',END,values=row)
        self.db.commit()
        #self.db.close()

    def search1(self):
        self.list2 = ("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
        self.trees = self.create_tree(self.f1, self.list2)
        self.trees.place(x=25, y=150)

        try:
            c = self.db.execute("select * from Book_info where book_id=? ",
                             (self.a_id.get(),))
            d = c.fetchall()
            if len(d) != 0:
                for row in d:
                    self.trees.insert("", END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found.")
            self.db.commit()

        except Exception as e:
            messagebox.showinfo(e)


    # -------------student data -------------

    def student(self):
        self.ph1.destroy()
        self.ph1 = self.photos(img2)
        b1 = Button(self.ph1, text="Issue book", font='Papyrus 22 bold',
                    fg='white', bg='Black', width=15, padx=10, command=self.issue)
        b1.place(x=12, y=100)
        b2 = Button(self.ph1, text="Return book", font='Papyrus 22 bold',
                    fg='white', bg='Black', width=15, padx=10, command=self.returnn)
        b2.place(x=12, y=200)
        b3 = Button(self.ph1, text="Student Activity", font='Papyrus 22 bold',
                    fg='white', bg='Black', width=15, padx=10, command=self.activetiy)
        b3.place(x=12, y=300)
        b4 = Button(self.ph1, text="Main Page", font='Papyrus 22 bold',
                    fg='white', bg='Black', width=15, padx=10, command=self.mainmenu)
        b4.place(x=12, y=600)

    def issue(self):
        self.a_id = IntVar()
        self.a_student = IntVar()
        self.f1 = Frame(self.ph1, height=550, width=500, bg='black')
        self.f1.place(x=500, y=100)
        lb1 = Label(self.f1, text="Book ID : ",font="papyrus 15 bold", fg="white", bg="black")
        lb1.place(x=50, y=100)
        e1 = Entry(self.f1, textvariable=self.a_id, bg="white", width=25, bd=4)
        e1.place(x=180, y=100)
        lb2 = Label(self.f1, text="Student ID :  ",font="papyrus 15 bold", fg="white", bg="black")
        lb2.place(x=50, y=150)
        e2 = Entry(self.f1, textvariable=self.a_student,bg="white", width=25, bd=4)
        e2.place(x=180, y=150)
        btn1 = Button(self.f1, text="Issue", bg="purple",fg="black", width=10, bd=3, font='Papyrus 10 bold', command=self.IssueBook_db)  # Done
        btn1.place(x=50, y=250)
        btn2 = Button(self.f1, text="Back", bg="purple", fg="black", width=10, font='Papyrus 10 bold', bd=3, command=self.rm)
        btn2.place(x=200, y=250)

    # -----------retuen book ---------

    def returnn(self):
        self.a_id = IntVar()
        self.a_student = IntVar()

        self.f1 = Frame(self.ph1, height=550, width=500, bg='black')
        self.f1.place(x=500, y=100)

        l1 = Label(self.f1, text='Book ID : ',font='papyrus 15 bold', fg='white', bg='black')
        l1.place(x=50, y=100)
        e1 = Entry(self.f1, width=25, bd=4, bg='white', textvariable=self.a_id)
        e1.place(x=180, y=100)
        l2 = Label(self.f1, text='Student ID : ',font='papyrus 15 bold', fg='white', bg='black')
        l2.place(x=50, y=150)
        e2 = Entry(self.f1, width=25, bd=4, bg='white',textvariable=self.a_student)
        e2.place(x=180, y=150)
        b1 = Button(self.f1, text='Back', font='Papyrus 10 bold',bg='purple', fg='black', width=10, bd=3, command=self.rm)
        b1.place(x=50, y=250)
        b2 = Button(self.f1, text='Return', font='Papyrus 10 bold', bg='purple', fg='black', width=10, bd=3, command=self.ReturnBook_db)
        b2.place(x=200, y=250)
        self.f1.grid_propagate(0)

    def activetiy(self):
        self.a_id = IntVar()
        self.a_student = IntVar()
        self.f1 = Frame(self.ph1, width=500, height=550, bg='black')
        self.f1.place(x=500, y=80)

        self.lists = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.lists)
        self.trees.place(x=50, y=150)

        lb1 = Label(self.f1, text="Book ID :", fg="white",
                    bg="black", font="Papyrus 15 bold")
        lb1.place(x=50, y=30)
        en1 = Entry(self.f1, textvariable=self.a_id,
                    width=20, bd=4, bg="white")
        en1.place(x=280, y=35)
        btn1 = Button(self.f1, text="Search", bg="purple",
                      fg="black", width=10, font='Papyrus 10 bold',command=self.searchact)
        btn1.place(x=40, y=450)
        btn2 = Button(self.f1, text="All", bg="purple",
                      fg="black", width=10, font='Papyrus 10 bold',command=self.searchall)
        btn2.place(x=190, y=450)
        btn3 = Button(self.f1, text="Back", bg="purple", fg="black",
                      width=10, font='Papyrus 10 bold', command=self.rm)
        btn3.place(x=340, y=450)

    def searchact(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2)
        self.trees.place(x=50, y=150)
        #self.db = sqlite3.connect('lib.db')
        #bid = self.a_id.get()

        try:
            c = self.db.execute("select * from book_issue where book_id=? ",
                             (self.a_id.get(),))
            d = c.fetchall()
            if len(d) != 0:
                for row in d:
                    self.trees.insert("", END, values=row)
            else:
                messagebox.showinfo("Error", "Data not found.")
            self.db.commit()

        except Exception as e:
            messagebox.showinfo(e)
        #self.db.close()

    def searchall(self):
        self.list2 = ("BOOK ID", "STUDENT ID", "ISSUE DATE", "RETURN DATE")
        self.trees = self.create_tree(self.f1, self.list2)
        self.trees.place(x=50, y=150)

        try:
            c = self.db.execute("select * from Book_issue")
            d = c.fetchall()
            for row in d:
                self.trees.insert("", END, values=row)

            self.db.commit()

        except Exception as e:
            messagebox.showinfo(e)
        #self.db.close()
#a = main_lb()
#a.mainloop()



app= Tk()
app.title("Library Management System")
app.state("zoomed")
def photos(image,w,h):
    photo = Image.open(image)
    photo1 = photo.resize((w, h), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(photo1)
    cnv = Canvas(app, width='%d'% w, height='%d'% h)
    cnv.grid(row=0, column=0)
    cnv.grid_propagate(0)
    cnv.create_image(0, 0, anchor=NW, image=photo2)
    cnv.image = photo2
    return cnv

w=app.winfo_screenwidth()
h=app.winfo_screenheight()
cnv = photos(img3,w,h)


#--------database---------
def admin_db():
    global db, cur
    db = sqlite3.connect("library.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS `Admins` (admin_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, "
                "username TEXT ,"
                " password TEXT)")
    cur.execute("INSERT INTO `Admins` (username, password) VALUES('admin', 'admin')")
    # cur.execute("SELECT * FROM `Admins` WHERE `password` = 'admin'")
    # print(cur.fetchall())
    db.commit()


def Login():
    admin_db()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cur.execute("SELECT * FROM `Admins` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cur.fetchone() is not None:
            app.destroy()
            a=main_lb()
            a.mainloop()

        else:
            messagebox.showinfo("Error","Invalid username or password.")
            USERNAME.set("")
            PASSWORD.set("")
    # cur.close()
    # db.close()

#---------login page-------

USERNAME = StringVar()
PASSWORD = StringVar()

lbl_title = Label(cnv,text="ADMIN  LOGIN" , font=('Papyrus', 30,'bold'), bg='black' , fg= 'white' , width=15)
lbl_title.place(x =490 , y = 90)

lbl1 = Label(cnv,text=' Username ' , font=('Papyrus', 15,'bold') , bg='black', fg='white' , bd =4)
lbl1.place(x = 500 ,y= 230)
ent_username = Entry(cnv,textvariable=USERNAME , bg='black', fg='white' , font = (14) , bd=4)
ent_username.place(x=650 ,y = 230)
lbl2 = Label(cnv,text=' Password  ' , font=('Papyrus', 15,'bold') , bg='black', fg='white' , bd = 3)
lbl2.place(x= 500 ,y = 330 )
ent_password = Entry(cnv,textvariable=PASSWORD , bg='black', fg='white' , font = (14) , show='*' , bd=4)
ent_password.place(x=650 ,y = 330)

btn_login = Button(cnv,text=" LOGIN ", font=('Papyrus', 15,'bold'),bg='black',fg='white' , width=20,command=Login)
btn_login.place(x=550 , y = 450)
btn_login.bind('<Return>', Login)


app.mainloop()