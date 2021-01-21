from tkinter import *

# def onclick():
#    pass
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# root.mainloop()
# from tkinter import *

root = Tk()
root.geometry("1280x720")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
textbox = Text(root)
textbox.pack()
for i in range(100):
   textbox.insert(END, f"This is an example line {i}\n")
# attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

root.mainloop()