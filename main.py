from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import *
#import database
import tree

Date_0 = datetime.datetime.now()
Date = "%d-%d-%d" % (Date_0.day, Date_0.month, Date_0.year)

root = Tk()
root.title("Prime Link Stock Management")
root.iconbitmap('logo.ico')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (screenWidth, screenHeight))


header0 = Label(root, text="PRIME LINK", bg="blue", font=("arial black", 28), borderwidth = 0, pady=0, padx=0)
header1 = Label(root, text="STOCK MANAGEMENT", bg="blue", font=("arial ", 14), borderwidth = 0, pady=2, padx=0, anchor=N)


frame0 = Frame(root, borderwidth=3)  # ADD, DEL, HISTORY  buttons
frame1 = Frame(root)  # Stock list
frame2 = Frame(root, width=410, borderwidth=10)  # Sales

# img = ImageTk.PhotoImage(Image.open("img.jpg"))
# img_label = Label(image=img)



class iTile:
    def __init__(self, name, codeNum, quantity, price):
        self.name = name
        self.codeNum = codeNum
        self.quantity = quantity
        self.price = price




#item_list = []


############################### ADD ITEM BUTTON DIALOG BOX #######################
def add_item():
    add_dialog = Tk()
    add_dialog.title("Add Item")
    add_dialog.geometry("250x250")

    type_list = ["Tiles", "Sanitary", "Pipe-fitting", "Geysers", "Other Accessories"]

    variable = StringVar(add_dialog)
    variable.set("Tiles")

    option_type = OptionMenu(add_dialog, variable, *type_list)


    label_0 = Label(add_dialog, text="Name")
    item_name = Entry(add_dialog)
    item_name.insert(0, "Item Name")
    label_1 = Label(add_dialog, text="Code No")
    item_codeNum = Entry(add_dialog)
    item_codeNum.insert(0, "000")
    label_2 = Label(add_dialog, text="Quantity")
    item_quantity = Entry(add_dialog)
    item_quantity.insert(0, "1")
    label_3 = Label(add_dialog, text="Price")
    item_price = Entry(add_dialog)
    item_price.insert(0, "0")
    
    add_button = Button(add_dialog, text="Confirm", padx=22, command = lambda: save_item(add_dialog, option_type, variable, item_name, item_codeNum, item_quantity, item_price))

    option_type.pack()

    label_0.pack()
    item_name.pack()
    label_1.pack()
    item_codeNum.pack()
    label_2.pack()
    item_quantity.pack()
    label_3.pack()
    item_price.pack()
    add_button.pack()


    add_dialog.mainloop()
####################################################################################################



####################### ADD ITEM CONFIRM BUTTON COMMAND ##################################
def save_item(add_dialog, option_type, variable, item_name, item_codeNum, item_quantity, item_price):
    name = str(item_name.get())
    codeNum = str(item_codeNum.get())
    quantity = str(item_quantity.get())
    price = str(item_price.get())
    #iTile_0 = iTile(name, codeNum, quantity, price)
    #item_list.append(iTile_0)

    if variable.get() == "Tiles":
        tree_all.treev.insert(All_Tiles, "end", text=codeNum, values=(name, Date, quantity, price))
        tree_tiles.treev.insert("" , "end", text=codeNum, values=(name, Date, quantity, price))

    if variable.get() == "Sanitary":
        tree_all.treev.insert(All_sanitary, "end",text=codeNum, values=(name, Date, quantity, price))
        tree_sanitary.treev.insert("", "end", text=codeNum, values=(name, Date, quantity, price))

    if variable.get() == "Pipe-fitting":
        tree_all.treev.insert(All_pipe, "end", text=codeNum, values=(name, Date, quantity, price))
        tree_pipe.treev.insert("", "end", text=codeNum, values=(name, Date, quantity, price))

    if variable.get() == "Geysers":
        tree_all.treev.insert(All_geysers, "end", text=codeNum, values=(name, Date, quantity, price))
        tree_geysers.treev.insert("", "end", text=codeNum, values=(name, Date, quantity, price))

    if variable.get() == "Other Accessories":
        tree_all.treev.insert(All_others, "end", text=codeNum, values=(name, Date, quantity, price))
        tree_other.treev.insert("", "end", text=codeNum, values=(name, Date, quantity, price))
    
    add_dialog.destroy()
