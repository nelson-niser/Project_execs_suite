from tkinter import *
from tkinter import ttk
import datetime
from tkcalendar import *
import tree
import database
import save_existing_database

Date_0 = datetime.datetime.now()
Date = "%d-%d-%d" % (Date_0.day, Date_0.month, Date_0.year)

root = Tk()
root.title("Prime Link Stock Management")
root.iconbitmap('logo.ico')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (screenWidth, screenHeight))

# Header ---PRIME LINK---
header0 = Label(root, text="PRIME LINK", bg="blue", font=("arial black", 28), borderwidth = 0, pady=0, padx=0)
header0.pack(fill=X, side=TOP)
header1 = Label(root, text="STOCK MANAGEMENT", bg="blue", font=("arial ", 14), borderwidth = 0, pady=2, padx=0, anchor=N)
header1.pack(fill=X, side=TOP)

# Dividing frames
frame0 = Frame(root, borderwidth=3)  # ADD, DEL, HISTORY  buttons
frame0.pack(side=LEFT)
frame1 = Frame(root)  # Stock list
frame1.pack(side=LEFT)
frame2 = Frame(root, width=410, borderwidth=10)  # Sales
frame2.pack(side=LEFT)


############################### ADD ITEM BUTTON DIALOG BOX #######################
def add_item():
    add_dialog = Tk()
    add_dialog.title("Add Item")
    add_dialog.iconbitmap('logo.ico')
    add_dialog.geometry("230x100")

    # Type
    label_type = Label(add_dialog, text="Type")
    label_type.pack()
    # Drop-down menu for types
    type_list = ["SELECT", "Tiles", "Sanitary", "Pipe-fitting", "Geysers", "Other Accessories"]
    var_type = StringVar(add_dialog)
    var_type.set("SELECT")
    option_type = OptionMenu(add_dialog, var_type, *type_list)
    option_type.pack()

    # Next button and call add_item_next
    next_button = Button(add_dialog, text="Next", width=10, command = lambda: add_item_next(add_dialog, option_type, var_type))
    next_button.pack(pady=10)

    add_dialog.mainloop()
####################################################################################################

def not_selected():
    warning_dialog = Tk()
    warning_dialog.title("Delete Item")
    warning_dialog.iconbitmap('logo.ico')
    warning_dialog.geometry('240x70')

    warning_text = Label(warning_dialog, text="Select an option", font=("arial", 12))

    ok_button = Button(warning_dialog, text="OK", fg="red", padx=35, pady = 4, command = lambda: destroy_dialog(warning_dialog))

    warning_text.pack()
    ok_button.pack()

    warning_dialog.mainloop()

def destroy_dialog(dialog):
    dialog.destroy()

def add_item_next(add_dialog, option_type, var_type):
    if var_type.get() == "SELECT":
        not_selected()

    else:
        add_dialog.destroy()

        add_next_dialog = Tk()
        add_next_dialog.title("Add Item")
        add_next_dialog.iconbitmap('logo.ico')
        add_next_dialog.geometry("250x270")

        if var_type.get() == "Tiles":
            class_list = tree_tiles_class_list
            pass_tree = tree_tiles

        elif var_type.get() == "Sanitary":
            class_list = tree_sanitary_class_list
            pass_tree = tree_sanitary

        elif var_type.get() == "Pipe-fitting":
            class_list = tree_pipe_class_list
            pass_tree = tree_pipe

        elif var_type.get() == "Geysers":
            class_list = tree_geysers_class_list
            pass_tree = tree_geysers

        elif var_type.get() == "Other Accessories":
            class_list = tree_other_class_list
            pass_tree = tree_other


        # Class
        label_class = Label(add_next_dialog, text="Class")
        label_class.pack()
        # Drop-down menu for class
        var_class = StringVar(add_next_dialog)
        var_class.set("SELECT")
        option_class = OptionMenu(add_next_dialog, var_class, *class_list)
        option_class.pack()

        # Name
        label_0 = Label(add_next_dialog, text="Name")
        label_0.pack()
        # Name Entry box
        item_name = Entry(add_next_dialog)
        item_name.pack()
        # Code number
        label_1 = Label(add_next_dialog, text="Code No")
        label_1.pack()
        # Code number Entry box
        item_codeNum = Entry(add_next_dialog)
        item_codeNum.pack()
        # Quantity
        label_2 = Label(add_next_dialog, text="Quantity")
        label_2.pack()
        # Quantity Entry box
        item_quantity = Entry(add_next_dialog)
        item_quantity.pack()
        # Price
        label_3 = Label(add_next_dialog, text="Price")
        label_3.pack()
        # Price Entry box
        item_price = Entry(add_next_dialog)
        item_price.pack()
        # Confirm button
        add_button = Button(add_next_dialog, text="Confirm", padx=22, command = lambda: save_item(add_next_dialog,
                                                                                                pass_tree,
                                                                                                option_class,
                                                                                                var_type.get(),
                                                                                                var_class,
                                                                                                item_name,
                                                                                                item_codeNum,
                                                                                                item_quantity,
                                                                                                item_price
                                                                                                ))
        add_button.pack(pady=10)

        add_next_dialog.mainloop()

