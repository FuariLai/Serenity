import tkinter as tk
from tkinter import PhotoImage
from PIL import Image

def go():
    selectednote()
    update_image()
def selectednote():
    pass
def update_image():
    if not notesel1.get() == "Image/blank.png":
        textt.place(x=350, y=70)
    image_name = notesel1.get()
    image1 = Image.open(image_name)
    image1.thumbnail((120, 120))
    image1.save(image_name)
    image = PhotoImage(file=image_name)
    label.config(image=image)
    label.Ntimage = image
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

setting = tk.Tk()
setting.title("[Lai] Editor")
setting.geometry("600x400")
notesel = tk.StringVar(value="-1")
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
NtImage = PhotoImage(file="Image/blank.png")
label = tk.Label(setting, image=NtImage)
label.place(x=350, y=100, width=120, height=120)
textt = tk.Label(setting, text="미리보기")
textt.place_forget()
notesel1 = tk.StringVar(value="Image/blank.png")
note1 = tk.Radiobutton(setting, text='Alpha', value="Image/alpha.png", command=go, variable=notesel1)
note1.place_forget
note2 = tk.Radiobutton(setting, text='Arrow', value="Image/arrow.png", command=go, variable=notesel1)
note2.place_forget
note3 = tk.Radiobutton(setting, text='Bar', value="Image/bar.png", command=go, variable=notesel1)
note3.place_forget
note4 = tk.Radiobutton(setting, text='Circle(Bojii)', value="Image/circlebo.png", command=go, variable=notesel1)
note4.place_forget
note5 = tk.Radiobutton(setting, text='Circle(Original)', value="Image/circleor.png", command=go, variable=notesel1)
note5.place_forget
note6 = tk.Radiobutton(setting, text='Circle(Big)', value="Image/circlebi.png", command=go, variable=notesel1)
note6.place_forget
note7 = tk.Radiobutton(setting, text='Diamond', value="Image/rhombus.png", command=go, variable=notesel1)
note7.place_forget
note8 = tk.Radiobutton(setting, text='Round Diamond', value="Image/rounddia.png", command=go, variable=notesel1)
note8.place_forget
note9 = tk.Radiobutton(setting, text='Round Diamond(No Gradient)', value="Image/rounddiano.png", command=go, variable=notesel1)
note9.place_forget
note10 = tk.Radiobutton(setting, text='Rskin', value="Image/rskin.png", command=go, variable=notesel1)
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

setting.resizable(False,False)
setting.mainloop()