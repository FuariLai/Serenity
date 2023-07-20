import os
import tkinter as tk
import tkinter.font as tkf
from PIL import Image
from tkinter import filedialog

start = 0
def only_numeric_input(P):
    if P.isdigit() or P == "":
        return True
    return False

def openpath():
    global nowpath, perpath
    nowpath = filedialog.askopenfilename(filetypes=[("Skin Config", "*.ini")])
    pathstr.set(nowpath)
    dirpath = os.path.dirname(nowpath)
    perpath = dirpath + "/score-percent.png"

def onkey():
    if not modevar.get() == "-1":
        onmode()

def onmode():
    fn1()
    define()
    if not nowpath:
        pass
    else:
        fn2()

def define():
    global cs, ch, cp
    if keyvar.get() == "4":
        cs = 89
        ch = 83
        cp = 86
    elif keyvar.get() == "5":
        cs = 142
        ch = 146
        cp = 148
    elif keyvar.get() == "6":
        cs = 209
        ch = 213
        cp = 215
    elif keyvar.get() == "7":
        cs = 284
        ch = 289
        cp = 287
def fn1():
    if modevar.get() == "5":
        value.place_forget()
        scale.place(x=55, y=310, width=200, height=80)
    elif modevar.get() == "3":
        value.place(x=55, y=310, width=200, height=30)
        scale.place_forget()
    else:
        value.place(x=55, y=310, width=200, height=30)
        scale.place_forget()

