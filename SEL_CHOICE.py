import tkinter


from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
root3=Tk()
root3.title("one")
root3.geometry("1236x600+180+100")
root3.resizable(False,False)
#------------------------------------------------------------------------------------------------------------------------------------#
def Book_command():
    root3.destroy()
    import book_cab
def show_details():
    root3.destroy()
    import booking_details
#-------------------------------------------------------------------------------------------------------------------------------------#
bg_image=ImageTk.PhotoImage(file="backg.jpg")
bg_label=Label(root3,image=bg_image).place(x=0,y=0,relheight=1,relwidth=1)
frame1=Frame(root3,bg="white",highlightbackground="grey",highlightthickness=3).place(x=85,y=150,height=200,width=700)
l1=Label(frame1,text="Choose Your Command",font=("Impact",35,"bold"),bg="orange",fg="white").place(x=120,y=125)
Book_button=Button(frame1,text="Book Cab",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=Book_command).place(x=150,y=250)
details_button=Button(frame1,text="Show Booking Details",font=("goudy old style",20),fg="white",bg="#0271A2",cursor="hand2",command=show_details).place(x=400,y=250)
root3.mainloop()