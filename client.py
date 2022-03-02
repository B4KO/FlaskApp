import tkinter as tk

from sqlalchemy import column

bg = "#808080" #gray

root = tk.Tk()
root.title("AddEntity")

def open(option):
    
    top = tk.Toplevel()
    
    if option == "add":
        global AddWindow
        addWindow = AddMenu(top)
    if option == "edit":
        global EditWindow
        EditWindow = EditMenu(top)
    if option == "get":
        global GetWindow
        GetWindow = GetMenu(top)
        
    return


class AddMenu:
    
    def __init__(self, master):        
        labelId = tk.Label(master, text="ID", bg=bg).grid(row=0, column=0)
        entryId = tk.Entry(master).grid(row=0, column=1, columnspan=2)
        
        labelName = tk.Label(master, text="Name", bg=bg).grid(row=1, column=0)
        entryName = tk.Entry(master).grid(row=1, column=1, columnspan=2)
        
        labelEmail = tk.Label(master, text="Email", bg=bg).grid(row=2, column=0)
        entryEmail = tk.Entry(master).grid(row=2, column=1, columnspan=2)
        
        buttonSubmit = tk.Button(master, text="Submit", padx=20, pady=10).grid(row=3, column=1)


class EditMenu:
    
    def __init__(self, master):        
        labelId = tk.Label(master, text="ID", bg=bg).grid(row=0, column=0)
        entryId = tk.Entry(master).grid(row=0, column=1, columnspan=2)
        
        labelName = tk.Label(master, text="Name", bg=bg).grid(row=1, column=0)
        entryName = tk.Entry(master).grid(row=1, column=1, columnspan=2)
        
        labelEmail = tk.Label(master, text="Email", bg=bg).grid(row=2, column=0)
        entryEmail = tk.Entry(master).grid(row=2, column=1, columnspan=2)
        
        buttonSubmit = tk.Button(master, text="Submit", padx=20, pady=10).grid(row=3, column=1)
        
        
class GetMenu:
    
    def __init__(self, master):        
        labelId = tk.Label(master, text="ID", bg=bg).grid(row=0, column=0)
        entryId = tk.Entry(master).grid(row=0, column=1, columnspan=2)
        
        buttonSubmit = tk.Button(master, text="Submit", padx=20, pady=10).grid(row=3, column=1)


class MainMenu:
    
    def __init__(self, master):        
       buttonAdd = tk.Button(master, text="Add", padx=20, pady=10, command=lambda: open("add")).grid(row=0, column=0)
       buttonEdit = tk.Button(master, text="Edit", padx=20, pady=10, command=lambda: open("edit")).grid(row=0, column=1)
       buttonGet = tk.Button(master, text="Get", padx=20, pady=10, command=lambda: open("get")).grid(row=0, column=2)


window = MainMenu(root)

root.mainloop()

