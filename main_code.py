import cv2
from tkinter import *
import tkinter.filedialog
import PIL.Image, PIL.ImageTk
from utils import  image_resize


#prepare the detection cascades
face_cascade        = cv2.CascadeClassifier('Classifiers/haarcascade_frontalface_default.xml')
eyes_cascade        = cv2.CascadeClassifier('Classifiers/frontalEyes35x16.xml')


#Ahmed Samir (Code integration cv with TKinter)
#Rogina romani,Cathrine(Organizing the UI adding buttons and more glasses)

#start the application class
class App:
     def __init__(self):
        global window

        window=Tk()

        window.title("A-Team Shop")
        label1 =Label(text="Welcome to the A-team shop", fg='black')
        label2 = Label(text="Choose the BEST from the LIST ", fg='black')
        label3 =Label(text="Choose your type of glasses", fg="black")
        label4 = Label(text="Select live-video or picture", fg="black")
        label5 = Label(text="Press S to take screenshot and save it ", fg="black")
        label6 = Label(text="Press N to try another glass", fg="black")

        label1.grid(row=0, column=3)
        label2.grid(row=2, column=3)
        label3.grid(row=7, column=0)
        label4.grid(row=4, column=0)
        label5.grid(row=17, column=0)
        label6.grid(row=18, column=0,sticky=W)

        # creating the buttons
        global btn_sun
        global btn_eye
        btn_sun = Button(window, bg="orange", text="Sun glasses", command=show_sun)
        btn_eye = Button(window, bg="orange", text="Eye glasses", command=show_eye)
        btn_sun.grid(row=8, column=1)
        btn_eye.grid(row=8, column=4)

        quitButton = Button(window, text="Quit", command=window.destroy)
        quitButton.grid(row=20, column=3)



        global video_button
        i =IntVar()
        #video_button = Button(window, text="Live-video", width="10", height="5", command=frame_source())
        #video_button.grid(row=2)
        video =Radiobutton(window, text="video", variable=i, value=1)
        video.grid(row=6,column=1)

        global picture_button
        #picture_button = Button(window, text="Picture", width="10", height="5")
        #picture_button.grid(row=3)
        picture=Radiobutton(window, text="picture", variable=i, value=2)
        picture.grid(row=6,column=4)

        # read all the glasses you want to add
        sun_glass1 = cv2.imread('Sun_Glasses/glass8.png', -1)
        sun_glass2 = cv2.imread('Sun_Glasses/glass7.png', -1)
        sun_glass3 = cv2.imread('Sun_Glasses/glass2.png', -1)
        sun_glass4 = cv2.imread('Sun_Glasses/Picture1.png', -1)
        sun_glass5 = cv2.imread('Sun_Glasses/Picture2.png', -1)
        sun_glass6 = cv2.imread('Sun_Glasses/Picture4.png', -1)
        eye_glass1 = cv2.imread('Eye_Glasses/Orange glasses.png', -1)
        eye_glass2 = cv2.imread('Eye_Glasses/Blue glasses.png', -1)
        eye_glass3 = cv2.imread('Eye_Glasses/Heart Glasses.png', -1)
        eye_glass4 = cv2.imread('Eye_Glasses/Tiger glasses.png', -1)
        eye_glass5 = cv2.imread('Eye_Glasses/Rectangle_Black frame.png', -1)
        eye_glass6 = cv2.imread('Eye_Glasses/Brown glasses.png', -1)
        # eye_glass6 = cv2.imread('Eye_Glasses/Orange glasses.png', -1)

        # convert glasses images to RGB
        glass_s1 = cv2.cvtColor(sun_glass1, cv2.COLOR_BGR2RGBA)
        glass_s2 = cv2.cvtColor(sun_glass2, cv2.COLOR_BGR2RGBA)
        glass_s3 = cv2.cvtColor(sun_glass3, cv2.COLOR_BGR2RGBA)
        glass_s4 = cv2.cvtColor(sun_glass4, cv2.COLOR_BGR2RGBA)
        glass_s5 = cv2.cvtColor(sun_glass5, cv2.COLOR_BGR2RGBA)
        glass_s6 = cv2.cvtColor(sun_glass6, cv2.COLOR_BGR2RGBA)
        glass_e1 = cv2.cvtColor(eye_glass1, cv2.COLOR_BGR2RGBA)
        glass_e2 = cv2.cvtColor(eye_glass2, cv2.COLOR_BGR2RGBA)
        glass_e3 = cv2.cvtColor(eye_glass3, cv2.COLOR_BGR2RGBA)
        glass_e4 = cv2.cvtColor(eye_glass4, cv2.COLOR_BGR2RGBA)
        glass_e5 = cv2.cvtColor(eye_glass5, cv2.COLOR_BGR2RGBA)
        glass_e6 = cv2.cvtColor(eye_glass6, cv2.COLOR_BGR2RGBA)


        # resize a copy of them to make sure they fit in the button size
        glass_sun1 = cv2.resize(glass_s1.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_sun2 = cv2.resize(glass_s2.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_sun3 = cv2.resize(glass_s3.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_sun4 = cv2.resize(glass_s4.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_sun5 = cv2.resize(glass_s5.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_sun6 = cv2.resize(glass_s6.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye1 = cv2.resize(glass_e1.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye2 = cv2.resize(glass_e2.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye3 = cv2.resize(glass_e3.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye4 = cv2.resize(glass_e4.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye5 = cv2.resize(glass_e5.copy(), (0, 0), fx=0.3, fy=0.3)
        glass_eye6 = cv2.resize(glass_e6.copy(), (0, 0), fx=0.3, fy=0.3)
        # glass_smalln=cv2.resize(glassesn.copy(), (0,0),fx=0.3,fy=0.3)

        #Sunglasses
        global btn0
        global btn1
        global btn2
        global btn3
        global btn4
        global btn5
        global btn6
        global btn7
        global btn8
        global btn9
        global btn10
        global btn11

        # getting the opencv images ready to be added to the buttons by conversion using pillow
        photo0 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun1))
        photo1 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun2))
        photo2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun3))
        photo3 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun4))
        photo4 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun5))
        photo5 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_sun6))
        photo6 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye1))
        photo7 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye2))
        photo8 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye3))
        photo9 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye4))
        photo10 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye5))
        photo11 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(glass_eye6))
        # photon = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(glass_smalln))


        btn0 = Button(window, image=photo0, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass1))
        btn1 = Button(window, image=photo1, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass2))
        btn2 = Button(window, image=photo2, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass3))
        btn3 = Button(window, image=photo3, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass4))
        btn4 = Button(window, image=photo4, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass5))
        btn5 = Button(window, image=photo5, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),sun_glass6))
        btn6 = Button(window, image=photo6, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass1))
        btn7 = Button(window, image=photo7, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass2))
        btn8 = Button(window, image=photo8, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass3))
        btn9 = Button(window, image=photo9, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass4))
        btn10 = Button(window, image=photo10, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass5))
        btn11 = Button(window, image=photo11, bg="white", width=200, height=70, command=lambda: put_glasses(i.get(),eye_glass6))
        #btnn=Button(window, image=photon, bg="white",width=100,height=50)



        window.mainloop()

