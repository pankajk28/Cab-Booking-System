from tkinter import *
from PIL import ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
root6=Tk()
root6.title("ONE")
root6.geometry("1500x700+20+20")
root6.resizable(False,False)
mydb=mysql.connector.connect(host="localhost",user="root",password="password",database="booking")
cur=mydb.cursor() 
def show_fn():
    try:
        cur.execute("select * from Login_details where E_mail=%s",(v1.get(),))
        result=cur.fetchone()
        print(result)
        if result==None:
            messagebox.showerror("Error","User Not Found")
        else:
            curr2=mydb.cursor()
            curr2.execute("select Pickup_Location,Drop_Location,Pickup_date,Pickup_Time_hrs,Pickup_Time_min,Insurance_opted,Total_Amount from booking_details where Email=%s",(v1.get(),))
           
           
            i=0
            for val in curr2:
                tree.insert('',i,text="",values=(val[0],val[1],val[2],val[3],val[4],val[5],val[6]))
                i=i+1
            tree.place(x=110,y=250)
    except Exception as es:
            messagebox.showerror("Error",f"Eroor due to: {str(es)}")
def back_fn():
    root6.destroy()
    import SEL_CHOICE
def delete_fn():
    sel_item=tree.selection()[0]
    print(tree.item(sel_item)['values'])
    pic_l=tree.item(sel_item)['values'][0]
    query="delete from booking_details where Pickup_Location=%s"
    sel_data=(pic_l,)
    cur2=mydb.cursor()
    cur2.execute(query,sel_data)
    mydb.commit()
    tree.delete(sel_item)
    messagebox.showinfo("Sucess","Booking cancelled Sucessfully")
    mydb.close()
        

bg_image=ImageTk.PhotoImage(file="backg.jpg")
bg_label=Label(root6,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
frame1=Frame(root6,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=100,height=480,width=1100)
tree=ttk.Treeview(frame1)
tree['show']='headings'
s=ttk.Style(frame1)
s.theme_use("clam")
tree["columns"]=("pickup","drop","date","time_hrs","time_min","insurance","total")
tree.column("pickup",width=150,minwidth=150,anchor=CENTER)
tree.column("drop",width=150,minwidth=150,anchor=CENTER)
tree.column("date",width=150,minwidth=150,anchor=CENTER)
tree.column("time_hrs",width=150,minwidth=150,anchor=CENTER)
tree.column("time_min",width=150,minwidth=150,anchor=CENTER)
tree.column("insurance",width=150,minwidth=150,anchor=CENTER)
tree.column("total",width=150,minwidth=150,anchor=CENTER)
tree.heading("pickup",text="Pickup Location",anchor=CENTER)
tree.heading("drop",text="Drop Location",anchor=CENTER)
tree.heading("date",text="Pickup Date",anchor=CENTER)
tree.heading("time_hrs",text="Time_hrs",anchor=CENTER)
tree.heading("time_min",text="Time_min",anchor=CENTER)
tree.heading("insurance",text="Insurance Opted",anchor=CENTER)
tree.heading("total",text="Total Amount",anchor=CENTER)
l1=Label(frame1,text="Booking Details",font=("Impact",35,"bold"),bg="orange",fg="white").place(x=120,y=85)
l2=Label(frame1,text="Enter Your Email",font=(15),bg="white").place(x=110,y=180)
v1=StringVar()
email=Entry(frame1,font=("times new roman",15),bg="lightgray",textvariable=v1)
email.place(x=300,y=180,width=300)
show_button=Button(frame1,text="Show",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=show_fn).place(x=700,y=170)
back_button=Button(frame1,text="Back",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=back_fn).place(x=1050,y=500)
delete_button=Button(frame1,text="Cancel",font=("goudy old style",20),fg="white",bg="red",cursor="hand2",command=delete_fn).place(x=950,y=500)
root6.mainloop()