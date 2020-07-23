import sqlite3




#Create a database or connect to one
conn = sqlite3.connect('items.db')

# Create cursor
c = conn.cursor()

# Create table #datatypes; null, integer, real, text, blop

c.execute("""CREATE TABLE IF NOT EXISTS stocks (
		item_type text,
		item_class text,
		item_name text,
        item_codeNum text,
        item_dateModified text,
		item_quantity text,
		item_price text
		)""")


item = [
		('Tiles', '2x2', 'Rose', '001', '02-05-2020', '100', '300'),
		('Tiles', '2x2', 'Lily', '002', '02-05-2020', '50', '210'),
		]

def add_record(item):
	conn = sqlite3.connect('items.db')
	c = conn.cursor()
	c.execute("INSERT INTO stocks VALUES (?,?,?,?,?,?,?)", item)
	conn.commit()
	conn.close()

#c.executemany("INSERT INTO stocks VALUES (?,?,?,?,?,?,?)", item)


c.execute("SELECT rowid, * FROM stocks")
#c.execute("DELETE from stocks WHERE rowid == '12' OR rowid == '13'OR rowid == '14'")
for tup in c.fetchall():
	print(tup)

def query():
	# Create a database or connect to one
	conn = sqlite3.connect('items.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT * FROM stocks")
	return c.fetchall()      # This is a LIST of Tuples

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()










#Commit Changes
conn.commit()

# Close Connection 
conn.close()

