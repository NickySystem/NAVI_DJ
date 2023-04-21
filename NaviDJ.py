import os
import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence

song1_list = [" ", " ", " "]
song2_list = [" ", " ", " "]

bgColour = "#454545"
##F49EF3

def send2pd(message = ''):
    os.system("echo " + message +"|" + pdFilePath + "pdsend 6000 127.0.0.1 udp")

#Set user input to be sent to PD
def sendCommand():
    send2pd(player_name.get())
    
def printValue():
    global lstCmdIndex
    # get, send and print last command
    pname = player_name.get()
    #Label(canvas, text=f'>_ {pname}', pady=20, bg='#ffbf00').pack()
    sendCommand()
    player_name.delete(0,100)
    
    if pname.startswith("deck1 load "):
        song1_list = pname.split()
        dek1.config(text = "deck 1: " + song1_list[2] )
    if pname.startswith("deck2 load "):
        song2_list = pname.split()
        dek2.config(text = "deck 2: " + song2_list[2] )
    
def handler(e):
    #what to do when ENTER key is hit
    printValue()
    
def dek1Up():
    send2pd("lain deck1 bang")
    
def dek2Up():
    send2pd("lain deck2 bang")
    
filePath = open('pdpath.txt')
pathContent = filePath.read().splitlines()
pdFilePath = pathContent[0]

root = Tk()
root.title("DJ_NAVI")
#root.geometry('1080x800')
#set window background colour
root['bg'] = bgColour
#make it full screen and write size to a variable
root.geometry("700x750")
root.iconbitmap("icon.ico")
wWidth = root.winfo_screenwidth()
wHeight = root.winfo_screenheight()
#bind the enter key to entering text and call a function called handler
root.bind('<Return>',handler)

canvas=Canvas(root, width = wWidth, height= wHeight,  bg = bgColour)
canvas.pack()


pad=ImageTk.PhotoImage(file="pad3.png")
canvas.create_image(350, 400, image=pad, anchor="center")

#command entry box
player_name = Entry(
    canvas,
    width=30,
    font = ("Helvetica", 16)
    )
player_name.place(x = 75, y = 50)
player_name.insert(0, "enter command...")

dek1 = Label(root, text = "deck 1: " + song1_list[2] , bg = bgColour, font = ("Helvetica", 16), anchor = W, fg = "#ff9cfc")
dek1.place(x = 75, y = 100)
dek2 = Label(root, text = "deck 2: " + song2_list[2], bg = bgColour, font = ("Helvetica", 16), anchor = W, fg = "#ff9cfc")
dek2.place(x = 75, y = 150)

root.mainloop()