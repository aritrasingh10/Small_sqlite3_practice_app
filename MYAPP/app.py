import database
# Add a record to the database 
# database.add_one('Aritra','Singh','aritrasingh1998@gmail.com')
# Show all data in database 

# Delete Record use rowid as string 
# database.delete_one('4')


#Add many records

stuff = [
    ('Tansuk','Maitra','tansukmaitra@gmail.com'),
    ('Himon','Patra','himonpatra@gmail.com'),
    ('Arghadeep','Mondal','arghadeep@gmail.com'),
]

database.add_many(stuff)



database.show_all()


