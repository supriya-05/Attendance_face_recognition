from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from cv2 import exp
from django.forms import HiddenInput
from matplotlib.pyplot import table
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("Face Recognition System")

        conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123")
        my_cursor = conn.cursor()
        query = "CREATE DATABASE IF NOT EXISTS face"
        my_cursor.execute(query)

        
        conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database = 'face')
        my_cursor = conn.cursor()
        TableName ="CREATE TABLE IF NOT EXISTS Student_details (Dep VARCHAR(45), course VARCHAR(45), year VARCHAR(45),SEMESTER VARCHAR(45), Student_id VARCHAR(45) PRIMARY KEY,Name VARCHAR(45),Division VARCHAR(45),Roll VARCHAR(45),Gender VARCHAR(45),Dob VARCHAR(45),Email VARCHAR(45),Phone VARCHAR(45),Address VARCHAR(45),Teacher VARCHAR(45),photoSample VARCHAR(45));"

        my_cursor.execute(TableName)
        
        
        # variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher= StringVar()
        
        

        # bg image

        img3 = Image.open(r"images\white.jpg")
        img3 = img3.resize((1500, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=50, width=1500, height=710)

        
        tile_label = Label(
            self.root,
            text="Student Details",
            font=("times new roman", 25),
            bg="dark blue",
            fg= "white",
        )
        tile_label.place(x=0, y=0, width=1400, height= 50)



        main_frame = Frame(bg_img, bd = 2, bg = "white")
        main_frame.place(x = 10, y = 25, width = 1300, height = 700)


        #left label frame

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,  text="Student Details", font = ("times new roman", 12),bg = "white" )
        Left_frame.place(x=10, y=10, width=580, height=550)

        # current course information

        current_course_frame = LabelFrame(Left_frame, bd=2, bg = "white", relief=RIDGE,  text="Current course information", font = ("times new roman", 12))
        current_course_frame.place(x=10, y=10, width=560, height=105)

        #Department
        dep_label = Label(current_course_frame, text='Department', font = ("times new roman", 12), bg="white")
        dep_label.grid(row = 0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font = ("times new roman", 12), width=17, state="readonly")
        dep_combo['values'] = ("Select department", "CSE", "Civil", 'Mechanical', 'IT', "ECE", "EEE", "Others")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10)

        # Course
        course_label = Label(current_course_frame, text='Course', font = ("times new roman", 12), bg="white")
        course_label.grid(row = 0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font = ("times new roman", 12), width=17, state="readonly")
        course_combo['values'] = ("Select course", 'BE', 'B-Tech', "Others")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text='Year', font = ("times new roman", 12), bg="white")
        year_label.grid(row = 1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font = ("times new roman", 12), width=17, state="readonly")
        year_combo['values'] = ("Select year", "2020-2024", "2019-2023", '2018-2022', "2017-2021", "2021- 2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        #semester

        semester_label = Label(current_course_frame, text='Semester', font = ("times new roman", 12), bg="white")
        semester_label.grid(row = 1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,font = ("times new roman", 12), width=17, state="readonly")
        semester_combo['values'] = ("Select Semester", "Semester - 1", "Semester - 2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

        #Class Student information   borderwidth = 0, highlightthickness = 0, 
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg = "white", relief=RIDGE, text="Class Student information", font = ("times new roman", 12))
        Class_Student_frame.place(x=10, y=115, width=560, height=390)

        # Student id
        studentID_label = Label(Class_Student_frame, text='Student ID:', font = ("times new roman", 12), bg="white")
        studentID_label.grid(row = 0, column=0,sticky=W)

        studentID_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,font = ("times new roman", 12))
        studentID_entry.grid(row=0, column=1, padx=2,sticky=W)

        # Student name
        studentName_label = Label(Class_Student_frame, text='Student Name:', font = ("times new roman", 12), bg="white")
        studentName_label.grid(row = 0, column=2, padx=10,pady = 10, sticky=W)

        studentName_entry = ttk.Entry(Class_Student_frame, width=15,textvariable=self.var_std_name, font = ("times new roman", 12))
        studentName_entry.grid(row=0, column=3, padx=2, pady = 2, sticky=W)

        #Class Division
        class_div_label = Label(Class_Student_frame, text='Class Division', font = ("times new roman", 12), bg="white")
        class_div_label.grid(row = 1, column=0, padx=0, sticky=W)

        div_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_div, font = ("times new roman", 12), width=17, state="readonly")
        div_combo['values'] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1, padx=2, pady=1, sticky=W)

        #Roll no
        roll_no_label = Label(Class_Student_frame, text='Roll No', font = ("times new roman", 12), bg="white")
        roll_no_label.grid(row = 1, column=2, padx=2, sticky=W)

        roll_no_entry = ttk.Entry(Class_Student_frame, width=15, textvariable=self.var_roll, font = ("times new roman", 12))
        roll_no_entry.grid(row=1, column=3, padx=2, pady = 2, sticky=W)

        #Gender
        Gender_label = Label(Class_Student_frame, text='Gender:', font = ("times new roman", 12), bg="white")
        Gender_label.grid(row = 2, column=0, padx=2, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_gender, font = ("times new roman", 12), width=10, state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other", )
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1, padx=1, pady=1, sticky=W)

         #DOB
        dob_label = Label(Class_Student_frame, text='DOB:', font = ("times new roman", 12), bg="white")
        dob_label.grid(row = 2, column=2, padx=2, sticky=W)

        dob_entry = ttk.Entry(Class_Student_frame, width=15, textvariable=self.var_dob,font = ("times new roman", 12))
        dob_entry.grid(row=2, column=3, padx=2, pady = 2, sticky=W)

         #Email
        email_label = Label(Class_Student_frame, text='Email:', font = ("times new roman", 12), bg="white")
        email_label.grid(row = 3, column=0, padx=2, sticky=W)

        email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email, width=15, font = ("times new roman", 12))
        email_entry.grid(row=3, column=1, padx=2, pady = 2, sticky=W)

        #phone number
        phone_label = Label(Class_Student_frame, text='Phone', font = ("times new roman", 12), bg="white")
        phone_label.grid(row = 3, column=2, padx=2, sticky=W)

        phone_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_phone, width=15, font = ("times new roman", 12))
        phone_entry.grid(row=3, column=3, padx=2, pady = 2, sticky=W)

        # address
        address_label = Label(Class_Student_frame, text='Address', font = ("times new roman", 12), bg="white")
        address_label.grid(row = 4, column=0, padx=2, sticky=W)

        address_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_address, width=15, font = ("times new roman", 12))
        address_entry.grid(row=4, column=1, padx=2, pady = 2, sticky=W)

        # teacher
        teacher_label = Label(Class_Student_frame,text='Teacher', font = ("times new roman", 12), bg="white")
        teacher_label.grid(row = 4, column=2, padx=2, sticky=W)

        teacher_entry = ttk.Entry(Class_Student_frame, width=15,textvariable=self.var_teacher, font = ("times new roman", 12))
        teacher_entry.grid(row=4, column=3, padx=2, pady = 2, sticky=W)
        
    

        #radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text = "Take photo Sample", value = "Yes")
        radiobtn1.grid(row=6, column=0, padx=5, pady=5, sticky = W)

        radiobtn2 = ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1, text = "No photo Sample", value = "No")
        radiobtn2.grid(row=6, column=1, padx=5, pady=5, sticky = W)
        
        # button frame
        btn_frame = Frame(Class_Student_frame, bd = 2, relief=RIDGE, bg = "white")
        btn_frame.place(x=0,y=250,width=600, height=35)
        
        save_btn = Button(btn_frame, text = 'Save', command = self.add_data, font=("times new roman", 13), width=14, bg = "darkblue", fg = "white", activebackground="darkblue", activeforeground="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text = 'Update', command = self.update_data, font=("times new roman", 13), width=14, bg = "darkblue", fg = "white", activebackground="darkblue", activeforeground="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text = 'Delete', command=self.delete_data, font=("times new roman", 13), width=14, bg = "darkblue", fg = "white", activebackground="darkblue", activeforeground="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text = 'Reset', command=self.reset_data,font=("times new roman", 13), width=15, bg = "darkblue", fg = "white", activebackground="darkblue", activeforeground="white")
        reset_btn.grid(row=0, column=3)

        #Button Frame
        btn_frame1 = Frame(Class_Student_frame, bd = 2, relief=RIDGE, bg = "white")
        btn_frame1.place(x=0,y=320,width=550, height=30)

        take_photo_btn = Button(btn_frame1,command = self.generate_dataset, text = 'Take photo', font=("times new roman", 13), width=50, bg = "darkblue", fg = "white", activebackground="darkblue", activeforeground="white")
        take_photo_btn.place(x = 0, y = 0, width = 550)

        

        #rightlabel frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg = "white",   text="Student Details", font = ("times new roman", 12))
        Right_frame.place(x=610, y=10, width=590, height=540)
      
        #table frame
        Table_frame = LabelFrame(Right_frame, bd=2, bg = "white", relief=RIDGE)
        Table_frame.place(x=10, y=10, width=560, height=500)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"


        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #Function Definitions

    #Add data Function
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == ""or self.var_std_id.get == "":
            messagebox.showerror("Error", "All Fields are required", parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database= "face")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into Student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess", "Student details have been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Dur To :{str(es)}", parent=self.root)


    #Fetch data Function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database= "face")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student_details")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # get cursor Function
    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    ###  Update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == ""or self.var_std_id.get == "":
            messagebox.showerror("Error", "All Fields are required", parent= self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Upadte", "DO you want to update this details", parent = self.root)
                if Upadate > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database= "face")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update Student_details set Dep=%s, course=%s, Year=%s,  Semester=%s, name = %s,Division=%s, Roll=%s, Gender= %s, Dob = %s, Email=%s, Phone = %s, Address=%s, Teacher=%s, PhotoSample=%s where student_id=%s", (
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_std_id.get()
                                    

                                    ))
                else:
                    if not Upadate:
                        return

                messagebox.showinfo("Success", "Student details successfully update complete", parent=self.root)

                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent= self.root)

                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database= "face")
                    my_cursor = conn.cursor()
                    sql = "delete from Student_details where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # reset Function
    def reset_data(self):
        self.var_dep.set("Select Departmnet")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        self.var_std_id.set("")
        

        
    #Generate data set Function
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == ""or self.var_std_id.get == "":
            messagebox.showerror("Error", "All Fields are required", parent= self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Hello@#123", database= "face")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from Student_details")
                myResult = my_cursor.fetchall()
                id = 0
                for x in myResult:
                    id += 1
                
                my_cursor.execute("update Student_details set Dep=%s, course=%s, Year=%s,  Semester=%s, name = %s,Division=%s, Roll=%s, Gender= %s, Dob = %s, Email=%s, Phone = %s, Address=%s, Teacher=%s, PhotoSample=%s where student_id=%s", (
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio1.get(),
                                    self.var_std_id.get() == id+1
                                    

                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on fronttals from opencv  
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5) #Scaling factor = 1.3, Minimum Number = 5
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img[y: y +h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/Student." + str(id) + "." + str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set Completed!", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
