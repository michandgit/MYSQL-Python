import mysql.connector as ms
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


window=Tk()
window.geometry("800x500")
window.title("HOSPITAL FACILITY")
label=Label(window,text="WELCOME TO OUR HOSPITAL FACILITY",bg="blue",relief="solid",font=("cooper black",28,"bold"))
label.pack(fill=BOTH,padx=2,pady=10)
label1=Label(window,text="Our hospital facility focuses on providing a good hospital and good health to you.",font=("baskerville old face",16))
label1.pack()
label2=Label(window,text="It will provide you many choices and hospitals of DELHI and UP.",font=("baskerville old face",16))
label2.pack()
def action():
    newwindow=Toplevel(window)
    newwindow.title("Registration")
    newwindow.geometry("500x250")
    lbl=Label(newwindow,text="REGISTER THE FORM",bg="black",fg="white",font=("baskerville old face",18,"bold"))
    lbl.grid(row=0,column=1)
    Name=ttk.Label(newwindow,text="Enter your Name::")
    Name.grid(row=1,column=0,sticky=tk.W)
    Email=ttk.Label(newwindow,text="Enter your Email::")
    Email.grid(row=2,column=0,sticky=tk.W)
    Age=ttk.Label(newwindow,text="Enter your age::")
    Age.grid(row=3,column=0,sticky=tk.W)
    BG=Label(newwindow,text="Enter your blood group::")
    BG.grid(row=4,column=0,sticky=tk.W)
    gender=ttk.Label(newwindow,text="Enter your gender::")
    gender.grid(row=5,column=0,sticky=tk.W)
    Name_var = tk.StringVar()
    Name=ttk.Entry(newwindow,width=16,textvariable=Name_var)
    Name.grid(row=1,column=1)
    Name.focus()
    Email_var = tk.StringVar()
    Email=ttk.Entry(newwindow,width=16,textvariable=Email_var)
    Email.grid(row=2,column=1)
    Age_var = tk.StringVar()
    Age=ttk.Entry(newwindow,width=16,textvariable=Age_var)
    Age.grid(row=3,column=1)
    BG_var=tk.StringVar()
    BG=ttk.Entry(newwindow,width=16,textvariable=BG_var)
    BG.grid(row=4,column=1)
    gender_var=tk.StringVar()
    gender_box=ttk.Combobox(newwindow,width=14,textvariable=gender_var,state='readonly')
    gender_box["values"]=("Male","Female","Others")
    gender_box.current(1 )
    gender_box.grid(row=5,column=1)
    usertype=tk.StringVar()
    checkbtn_var=tk.IntVar()
    checkbtn=ttk.Checkbutton(newwindow,text='check if u want to explore our hospital facility',variable=checkbtn_var)
    checkbtn.grid(row=7,columnspan=3)
    def com():
        username= Name_var.get()
        useremail=Email_var.get()
        userage=Age_var.get()
        userBG=BG_var.get()
        print("Patient's name:",username)
        print("Patient's email:",useremail)
        print("Patient's age:",userage)
        print("Patient's blood group:",userBG)
        user_gender=gender_var.get()
        user_type=usertype.get()
        if checkbtn_var.get()==0:
            checked='No'
        else:
            checked='Yes'
            print(user_gender,user_type,":",checked)
        con=ms.connect(host="localhost",user="root",passwd="12345678",database='assign')
        if con.is_connected():
            print("successfuly connected")
        cur=con.cursor()
        query="insert into patientdat(NAME,EMAIL,AGE,GENDER,BLOOD_GROUP) values ('{name}','{email}',{age},'{gender}','{blood}')".format(name=username,email=useremail,age=userage,gender=user_gender,blood=userBG)
        cur.execute(query)
        con.commit()
        messagebox.showinfo("submitted","You have been registered successfully")
        
    submit=ttk.Button(newwindow,text="Submit",command=com)
    submit.grid(row=8,column=1)

