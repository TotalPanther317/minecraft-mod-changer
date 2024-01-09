import shutil
import os
from tkinter import *
import customtkinter as ctk

fActive = "#ffa500"
fDisabled = "#805300"
fCActive = "#00ffff"
fCDisabled = "#008080"
forgeActive = "#aa00ff"
forgeDisabled = "#800080"

numDirs = 3
mods = "nothing"

print(os.getenv('APPDATA'))

appdataPath = os.getenv('APPDATA')

def getEmpty():
    global mods
    i = 0
    while i < numDirs:
        i = i + 1
        dir = str(appdataPath) + "/.minecraft/mods" + str(i) + "/"
        print(dir)
        print(os.listdir(dir))
        if str(os.listdir(dir)) == "[]":
            print("got empty on " + str(i))
            emptyDir = i
    
    if emptyDir == 1:
        print("Fabric loaded")
        mods = "fabric"
        fabricCreate.configure(state=ACTIVE, bg_color=fCActive)
        fabricCreate.update()
        fabric.configure(state=DISABLED, bg_color=fDisabled)
        fabric.update()
        forge.configure(state=ACTIVE, bg_color=forgeActive)
        forge.update()
    elif emptyDir == 2:
        print("FabricCreate loaded")
        mods = "fabricCreate"
        fabricCreate.configure(state=DISABLED, bg_color=fCDisabled)
        fabricCreate.update()
        fabric.configure(state=ACTIVE, bg_color=fActive)
        fabric.update()
        forge.configure(state=ACTIVE, bg_color=forgeActive)
        forge.update()
    else:
        print("Forge loaded")
        mods = "forge"
        fabricCreate.configure(state=ACTIVE, bg_color=fCActive)
        fabricCreate.update()
        fabric.configure(state=ACTIVE, bg_color=fActive)
        fabric.update()
        forge.configure(state=DISABLED, bg_color=forgeDisabled)
        forge.update()


def useFabric():
    print("Fabric")

    #put out
    source_dir = str(appdataPath) + '/.minecraft/mods/'
    if mods == "fabricCreate":
        target_dir = str(appdataPath) + '/.minecraft/mods2/'
        print("moving to FabricCreate")
    elif mods == "forge":
        target_dir = str(appdataPath) + '/.minecraft/mods3/'
        print("moving to Forge")
    else:
        print("no target")
        
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    #put in
    source_dir = str(appdataPath) + '/.minecraft/mods1/'
    target_dir = str(appdataPath) + '/.minecraft/mods/'
    
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    
    getEmpty()

def useFabricCreate():
    print("FabricCreate")

    #put out
    source_dir = str(appdataPath) + '/.minecraft/mods/'
    if mods == "fabric":
        target_dir = str(appdataPath) + '/.minecraft/mods1/'
        print("moving to Fabric")
    elif mods == "forge":
        target_dir = str(appdataPath) + '/.minecraft/mods3/'
        print("moving to Forge")
    else:
        print("no target")
    
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    #put in
    source_dir = str(appdataPath) + '/.minecraft/mods2/'
    target_dir = str(appdataPath) + '/.minecraft/mods/'
    
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    
    getEmpty()

def useForge():
    print("Forge")

    #put out
    source_dir = str(appdataPath) + "/.minecraft/mods/"
    if mods == "fabric":
        target_dir = str(appdataPath) + '/.minecraft/mods1/'
        print("moving to Fabric")
    elif mods == "fabricCreate":
        target_dir = str(appdataPath) + '/.minecraft/mods2/'
        print("moving to FabricCreate")
    else:
        print("no target")
    
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    #put in
    source_dir = str(appdataPath) + '/.minecraft/mods3/'
    target_dir = str(appdataPath) + '/.minecraft/mods/'
    
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

    getEmpty()

def exitScript():
    os.system("TASKKILL /IM mc_mod_changer.exe /F")

def move_window(event):
    tk.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

tk = ctk.CTk()

#tk = Tk()
tk.configure(bg='black')
#tk.attributes('-topmost', 'true')
#tk.geometry("500x500")
#tk.overrideredirect(True)
tk.title("Minecraft mod changer")

#title_bar = ctk.CTkFrame(tk, bg="black", relief="raised", bd=0)
#title_bar.pack(expand=1, fill=X)
#title_bar.bind('<B1-Motion>', move_window)
#close_label = Button(title_bar, text="  X  ", bg="red", fg="white", relief="sunken", bd=0, command=exitScript)
#close_label.pack(side=RIGHT, pady=4)

if mods == "fabric":
    Label(tk, text="Fabric loaded").pack()

def updateButtons():
    print("nothing in here")

fabric = ctk.CTkButton(tk, text="Mods 1", width=175, font=("Arial", 20), corner_radius=0, border_spacing=0, border_color='black', bg_color='black', fg_color=fActive, text_color="black", state=ACTIVE, command=useFabric)
fabric.pack()

fabricCreate = ctk.CTkButton(tk, text="Mods 2", width=175, font=("Arial", 20), corner_radius=0, border_spacing=0, border_color='black', bg_color='black', fg_color=fCActive, text_color="black", state=ACTIVE, command=useFabricCreate)
fabricCreate.pack()

forge = ctk.CTkButton(tk, text="Mods 3", width=175, font=("Arial", 20), corner_radius=0, border_spacing=0, border_color='black', bg_color='black', fg_color=forgeActive, text_color="black", state=ACTIVE, command=useForge)
forge.pack()

fabric.configure(state=DISABLED)
fabricCreate.configure(state=DISABLED)
forge.configure(state=DISABLED)

getEmpty()

tk.mainloop()
    
#for file_name in file_names:
#    shutil.move(os.path.join(source_dir, file_name), target_dir)