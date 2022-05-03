from tkinter import *
from tkinter import ttk
import mysql.connector


class StudentData:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=5, relief=RIDGE,
                      font=("times new roman", 40, "bold"), bg="#17F5AE")
        title.pack(side=TOP, fill=X)

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gander_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        entry_manage_Frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        entry_manage_Frame1.place(x=20, y=100, width=450, height=575)

        fm1_title = Label(entry_manage_Frame1, text="Manage student", bg="crimson", fg="white",
                          font=("times new roman", 30, "bold"))
        fm1_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(entry_manage_Frame1, text="Roll no.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=5, padx=20, sticky=W)

        txt_Roll = Entry(entry_manage_Frame1, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky=W)

        lbl_name = Label(entry_manage_Frame1, text="Name", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=5, padx=20, sticky=W)

        txt_name = Entry(entry_manage_Frame1, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=SUNKEN)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky=W)

        lbl_Email = Label(entry_manage_Frame1, text="Email", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=5, padx=20, sticky=W)

        txt_Email = Entry(entry_manage_Frame1, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=SUNKEN)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky=W)

        lbl_Gander = Label(entry_manage_Frame1, text="Gander", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Gander.grid(row=4, column=0, pady=5, padx=20, sticky=W)

        combo_gander = ttk.Combobox(entry_manage_Frame1, textvariable=self.gander_var,
                                    font=("times new roman", 13, "bold"), state='readonly')
        combo_gander['value'] = ("male", "female", "other")
        combo_gander.grid(row=4, column=1, padx=20, pady=10)

        lbl_Contact = Label(entry_manage_Frame1, text="Contact", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=5, padx=20, sticky=W)

        txt_Contact = Entry(entry_manage_Frame1, textvariable=self.contact_var, font=("times new roman", 15, "bold"),
                            bd=5, relief=SUNKEN)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky=W)

        lbl_B_O_D = Label(entry_manage_Frame1, text="B.O.D", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_B_O_D.grid(row=6, column=0, pady=5, padx=20, sticky=W)

        txt_B_O_D = Entry(entry_manage_Frame1, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=SUNKEN)
        txt_B_O_D.grid(row=6, column=1, pady=10, padx=20, sticky=W)

        lbl_Address = Label(entry_manage_Frame1, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=5, padx=20, sticky=W)

        self.txt_Address = Text(entry_manage_Frame1, width=30, height=4, font=("", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky=W)

        # button frame----------------->
        btn_Frame = Frame(entry_manage_Frame1, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                              pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                              pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        data_manage_Frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="red")
        data_manage_Frame2.place(x=500, y=100, width=800, height=575)

        lbl_Search = Label(data_manage_Frame2, text="Search", bg="red", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=15, sticky=W)

        combo_Search = ttk.Combobox(data_manage_Frame2, font=("times new roman", 13, "bold"), state='readonly')
        combo_Search['value'] = ("Roll", "Name", "Contact")
        combo_Search.grid(row=0, column=1, padx=15, pady=10)

        txt_Search = Entry(data_manage_Frame2, font=("times new roman", 15, "bold"), bd=3, relief=SUNKEN)
        txt_Search.grid(row=0, column=2, pady=10, padx=15, sticky=W)

        Search_btn = Button(data_manage_Frame2, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(data_manage_Frame2, text="Show All", width=10, pady=5).grid(row=0, column=4, padx=10,
                                                                                         pady=10)

        Tabel_Frame = Frame(data_manage_Frame2, bd=4, relief=RIDGE, bg="crimson")
        Tabel_Frame.place(x=15, y=70, width=760, height=495)

        scroll_x = Scrollbar(Tabel_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Tabel_Frame, orient=VERTICAL)
        self.Student_tabel = ttk.Treeview(Tabel_Frame,
                                          columns=("roll", "name", "email", "gander", "contact", "dob", "Address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_tabel.xview)
        scroll_y.config(command=self.Student_tabel.yview)
        self.Student_tabel.heading("roll", text="Roll No.")
        self.Student_tabel.heading("name", text="Name")
        self.Student_tabel.heading("email", text="Email")
        self.Student_tabel.heading("gander", text="Gander")
        self.Student_tabel.heading("contact", text="Contact")
        self.Student_tabel.heading("dob", text="dob")
        self.Student_tabel.heading("Address", text="Address")
        self.Student_tabel['show'] = 'headings'
        self.Student_tabel.column('roll', width=105)
        self.Student_tabel.column('name', width=105)
        self.Student_tabel.column('email', width=105)
        self.Student_tabel.column('gander', width=105)
        self.Student_tabel.column('contact', width=105)
        self.Student_tabel.column('dob', width=105)
        self.Student_tabel.column('Address', width=105)
        self.Student_tabel.pack(fill=BOTH, expand=1)
        self.Student_tabel.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_student(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gander_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_Address.get("1.0", END)
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select *from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_tabel.delete(*self.Student_tabel.get_children())
            for row in rows:
                self.Student_tabel.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gander_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, even):
        cursor_row = self.Student_tabel.focus()
        contents = self.Student_tabel.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gander_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update student set Name=%s,Email=%s,gander=%s,contact=%s,DOB=%s,Address=%s where roll_no=%s", (
            self.Name_var.get(),
            self.Email_var.get(),
            self.gander_var.get(),
            self.contact_var.get(),
            self.DOB_var.get(),
            self.txt_Address.get("1.0", END),
            self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute(f'delete from student where roll_no={self.Roll_No_var.get()}')
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


root = Tk()
obj = StudentData(root)
root.mainloop()