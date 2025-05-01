### Importing all the needed modules from tkinter
from tkinter import ttk
from tkinter import Tk, Button, Label, PhotoImage, LabelFrame, W, E, N, S,Entry, END, StringVar, Scrollbar, Toplevel

class Contacts:
    def __init__(self, root):
        self.root = root
        self.create_left_icon()     ## calling the function
    
    def create_left_icon(self):
        photo = PhotoImage(file='icons/logo.png')
        label = Label(image=photo)
        label.image = photo
        label.grid(row = 0, column = 0)   ## positioning the image at the top left corner.

if __name__ == '__main__':
    root = Tk()
    root.title('My Contacts List')
    application = Contacts(root)
    root.mainloop()