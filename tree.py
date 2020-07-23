from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import *



Date_0 = datetime.datetime.now()
Date = "%d-%d-%d" % (Date_0.day, Date_0.month, Date_0.year)
########### TREEVIEW Tiles #######################

class Tree:

    # Save new class
    def save_class(self, add_new_class_dialog, class_name, class_list):

        name = str(class_name.get())
        parnt = self.treev.insert("", "end", text=name, values=("","","","",""))
        class_list.append(name)
        add_new_class_dialog.destroy()
        
    # Double click function
    def on_double_click(self, event, class_list):
        
        item_id = event.widget.focus()
        item = event.widget.item(item_id)
        print(item)
        values = item['values']

        # Condition for Add type
        if item['text'] == "Add New Class":
            add_new_class_dialog = Tk()
            add_new_class_dialog.title("Add New Class")
            add_new_class_dialog.iconbitmap('logo.ico')
            add_new_class_dialog.geometry("250x110")

            # Label -New Class Name-
            label_0 = Label(add_new_class_dialog, text="New Class Name")
            label_0.pack(pady=10)
            # Class name Entry box
            class_name = Entry(add_new_class_dialog, width=30)
            class_name.pack()
            # ADD button
            add_button_class = Button(add_new_class_dialog, text="Add Class", padx=22, command = lambda: self.save_class(add_new_class_dialog, class_name, class_list))
            add_button_class.pack(pady=10)

            add_new_class_dialog.mainloop()


        # For Update or Sale
        elif item["text"] not in class_list:
            print("RIGHT")
            item_select_dialog = Tk()
            item_select_dialog.title("Item Selected")
            item_select_dialog.iconbitmap('logo.ico')
            # Update
            update_button = Button(item_select_dialog, text="Update item", padx=22)
            update_button.pack()


            # Sale
            sale_button = Button(item_select_dialog, text="Add to Sale", padx=22)
            sale_button.pack()


            item_select_dialog.mainloop()

        else :
            print("you clicked!", values, item['text'])  
             

    def __init__(self, tab, class_list):
        self.treev=ttk.Treeview(tab, height=32, selectmode ='browse')

        # Defining number of columns 
        self.treev["columns"]=("1", "2", "3", "4", "5")

        # Defining heading 
        self.treev['show'] = 'tree headings'

        # Assigning the width and anchor to  the 
        # respective columns
        self.treev.column("0")
        self.treev.column("1")
        self.treev.column("2", width=100)
        self.treev.column("3", width=160)
        self.treev.column("4", width=130)
        self.treev.column("5")

        # Assigning the heading names to the  
        # respective columns 
        self.treev.heading("0", text="Type")
        self.treev.heading("1", text="Name", anchor=W)
        self.treev.heading("2", text="Code No.", anchor=W)
        self.treev.heading("3", text="Date Modified", anchor=W)
        self.treev.heading("4", text="Quantity", anchor=W)
        self.treev.heading("5", text="Price", anchor=W)

        # Insert "Add type" in level 1
        self.treev.insert("", "end", text="Add New Class", values=("","","","",""))
      
        # Binding double click
        self.treev.bind("<Double-Button-1>", lambda event, class_list = class_list: self.on_double_click(event, class_list))

        # Pack treeview
        self.treev.pack()

    
