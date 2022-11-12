from tkinter import*
from tkinter import ttk


class Login_Window:
    def __init__(self, root):
      self.root = root
      self.root.title("Login")
      self.root.geometer("1550X800+0+0")

     
      label_bg = Label(self.root, image="blue")
      label_bg.place(x=0, y=0, relwidth=1, relheight=1)  #relwidth=1, relheight=1 vertivcal HORIZONTAL offset

       frame = Frame(self.root, bg= "white")
       frame.place(x= 610, y=170, width = 340, height = 540)


if __name__ == "_main_" :
    root = Tk()
    app= Login_Window(root)
    root.mainloop()
