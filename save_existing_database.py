# Function to add records to corresponding types
def add_rec(record, tree_all, tree, class_list):
    # Crete a list of class to later check if it is present or not
            item_class_list = ["--root--"]
            # Read the treeview items one by one
            for line in tree.treev.get_children():
                item_class = str(tree.treev.item(line)["text"])
                if item_class not in item_class_list and item_class != "" and item_class != "Add New Class":
                    item_class_list.append(item_class)
                # # If the class is already present
            if record[1] in item_class_list:
                # Fetch parent
                for line in tree.treev.get_children():
                    if record[1] == "--root--":
                        parent = tree.treev.parent(line)
                    elif record[1] == str(tree.treev.item(line)["text"]):
                        parent = line
            # Else create the class
            else:
                parent = tree.treev.insert("", "end", text=record[1], values=("","","","",""))
                class_list.append(record[1])
            # After finding class parent insert record
            tree.treev.insert(parent, "end", text="", values = (record[2], record[3], record[4], record[5], record[6]))
            for line_ in tree_all.treev.get_children():
                item_type = str(tree_all.treev.item(line_)["text"])
                if item_type == record[0]:
                    tree_all.treev.insert(line_, "end", text="", values = (record[2], record[3], record[4], record[5], record[6]))