##########################################################################################


########### SEARCH BUTTON ######################
Search = Button(frame0, text="Search", padx=29)
spacer0 = Label(frame0, text=' ', pady=35)

################ ADD ITEM BUTTON ####################################
Add = Button(frame0, text="Add item", padx=22, command = add_item)


################ DEL ITEM BUTTON ####################################
# Need def modification for del to delete from item_list
Del = Button(frame0, text="Delete", padx=30, command = lambda: Del_button_command())


def Del_button_command():
    Del_confirmation_dialog = Tk()
    Del_confirmation_dialog.title("Delete Item")
    Del_confirmation_dialog.geometry('350x100')

    Confirmation_text0 = Label(Del_confirmation_dialog, text="Are you sure you want to delete this item", font=("arial", 12))
    Confirmation_text1 = Label(Del_confirmation_dialog, text="completely from the database?", font=("arial", 12))

    Confirm_button = Button(Del_confirmation_dialog, text="Confirm", fg="red", padx=35, pady = 4)

    Confirmation_text0.pack()
    Confirmation_text1.pack()
    Confirm_button.pack()

    Del_confirmation_dialog.mainloop()


##################### ADD ITEMS ENTRY VARIABLES #############################
var0 = StringVar()
var0 = "NOT SELECTED"
item_description_name = Label(text = var0)

var1 = StringVar()
var1 = "NOT SELECTED"
item_description_codeNum = Label(text = var1)

var2 = StringVar()
var2 = "NOT SELECTED"
item_description_quantity = Label(text = var2)

var3 = StringVar()
var3 = "NOT SELECTED"
item_description_price = Label(text = var3)
###########################################################################
   






item_description_0 = Label(text = "Name: ", anchor=E, borderwidth=4)
item_description_1 = Label(text = "Code No: ", anchor=E, borderwidth=4)
item_description_2 = Label(text = "Quantity: ", anchor=E, borderwidth=4)
item_description_3 = Label(text = "Price: ", anchor=E, borderwidth=4)

header0.pack(fill=X, side=TOP)
header1.pack(fill=X, side=TOP)




frame0.pack(side=LEFT)

Search.pack(side=TOP)
spacer0.pack(side=TOP)
Add.pack(side=TOP)
Del.pack(side=TOP)

frame1.pack(side=LEFT)

frame2.pack(side=LEFT)





########## NOTEBOOK AND TABS ###################################
style = ttk.Style()
style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [10, 5] }}})

style.theme_use("default")


tabParent = ttk.Notebook(frame1)


tab_all = Frame(tabParent, background = "blue", width='%d' % (screenWidth-((screenWidth/100)*65)), height= '%d' % (screenHeight-((screenHeight/100)*30)))
tab_tiles = Frame(tabParent)
tab_sanitary = Frame(tabParent)
tab_pipe = Frame(tabParent)
tab_geysers = Frame(tabParent)
tab_other = Frame(tabParent)

tabParent.add(tab_all, text="All")
tabParent.add(tab_tiles, text="Tiles")
tabParent.add(tab_sanitary, text="Sanitary")
tabParent.add(tab_pipe, text="Pipe-fitting")
tabParent.add(tab_geysers, text="Geysers")
tabParent.add(tab_other, text="Other Accessories")

tabParent.pack()


##################################################################



########### TREEVIEW ALL #######################

tree_all = tree.Tree(tab_all)

#Level 1
All_Tiles = tree_all.treev.insert("", "end", text="Tiles", values=("","","",""))
All_sanitary = tree_all.treev.insert("", "end", text="Sanitary", values=("","","",""))
All_pipe = tree_all.treev.insert("", "end", text="Pipe-fitting", values=("","","",""))
All_geysers = tree_all.treev.insert("", "end", text="Geysers", values=("","","",""))
All_others = tree_all.treev.insert("", "end", text="Others", values=("","","",""))


###########################################################

tree_tiles = tree.Tree(tab_tiles)
tree_sanitary = tree.Tree(tab_sanitary)
tree_pipe = tree.Tree(tab_pipe)
tree_geysers = tree.Tree(tab_geysers)
tree_other = tree.Tree(tab_other)


############ Sales ##################################################

Sales_logo = Label(frame2, text='SALES', bg="green", font=("arial black", 18), borderwidth = 0, pady=0, padx=0, anchor=CENTER)


