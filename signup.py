from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import re
root1=Tk()
root1.title("ONE")
root1.geometry("1200x700+20+30")
root1.resizable(False,False)
##-----------------------------------------------------------------------------------------------------------------------------------##
def signup():
    v10=StringVar()
    v10=v6.get()
    v11=v5.get()
    validate='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(validate,v4.get())):   
        pass   
    else:   
        messagebox.showerror("Error","Invalid Email")
    if(v1.get()=="" or v2.get()=="" or cmb_gender.get()=="Select" or v4.get()=="" or v5.get()=="" or v6.get()=="" or v7.get()=="" or v8.get()=="" or v9.get()==""):
        messagebox.showerror("Error","All fields are mandatory")
    elif(len(v10)<6):
        messagebox.showerror("Error","Password must be greater than six.")
    elif(v6.get()!=v7.get()):
        messagebox.showerror("Error","Password must be same")
    elif(not(v11.isdigit()) or len(v11)!=10):
        messagebox.showerror("Error","Enter correct mobile number")
    else:
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
            cur=con.cursor()
            cur.execute("insert into Login_details() values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (v1.get(),v2.get(),cmb_gender.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Successfully Signed Up")
            root1.destroy()
            import login
        except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}")
def back_fn():
    root1.destroy()
    import login
def reset_fn():
    f_n.delete(0,END)
    l_n.delete(0,END)
    cmb_gender.current(0)
    e_mail.delete(0,END)
    Phoneno.delete(0,END)
    pass_text.delete(0,END)
    passc_text.delete(0,END)
    State_t.delete(0,END)
    city_t.delete(0,END)
##-----------------------------------------------------------------------------------------------------------------------------------##

bg_image=ImageTk.PhotoImage(file="backg.jpg")
bg_label=Label(root1,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
signup_frame=Frame(root1,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=500,width=480)
Detail_label=Label(signup_frame,text="Enter Your Details",font=("Impact",35,"bold"),fg="white",bg="orange").place(x=115,y=65)
l1=Label(signup_frame,text="First Name",font=(15),bg="white").place(x=110,y=170)
v1=StringVar()
f_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
f_n.place(x=300,y=170)
l2=Label(signup_frame,text="Last Name",font=(15),bg="white").place(x=110,y=205)
v2=StringVar()
l_n=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
l_n.place(x=300,y=205)
gender_label=Label(signup_frame,text="Gender",font=(15),bg="white").place(x=110,y=240)
cmb_gender=ttk.Combobox(signup_frame,font=("times new roman",15),state="readonly",justify="center")
cmb_gender['values']=("Select","Male","Female","Other")
cmb_gender.place(x=300,y=240,width=200)
cmb_gender.current(0)
e_mail_label=Label(signup_frame,text="E-mail",font=(15),bg="white").place(x=110,y=275)
v4=StringVar()
e_mail=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v4)
e_mail.place(x=300,y=275)
Phone_label=Label(signup_frame,text="Mobile No.",font=(15),bg="white").place(x=110,y=310)
v5=StringVar()
Phoneno=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v5)
Phoneno.place(x=300,y=310)
Password_label=Label(signup_frame,text="Password",font=(15),bg="white").place(x=110,y=345)
v6=StringVar()
pass_text=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v6)
pass_text.place(x=300,y=345)
Passwordc_label=Label(signup_frame,text="Confirm Password",font=(15),bg="white").place(x=110,y=380)
v7=StringVar()
passc_text=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v7)
passc_text.place(x=300,y=380)
State_l=Label(signup_frame,text="State",font=(15),bg="white").place(x=110,y=415)
v8=StringVar()
State_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v8)
State_t.place(x=300,y=415)
City_l=Label(signup_frame,text="City",font=(15),bg="white").place(x=110,y=450)
v9=StringVar()
city_t=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v9)
city_t.place(x=300,y=450)
submit_button=Button(signup_frame,text="Sign Up",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=signup).place(x=390,y=520)
reset_button=Button(signup_frame,text="Reset",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=reset_fn).place(x=300,y=520)
back_button=Button(signup_frame,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn).place(x=215,y=520)
root1.mainloop()