#list of hospital
def lists():
    newwindow2=Tk()
    global hospital_var,hospital_box
    global department_var,department_box
    newwindow2.geometry("500x500")
    newwindow2.title("HOSPITALS")
    lb=Label(newwindow2,text="SELECT THE HOSPITALS ",bg="skyblue",fg="black",font=("algerian",20,"bold"))
    lb.grid(row=1,column=2)
    hospital_var=tk.StringVar()
    hospital_box=ttk.Combobox(newwindow2,width=25,textvariable=hospital_var,state='readonly' )
    hospital_box["values"]=("PHC","ABA HOSPITAL","HOLY HOSPITAL","NEO HOSPITAL","TESTS HOSPITAL","BHEEM RAV AMBEDKAR","METRO HOSPITAL","FORTIS HOSPITAL","LOK NAYAK HOSPITAL","GOVERNMENT HOSPITAL")
    hospital_box.current(1 )
    hospital_box.grid(row=2,column=2)
    department=Label(newwindow2,text="SELECT THE DEPARTMENT NAME",bg="skyblue",fg="black",font=("algerian",20,"bold"))
    department.grid(row=3,column=2)
    department_var=tk.StringVar()
    department_box=ttk.Combobox(newwindow2,width=32,textvariable=department_var,state='readonly' )
    department_box["values"]=("ANESTHETICS","cardiology","ENT","NEUROLOGY","ONCOLOGY","ORTHOPEDICS","GYNECOLOGY","GASTROENTEROLOGY","HEMATOLOGY","UROLOGY")
    department_box.current(7)
    department_box.grid(row=4,column=2)
    def selection():
        nwd=Toplevel(newwindow2)
        nwd.geometry("1000x300")
        nwd.title("appointments")
        e=hospital_box.get()
        f=department_box.get()
        x=("Welcome to "+str(e))
        lbl=Label(nwd,text=x,font=("Bodoni MT",26),bg="black",fg="white")
        lbl.grid(row=0,column=0)
        con=ms.connect(host="localhost",user="root",passwd="12345678",database='assign')
        cur=con.cursor()
        qur=("select * from "+str(f))
        cur.execute(qur)
        r=cur.fetchall()
        frm=Frame(nwd)
        frm.grid(row=2,column=0)
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height="7")
        tv.grid(row=3,column=0)
        tv.heading(1,text="SNO")
        tv.heading(2,text="DOCTOR_NAME")
        tv.heading(3,text="CONTACT_NO")
        tv.heading(4,text="MORN_TIMING")
        tv.heading(5,text="EVEN_TIMING")
        for i in r:
            tv.insert('','end',values=i)
        def select_record():
            #grab record nmuber
            s=ttk.Treeview.focus()
            #grab record values
            values=ttk.Treeview.item(s,'values')
            Label(nwd,text='values',font=("baskerville old face",16)).grid(row=6,column=0)
        def selectitem():
            tv.bind("<Double-1>",select_record)
            Label(nwd,text="You successfully got an appointment!!...",font=("baskerville old face",16)).grid(row=7,column=0)
            
        btn=Button(nwd,text="Get your appointment",bg="pink",fg="black",relief=GROOVE,font=("arial",10,"bold"),command=selectitem)
        btn.grid(row=5,column=0)
    but=Button(newwindow2,text="Selected",bg="pink",fg="black",relief=GROOVE,font=("arial",10,"bold"),command=selection)
    but.grid(row=5,column=2)


button1=Button(window,text="Register",bg="pink",fg="black",relief=GROOVE,font=("arial",10,"bold"),command=action)
button1.pack()
label3=Label(window,text="Explore the hospitals",font=("baskerville old face",16))
label3.pack()
button2=Button(window,text="Explore",bg="pink",fg="black",relief=GROOVE,font=("arial",10,"bold"),command=lists)
button2.pack()
#hospital table and departments

window.mainloop()