def fn2():
    global resulti, resultii, height, cs, ch, cp
    with open(nowpath, "r", encoding="cp949") as f:
        lines = f.readlines()
        if(keyvar.get() == "4"):
            if(modevar.get() == "1"):
                showvalue.set(lines[cs].strip())
                now.set("ColumnStart: " + value.get() + "\n")
                originvar.set("ColumnStart: 294")
                root.after(10, onmode)
            elif(modevar.get() == "2"):
                showvalue.set(lines[ch].strip())
                now.set("HitPosition: " + value.get() + "\n")
                originvar.set("HitPosition: 446")
                root.after(10, onmode)
            elif(modevar.get() == "3"):
                now.set("세부설정에서 설정하세요")
                originvar.set("세부설정에서 설정하세요")
                root.after(10, onmode)
            elif(modevar.get() == "4"):
                showvalue.set(lines[cp].strip())
                now.set("ComboPosition: " + value.get() + "\n")
                originvar.set("ComboPosition: 150")
                root.after(10, onmode)
            elif(modevar.get() == "5"):
                with Image.open(perpath) as image1:
                    width, height = image1.size
                    imagesc = (98 - scale.get()) * 20 * (4/3)
                    resulti = repr(int(imagesc))
                    perofi = "(" + repr(98 - scale.get()) + "%)"
                    resultii = (int(imagesc))
                    oldper = "(" + repr(round((width/2613) * 98, 1)) + "%)"
                    oldscale = "Scale: " + repr(width) + oldper + " x " + repr(height) + "\n"
                    nowscale = "Scale: " + resulti + perofi + " x " + repr(height) + "\n"
                    showvalue.set(oldscale)
                    now.set(nowscale)
                    originvar.set("Scale: 1280 x 148")
                    root.after(10, onmode)
                image1.close()
        elif(keyvar.get() == "5"):
            if(modevar.get() == "1"):
                showvalue.set(lines[cs].strip())
                now.set("ColumnStart: " + value.get() + "\n")
                originvar.set("ColumnStart: 299")
                root.after(10, onmode)
            elif(modevar.get() == "2"):
                showvalue.set(lines[ch].strip())
                now.set("HitPosition: " + value.get() + "\n")
                originvar.set("HitPosition: 444")
                root.after(10, onmode)
            elif(modevar.get() == "3"):
                now.set("세부설정에서 설정하세요")
                originvar.set("세부설정에서 설정하세요")
            elif(modevar.get() == "4"):
                showvalue.set(lines[cp].strip())
                now.set("ComboPosition: " + value.get() + "\n")
                originvar.set("ComboPosition: 150")
                root.after(10, onmode)
            elif(modevar.get() == "5"):
                with Image.open(perpath) as image1:
                    width, height = image1.size
                    imagesc = (98 - scale.get()) * 20 * (4/3)
                    resulti = repr(int(imagesc))
                    perofi = "(" + repr(98 - scale.get()) + "%)"
                    resultii = (int(imagesc))
                    oldper = "(" + repr(round((width/2613) * 98, 1)) + "%)"
                    oldscale = "Scale: " + repr(width) + oldper + " x " + repr(height) + "\n"
                    nowscale = "Scale: " + resulti + perofi + " x " + repr(height) + "\n"
                    showvalue.set(oldscale)
                    now.set(nowscale)
                    originvar.set("Scale: 1280 x 148")
                    root.after(10, onmode)
                image1.close()
        elif(keyvar.get() == "6"):
            if(modevar.get() == "1"):
                showvalue.set(lines[cs].strip())
                now.set("ColumnStart: " + value.get() + "\n")
                originvar.set("ColumnStart: 273")
                root.after(10, onmode)
            elif(modevar.get() == "2"):
                showvalue.set(lines[ch].strip())
                now.set("HitPosition: " + value.get() + "\n")
                originvar.set("HitPosition: 444")
                root.after(10, onmode)
            elif(modevar.get() == "3"):
                now.set("세부설정에서 설정하세요")
                originvar.set("세부설정에서 설정하세요")
            elif(modevar.get() == "4"):
                showvalue.set(lines[cp].strip())
                now.set("ComboPosition: " + value.get() + "\n")
                originvar.set("ComboPosition: 150")
                root.after(10, onmode)
            elif(modevar.get() == "5"):
                with Image.open(perpath) as image1:
                    width, height = image1.size
                    imagesc = (98 - scale.get()) * 20 * (4/3)
                    resulti = repr(int(imagesc))
                    perofi = "(" + repr(98 - scale.get()) + "%)"
                    resultii = (int(imagesc))
                    oldper = "(" + repr(round((width/2613) * 98, 1)) + "%)"
                    oldscale = "Scale: " + repr(width) + oldper + " x " + repr(height) + "\n"
                    nowscale = "Scale: " + resulti + perofi + " x " + repr(height) + "\n"
                    showvalue.set(oldscale)
                    now.set(nowscale)
                    originvar.set("Scale: 1280 x 148")
                    root.after(10, onmode)
                image1.close()
        elif(keyvar.get() == "7"):
            if(modevar.get() == "1"):
                showvalue.set(lines[cs].strip())
                now.set("ColumnStart: " + value.get() + "\n")
                originvar.set("ColumnStart: 247")
                root.after(10, onmode)
            elif(modevar.get() == "2"):
                showvalue.set(lines[ch].strip())
                now.set("HitPosition: " + value.get() + "\n")
                originvar.set("HitPosition: 444")
                root.after(10, onmode)
            elif(modevar.get() == "3"):
                now.set("세부설정에서 설정하세요")
                originvar.set("세부설정에서 설정하세요")
            elif(modevar.get() == "4"):
                showvalue.set(lines[cp].strip())
                now.set("ComboPosition: " + value.get() + "\n")
                originvar.set("ComboPosition: 150")
                root.after(10, onmode)
            elif(modevar.get() == "5"):
                with Image.open(perpath) as image1:
                    width, height = image1.size
                    imagesc = (98 - scale.get()) * 20 * (4/3)
                    resulti = repr(int(imagesc))
                    perofi = "(" + repr(98 - scale.get()) + "%)"
                    resultii = (int(imagesc))
                    oldper = "(" + repr(round((width/2613) * 98, 1)) + "%)"
                    oldscale = "Scale: " + repr(width) + oldper + " x " + repr(height) + "\n"
                    nowscale = "Scale: " + resulti + perofi + " x " + repr(height) + "\n"
                    showvalue.set(oldscale)
                    now.set(nowscale)
                    originvar.set("Scale: 1280 x 148")
                    root.after(10, onmode)
                image1.close()
    f.close()

