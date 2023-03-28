from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
# import cv2
# import os
# import numpy as np

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
#=========================Background Image==================================
        img_bg = Image.open(
            r"college_images/2-AI-invades-automobile-industry-in-2019.jpeg")
        img_bg = img_bg.resize((1530, 710), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img_bg)
        # self.bg = ImageTk.PhotoImage(
        #     file=r"college_images/2-AI-invades-automobile-industry-in-2019.jpeg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=130,width=1530,height=710)

#===========================Images==============================================
        # First Img
        img10 = Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\BestFacialRecognition.jpg")
        img10 = img10.resize((500, 130), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        f_lbl = Label(self.root, image=self.photoimg10)
        f_lbl.place(x=0, y=0, width=500, height=130)
# -----------------------------------------------------------------
 # Second img
        img11 = Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\facialrecognition.png")
        img11 = img11.resize((500, 130), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        f_lbl = Label(self.root, image=self.photoimg11)
        f_lbl.place(x=500, y=0, width=500, height=130)

   # ---------------------Third Image------------------

        img12 = Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\images.jpg")
        img12 = img12.resize((500, 130), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        f_lbl = Label(self.root, image=self.photoimg12)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        title_lbl = Label(lbl_bg, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)



#================================Login Frame ===========================================
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=210,width=340,height=450)

        img1 = Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730, y=215, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95,y=100)


        #Label
        username = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser =ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)


        #=======================Icon Images=============

        img2 = Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2,
                        bg="black", borderwidth=0)
        lblimg2.place(x=650, y=363, width=25, height=25)

        img3= Image.open(
            r"C:\Users\pawan\Desktop\Face-Recognition\college_images\lock-512.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(self.root, image=self.photoimg3,
                        bg="black", borderwidth=0)
        lblimg3.place(x=650, y=433, width=25, height=25)


        #===================Login Button=================

        loginbtn = Button(frame, text="Login",command=self.login, font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
#==========================Register Buttton========================
        registerbtn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0,
                          relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # ==========================Forget Password  Buttton========================
        loginbtn = Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman", 10, "bold"),borderwidth=0,
                          relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        loginbtn.place(x=10, y=370, width=160)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welocome to Facial Recoginition System")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login")
            my_cursor = conn.cursor()
            my_cursor.execute("select* from register where email=%s and password=%s " ,(

                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                        ))
            row =my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")  
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
#=====================Reset Password=========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror(
                "Error", "Select the Security Question", parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror(
                "Error", "Please enter the Answer", parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror(
                "Error", "Please enter the new Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login")
            my_cursor = conn.cursor()
            query=("select* from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row =my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please Enter The correct Answer",parent=self.root2)
            else:
                qry=("update register set password=%s where email=%s")
                val=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(qry,val)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()




#==========================Forget Password Window================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to reset the Password ")
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login")
            my_cursor = conn.cursor()
            query =("select* from register where email= %s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row ==None:
                messagebox.showerror("Error","Please Enter the Valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)

                # Security Question
            security_Q = Label(self.root2, text="Select Seurity Question", font=(
                "times new roman", 15, "bold"), bg="white", fg="black")
            security_Q.place(x=50, y=80)

            self.combo_security_Q = ttk.Combobox(self.root2, 
                                                font=("times new Roman", 15, "bold"), state="readonly", width=15)
            self.combo_security_Q["values"] = ("Select ",
                                            "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
            self.combo_security_Q.current(0)
            self.combo_security_Q.place(x=50, y=115, width=250)

        # Security Answer
            security_A = Label(self.root2, text="Security Answer", font=(
                "times new roman", 15, "bold"), bg="white", fg="black")
            security_A.place(x=50, y=150)

            self.txt_security = ttk.Entry(
                self.root2,  font=("times new roman", 15, "bold"))
            self.txt_security.place(x=50, y=185, width=250)
# Reset Password ==============================
            new_password = Label(self.root2, text="New Password", font=(
                "times new roman", 15, "bold"), bg="white", fg="black")
            new_password.place(x=50, y=220)

            self.txt_newpass = ttk.Entry(
                self.root2,  font=("times new roman", 15, "bold"))
            self.txt_newpass.place(x=50, y=255, width=250)

            btn = Button(self.root2, text="Reset",command=self.reset_pass, font=(
                "times new roman", 15, "bold"),fg="white",bg="green")
            btn.place(x=140,y=290)








    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ==============Variables==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()


# ===========================Background Image======================
        img_top = Image.open(
            r"college_images\employee_img2.jpg")
        img_top = img_top.resize((1550, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img_top)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1530, height=790)


# ==========================Left Image========================

        img_top1 = Image.open(
            r"college_images\thought-good-morning-messages-LoveSove.jpg")
        img_top1 = img_top1.resize((470, 550), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img_top1)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)
# ----------------------Main frame---------------------------
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

# ===================Labels And Entry=======================
        # First name
        fname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=(
            "times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)
       # Last name
        l_name = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)
       # Email
        email = Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        security_Q = Label(frame, text="Select Seurity Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ,
                                             font=("times new Roman", 15, "bold"), state="readonly", width=15)
        self.combo_security_Q["values"] = ("Select ",
                                           "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)

       # Security Answer
        security_A = Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # Password
        pswd = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)
       # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # =========================Check Button====================
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree the Terms  & Conditions ", font=(
            "times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

# ==========================Buttons====================================
        img = Image.open(
            r"college_images\register-now-button1.jpg")
        img = img.resize((200, 45), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data,
                    image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(
            r"college_images\loginpng.png")
        img1 = img1.resize((200, 40), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame,command=self.return_login, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b1.place(x=330, y=420, width=200)


# ==========================Function Decleration================

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All Fields Are Required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree Our terms And Condition")

        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="", database="login")
            my_cursor = conn.cursor()
            query = ("Select * from register where email =%s ")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showinfo(
                    "Error", "User Already Exist, Please try another Email")
            else:
                my_cursor.execute(
                    "insert into register values (%s,%s,%s,%s,%s,%s,%s) ", (

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
            messagebox.showinfo("Success", "Register Successfully")

    def return_login(self):
        self.root.destroy()




if __name__ == "__main__":
    main()
