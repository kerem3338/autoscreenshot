from tkinter import *
import pyautogui
import time
root = Tk()
root.title("AutoScreenShot")
root.geometry("500x500")

def take_screenshot():
	
	if var.get() == 1:
		root.withdraw()
		time.sleep(2)
		screenshot = pyautogui.screenshot()
		screenshot.save(output.get("1.0",'end-1c'))
		time.sleep(2)
		root.deiconify()
	elif var.get() == 0:
		screenshot = pyautogui.screenshot()
		screenshot.save(output.get("1.0",'end-1c'))
	else:
		print("InvalidOption")
		print(var.get())
	
output = Text(root,width=150, height=1)
start = Button(root, text="Start!", command=take_screenshot)
var = IntVar()
hide = Checkbutton(root, text="Hide This Window", variable=var)

hide.pack()

start.pack()
output.pack()
root.mainloop()