from tkinter import*
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

root=Tk()
root.geometry('1000x700')
root.title("Bill Management System")
root.resizable(False,False)

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="food"
)        
cursor = conn.cursor()

def insert_data():
    
    
    
    # Retrieve data entered by the user
    a1=dosa.get()
    a2=puri.get()
    a3=khichdi.get()
    a4=dal_rice.get()
    a5=mutton_biryani.get()
    a6=chicken_biryani.get()
    a7=fish_fry.get()
    a8=total_bill.get()
    


    # Define SQL query to insert data into MySQL database
    sql = "INSERT INTO count (dosa, puri, khichdi, dal_rice, mutton_biryani, chicken_biryani, fish_fry, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (a1,a2,a3,a4,a5,a6,a7,a8)

    # Execute SQL query to insert data into MySQL database
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    print(cursor.rowcount, "record inserted.")

    # Show message box to inform the user that the data has been inserted
    messagebox.showinfo("Data Inserted", "Data has been successfully inserted into the database.")
    cursor.close()
    
    display_records()
    
    
    Reset()

def Exit():
    exit=messagebox.askokcancel("","Confirm you want to exit")
    if exit>0:
        root.destroy()
        return

def view_record():
    
    if not datahead.selection():
        mb.showerror('Error!', 'Please select a record to view')
    else:
        current_item = datahead.focus()
        values = datahead.item(current_item)
        selection = values["values"]

        dosa.set(selection[0])
        puri.set(selection[1])
        khichdi.set(selection[2])
        dal_rice.set(selection[3])
        mutton_biryani.set(selection[4])
        chicken_biryani.set(selection[5])  
        fish_fry.set(selection[6])  
        total_bill.set(selection[7]) 

def display_records():
    
    cursor.execute('SELECT * FROM count')
    data = cursor.fetchall()
    datahead.delete(*datahead.get_children())
    for record in data:
        datahead.insert("", END, values=record) 


def Reset():
    entry_dosa.delete(0,END)
    entry_puri.delete(0,END)
    entry_khichdi.delete(0,END)
    entry_dal_rice.delete(0,END)
    entry_mutton_biryani.delete(0,END)
    entry_chicken_biryani.delete(0,END)
    entry_fish_fry.delete(0,END)
    total_bill.set('')
    

def Total():
    try:a1=int(dosa.get())
    except: a1=0
    
    try:a2=int(puri.get())
    except: a2=0
    
    try:a3=int(khichdi.get())
    except: a3=0
    
    try:a4=int(dal_rice.get())
    except: a4=0                        #dosa,puri,khichdi,dal_rice,mutton_biryani,chicken_biryani,fish_fry
    
    try:a5=int(mutton_biryani.get())
    except: a5=0
    
    try:a6=int(chicken_biryani.get())
    except: a6=0
    
    try:a7=int(fish_fry.get())
    except: a7=0
    
    
    #Cost of Each items per quantity
    r1=60*a1
    r2=60*a2
    r3=60*a3
    r4=60*a4
    r5=280*a5
    r6=190*a6
    r7=120*a7

    lbl_total=Label(f2,font=("aria",25,"bold"),text="Total",width=12,fg="#F9F54B",bg="#609EA2")
    lbl_total.place(x=1,y=50)
    
    
    entry_total=Entry(f2,font=("aria",24,"bold"),state="readonly",textvariable=total_bill,bd=6,width=10,bg="lightgreen")
    entry_total.place(x=30,y=100)
       
    
    totalcost=r1+r2+r3+r4+r5+r6+r7
    string_bill=str('%.2f' %totalcost)
    total_bill.set(string_bill)
    
   