####################### ADD ITEM CONFIRM BUTTON COMMAND ##################################
def save_item(add_next_dialog,
            pass_tree,
            option_class,
            var_type,
            var_class,
            item_name,
            item_codeNum,
            item_quantity,
            item_price
            ):
    name = str(item_name.get())
    codeNum = str(item_codeNum.get())
    quantity = str(item_quantity.get())
    price = str(item_price.get())

    if var_class.get() == "SELECT":
        not_selected()
    elif var_class.get() == "--root--":
        item = (var_type, "--root--", name, codeNum, Date, quantity, price)
        database.add_record(item)
        pass_tree.treev.insert("", "end", text="", values = (name, codeNum, Date, quantity, price))
        for line_ in tree_all.treev.get_children():
            item_type = str(tree_all.treev.item(line_)["text"])
            if item_type == var_type:
                tree_all.treev.insert(line_, "end", text="", values = (name, codeNum, Date, quantity, price))
        add_next_dialog.destroy()
    else:
        for line in pass_tree.treev.get_children():
            item_class = str(pass_tree.treev.item(line)["text"])
            if item_class == var_class.get():
                item = (var_type, var_class.get(), name, codeNum, Date, quantity, price)
                database.add_record(item)
                pass_tree.treev.insert(line, "end", text="", values = (name, codeNum, Date, quantity, price))
                for line_ in tree_all.treev.get_children():
                    item_type = str(tree_all.treev.item(line_)["text"])
                    if item_type == var_type:
                        tree_all.treev.insert(line_, "end", text="", values = (name, codeNum, Date, quantity, price))

        add_next_dialog.destroy()
##########################################################################################


########### SEARCH BUTTON ######################
Search = Button(frame0, text="Search", padx=29)
Search.pack(side=TOP)
spacer0 = Label(frame0, text=' ', pady=35)
spacer0.pack(side=TOP)

################ ADD ITEM BUTTON ####################################
Add = Button(frame0, text="Add item", padx=22, command = add_item)
Add.pack(side=TOP)

################ DEL ITEM BUTTON ####################################
# Need def modification for del to delete from item_list
Del = Button(frame0, text="Delete", padx=30, command = lambda: Del_button_command())
Del.pack(side=TOP)

def Del_button_command():
    Del_confirmation_dialog = Tk()
    Del_confirmation_dialog.title("Delete Item")
    Del_confirmation_dialog.iconbitmap('logo.ico')
    Del_confirmation_dialog.geometry('350x100')

    Confirmation_text0 = Label(Del_confirmation_dialog, text="Are you sure you want to delete this item", font=("arial", 12))
    Confirmation_text1 = Label(Del_confirmation_dialog, text="completely from the database?", font=("arial", 12))

    Confirm_button = Button(Del_confirmation_dialog, text="Confirm", fg="red", padx=35, pady = 4)

    Confirmation_text0.pack()
    Confirmation_text1.pack()
    Confirm_button.pack()

    Del_confirmation_dialog.mainloop()


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
tree_all_class_list = []
tree_all = tree.Tree(tab_all, tree_all_class_list)

