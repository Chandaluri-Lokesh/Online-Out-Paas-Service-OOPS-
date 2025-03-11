from tkinter import *
from tkinter import messagebox
import re
import subprocess
import pandas as pd

root = Tk()
root.title("OOPs")
root.geometry("1450x700+0+0")


def Signin():

    def create_account():
        username_data = username.get()
        email_data = email.get()
        password_data = password.get()
        role_data = var.get()
        confirm_password_data = confirmpassword.get()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_data):
            messagebox.showerror("Error", "Invalid email address.")
            return

        if password_data != confirm_password_data:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        if role_data == "":  # No role selected
            messagebox.showerror("Error", "Please select a role.")
            return

        # Create a DataFrame to store user details
        user_details = pd.DataFrame({
            'Name': [username_data],
            'Email': [email_data],
            'Password': [password_data],
            'Role': [role_data]
        })

        # Save the DataFrame to an Excel file
        user_details.to_excel('user_details.xlsx', index=False)

        # Display a success message
        messagebox.showinfo("Success", "User created successfully.")
    
    f2=Frame(height=450,width=380,bg="white")
    f2.place(x=800,y=100)

    heading=Label(f2,text="Create an account",font=("microsoft yahei UI light",20 ,"bold"),bg="white",fg ="firebrick1")
    heading.place(x=30,y=5)
    Label(f2,text="Email",font=("microsoft yahei UI light",12 ,"bold"),fg="firebrick1",bg="white").place(x=20,y=60)
    Label(f2,text="Username",font=("microsoft yahei UI light",12 ,"bold"),fg="firebrick1",bg="white").place(x=20,y=120)
    Label(f2, text="Role", font=("microsoft yahei UI light", 12, "bold"), fg="firebrick1", bg="white").place(x=20, y=290)
    
    email=Entry(f2,font=("microsoft yahei UI light",12 ,"bold"),width=33,bg="dodger blue")
    email.place(x=20,y=90)
    username=Entry(f2,font=("microsoft yahei UI light",12,"bold"),width=33,bg="dodger blue")
    username.place(x=20,y=145)

    password=Entry(f2,font=("microsoft yahei UI light",12,"bold"),width=33,bg="dodger blue", show="*")
    password.place(x=20,y=210)
    
    Label(f2,text="Password",font=("microsoft yahei UI light",12 ,"bold"),fg="firebrick1",bg="white").place(x=20,y=180)
    Label(f2,text="Confirm Password",font=("microsoft yahei UI light",12 ,"bold"),fg="firebrick1",bg="white").place(x=20,y=235)
    confirmpassword=Entry(f2,font=("microsoft yahei UI light",12,"bold"),width=33,bg="dodger blue", show="*")
    confirmpassword.place(x=20,y=265)

    var = StringVar()
    var.set("")

    teacher_button = Radiobutton(f2, text="Teacher", variable=var, value="Teacher", font=("microsoft yahei UI light", 12), bg="white")
    teacher_button.place(x=20, y=320)

    student_button = Radiobutton(f2, text="Student", variable=var, value="Student", font=("microsoft yahei UI light", 12), bg="white")
    student_button.place(x=110, y=320)

    warden_button = Radiobutton(f2, text="Warden", variable=var, value="Warden", font=("microsoft yahei UI light", 12), bg="white")
    warden_button.place(x=200, y=320)

    signinbutton=Button(f2,text="Signup",font=("microsoft yahei UI light",15 ,"bold"),width=26,bg="firebrick1",fg="white",activebackground="firebrick1", command=create_account)
    signinbutton.place(x=25,y=350)


    Label(f2,text="Dont have an account？",font=("open sans",11,"bold"),fg="firebrick1",bg="white").place(x=20,y=400)
    b2=Button(f2,text="login",font=("open sans",11 ,"bold","underline"),bg="white",fg="deep sky blue",bd=0,activebackground="white",activeforeground="deep sky blue",command=login).place(x=200,y=400)