########## Sales Treeview ############################################
sales_tree=ttk.Treeview(frame2, height=20, selectmode ='browse')

sales_tree["columns"]=("1", "2", "3")

sales_tree["show"] = "headings"

sales_tree.column("1")
sales_tree.column("2", width = 90)
sales_tree.column("3", width = 130)

sales_tree.heading("1", text="Name", anchor=W)
sales_tree.heading("2", text="Quantity", anchor=W)
sales_tree.heading("3", text="Price", anchor=W)



#################################################################

generate_bill_button = Button(frame2, text="Generate Bill", padx=30)
proceed_button = Button(frame2, text="Proceed without Bill", padx=30)



Sales_logo.pack(side=TOP)
sales_tree.pack(side=TOP, expand=YES)
proceed_button.pack(side=RIGHT)
generate_bill_button.pack(side=RIGHT,padx=5)
##################################################################



################### History ############################################

spacer1 = Label(frame0, text=' ', pady=190)
history_button = Button(frame0, text="History", padx=27, command = lambda: history())

# HISTORY BUTTON COMMAND #######################
def history():
    history_window = Tk()
    history_window.title("History")
    history_window.geometry('%dx%d+0+0' % (screenWidth, screenHeight))


    history_label_0 = Label(history_window, text="History", bg="blue", font=("arial black", 26), borderwidth = 0, pady=0, padx=0, anchor=CENTER)
    

    ####### CALENDAR choosing date ############
    date_frame = Frame(history_window)

    history_date_from = Label(date_frame, text="From:")
    from_date = "%d-%d-%d" % (Date_0.day, Date_0.month, Date_0.year-1)
    history_date_from_button = Button(date_frame, text=from_date, command = lambda:show_cal())
    history_date_to = Label(date_frame, text="To:")
    history_date_to_button = Button(date_frame, text=Date, command = lambda:show_cal())
    
        ############# Cal Window ############
    def show_cal():
        cal_window = Tk()
        cal_window.title("Select Date")
        history_cal = Calendar(cal_window, selectmode="day", year=Date_0.year, month=Date_0.month, day=Date_0.day)
        history_cal.pack()

        select_button = Button(cal_window, text="Select",padx=15)
        select_button.pack(pady=8)

        cal_window.mainloop()
        #####################################
    ###########################################
    show_history = Button(date_frame, text="Show History", padx=22)

    history_tabParent = ttk.Notebook(history_window)


    history_tab0 = Frame(history_tabParent, background = "red", width='%d' % (screenWidth-((screenWidth/100)*65)), height= '%d' % (screenHeight-((screenHeight/100)*30)))
    history_tab1 = Frame(history_tabParent)
    history_tab2 = Frame(history_tabParent)


    history_tabParent.add(history_tab0, text="All")
    history_tabParent.add(history_tab1, text="Arrive")
    history_tabParent.add(history_tab2, text="Sales")
    
    ###################################


    tree_history_all=ttk.Treeview(history_tab0, height=32)

    tree_history_all["columns"]=("one", "two", "three", "four")

    tree_history_all.column("0")
    tree_history_all.column("one")
    tree_history_all.column("two")
    tree_history_all.column("three")
    tree_history_all.column("four")

    tree_history_all.heading("0", text="Name", anchor=W)
    tree_history_all.heading("one", text="Date Modified", anchor=W)
    tree_history_all.heading("two", text="Code No.", anchor=W)
    tree_history_all.heading("three", text="Quantity", anchor=W)
    tree_history_all.heading("four", text="Price", anchor=W)

    All_History_Tiles = tree_history_all.insert("", 1, text="Tiles", values=("","","",""))

    tree_history_all.pack()

    ####################################



    history_label_0.pack(side=TOP, fill=X)
    date_frame.pack(side=TOP, fill=X, pady=10)
    history_date_from.pack(side=LEFT,padx=50)
    history_date_from_button.pack(side=LEFT,padx=0)
    history_date_to.pack(side=LEFT,padx=50)
    history_date_to_button.pack(side=LEFT,padx=0)
    show_history.pack(side=LEFT,padx=50)
    history_tabParent.pack()


    history_window.mainloop()




spacer1.pack(side=TOP)
history_button.pack(side=BOTTOM)
#################################################################


root.mainloop()