#Level 1
All_Tiles = tree_all.treev.insert("", "end", text="Tiles", values=("","","","",""))
All_sanitary = tree_all.treev.insert("", "end", text="Sanitary", values=("","","","",""))
All_pipe = tree_all.treev.insert("", "end", text="Pipe-fitting", values=("","","","",""))
All_geysers = tree_all.treev.insert("", "end", text="Geysers", values=("","","","",""))
All_others = tree_all.treev.insert("", "end", text="Other Accessories", values=("","","","",""))


# Deleting "Add Type for All"
tree_all.treev.delete(tree_all.treev.get_children()[0])

####################### TREES ##############################
tree_tiles_class_list = ["SELECT", "--root--"]
tree_tiles = tree.Tree(tab_tiles, tree_tiles_class_list)

tree_sanitary_class_list = ["SELECT", "--root--"]
tree_sanitary = tree.Tree(tab_sanitary, tree_sanitary_class_list)

tree_pipe_class_list = ["SELECT", "--root--"]
tree_pipe = tree.Tree(tab_pipe, tree_pipe_class_list)

tree_geysers_class_list = ["SELECT", "--root--"]
tree_geysers = tree.Tree(tab_geysers, tree_geysers_class_list)

tree_other_class_list = ["SELECT", "--root--"]
tree_others = tree.Tree(tab_other, tree_other_class_list)




#            ################ READ EXISTING DATABASE AND ADD EXISTING ITEMS ########################


records = database.query()


if records != None:
    # Read records one by one
    for record in records:
        
        if record[0] == "Tiles":
            save_existing_database.add_rec(record, tree_all, tree_tiles, tree_tiles_class_list)
        elif record[0] == "Sanitary":
            save_existing_database.add_rec(record, tree_all, tree_sanitary,tree_sanitary_class_list)
        elif record[0] == "Pipe-fitting":
            save_existing_database.add_rec(record, tree_all, tree_pipe, tree_pipe_class_list)
        elif record[0] == "Geysers":
            save_existing_database.add_rec(record, tree_all, tree_geysers, tree_geysers_class_list)
        elif record[0] == "Other Accessories":
            save_existing_database.add_rec(record, tree_all, tree_others, tree_other_class_list)



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
    history_window.iconbitmap('logo.ico')
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
    updates_tab = Frame(history_tabParent)


    history_tabParent.add(history_tab0, text="All")
    history_tabParent.add(history_tab1, text="Arrive")
    history_tabParent.add(history_tab2, text="Sales")
    history_tabParent.add(updates_tab, text="Updates")
    
    ###################################


    tree_history_all=ttk.Treeview(history_tab0, height=32)

    # tree_history_all["columns"]=("one", "two", "three", "four")

    # tree_history_all.column("0")
    # tree_history_all.column("one")
    # tree_history_all.column("two")
    # tree_history_all.column("three")
    # tree_history_all.column("four")

    # tree_history_all.heading("0", text="Name", anchor=W)
    # tree_history_all.heading("one", text="Date Modified", anchor=W)
    # tree_history_all.heading("two", text="Code No.", anchor=W)
    # tree_history_all.heading("three", text="Quantity", anchor=W)
    # tree_history_all.heading("four", text="Price", anchor=W)

    # Defining number of columns 
    tree_history_all["columns"]=("1", "2", "3", "4", "5")

    # Defining heading 
    tree_history_all['show'] = 'tree headings'

    # Assigning the width and anchor to  the 
    # respective columns
    tree_history_all.column("0")
    tree_history_all.column("1")
    tree_history_all.column("2", width=100)
    tree_history_all.column("3", width=160)
    tree_history_all.column("4", width=130)
    tree_history_all.column("5")

    # Assigning the heading names to the  
    # respective columns 
    tree_history_all.heading("0", text="Type")
    tree_history_all.heading("1", text="Name", anchor=W)
    tree_history_all.heading("2", text="Code No.", anchor=W)
    tree_history_all.heading("3", text="Date Modified", anchor=W)
    tree_history_all.heading("4", text="Quantity", anchor=W)
    tree_history_all.heading("5", text="Price", anchor=W)

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

print(tree_tiles_class_list)
root.mainloop()