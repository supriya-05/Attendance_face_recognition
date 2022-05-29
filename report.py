import tkinter as tk
from tkinter import messagebox
import pandas as pd
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from time import strftime
from datetime import datetime

class Report:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face recognition System")


        df = pd.read_csv("attendance.csv")
        self.students = df['Names'].tolist()
        self.students = ["Select Student"] + self.students
    


        days_df = df.columns
        self.days = list(days_df)[2:]
        self.days = ["Select Date"] + self.days

        title_label_report = tk.Label(
            self.root,
            text="Report",
            font= ("Arial Narrow", 35, "italic"),
            bg="dark blue",
            fg="white",
        )
        title_label_report.place(x=0, y=0, width=1270, height=100)

        bg_img = Image.open(r"images\white.jpg")
        bg_img = bg_img.resize((1500, 710))
        self.bgimg = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.bgimg)
        bg_img.place(x=0, y=100, width=1500, height=710)
        
        #Image for report by name
        mark_name = Image.open(r"images\atten.png")
        mark_name = mark_name.resize((200, 210))
        self.photo_report_name = ImageTk.PhotoImage(mark_name)

        mark_lbl = Label(bg_img, image=self.photo_report_name)
        mark_lbl.place(x=450, y=55, width=200, height=210)

        #Image for report by date
        mark_date = Image.open(r"images\report_date.jpg")
        mark_date = mark_date.resize((200, 210))
        self.photo_report_date = ImageTk.PhotoImage(mark_date)

        mark_lbl = Label(bg_img, image=self.photo_report_date)
        mark_lbl.place(x=750, y=55, width=200, height=210)


        #Left Frame
        left_frame = Frame(bg_img, bd = 2, bg = "white")
        left_frame.place(x = 410, y = 300, width = 300, height = 100)
        #Right Frame
        right_frame = Frame(bg_img, bd = 2, bg = "white")
        right_frame.place(x = 730, y = 300, width = 400, height = 100)

 
        
        #Selecting student 
        select_names = Label(left_frame, text='Select a Student', font = ("times new roman", 12), bg="white")
        select_names.grid(row = 1, column=0, padx=10)
        self.std_name = Combobox(left_frame, values=self.students)
        self.std_name.grid(row = 1, column=1)
        self.std_name.current(0)

        self.b1 = Button(left_frame, text="Generate Report by Name", command=self.plot_graph_name, font = ("times new roman", 12),bg='darkblue', fg = "white", activebackground="darkblue", activeforeground= "white" ).place(x = 30, y = 40, width= 210)
        
        or_label_report = tk.Label(
            bg_img,
            text="OR",
            font= ("Arial Narrow", 18, "italic"),
            bg="white",
            fg="Black",
        )
        or_label_report.place(x=670, y=200, width=35, height=20)

        #selecting Date
        select_date = Label(right_frame, text='Select date', font = ("times new roman", 12), bg="white")
        select_date.grid(row = 1, column=15, padx=10)
        self.std_date = Combobox(right_frame, values=self.days)
        self.std_date.current(0)

        self.std_date.grid(row = 1, column=20)
        self.b11 = Button(right_frame, text="Generate Report by Date", command=self.plot_graph_date,font = ("times new roman", 12), bg='darkblue', fg = "white", activebackground="darkblue", activeforeground= "white" ).place(x = 25, y = 40, width=210)
        


    def plot_graph_date(self):
        global df
        df = pd.read_csv("attendance.csv")
        date = self.std_date.get()


        if date == "Select Date":
            messagebox.showerror("Error", "Select a valid Date!", parent=self.root)
        
        #ondition to check When no Class is Conducted
        elif df[date].isnull().all():
            messagebox.showinfo("Message", "No Class on " + str(date) + "\n" + "Check on another Date", parent=self.root)

        else:
            day_details = df[date].tolist()
            no_present = day_details.count('Present')
            no_absent = day_details.count('Absent')

            #Plotting Graph
            plt.pie([no_present, no_absent], labels=["Students present", "Students absent"], autopct='%1.1f%%', shadow=True)
            plt.title("Report on " +  date )
            plt.show()
        

    def plot_graph_name(self):
            global df
            df = pd.read_csv("attendance.csv")
            days_df = df.columns
            days = list(days_df)[2:]
            name = self.std_name.get()

            if name == "Select Student":
                messagebox.showerror("Error", "Select a valid Name!", parent=self.root)
            else:
                student_df = df.loc[df["Names"] == name]
                student = student_df.values[0].tolist()

                #Calculating No of days present and absent
                present_days = student.count("Present")
                absent_days = student.count("Absent")
                data = [present_days, absent_days]
                
                #Plotting graph
                plt.pie(data, labels=["present", "absent"], autopct='%1.1f%%', shadow=True)
                plt.title(name + "  Report")
                plt.show()


    
if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()