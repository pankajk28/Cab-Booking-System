from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
root=Tk()
root.title("ONE")
root.geometry("1000x600+100+50")
root.resizable(False,False)
def validate():
    v=v2.get()
    if(v1.get()=="" or v2.get()==""):
        messagebox.showerror("Error","All fields are required")
    else:
        try:
            mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
            cur=mydb.cursor()
            cur.execute("select * from Login_details where E_mail=%s and password=%s",(v1.get(),v2.get()))
            result=cur.fetchone()
            print(result)
            if result==None:
                messagebox.showerror("Error","User Not Found")
            else:
                root.destroy()
                import SEL_CHOICE
            mydb.close()
        except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}")
           

def sign_up():
    root.destroy()
    import signup
def forgot_fn():
    root.destroy()
    import forgot_pass    
bg=ImageTk.PhotoImage(file="backg.jpg")
bg_image=Label(image=bg).place(x=0,y=0,relwidth=1,relheight=1)
login_frame=Frame(root,bg="white",highlightbackground="grey",highlightthickness=3).place(x=100,y=150,height=350,width=300)
login_text=Label(login_frame,text="Login Here",font=("Impact",35,"bold"),fg="white",bg="orange").place(x=120,y=120)
username=Label(login_frame,text="Email ID",font=("goudy old style",20),fg="grey",bg="white").place(x=120,y=230)
v1=StringVar()
user_txt=Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable=v1)
user_txt.place(x=120,y=270)
userpass=Label(login_frame,text="Password",font=("goudy old style",20),fg="grey",bg="white").place(x=120,y=300)
v2=StringVar()
pass_txt=Entry(login_frame,font=("times new roman",15),bg="lightgray",textvariable=v2)
pass_txt.place(x=120,y=340)
forgot=Button(login_frame,text="Forgot Password?",bg="white",fg="#0271A2",font=("times new roman",12),bd=0,cursor="hand2",command=forgot_fn).place(x=120,y=375)
submit_button=Button(login_frame,text="Login",font=("goudy old style",20),fg="white",bg="#0271A2",command=validate,cursor="hand2").place(x=120,y=430)
signup_button=Button(login_frame,text="SignUp",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=sign_up).place(x=230,y=430)
root.mainloop()