from tkinter import*            #tkinter와 그 안에 내장함수 호출
from PIL import ImageTk, Image  #이미지를 객체화 내장함수 ImageTk 호출
import random                   #랜덤 변수 내장함수 호출


def startTimer():               #타이머 작동 함수
    if (running):
        global timer
        timer -= 1
        timeText.configure(text=str(timer))

    win.after(1000, startTimer)
    
    if (timer == 0) :
        timer = 0
        stop()
        

    
def start():
    global running
    running = True

def stop():
    global running
    running = False

def reset():
    global running
    running = False
    
    global timer
    timer = 60
    timeText.config(text='60')

running = False



def pushup():
    record_text = "pushup 횟수 : " + record.get()
    pushuplabel.config(text=record_text)
    
def dumpbell():
    record_text = "dumpbell 횟수 : " + record.get()
    dumplabel.config(text=record_text)
    
def crench():
    record_text = "crench 횟수 : " + record.get()
    crenchlabel.config(text=record_text)
    
def squat():
    record_text = "squat 횟수 : " + record.get()
    squatlabel.config(text=record_text)
    
def pullup():
    record_text = "pullup 횟수 : " + record.get()
    pulluplabel.config(text=record_text)
    

win = Tk()
win.geometry("956x700")
win.title("오늘 뭐하지?")

back = ImageTk.PhotoImage(file = "back.jpg")
back_label = Label(win, image = back)
back_label.place(x=0,y=0)

label1 = Label(win, text = "")




pushuplabel=Label(win, text="", font = ('돋움',13))
pushuplabel.place(x=400,y=550)
dumplabel=Label(win, text="", font = ('돋움',13))
dumplabel.place(x=400,y=580)
crenchlabel=Label(win, text="", font = ('돋움',13))
crenchlabel.place(x=400,y=610)
squatlabel=Label(win, text="", font = ('돋움',13))
squatlabel.place(x=400,y=640)
pulluplabel=Label(win, text="", font = ('돋움',13))
pulluplabel.place(x=400,y=670)


record = Entry(win, width=30, font=('궁서',13))
record.place(x=580,y=600)


part = '가슴','팔','복근','하체','등'


def change():
    value = random.choice(part)
    
    label1.config(text="오늘은 "+value+" 운동 어떠세요?", font=("궁서", 20),fg="#FF0000")
    label1.place(x=320,y=10)
    
    global photo1
    photo1 = ImageTk.PhotoImage(file="pushup.jpg")

    global photo2
    photo2 = ImageTk.PhotoImage(file="press.jpg")

    global photo3
    photo3 = ImageTk.PhotoImage(file="crench.jpg")

    global photo4
    photo4 = ImageTk.PhotoImage(file="squat.jpg")

    global photo5
    photo5 = ImageTk.PhotoImage(file="pullup.jpg")
    

    
    if (value == '가슴') :
        label2 = Label(win, image=photo1)
        label2.config(image=photo1)
        label2.place(x=6, y=70)
        btn2 = Button(win, text = "기록 입력",font = ('돋움',15), command=pushup)
        btn2.place(x=580,y=630)


    elif (value == '팔') :
        label3 = Label(win, image=photo2)
        label3.config(image=photo2)
        label3.place(x=6, y=70)
        btn2 = Button(win, text = "기록 입력",font = ('돋움',15), command=dumpbell)
        btn2.place(x=580,y=630)
       

        
    elif (value == '복근') :
        label3 = Label(win, image=photo3)
        label3.config(image=photo3)
        label3.place(x=6, y=70)
        btn2 = Button(win, text = "기록 입력", font = ('돋움',15), command=crench)
        btn2.place(x=580,y=630)
 
    elif (value == '하체') :
        label3 = Label(win, image=photo4)
        label3.config(image=photo4)
        label3.place(x=6, y=70)
        btn2 = Button(win, text = "기록 입력",font = ('돋움',15), command=squat)
        btn2.place(x=580,y=630)
    

    else : 
        label3 = Label(win, image=photo5)
        label3.config(image=photo5)
        label3.place(x=6, y=70)
        btn2 = Button(win, text = "기록 입력",font = ('돋움',15), command=pullup)
        btn2.place(x=580,y=630)
    
    
timer = 60
    
timeText = Label(win, text='60', font=("궁서",95))
timeText.place(x=65,y=550)

startButton = Button(win, text = 'Start',bg='#FFFFE0',font =('돋움', 18),command=start)
startButton.place(x=220,y=550)

stopButton = Button(win, text = 'Stop',bg='#FFFFE0',font =('돋움', 18),command=stop)
stopButton.place(x=220,y=595)

resetButton = Button(win, text = 'Reset',bg='#FFFFE0',font =('돋움', 18),command=reset)
resetButton.place(x=220,y=640)  

startTimer()    
   
btn = Button(win, text = "오늘 운동 뭐하지?", bg='#E6E6FA',font=("궁서",20), command=change)
btn.place(x=5, y= 5)


win.mainloop()   
