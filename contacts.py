### Importing all the needed modules from tkinter
from tkinter import ttk
from tkinter import Tk, Button, Label, PhotoImage, LabelFrame, W, E, N, S,Entry, END, StringVar, Scrollbar, Toplevel
import sqlite3              ## module for database interaction.

class Contacts:
    db_filename = 'contacts.db'  ### A variable that stores the database filename.
    def __init__(self, root):
        self.root = root
        self.create_gui()

        ## start of styling.##

        ttk.style = ttk.Style()
        ttk.style.configure('Treeview', font = ('helvetica', 10))
        ttk.style.configure('Treeview.Heading', font = ('helvetica', 12, 'bold'))

    def execute_db_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_filename) as conn:
            print(conn)
            print('You have successfully connected to the database.')
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def create_gui(self):
        self.create_left_icon()             ## calling the function for the left icon
        self.create_label_frame()           ## calling the function for the labelframe.
        self.create_message_area()          ## calling the message function.
        self.create_tree_view()             ## calling the tree view function
        self.create_bottom_buttons()        ## calling the bottom buttons function
        self.create_scrollbar()             ## calling the scrollbar function


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
        Button(labelframe, text = 'Add Contact', command = self.on_add_contact_button_clicked, bg = 'blue', fg = 'white').grid(row = 4, column = 2, padx = 5, pady = 5, sticky = E)

    def create_message_area(self):
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 1, sticky = W)

    def create_tree_view(self):
        self.tree = ttk.Treeview(height = 10, columns = ('email', 'number'), style = 'Treeview')
        self.tree.grid(row = 6, column = 0, columnspan = 3)
        self.tree.heading('#0', text = 'Name', anchor = W)
        self.tree.heading("email", text = 'Email Address', anchor = W)
        self.tree.heading("number", text = 'Contact Number', anchor = W)
        self.view_contacts()  ## I added this

    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient = 'vertical', command = self.tree.yview)
        self.scrollbar.grid(row = 6, column = 3, rowspan = 10, sticky = 'sn')

    def create_bottom_buttons(self):
        Button(text = "Delete Selected", command = self.on_delete_selected_button_clicked, bg = 'red', fg = 'white').grid(row = 8, column = 0, sticky = W, pady = 10, padx = 20)
        Button(text = 'Modify Selected', command = '', bg = 'purple', fg = 'white').grid(row = 8, column = 1, sticky = E)

    def on_add_contact_button_clicked(self):
        self.add_new_contact()

    def add_new_contact(self):
        if self.new_contacts_validated():
            query = 'INSERT INTO contacts_list VALUES(NULL,?,?,?)'
            parameters = (self.namefield.get(), self.emailfield.get(), self.numfield.get())
            self.execute_db_query(query, parameters)
            self.message['text'] = 'New Contact {} added'.format(self.namefield.get())
            self.namefield.delete(0, END)
            self.emailfield.delete(0, END)
            self.numfield.delete(0, END)
            self.view_contacts()
        else:
            self.message['text'] = 'Name Email and Number cannot be blank'
        self.view_contacts()
    
    def new_contacts_validated(self):
        return len(self.namefield.get()) != 0 and len(self.emailfield.get()) !=0 and len(self.numfield.get()) != 0

    def view_contacts(self):
        items = self.tree.get_children()  ## returns a list of items ids one for each child i.e a dictionary for a given item.
        for item in items:
            self.tree.delete(item)
        query = 'SELECT * FROM contacts_list ORDER BY name DESC'
        contact_entries = self.execute_db_query(query)
        for row in contact_entries:
            self.tree.insert('', 0, text=row[1], values=(row[2], row[3]))

    def on_delete_selected_button_clicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No Item Selected to delete'
            return
        self.delete_contacts()

    def delete_contacts(self):
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM contacts_list WHERE name = ?'
        self.execute_db_query(query, (name,))
        self.message['text'] = 'Contacts for {} deleted'.format(name)
        self.view_contacts()



if __name__ == '__main__':
    root = Tk()
    root.title('My Contacts List')
    application = Contacts(root)
    root.mainloop()
