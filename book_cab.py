from random import randint
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import re
root2=Tk()
root2.title("ONE")
root2.geometry("1000x700+300+50")
root2.resizable(False,False)

def reset_fn():
    txt_email.delete(0,END)
    pickup.delete(0,END)
    drop.delete(0,END)
    hrs_text.delete(0,END)
    min_text.delete(0,END)
    amount.delete(0,END)
    tax.delete(0,END)
    insurance.delete(0,END)
    total.delete(0,END)
    cmb_insurance.current(0)
def  back_fn():
    root2.destroy()
    import SEL_CHOICE
def calculate_fn():
    dummy_insurance=5
    dummy_charge=randint(150,2000)
    if pickup.get()=="" or drop.get()=="Select" or cmb_insurance.get()=="Select":
        messagebox.showerror("Error","Please fill all the details.")
    elif types.get()==1:
        amount.delete(0,END)
        amount.insert(END,dummy_charge)
    elif types.get()==2:
        dummy_charge=dummy_charge+100
        amount.delete(0,END)
        amount.insert(END,dummy_charge)
    elif cmb_insurance.get()=="Yes":
        insurance.delete(0,END)
        insurance.insert(0,dummy_insurance)
        
    elif cmb_insurance.get()=="No":
            insurance.delete(0,END)
            insurance.insert(0,dummy_insurance)
    else:
        messagebox.showerror("Error","Please Fill all details.")
    
    dummy_tax=0.05*dummy_charge
    
    total_charge=dummy_charge+dummy_tax+dummy_insurance
    tax.delete(0,END)
    tax.insert(0,dummy_tax)
    insurance.delete(0,END)
    insurance.insert(0,dummy_insurance)
    total.delete(0,END)
    total.insert(0,total_charge)
def book_fn():
    validate='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(validate,v1.get())):   
        pass   
    else:   
        messagebox.showerror("Error","Invalid Email")   
    if(v1.get()=="" or pickup.get()=="" or drop.get()=="Select"  or hrs_text.get()=="" or min_text.get()=="" or cmb_insurance.get()=="Select"):
        messagebox.showerror("Error","All fields are mandatory")
    else:
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
            cur=con.cursor()
            cur.execute("insert into booking_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (pickup.get(),drop.get(),cal.get_date(),hrs_text.get(),min_text.get(),cmb_insurance.get(),amount.get(),tax.get(),insurance.get(),total.get(),v1.get()))
            con.commit()
            messagebox.showinfo("Success","Cab Successfully Booked")
        except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}")
    
def exit_fn():
    root2.destroy()


bg_image=ImageTk.PhotoImage(file="backg.jpg")
bg_label=Label(root2,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
your_email=Label(root2,text="Enter Your E-mail",font=20,bg="white").place(x=85,y=75)
v1=StringVar()
txt_email=Entry(root2,font=("times new roman",15),bg="white",textvariable=v1)
txt_email.place(x=275,y=75,width=250)
frame2=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=480,height=100,width=480)
l3=Label(frame2,text="Cab Type",font=("Impact",20,"bold"),bg="orange",fg="white").place(x=120,y=460)
types=IntVar()
gender_label=Label(frame2,text="Select Cab Type",font=(15),bg="white").place(x=110,y=520)
mini=Radiobutton(frame2,text="Mini(Two Seater)",font=("times new roman",15),variable=types,value=1,bg="white")
mini.place(x=300,y=500)
prime=Radiobutton(frame2,text="Prime(Four Seater)",font=("times new roman",15),variable=types,value=2,bg="white")
prime.place(x=300,y=535)
frame3=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=320,y=600,height=75,width=410) 
frame4=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=150,height=275,width=480)
l5=Label(frame4,text="Booking Details",font=("Impact",20,"bold"),bg="orange",fg="white").place(x=120,y=130)
l4=Label(frame4,text="Pickup Location",font=(15),bg="white").place(x=110,y=190)
pickup=Entry(frame4,font=("times new roman",15),bg="lightgray")
pickup.place(x=300,y=190)
l6=Label(frame4,text="Drop Location",font=(15),bg="white").place(x=110,y=225)
drop=Entry(frame4,font=("times new roman",15),bg="lightgray")
drop.place(x=300,y=225)
l7=Label(frame4,text="Pickup Date",font=(15),bg="white").place(x=110,y=260)
cal = DateEntry(frame4, width= 16, background= "magenta3", foreground= "white",bd=2)
cal.place(x=300,y=260,height=30,width=200)
l8=Label(frame4,text="Pickup Time",font=(15),bg="white").place(x=110,y=295)
hrs_text=Entry(frame4,font=("times new roman",15),bg="lightgray")
hrs_text.place(x=300,y=295,width=85)
l9=Label(frame4,text="hrs",font=(15),bg="white").place(x=400,y=295)
min_text=Entry(frame4,font=("times new roman",15),bg="lightgray")
min_text.place(x=450,y=295,width=55)
l9=Label(frame4,text="min",font=(15),bg="white").place(x=510,y=295)
l10=Label(frame4,text="Insurance",font=(15),bg="white").place(x=110,y=330)
cmb_insurance=ttk.Combobox(frame4,font=("times new roman",15),state="readonly",justify="center")
cmb_insurance['values']=("Select","Yes","No")
cmb_insurance.place(x=300,y=330,width=200)
cmb_insurance.current(0)

resetbutt=Button(frame3,text="Reset",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=reset_fn)
resetbutt.place(x=400,y=610,width=80)
back_button=Button(frame3,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn)
back_button.place(x=500,y=610,width=80)
Exit_button=Button(frame3,text="Exit",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=exit_fn)
Exit_button.place(x=600,y=610,width=80)


frame5=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=600,y=480,height=100,width=340)
book_button=Button(frame5,text="Book",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=book_fn)
book_button.place(x=730,y=500) 

frame6=Frame(root2,bg="white",highlightbackground="grey",highlightthickness=3).place(x=600,y=150,height=275,width=340)
l10=Label(text="Amount Details",font=("Impact",20,"bold"),fg="white",bg="orange").place(x=620,y=130)
Travel_amount=Label(frame6,text="Travel Amount",font=(15),bg="white").place(x=620,y=190)
amount=Entry(frame6,font=("times new roman",15),bg="lightgray")
amount.place(x=800,y=190,width=120)
Tax_amount=Label(frame6,text="Tax Amount",font=(15),bg="white").place(x=620,y=225)
tax=Entry(frame6,font=("times new roman",15),bg="lightgray")
tax.place(x=800,y=225,width=120)
ins_amount=Label(frame6,text="Insurance Amount",font=(15),bg="white").place(x=620,y=260)
insurance=Entry(frame6,font=("times new roman",15),bg="lightgray")
insurance.place(x=800,y=260,width=120)
total_amount=Label(frame6,text="Total Amount",font=(15),bg="white").place(x=620,y=295)
total=Entry(frame6,font=("times new roman",15),bg="lightgray")
total.place(x=800,y=295,width=120)
cal_button=Button(frame6,text="Calculate",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=calculate_fn).place(x=710,y=350)
root2.mainloop()