#Head Line                                                          (Courier New, Courier, monospace)
Label(text="Food Bill Management",bg="#FEC260",fg="#ffffff", font=("Gabriola",28),width="300",height="1").pack()

 
#Menu Card
f=Frame(root,bg="#E0C097",highlightbackground="#400E32",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",20,"bold"),fg="#000000",bg="#E0C097").place(x=120,y=0)
Label(f,text="Dosa.....Rs.60/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=50)
Label(f,text="Puri.....Rs.60/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=80)
Label(f,text="Khichdi.....Rs.60/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=110)
Label(f,text="Dal rice.....Rs.60/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=140)
Label(f,text="Mutton Biryani.....Rs.280/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=170)
Label(f,text="Chicken Biryani.....Rs.190/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=200)
Label(f,text="Fish Fry.....Rs.120/plate",font=("Lucida calligraphy",10,"bold"),fg="#000000",bg="#E0C097").place(x=10,y=230)


#Bill

f2=Frame(root,bg="#FFE1E1",highlightbackground="black",highlightthickness="1",width=250,height=370)
f2.place(x=735,y=118)

Bill=Label(f2,text="Bill",font=("Courier New",26,"bold"),bg="#FFE1E1",fg="#251749")
Bill.place(x=90,y=10)

# Head of Bill

f6=Frame(root,bg="#C9F4AA",bd=5,height=50,width=300,relief=RAISED)
f6.place(x=332,y=95)


#Entry Work

f1=Frame(root,bg="#C9F4AA",bd=5,height=370,width=300,relief=RAISED)
f1.place(x=330,y=143)

dosa=StringVar()
puri=StringVar()
khichdi=StringVar()
dal_rice=StringVar()      
mutton_biryani=StringVar()
chicken_biryani=StringVar()
fish_fry=StringVar()
total_bill=StringVar()


#Label
lbl_menu=Label(f6,font=("aria",18,"bold"),text="Menu",width=15,fg="#000000",bg="#C9F4AA")
lbl_count=Label(f6,font=("aria",18,"bold"),text="Count",width=9,fg="#000000",bg="#C9F4AA")
lbl_dosa=Label(f1,font=("aria",18,"bold"),text="Dosa",width=15,fg="#243763",bg="#C9F4AA")
lbl_puri=Label(f1,font=("aria",18,"bold"),text="Puri",width=15,fg="#243763",bg="#C9F4AA")
lbl_khichdi=Label(f1,font=("aria",18,"bold"),text="Khichdi",width=15,fg="#243763",bg="#C9F4AA")
lbl_dal_rice=Label(f1,font=("aria",18,"bold"),text="Dal Rice",width=15,fg="#243763",bg="#C9F4AA")
lbl_mutton_biryani=Label(f1,font=("aria",18,"bold"),text="Mutton Biryani",width=15,fg="#243763",bg="#C9F4AA")
lbl_chicken_biryani=Label(f1,font=("aria",18,"bold"),text="Chicken Biryani",width=15,fg="#243763",bg="#C9F4AA")
lbl_fish_fry=Label(f1,font=("aria",18,"bold"),text="Fish Fry",width=15,fg="#243763",bg="#C9F4AA")


lbl_menu.grid(row=1,column=0)
lbl_count.grid(row=1,column=1)
lbl_dosa.grid(row=1,column=0)
lbl_puri.grid(row=2,column=0)
lbl_khichdi.grid(row=3,column=0)
lbl_dal_rice.grid(row=4,column=0)
lbl_mutton_biryani.grid(row=5,column=0)
lbl_chicken_biryani.grid(row=6,column=0)
lbl_fish_fry.grid(row=7,column=0)


#Entry
entry_dosa=Entry(f1,font=("aria",18,"bold"),textvariable=dosa,bd=5,width=8,bg="#FFC3A1")
entry_puri=Entry(f1,font=("aria",18,"bold"),textvariable=puri,bd=5,width=8,bg="#FFC3A1")
entry_khichdi=Entry(f1,font=("aria",18,"bold"),textvariable=khichdi,bd=5,width=8,bg="#FFC3A1")
entry_dal_rice=Entry(f1,font=("aria",18,"bold"),textvariable=dal_rice,bd=5,width=8,bg="#FFC3A1")
entry_mutton_biryani=Entry(f1,font=("aria",18,"bold"),textvariable=mutton_biryani,bd=5,width=8,bg="#FFC3A1")
entry_chicken_biryani=Entry(f1,font=("aria",18,"bold"),textvariable=chicken_biryani,bd=5,width=8,bg="#FFC3A1")
entry_fish_fry=Entry(f1,font=("aria",18,"bold"),textvariable=fish_fry,bd=5,width=8,bg="#FFC3A1")


entry_dosa.grid(row=1,column=1)
entry_puri.grid(row=2,column=1)
entry_khichdi.grid(row=3,column=1)
entry_dal_rice.grid(row=4,column=1)
entry_mutton_biryani.grid(row=5,column=1)
entry_chicken_biryani.grid(row=6,column=1)
entry_fish_fry.grid(row=7,column=1)

#buttons

btn_reset=Button(f1,bd=5,fg="#000000",bg="#C58940",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="#000000",bg="#C58940",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

btn_add=Button(f2,bd=5,fg="#000000",bg="#C58940",font=("ariel",16,'bold'),width=10,text="Add",command=insert_data)
btn_add.place(x=50,y=160)

btn_add=Button(f2,bd=5,fg="#000000",bg="#C58940",font=("ariel",16,'bold'),width=10,text="Exit",command=Exit)
btn_add.place(x=50,y=220)

btn_add=Button(f2,bd=5,fg="#000000",bg="#C58940",font=("ariel",16,'bold'),width=10,text="View",command=view_record)
btn_add.place(x=50,y=280)


#Datashow

# data=LabelFrame(root,bd=5,bg="#E0C097",relief=RIDGE,font=("arial",6,"bold"),text="Data From Database")
# data.place(x=40,y=500,width=910,height=200)
txtdata=Text(root,font=("arial",12,"bold"),width=40,height=15,padx=2,pady=6)
txtdata.place(x=40,y=500,width=910,height=190)

#====================table=============
#=======Scrollbar==========
datahead=ttk.Treeview(txtdata,columns=("dosa","puri","khichdi","dal_rice","mutton_biryani","chicken_biryani","fish_fry","total_bill"))
scroll_y=ttk.Scrollbar(txtdata,orient=VERTICAL,command=datahead.yview)
scroll_x=ttk.Scrollbar(txtdata,orient=HORIZONTAL,command=datahead.xview)
datahead.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
        
scroll_x=ttk.Scrollbar()
scroll_y=ttk.Scrollbar()
        
datahead.heading("dosa",text="Dosa")
datahead.heading("puri",text="Puri")
datahead.heading("khichdi",text="Khichidi")
datahead.heading("dal_rice",text="Dal Rice")
datahead.heading("mutton_biryani",text="Mutton Biryani")
datahead.heading("chicken_biryani",text="Chicken Biryani")
datahead.heading("fish_fry",text="Fish Fry")
datahead.heading("total_bill",text="Total")

datahead["show"]="headings"
        
datahead.column("dosa",width=50,anchor=CENTER)
datahead.column("puri",width=100,anchor=CENTER)
datahead.column("khichdi",width=50,anchor=CENTER)
datahead.column("dal_rice",width=100,anchor=CENTER)
datahead.column("mutton_biryani",width=100,anchor=CENTER)
datahead.column("chicken_biryani",width=100,anchor=CENTER)
datahead.column("fish_fry",width=100,anchor=CENTER)
datahead.column("total_bill",width=100,anchor=CENTER)
    
datahead.pack(fill=BOTH,expand=1)

display_records()

root.mainloop()




#----------Templete-------------#

# from tkinter import *

# root = Tk()
# root.geometry('300x200')
# root.title("Total Calculator")
# root.resizable(False, False)

# def calculate_total():
#     # Get the values entered by the user
#     val1 = int(entry_val1.get())
#     val2 = int(entry_val2.get())
#     val3 = int(entry_val3.get())
#     val4 = int(entry_val4.get())
#     val5 = int(entry_val5.get())
    
#     # Calculate the total
#     total = val1 + val2 + val3 + val4 + val5
    
#     # Update the total label
#     total_label.config(text="Total: " + str(total))
    
# # Create the input fields
# Label(root, text="Value 1").grid(row=0, column=0)
# entry_val1 = Entry(root)
# entry_val1.grid(row=0, column=1)

# Label(root, text="Value 2").grid(row=1, column=0)
# entry_val2 = Entry(root)
# entry_val2.grid(row=1, column=1)

# Label(root, text="Value 3").grid(row=2, column=0)
# entry_val3 = Entry(root)
# entry_val3.grid(row=2, column=1)

# Label(root, text="Value 4").grid(row=3, column=0)
# entry_val4 = Entry(root)
# entry_val4.grid(row=3, column=1)

# Label(root, text="Value 5").grid(row=4, column=0)
# entry_val5 = Entry(root)
# entry_val5.grid(row=4, column=1)

# # Create the calculate button
# Button(root, text="Calculate", command=calculate_total).grid(row=5, column=0)

# # Create the total label
# total_label = Label(root, text="Total: 0")
# total_label.grid(row=5, column=1)

# root.mainloop()

#======Update==========
# import mysql.connector

# # Establish a connection to the database
# mydb = mysql.connector.connect(
#   host="yourhostname",
#   user="yourusername",
#   password="yourpassword",
#   database="yourdatabase"
# )

# # Create a cursor object to execute SQL queries
# mycursor = mydb.cursor()

# # Write the SQL query to update the row
# sql = "UPDATE employees SET first_name = 'John', last_name = 'Doe', email = 'johndoe@example.com', hire_date = '2022-01-01', salary = 50000 WHERE employee_id = 12345"

# # Execute the SQL query
# mycursor.execute(sql)

# # Commit the changes to the database
# mydb.commit()

# # Print the number of rows affected
# print(mycursor.rowcount, "record(s) updated")


#----------Templete-------------#