def login():
        
    def check_credentials():
        email_data = email.get()
        password_data = password.get()

        # Read user details from the Excel file
        user_details = pd.read_excel('user_details.xlsx')

        # Check if the entered email and password match with any user details
        matching_user = user_details[
            (user_details['Email'] == email_data) & (user_details['Password'] == password_data)
        ]

        if not matching_user.empty:
            stored_username = matching_user['Name'].values[0]
            stored_role = matching_user['Role'].values[0]

            messagebox.showinfo("Success", f"Login successful. Welcome, {stored_username}!")

            root.destroy()  # Close the login window

            if stored_role == "Student":
                subprocess.call(["python", "student_page.py", stored_username])  # Execute student_page.py with username as an argument
            elif stored_role == "Teacher":
                subprocess.call(["python", "teacher_page_dayout.py"])  # Execute teacher_page.py
            elif stored_role == "Warden":
                subprocess.call(["python", "warden_page.py"])  # Execute warden_page.py
        else:
            # If no matching credentials found, display an error message
            messagebox.showerror("Error", "Invalid email or password.")

    
    f1=Frame(height=450,width=380,bg="white")
    f1.place(x=800,y=100)
    
    Frame(f1,width=290,height=2,bg="firebrick1",bd=0).place(x=830,y=220)
    Frame(f1,width=290,height=2,bg="firebrick1",bd=0).place(x=830,y=280)
        

    heading=Label(f1,text="USER LOGIN",font=("microsoft yahei UI light",23 ,"bold"),bg="white",fg ="firebrick1")
    heading.place(x=90,y=20)
    Label(f1,text="Email",font=("microsoft yahei UI light",16,"bold"),fg="firebrick1",bg="white").place(x=30,y=85)
    Label(f1,text="Password",font=("microsoft yahei UI light",16,"bold"),fg="firebrick1",bg="white").place(x=30,y=150)
    Label(f1,text="Dont have an account？",font=("open sans",11,"bold"),fg="firebrick1",bg="white").place(x=30,y=380)
        
    email=Entry(f1,font=("microsoft yahei UI light",16 ,"bold"),width=24,bd=0,bg="hotpink",fg="white")
    email.place(x=30,y=120)
    password=Entry(f1,font=("microsoft yahei UI light",16,"bold"),width=24,bd=0,bg="hotpink",fg="white", show="*")
    password.place(x=30,y=190)

    loginbutton=Button(f1,text="LOGIN",font=("microsoft yahei UI light",15 ,"bold"),width=25,bg="firebrick1",fg="white",activebackground="firebrick1",activeforeground="white", command=check_credentials)
    loginbutton.place(x=30,y=270)
    b2=Button(f1,text="Create an account",font=("open sans",11 ,"bold","underline"),bg="white",fg="deep sky blue",bd=0,activebackground="white",activeforeground="deep sky blue",command=Signin).place(x=200,y=380)
 
def frogetpassword():

    f3=Frame(height=450,width=380,bg="white")
    f3.place(x=800,y=100)
    
    Frame(f3,width=290,height=2,bg="firebrick1",bd=0).place(x=830,y=220)
    Frame(f3,width=290,height=2,bg="firebrick1",bd=0).place(x=830,y=280)
    heading=Label(f3,text="Forget Password",font=("microsoft yahei UI light",23 ,"bold"),bg="white",fg ="firebrick1")
    heading.place(x=90,y=20)
    Label(f3,text="Username",font=("microsoft yahei UI light",16,"bold"),fg="firebrick1",bg="white").place(x=30,y=80)
    Label(f3,text="New Password",font=("microsoft yahei UI light",16,"bold"),fg="firebrick1",bg="white").place(x=30,y=150)
    Label(f3,text="Confirm Password",font=("microsoft yahei UI light",16,"bold"),fg="firebrick1",bg="white").place(x=30,y=220)

    
    username=Entry(f3,font=("microsoft yahei UI light",16 ,"bold"),width=24,bd=0,bg="hotpink",fg="white")
    username.place(x=30,y=120)
    password=Entry(f3,font=("microsoft yahei UI light",16,"bold"),width=24,bd=0,bg="hotpink",fg="white")
    password.place(x=30,y=190)
    confirmpassword=Entry(f3,font=("microsoft yahei UI light",16,"bold"),width=24,bd=0,bg="hotpink",fg="white")
    confirmpassword.place(x=30,y=260)

    Button(f3,text="Reset Password",font=("microsoft yahei UI light",15 ,"bold"),width=25,bg="firebrick1",fg="white",activebackground="firebrick1",activeforeground="white").place(x=30,y=340)
 



login()      




root.mainloop() 