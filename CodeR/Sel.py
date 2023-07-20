import tkinter as tk

def selectednote():
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

setting = tk.Tk()
setting.title("[Darae] Editor")
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

setting.resizable(False,False)
setting.mainloop()
