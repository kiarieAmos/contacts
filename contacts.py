### Importing all the needed modules from tkinter
from tkinter import ttk
from tkinter import Tk, Button, Label, PhotoImage, LabelFrame, W, E, N, S,Entry, END, StringVar, Scrollbar, Toplevel

class Contacts:
    def __init__(self, root):
        self.root = root
        self.create_left_icon()     ## calling the function for the left icon
        self.create_label_frame()   ## calling the function for the labelframe.
        self.create_message_area()  ## calling the message function.
        self.create_tree_view()     ## calling the tree view function

        ## start of styling.##

        ttk.style = ttk.Style()
        ttk.style.configure('Treeview', font = ('helvetica', 10))
        ttk.style.configure('Treeview.Heading', font = ('helvetica', 12, 'bold'))
    
    def create_left_icon(self):
        photo = PhotoImage(file='icons/logo.png')
        label = Label(image=photo)
        label.image = photo
        label.grid(row = 0, column = 0)   ## positioning the image at the top left corner.

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text = 'Create New Contact', bg = 'sky blue', font = 'helvetica 10')
        labelframe.grid(row = 0, column = 1, padx = 8, pady = 8, sticky = 'ew')
        Label(labelframe, text = 'Name', bg = 'green', fg = 'white').grid(row = 1, column = 1, padx = 15, pady = 2, sticky = W)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row = 1, column = 2, padx = 5, pady = 2, sticky = 'w')
        Label(labelframe, text = 'Email', bg = 'brown', fg = 'white').grid(row = 2, column = 1, padx = 15, pady = 2, sticky = W)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row = 2, column = 2, padx = 5, pady = 2, sticky = 'w')
        Label(labelframe, text = 'Number', bg = 'black', fg = 'white').grid(row = 3, column = 1, padx = 15, pady = 2, sticky = W)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row = 3, column = 2, padx = 5, pady = 2, sticky = 'w')
        Button(labelframe, text = 'Add Contact', command = '', bg = 'blue', fg = 'white').grid(row = 4, column = 2, padx = 5, pady = 5, sticky = E)

    def create_message_area(self):
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 1, sticky = W)

    def create_tree_view(self):
        self.tree = ttk.Treeview(height = 10, columns = ('email', 'number'), style = 'Treeview')
        self.tree.grid(row = 6, column = 0, columnspan = 3)
        self.tree.heading('#0', text = 'Name', anchor = W)
        self.tree.heading("email", text = 'Email Address', anchor = W)
        self.tree.heading("number", text = 'Contact Number', anchor = W)


if __name__ == '__main__':
    root = Tk()
    root.title('My Contacts List')
    application = Contacts(root)
    root.mainloop()
