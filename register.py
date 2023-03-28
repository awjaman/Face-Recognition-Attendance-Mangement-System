from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==============Variables==============
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact=StringVar()
        self.var_email = StringVar()
        self.var_securityQ= StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


#===========================Background Image======================
        img_top = Image.open(
            r"college_images\employee_img2.jpg")
        img_top = img_top.resize((1550, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img_top)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1530, height=790)


#==========================Left Image========================

        img_top1 = Image.open(
            r"college_images\thought-good-morning-messages-LoveSove.jpg")
        img_top1 = img_top1.resize((470, 550), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img_top1)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
#----------------------Main frame---------------------------
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)

#===================Labels And Entry=======================
        # First name
        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)
       # Last name
        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white",fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)
       # Email
        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        security_Q = Label(frame, text="Select Seurity Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,
                                      font=("times new Roman", 15, "bold"), state="readonly", width=15)
        self.combo_security_Q["values"] = ("Select ",
                                    "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

       
       # Security Answer
        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # Password
        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame,textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)
       # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)


        #=========================Check Button====================
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check, text="I agree the Terms  & Conditions ", font=("times new roman", 12, "bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

#==========================Buttons====================================
        img = Image.open(
            r"college_images\register-now-button1.jpg")
        img = img.resize((200, 45), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1= Button(frame,command=self.register_data, image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1 = Image.open(
            r"college_images\loginpng.png")
        img1 = img1.resize((200, 40), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)


#==========================Function Decleration================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree Our terms And Condition")
        
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login")
            my_cursor= conn.cursor()
            query =("Select * from register where email =%s ")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showinfo("Error","User Already Exist, Please try another Email")
            else:
                my_cursor.execute(
                    "insert into register values (%s,%s,%s,%s,%s,%s,%s) ",(

                                                                            self.var_fname.get(),
                                                                            self.var_lname.get(),
                                                                            self.var_contact.get(),
                                                                            self.var_email.get(),
                                                                            self.var_securityQ.get(),
                                                                            self.var_securityA.get(),
                                                                            self.var_pass.get()
                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")



    













if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
