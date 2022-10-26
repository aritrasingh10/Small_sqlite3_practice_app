import sqlite3


def show_all():
    con = sqlite3.connect('customer.db')
    c=con.cursor()
    c.execute('''SELECT rowid,* FROM customers''')

    items = c.fetchall()
    for item in items:
        print(item)

    con.commit()
    con.close()


# Add a new record to the table 
def add_one(first_name,last_name,email):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute('''INSERT INTO customers VALUES(?,?,?)''',(first_name,last_name,email))
    con.commit()
    con.close()


def delete_one(id):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)",id)
    con.commit()
    con.close()


def add_many(stuff):
    con= sqlite3.connect('customer.db')
    c = con.cursor()
    c.executemany('''INSERT INTO customers VALUES(?,?,?)''',(stuff))
    con.commit()
    con.close()    







# Create table 
# c.execute('''CREATE TABLE customers(first_name text,last_name text,email text)''')
# con.commit()
# con.close()


# Data for the table
# mydata = [('Sayanjit','Ghosh','sayanjit1999@gmail.com'),
# ('Mainka','Barik','mainkabarik1998@gmail.com'),
# ('Somnath','Ghosh','somnathghosh1999@gmail.com')
# ]


# # INSERT DATA INTO THE TABLE 
# c.executemany('''INSERT INTO customers VALUES(?,?,?)''',mydata)
# con.commit()
# con.close()



# Show all data in the table 
# c.execute('''SELECT * FROM customers''')

# items = c.fetchall()
# for item in items:
#     print(item)

# con.commit()
# con.close()    