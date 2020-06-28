from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import *
#import database


Date_0 = datetime.datetime.now()
Date = "%d-%d-%d" % (Date_0.day, Date_0.month, Date_0.year)
########### TREEVIEW Tiles #######################

class Tree:
    # Double click function
    def on_double_click(self, event):
        item_id = event.widget.focus()
        item = event.widget.item(item_id)
        values = item['values']
        print("you clicked!", values)  
        dialog = Tk()
        dialog.mainloop() 

    def __init__(self,tab):
        self.treev=ttk.Treeview(tab, height=32, selectmode ='browse')

        # Defining number of columns 
        self.treev["columns"]=("1", "2", "3", "4")

        # Defining heading 
        self.treev['show'] = 'tree headings'

        # Assigning the width and anchor to  the 
        # respective columns
        self.treev.column("0")
        self.treev.column("1")
        self.treev.column("2")
        self.treev.column("3")
        self.treev.column("4")

        # Assigning the heading names to the  
        # respective columns 
        self.treev.heading("0", text="Type")
        self.treev.heading("1", text="Name", anchor=W)
        self.treev.heading("2", text="Date Modified", anchor=W)
        self.treev.heading("3", text="Quantity", anchor=W)
        self.treev.heading("4", text="Price", anchor=W)
        self.treev.bind("<Double-Button-1>", self.on_double_click)
        self.treev.pack()

    