#Aya Adel(Functions to show the glasses, modifying the glasses photos in the Sun_glasses and eye_glasses folders)
def show_sun():
    btn0.grid(row=9, column=1)
    btn1.grid(row=10, column=1)
    btn2.grid(row=11, column=1)
    btn3.grid(row=12, column=1)
    btn4.grid(row=13, column=1)
    btn5.grid(row=14, column=1)
    #btnn.grid(row=2, column=n)

def show_eye():

  btn6.grid(row=9, column=4)
  btn7.grid(row=10, column=4)
  btn8.grid(row=11, column=4)
  btn9.grid(row=12, column=4)
  btn10.grid(row=13, column=4)
  btn11.grid(row=14, column=4)
  #btnn.grid(row=2, column=n)



#Aya Abdelhamid (Eye and face detection and adding the glasses)
def put_glasses(x,glasses):
    if x==1:
        # start video capture
        # the code for replacing the eye pixels with glasses
        cap = cv2.VideoCapture(0)

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            framenew = filter(frame, glasses)
            framenew = cv2.cvtColor(framenew, cv2.COLOR_BGRA2BGR)
            cv2.imshow('frame', framenew)
            keypress = cv2.waitKey(1)
            if keypress == 110:
                cap.release()
                cv2.destroyAllWindows()
                break
            elif keypress == 115:
                cv2.imshow('New-look', framenew)
                cv2.imwrite("New-look.jpg", framenew)




            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

    elif x==2:
        path = tkinter.filedialog.askopenfilename()
        frame = cv2.imread(path)
        framenew =filter(frame, glasses)
        cv2.imshow('frame', framenew)
        keypress = cv2.waitKey(1)
        while (True):
            keypress = cv2.waitKey(1)
            if keypress == 110:
                cv2.destroyAllWindows()
                break
            elif keypress == 115:
                cv2.imshow('New-look', framenew)
                cv2.imwrite("New Look/New-look.jpg", framenew)

def filter(frame, glasses):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + h]  # rec
        roi_color = frame[y:y + h, x:x + h]
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(roi_color, (ex, ey), (ex + eh, ey + ew), (0, 255, 0), 3)
            roi_eyes = roi_gray[ey: ey + eh, ex: ex + ew]

            glasses2 = image_resize(glasses.copy(), width=eh)

            gw, gh, gc = glasses2.shape
            for i in range(0, gw):
                for j in range(0, gh):
                    # print(glasses[i, j]) #RGBA
                    if glasses2[i, j][3] != 0:  # alpha 0
                        roi_color[ey + i, ex + j] = glasses2[i, j]

    return frame

    # Create a window and pass it to the Application object


App()


