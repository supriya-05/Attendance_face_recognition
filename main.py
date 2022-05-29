from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from click import command
from student import Student
from face_recognition import Face_Recognition
from report import Report
from time import strftime
from datetime import datetime

class Face_Recognition_System:

    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recognition System")
        

        title_label = Label(
            
            text="Face recognition System",
            font= ("Arial Narrow", 35, "italic"),
            bg="dark blue",
            fg="white",
        )
        title_label.place(x=0, y=0, width=1270, height=100)
                 

        img3 = Image.open(r"images\white.jpg")
        img3 = img3.resize((1500, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1500, height=710)

        
        #Time Function
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(title_label, font= ("Arial Narrow", 20, "italic"), background= "dark blue", foreground="white")
        lbl.place(x = 1100, y = 0, width=190, height=50)
        time()

        # Student button
        img4 = Image.open(r"images\Profile.jpg")
        img4 = img4.resize((200, 210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(
            bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2"
        )
        b1.place(x=300, y=150, width=200, height=220)

        b1_1 = Button(
            bg_img,
            text="Student details",
            command=self.student_details,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="dark blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="white"
        )
        b1_1.place(x=300, y=350, width=200, height=40)

        # Detect Images
        img5 = Image.open(r"images\at.jpg")
        img5 = img5.resize((200, 210))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command = self.face_data, cursor="hand2")
        b1.place(x=600, y=150, width=200, height=220)

        b1_1 = Button(
            bg_img,
            text="Mark Attendance",
            command = self.face_data, 
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="dark blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="white"
        )
        b1_1.place(x=600, y=350, width=200, height=40)

        # Attendance face button
        img6 = Image.open(r"images\pie.jpg")
        img6 = img6.resize((210, 210))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, command=self.attendance_report, cursor="hand2",)
        b1.place(x=900, y=150, width=200, height=220)

        b1_1 = Button(
            bg_img,
            text="Report",
            command=self.attendance_report,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="dark blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="white"
        )
        b1_1.place(x=900, y=350, width=200, height=40)

        #Exit Button
        
        b1_1 = Button(
            title_label,
            text="Exit",
            cursor="hand2",
            command=self.isExit,
            font=("times new roman", 12, "bold"),
            bg="dark blue",
            fg="white",
        )
        b1_1.place(x=1110, y=73, width=150, height=20)



   
        # # ======================== Function Buttons ==========================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)



    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)
        
    def isExit(self):
        self.isExit = tkinter.messagebox.askyesno("Face recognition", "Are you sure exit this project?", parent=self.root)
        if self.isExit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

    