def Imagemodify():
    if(modevar.get() == "5"):
        scale.State['normal']
    else:
        scale.State['normal']
def option():
    global cs, ch, cp
    if(keyvar.get() == "4"):
        if(modevar.get() == "1"):
            B = "ColumnStart: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cs] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "2"):
            B = "HitPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[ch] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "3"):
            mode3()
        if(modevar.get() == "4"):
            B = "ComboPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cp] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "5"):
            with Image.open(perpath) as image2:
                image2 = image2.resize((resultii, height))
                image2.save(perpath)
            image2.close()
    elif(keyvar.get() == "5"):
        if(modevar.get() == "1"):
            B = "ColumnStart: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cs] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "2"):
            B = "HitPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[ch] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "3"):
            mode3()
        if(modevar.get() == "4"):
            B = "ComboPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cp] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "5"):
            with Image.open(perpath) as image2:
                image2 = image2.resize((resultii, height))
                image2.save(perpath)
            image2.close()
    elif(keyvar.get() == "6"):
        if(modevar.get() == "1"):
            B = "ColumnStart: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cs] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "2"):
            B = "HitPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[ch] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "3"):
            mode3()
        if(modevar.get() == "4"):
            B = "ComboPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cp] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "5"):
            with Image.open(perpath) as image2:
                image2 = image2.resize((resultii, height))
                image2.save(perpath)
            image2.close()
    elif(keyvar.get() == "7"):
        if(modevar.get() == "1"):
            B = "ColumnStart: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cs] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "2"):
            B = "HitPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[ch] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "3"):
            mode3()
        if(modevar.get() == "4"):
            B = "ComboPosition: " + value.get() + "\n"
            with open(nowpath, 'r') as file:
                lines = file.readlines()
            lines[cp] = B
            with open(nowpath, 'w') as file:
                file.writelines(lines)
            file.close()
        if(modevar.get() == "5"):
            with Image.open(perpath) as image2:
                image2 = image2.resize((resultii, height))
                image2.save(perpath)
            image2.close()
    success1 = tk.Label(root, text="성공하였습니다.", font=fontsize)
    success1.place(x=300, y=340)
    success1.after(5000, success1.destroy)

def mode3():
    pass

def onmode1():
    if notesel.get() == "1":
        key1.place_forget()
        key2.place_forget()
        key3.place_forget()
        key4.place_forget()
        key5.place_forget()
        key6.place_forget()
        key7.place_forget()
        key8.place_forget()
        key9.place_forget()
        note1.place(x=55, y=100)
        note2.place(x=55, y=125)
        note3.place(x=55, y=150)
        note4.place(x=55, y=175)
        note5.place(x=55, y=200)
        note6.place(x=55, y=225)
        note7.place(x=55, y=250)
        note8.place(x=55, y=275)
        note9.place(x=55, y=300)
        note10.place(x=55, y=325)
    if notesel.get() == "2":
        note1.place_forget()
        note2.place_forget()
        note3.place_forget()
        note4.place_forget()
        note5.place_forget()
        note6.place_forget()
        note7.place_forget()
        note8.place_forget()
        note9.place_forget()
        note10.place_forget()
        key1.place(x=55, y=100)
        key2.place(x=55, y=125)
        key3.place(x=55, y=150)
        key4.place(x=55, y=175)
        key5.place(x=55, y=200)
        key6.place(x=55, y=225)
        key7.place(x=55, y=250)
        key8.place(x=55, y=275)
        key9.place(x=55, y=300)
def selectednote():
    pass

root = tk.Tk()
root.title("[Lai] 스킨 편집기")
root.geometry("600x400")

