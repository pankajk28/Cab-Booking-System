from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
root5=Tk()
root5.title("ONE")
root5.geometry("700x500+300+170")
root5.resizable(False,False)
def submit_fn():
    if(v4.get()=="" or v1.get()=="" or v2.get()==""):
        messagebox.showerror("Error","All Fields Are Mandatory")
    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
            cur=mydb.cursor() 
            cur.execute("select * from Login_details where E_mail=%s",(v4.get(),))
            result=cur.fetchone()
            print(result)
            if result==None:
                messagebox.showerror("Error","User Not Found")
            else:
                curr2=mydb.cursor()
                curr2.execute("update login_details set password=%s,Confirm_password=%s where E_mail=%s",(v1.get(),v2.get(),v4.get()))
                mydb.commit()
                messagebox.showinfo("Sucess","Password successfully updated")
            mydb.close()
            root5.destroy()
            import login
        except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}") 

bg_image=ImageTk.PhotoImage(file="backg.jpg")
bg_label=Label(root5,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
signup_frame=Frame(root5,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=280,width=480)
Detail_label=Label(signup_frame,text="Change Password",font=("Impact",30,"bold"),fg="white",bg="orange").place(x=115,y=70)
e_mail_label=Label(signup_frame,text="Enter Your E-mail",font=(15),bg="white").place(x=110,y=160)
v4=StringVar()
e_mail=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v4)
e_mail.place(x=300,y=160)
np_label=Label(signup_frame,text="New Password",font=(15),bg="white").place(x=110,y=195)
v1=StringVar()
np=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
np.place(x=300,y=195)
npc_label=Label(signup_frame,text="Confirm Password",font=(15),bg="white").place(x=110,y=230)
v2=StringVar()
npc=Entry(signup_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
npc.place(x=300,y=230)
submit_button=Button(signup_frame,text="Submit",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=submit_fn).place(x=390,y=300)

root5.mainloop()