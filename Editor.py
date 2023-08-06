from CodeR import Boot
from Def import VeC
import tkinter as tk
import webbrowser
import subprocess as sp

def stop():
    webbrowser.open_new("https://github.com/FuariLai/Serenity")
    exit()
def checkv():
    if defver1 == 1:
        verc = tk.Tk()
        verc.title("[Darae] Update Checker")
        verc.eval('tk::PlaceWindow . center')
        verc.geometry("175x100")
        update = tk.Label(verc, text='업데이트가 있습니다.')
        update.place(x=28, y=20)
        iniv = tk.StringVar(value='현재: ' + repr(VeC.nowver) + '\n' + '최신: ' + VeC.iniverorigin)
        ver = tk.Label(verc, textvariable=iniv)
        ver.place(x=10,y=55)
        button = tk.Button(verc, text='업데이트', command=stop)
        button.place(x=80, y=55, width=75, height=30)
        verc.attributes('-toolwindow', True)
        verc.mainloop()
    elif defver1 == 2:
        Boot.startUI()
    else:
        vercw = tk.Tk()
        vercw.title("[Darae] Wrong Version")
        vercw.eval('tk::PlaceWindow . center')
        vercw.geometry("175x100")
        update = tk.Label(vercw, text='유효하지 않은 버전입니다.')
        update.place(x=5,y=20)
        iniv = tk.StringVar(value='현재: ' + repr(VeC.nowver) + '\n' + '최신: ' + VeC.iniverorigin)
        ver = tk.Label(vercw, textvariable=iniv)
        ver.place(x=10,y=55)
        button = tk.Button(vercw, text='업데이트', command=stop)
        button.place(x=80, y=55, width=75, height=30)
        vercw.attributes('-toolwindow', True)
        vercw.mainloop()

VeC.getLV()
defver1 = int(VeC.defver)
print('유효성 검사: ' + repr(defver1))
checkv()