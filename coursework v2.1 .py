import tkinter as tk
from tkinter import simpledialog, messagebox

import firebase_admin
from firebase_admin import db,credentials

cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred,{"databaseURL":'https://coursework-7e5bd-default-rtdb.asia-southeast1.firebasedatabase.app'})
ref = db.reference("/")

class LostAndFoundApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Lost and Found Database")
        self.lost_database = []

        tk.Button(self.main_window, text="Report a Lost Item", command=self.report_lost_item).pack()
        tk.Button(self.main_window, text="Mark an Item as Found", command=self.mark_as_found).pack()
        tk.Button(self.main_window, text="View Lost Items", command=self.view_lost_items).pack()
        tk.Button(self.main_window, text="Quit", command=self.quit_app).pack()

        self.main_window.mainloop()

    def report_lost_item(self):
        new_window = tk.Toplevel(self.main_window)
        new_window.title("Report a Lost Item")

        tk.Label(new_window, text="Name:").pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        tk.Label(new_window, text="Description:").pack()
        description_entry = tk.Entry(new_window)
        description_entry.pack()

        tk.Label(new_window, text="Location:").pack()
        location_entry = tk.Entry(new_window)
        location_entry.pack()

        tk.Label(new_window, text="Owner:").pack()
        owner_entry = tk.Entry(new_window)
        owner_entry.pack()


        # Add labels and entry fields for other details (location, owner)

        def submit_report():
            #name = name_entry.get()
            #description = description_entry.get()
            #location = location_entry.get()
            #owner = owner_entry.get()
            try:
                #item = itemNew(name, description,location,owner) # ... other details)
                #self.lost_database.append(item)
                itemUpload = ref.child(name_entry.get())
                itemUpload.set({
                    'description': description_entry.get(),
                    'location': location_entry.get(),
                    'owner': owner_entry.get(),
                    'isFound': False,
                })
                new_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(new_window, text="Submit", command=submit_report).pack()

    def mark_as_found(self):
        try:
            #itemUpdate = ref.child('')
            itemFound = str(simpledialog.askstring("Mark as Found", "Enter item name:"))
            itemUpdate = ref.child(itemFound)
            itemUpdate.update({
                'isFound': True,
            })
            messagebox.showerror("Success!","Success! Item marked as found.")
            #for item in self.lost_database:
            #    if item.id == item_id:
            #        item.isFound = True
            #        messagebox.showinfo("Success", "Item marked as found!")
            #        return
            #messagebox.showerror("Error", "Item not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid item ID.")

    def view_lost_items(self):
        new_window = tk.Toplevel(self.main_window)
        new_window.title("Lost Items")

        itemView =  ref.get()
        for i in itemView.items():
            print(i)
        # KYAN put it so that it displays i

        #listbox = tk.Listbox(new_window)
        #for item in self.lost_database:
        #    if not item.isFound:
        #        listbox.insert(tk.END, str(item))
        #listbox.pack()


    def quit_app(self):
        self.main_window.destroy()

#class itemNew:
    #def __init__(self, name, description, location, owner, isFound=False):  # Set default isFound value
        #self.id = 0  # Add an ID attribute for marking as found
        #self.isFound = isFound
        #self.name = name
        #self.description = description
        #self.location = location
        #self.owner = owner

    #def __str__(self):
        #return f"ID: {self.id}\n{self.name}\nDescription: {self.description}\nLast seen: {self.location}\nOwner: {self.owner}"

# Create app instance and start Tkinter event loop
app = LostAndFoundApp()