keyvar = tk.StringVar(value="-1")
tkke1 = tk.Radiobutton(root, text="4K", command=onkey, variable=keyvar, value="4")
tkke1.place(x=55, y=95)
tkke2 = tk.Radiobutton(root, text="5K", command=onkey, variable=keyvar, value="5")
tkke2.place(x=105, y=95)
tkke3 = tk.Radiobutton(root, text="6K", command=onkey, variable=keyvar, value="6")
tkke3.place(x=155, y=95)
tkke4 = tk.Radiobutton(root, text="7K", command=onkey, variable=keyvar, value="7")
tkke4.place(x=205, y=95)
modevar = tk.StringVar(value="-1")
tkop1 = tk.Radiobutton(root, text="Column Position", command=onmode, variable=modevar, value="1")
tkop1.place(x=55, y=150)
tkop2 = tk.Radiobutton(root, text="Judgement Line", command=onmode, variable=modevar, value="2")
tkop2.place(x=55, y=170)
tkop3 = tk.Radiobutton(root, text="Note Images", command=onmode, variable=modevar, value="3")
tkop3.place(x=55, y=190)
tkop4 = tk.Radiobutton(root, text="Combo Position", command=onmode, variable=modevar, value="4")
tkop4.place(x=55, y=210)
tkop5 = tk.Radiobutton(root, text="Rate Postion", command=onmode, variable=modevar, value="5")
tkop5.place(x=55, y=230)

fontsize = tkf.Font(size=10)
value = tk.Entry(root)
value.place(x=55, y=310, width=200, height=30)
vcmd = (root.register(only_numeric_input), '%P')
value.configure(validate='key', validatecommand=vcmd)
valuetext = tk.Label(root, text='변경하실 값을 입력해 주세요.', font=fontsize)
valuetext.place(x=55, y=285)
keytext = tk.Label(root, text='수정할 키를 선택해 주세요.', font=fontsize)
keytext.place(x=55, y=70)
modetext = tk.Label(root, text='변경하실 옵션을 선택해 주세요.', font=fontsize)
modetext.place(x=55, y=130)
button = tk.Button(root, text='변경', command=option, background="#C0E1FF", activebackground="#C0E1FF")
button.place(x=450, y=340, width=120, height=40)
selectk = keyvar.get()
selectm = modevar.get()
showvalue = tk.StringVar(value="0")
sva = tk.Label(root, textvariable=showvalue, font=fontsize)
sva.place(x=355, y=95)
svatext = tk.Label(root, text='현재 값', font=fontsize)
svatext.place(x=355, y=70)
svanow = tk.Label(root, text='변경할 값', font=fontsize)
svanow.place(x=355, y=130)
now = tk.StringVar(value="0")
svanow = tk.Label(root, textvariable=now, font=fontsize)
svanow.place(x=355, y=155)
originvar = tk.StringVar()
origin = tk.Label(root, text="기본 값", font=fontsize)
origin.place(x=355, y=190)
origintext = tk.Label(root, textvariable=originvar, font=fontsize)
origintext.place(x=355, y=215)
scale = tk.Scale(root, from_=0, to=98, orient=tk.HORIZONTAL, command=Imagemodify, label="실제 표시되는 위치입니다.", tickinterval=50, resolution=0.5)
filepath = tk.Button(root, text='파일 열기', command=openpath)
filepath.place(x=55, y=30)
nowpath = 0
pathstr = tk.StringVar()
nowp = tk.Entry(root, textvariable=pathstr, state="readonly")
nowp.place(x=130, y=30, width=400, height=25)
if os.path.exists(nowpath):
    pass
else:
    nopath = "파일이 존재하지 않습니다."
    nowp.insert(0, nopath)

root.resizable(False,False)
root.mainloop()

setting = tk.Tk()
setting.title("[Lai] Editor")
setting.geometry("600x400")
notesel = tk.StringVar(value=-1)
note = tk.Button(setting, text='수정하기')
note.place(x=450, y=340, width=120, height=40)
notesec = tk.Radiobutton(setting, text='Note', command=onmode1, variable=notesel, value="1")
notesec.place(x=55, y=40)
keysec = tk.Radiobutton(setting, text='Key', command=onmode1, variable=notesel, value="2")
keysec.place(x=135, y=40)
keybeamsel = tk.IntVar(value=-1)
keybeam = tk.Checkbutton(setting, text="키빔 표시", variable=keybeamsel)
keybeam.place(x=350, y=347)
keybeam.place()

