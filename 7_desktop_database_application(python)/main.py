# This is a database Application for Desktop Made with python

"""
Features:
View all records
Search
Add Entry
Update
Delete
Close
"""
from tkinter import *
from database import *
# main window of the application

window = Tk()

def view_command():
    list1.delete(0, END)
    for row in view():
        list1.insert(END, row)


# labels for the entries
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


# entries
title_text = StringVar()
e1 = Entry(window, textvariable=title_text )
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text )
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text )
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(window, textvariable=ISBN_text )
e4.grid(row=1, column=3)

# listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# binding
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


view_button = Button(window, text="View all", width=12,command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12)
close_button.grid(row=7, column=3)


window.mainloop()
