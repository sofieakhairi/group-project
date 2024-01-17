from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
import random
from tkinter import messagebox


class HotelManagementSystem:
    def __init__(self,root):

        self.cust = {}

        self.room = {}
        self.details = {}
        self.root=root
        self.root.title("Hotel Manangement System")
        self.root.geometry("1550x800+0+0")
        
        # ================== 1st img ================
        img1=Image.open(r"hotel1.jpeg")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
                # ===================== logo img ==================
        img2=Image.open(r"hotellogo.jpeg")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
         
        
        # ================== title===================
        lbl_title=Label(self.root,text="Hotel Management System", font=("times new roman", 40, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        # =================in frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        # ==================menu======================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        
        # =================btn frame==================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=22, font=("times new roman", 14, "bold"),bg="black",fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="LOG OUT", command=self.logout, width=22, font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="", width=22,font=("times new roman",14, "bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="", width=22, font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="", width=22, font=("times new roman", 14, "bold"),bg="black", fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
    
    #================ right side img =============
        img3=Image.open(r"hotel2.jpeg")
        img3=img3.resize((1310,590),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)

     #================= down img ===================
        img4=Image.open(r"hotel3.jpeg")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"hotel4.jpeg")
        img5=img5.resize((1310,590),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)
    
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window, self.cust)
        
    def logout(self):
        # Confirm before closing
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to logout and exit the application?", parent=self.root):
            self.root.destroy()


    
root=Tk()
obj= HotelManagementSystem (root)
root.mainloop()
    