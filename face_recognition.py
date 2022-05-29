from cmath import nan
from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import pandas as pd


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1270x650+0+0")
        self.root.title("face recognition System")

        #Title Label
        title_lbl=Label(self.root, text="Mark Attendance",font= ("Arial Narrow", 35, "italic"),  bg="darkblue", fg = "white")
        title_lbl.place(x = 0, y=0, width=1270, height=70)

        #Back Ground image
        img3 = Image.open(r"images\white.jpg")
        img3 = img3.resize((1500, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=70, width=1500, height=710)

        #Training images
        train_img = Image.open(r"images\train.png")
        train_img = train_img.resize((200, 210))
        self.photoimg4 = ImageTk.PhotoImage(train_img)

        #train Image Button
        train = Button(
            bg_img, image=self.photoimg4, command=self.train_classifier, cursor="hand2"
        )
        train.place(x=210, y=100, width=200, height=220)

        train_btn = Button( bg_img, text = 'Train Data', command = self.train_classifier, cursor="hand2", font=("times new roman", 13, "bold"), bg = "darkblue", fg = "white",activebackground="darkblue",
            activeforeground="white")
        train_btn.place(x=210, y=320, width=200, height=40)

        #Marking Attendance
        mark_img = Image.open(r"images\mark_attendance.jpg")
        mark_img = mark_img.resize((200, 210))
        self.photo_mark = ImageTk.PhotoImage(mark_img)

        mark = Button(
            bg_img, image=self.photo_mark, command=self.face_recognition, cursor="hand2"
        )
        mark.place(x=470, y=100, width=200, height=220)

        b1_1 = Button(
            bg_img,
            command=self.face_recognition,
            text="Mark Attendance",
            cursor="hand2",
            
            font=("times new roman", 15, "bold"),
            bg="dark blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="white"
        )
        b1_1.place(x=470, y=320, width=200, height=40)


        #photos
        images_img = Image.open(r"images\collage.jpg")
        images_img = images_img.resize((200, 210))
        self.photo_image = ImageTk.PhotoImage(images_img)

        images = Button(
            bg_img, image=self.photo_image, command=self.open_img, cursor="hand2"
        )
        images.place(x=730, y=100, width=200, height=220)


        b1_1 = Button(
            bg_img,
            text="photos",
            cursor="hand2",
            command=self.open_img,
            font=("times new roman", 15, "bold"),
            bg="dark blue",
            fg="white",
            activebackground="darkblue",
            activeforeground="white"
        )
        b1_1.place(x=730, y=320, width=200, height=40)

    #Train
    def train_classifier(self):
        data_dir = ("data") #give folder name
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Grey scale image
            imageNp=np.array(img, 'uint8')  #unit8 -- data type
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train the classifier And Save 
       
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "training datasets completed!", parent=self.root)
    
    
    #photos
    def open_img(self):
        os.startfile("data")
    
    #Attendance
    def mark_attendance(self, i, n):
        df = pd.read_csv("attendance.csv")
        columns = df.columns.tolist()
        id_list = df['Id'].tolist()
        student_names = df['Names'].tolist()
        dates = columns[2:]
        all_rows = df.values.tolist()
        now = datetime.now()
        d1=now.strftime("%d-%m-%Y")

        if df[d1].isnull().all():
            df[d1] = ["Absent"] * len(df.index)
        
        if (int(i) in id_list):
            df.loc[df["Id"] == i, d1] = "Present"

        if (int(i) not in id_list):
            all_rows = df.values.tolist()
            id_list = df['Id'].tolist()
            df.loc[len(df.index)] = [i, n] + [np.NaN] * len(dates)
            df.loc[df["Id"] == i, d1] = "Present"
          



        df1 = pd.DataFrame()
        df1.to_csv("attendance.csv")

        df.to_csv("attendance.csv", index=False)



#face recognition

    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict /300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="", database= "face")
                my_cursor = conn.cursor()


                my_cursor.execute("select Name from Student_details where Student_id = " + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Student_id from Student_details face where Student_id = " + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    self.mark_attendance(i, n)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)
                    cv2.putText(img, "Unkonown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                # coord = [x, y, w, h]
                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Press q after face is recognized", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        videoCap.release()
       
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
