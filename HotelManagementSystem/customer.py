from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import csv


class Cust_Win:
    def __init__(self,root, cust):
        self.root=root
        self.root.title("Hotel Manangement System")
        self.root.geometry("1295x550+230+220")
        
        #==================== variable ===================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        self.customer_data = cust


         # ================== title ===================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
         # =============== logo ======================
         
         # ============== label frame ================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE, text="Customer Details",font=("times new roman", 12, "bold") ,padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
         # ============ labels and entrys ============
         #cust ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref", font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
                          
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("times new roman", 13, "bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)
        
        #cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=1,column=1)
        
        #father name
        lblhname=Label(labelframeleft, font=("arial", 12, "bold"), text="Father Name:", padx=2, pady=6)
        lblhname.grid(row=2, column=0, sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_father,font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2,column=1)
        
        #gender combobox
        label_gender=Label(labelframeleft,font=("arial", 12, "bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial", 13, "bold"), width=27, state="readonly")
        combo_gender["value"]=("Male","Female")  
        combo_gender.current(0)      
        combo_gender.grid(row=3,column=1)
        
        #postcode
        lblPostCode=Label(labelframeleft,font=("arial", 12, "bold"),text="Post Code:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4,column=1)
        
        #mobilenumber
        lblMobile=Label(labelframeleft,font=("arial", 12, "bold"), text="Mobile:",padx=2, pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5,column=1)
        
        #email
        lblEmail=Label(labelframeleft, font=("arial", 12, "bold"), text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6,column=1)
        
        #nationality
        lblNationality=Label(labelframeleft,font=("arial", 12, "bold"), text="Nationality:", padx=2,pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial", 13, "bold"), width=27, state="readonly")
        combo_nationality["value"]=("Malay","Chinese","Indian","Other")  
        combo_nationality.current(0)      
        combo_nationality.grid(row=7,column=1)
        
        #idprooof type combo
        lblIdProof= Label(labelframeleft, font=("arial", 12, "bold"), text="ID Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        
        combo_IdProof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial", 13, "bold"), width=27, state="readonly")
        combo_IdProof["value"]=("Identification Card","Passport","Driving License","Other")  
        combo_IdProof.current(0)      
        combo_IdProof.grid(row=8,column=1)
      
        #id number
        lblIdNumber=Label(labelframeleft,font=("arial", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial", 13, "bold"), width=29)
        txtIdNumber.grid(row=9,column=1)
        
        #address
        lblAddress=Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtIdAddress=ttk.Entry(labelframeleft,textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtIdAddress.grid(row=10,column=1)
        
        # ===================== btn ===================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame, text="Add",command=self.add_data,font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        # ================ table frame search system ===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE, text="View Details And Search System",font=("times new roman", 12, "bold") ,padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)
        
        lblSearchBy=Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:",bg="red", fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2) 
        
        self.search_var=StringVar()
        combo_SearchBy=ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 13, "bold"), width=24, state="readonly")
        combo_SearchBy["value"]=("Mobile","Ref")  
        combo_SearchBy.current(0)      
        combo_SearchBy.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearchBy=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial", 13, "bold"), width=24)
        txtSearchBy.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        
        
    # ================ Show Data Table =================
    
        details_table=Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table, column=('ref', 'name', 'father', 'gender','postcode','mobile',
                                            'email', 'nationality', 'idproof', 'idnumber', 'address'), xscrollcommand="scroll_x", yscrollcommand="scroll_y")
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref",text="Refer Num")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("postcode",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile Number")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")    

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("postcode",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_father.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            # Using a dictionary to store customer data
            try:
                # Assuming you have a dictionary named 'customer_data'
                customer_id = self.var_ref.get()
                self.customer_data[customer_id] = {
                    'cust_name': self.var_cust_name.get(),
                    'father': self.var_father.get(),
                    'gender': self.var_gender.get(),
                    'post': self.var_post.get(),
                    'mobile': self.var_mobile.get(),
                    'email': self.var_email.get(),
                    'nationality': self.var_nationality.get(),
                    'id_proof': self.var_id_proof.get(),
                    'id_number': self.var_id_number.get(),
                    'address': self.var_address.get()
                }

                # Update the UI or other components as needed
                self.save_data_to_file("customers.txt")
                self.fetch_data()
                
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)




    def fetch_data(self):
        # Check if the customer data dictionary has entries
        if len(self.customer_data) != 0:
            # Clear existing entries in the table
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            # Iterating over the dictionary and adding each customer's data to the table
            for customer_id, customer_info in self.customer_data.items():
                # You might need to adjust the format depending on how your table is set up
                table_entry = (
                    customer_id,
                    customer_info['cust_name'],
                    customer_info['father'],
                    customer_info['gender'],
                    customer_info['post'],
                    customer_info['mobile'],
                    customer_info['email'],
                    customer_info['nationality'],
                    customer_info['id_proof'],
                    customer_info['id_number'],
                    customer_info['address']
                )
                self.Cust_Details_Table.insert("", END, values=table_entry)
        else:
            # Reading customer.txt and populating self.customer_data
            try:
                with open('customers.txt', mode='r') as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        self.customer_data[row['id']] = row

                # Now populate the table as self.customer_data is not empty
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for customer_id, customer_info in self.customer_data.items():
                    table_entry = (
                        customer_id,
                        customer_info['cust_name'],
                        customer_info['father'],
                        customer_info['gender'],
                        customer_info['post'],
                        customer_info['mobile'],
                        customer_info['email'],
                        customer_info['nationality'],
                        customer_info['id_proof'],
                        customer_info['id_number'],
                        customer_info['address']
                    )
                    self.Cust_Details_Table.insert("", "end", values=table_entry)
            except Exception as e:
                print("Error reading file:", e)
                # Handle error or notify user as needed
            


    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])
        
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            customer_ref = self.var_ref.get()
            if customer_ref in self.customer_data:
                # Update customer data in the dictionary
                self.customer_data[customer_ref] = {
                    'cust_name': self.var_cust_name.get(),
                    'father': self.var_father.get(),
                    'gender': self.var_gender.get(),
                    'post': self.var_post.get(),
                    'mobile': self.var_mobile.get(),
                    'email': self.var_email.get(),
                    'nationality': self.var_nationality.get(),
                    'id_proof': self.var_id_proof.get(),
                    'id_number': self.var_id_number.get(),
                    'address': self.var_address.get()
                }
                
                messagebox.showinfo("Success", "Customer data updated successfully", parent=self.root)
                self.save_data_to_file("customers.txt")
                self.fetch_data()  # Refresh the table
            else:
                # Handle the case where the customer Ref is not found
                messagebox.showerror("Error", "Customer not found", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent=self.root)
        if mDelete:
            customer_ref = self.var_ref.get()
            if customer_ref in self.customer_data:
                # Delete the customer from the dictionary
                del self.customer_data[customer_ref]
                
                # Update the table after deletion
                self.save_data_to_file("customers.txt")
                self.fetch_data()
            else:
                # Handle case where the reference ID is not found
                messagebox.showerror("Error", "Customer not found", parent=self.root)


    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
    
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    
    def search(self):
        # Retrieve the search term and the field to search in
        search_field = self.search_var.get()  # For example, 'cust_name', 'mobile', etc.
        search_term = self.txt_search.get().lower()  # Assuming this is the correct method to get the search text

        if search_term:
            # Clear existing entries in the table
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            # Iterating over the dictionary and searching for matches
            for customer_id, customer_info in self.customer_data.items():
                # Check if the search term is in the specified field
                if search_field.lower() == 'ref':
                        if search_term in customer_id.lower():
                            table_entry = (
                                customer_id,
                                customer_info['cust_name'],
                                customer_info['father'],
                                customer_info['gender'],
                                customer_info['post'],
                                customer_info['mobile'],
                                customer_info['email'],
                                customer_info['nationality'],
                                customer_info['id_proof'],
                                customer_info['id_number'],
                                customer_info['address']
                            )
                            self.Cust_Details_Table.insert("", "end", values=table_entry)
                else:
                    if search_term in str(customer_info[search_field.lower()]).lower():
                        table_entry = (
                            customer_id,
                            customer_info['cust_name'],
                            customer_info['father'],
                            customer_info['gender'],
                            customer_info['post'],
                            customer_info['mobile'],
                            customer_info['email'],
                            customer_info['nationality'],
                            customer_info['id_proof'],
                            customer_info['id_number'],
                            customer_info['address']
                        )
                        self.Cust_Details_Table.insert("", "end", values=table_entry)
        else:
            # Handle the case where no search term is entered
            # You might want to display all data or show a message
            pass  # Implement as needed
        

    def save_data_to_file(self, filename):
        try:
            # Open the file in write mode
            with open(filename, 'w', newline='') as file:
                # Create a CSV writer object
                writer = csv.DictWriter(file, fieldnames=self.customer_data[next(iter(self.customer_data))].keys())
                
                # Write the header
                writer.writeheader()

                # Write customer data
                for customer_id, customer_info in self.customer_data.items():
                    customer_info = {'id':customer_id, **customer_info}
                    writer.writerow(customer_info)

#             messagebox.showinfo("Success", "Data saved to " + filename, parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", "Failed to save data: " + str(e), parent=self.root)












if __name__=="__main":
    root=ttk()
    obj=Cust_Win(root)
    root.mainloop()