notesel1 = tk.StringVar(value="-1")
note1 = tk.Radiobutton(setting, text='Alpha', command=selectednote, variable=notesel1, value="1")
note1.place_forget
note2 = tk.Radiobutton(setting, text='Arrow', command=selectednote, variable=notesel1, value="2")
note2.place_forget
note3 = tk.Radiobutton(setting, text='Bar', command=selectednote, variable=notesel1, value="3")
note3.place_forget
note4 = tk.Radiobutton(setting, text='Circle(Bojii)', command=selectednote, variable=notesel1, value="4")
note4.place_forget
note5 = tk.Radiobutton(setting, text='Circle(Original)', command=selectednote, variable=notesel1, value="5")
note5.place_forget
note6 = tk.Radiobutton(setting, text='Circle(Big)', command=selectednote, variable=notesel1, value="6")
note6.place_forget
note7 = tk.Radiobutton(setting, text='Diamond', command=selectednote, variable=notesel1, value="7")
note7.place_forget
note8 = tk.Radiobutton(setting, text='Round Diamond', command=selectednote, variable=notesel1, value="8")
note8.place_forget
note9 = tk.Radiobutton(setting, text='Round Diamond(No Gradient)', command=selectednote, variable=notesel1, value="9")
note9.place_forget
note10 = tk.Radiobutton(setting, text='Rskin', command=selectednote, variable=notesel1, value="10")
note10.place_forget

notesel2 = tk.StringVar(value="-1")
key1 = tk.Radiobutton(setting, text='[4K]Circle', command=selectednote, variable=notesel2, value="1")
key1.place_forget
key2 = tk.Radiobutton(setting, text='[4K]Circle(high)', command=selectednote, variable=notesel2, value="2")
key2.place_forget
key3 = tk.Radiobutton(setting, text='[4K]Diamond', command=selectednote, variable=notesel2, value="3")
key3.place_forget
key4 = tk.Radiobutton(setting, text='[4K]Round Diamond', command=selectednote, variable=notesel2, value="4")
key4.place_forget
key5 = tk.Radiobutton(setting, text='[4K]Round Diamond(high)', command=selectednote, variable=notesel2, value="5")
key5.place_forget
key6 = tk.Radiobutton(setting, text='[4K]Arrow', command=selectednote, variable=notesel2, value="6")
key6.place_forget
key7 = tk.Radiobutton(setting, text='Circle', command=selectednote, variable=notesel2, value="7")
key7.place_forget
key8 = tk.Radiobutton(setting, text='Round Diamond', command=selectednote, variable=notesel2, value="8")
key8.place_forget
key9 = tk.Radiobutton(setting, text='Rskin', command=selectednote, variable=notesel2, value="9")
key9.place_forget


"""
할 일 : 3번, 5번 활성화하기(3번은 경로수정, 5번은 PIL이용)
3번 활성화 되었을 때 Entry 잠그기
5번 활성화 되었을 때 Entry 대신 Bar 설치하기
Bing AI굴려서 원하는거 찾기: Scale Wiget 쓸건데 여기서 1920*(n/100)으로 이미지 가로 조절해줄거임
var = tk.Scale 이용하기

from tkinter import *

root = Tk()
root.geometry("200x200")

def show_value(val):
    label.config(text=val)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=show_value)
scale.pack()

label = Label(root)
label.pack()

root.mainloop()
BingAI 왈 이렇게 라고 함

from PIL import Image

# 이미지 파일 열기
image = Image.open('image.jpg')
width, height = image.size
new_width = 300
image = image.resize((new_width, new_height), Image.ANTIALIAS)
image.save('resized_image.jpg')



"""