import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
from tkinter import *


# CSV file name to store contacts
filename = "contacts.csv"

# Initialize CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

# Save a contact to the CSV file
def save_contact(name, phone, email):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

# Load all contacts from the CSV file
def load_contacts():
    contacts = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            contacts.append(row)
    return contacts

# Add contact to CSV file and listbox
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name and phone and email:
        save_contact(name, phone, email)
        contacts_list.insert('', 'end', values=(name, phone, email))
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Please fill out all fields")

# Delete selected contact
def delete_contact():
    selected_item = contacts_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a contact to delete")
        return

    name = contacts_list.item(selected_item, 'values')[0]
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact[0] != name]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        writer.writerows(contacts)

    contacts_list.delete(selected_item)
    messagebox.showinfo("Success", "Contact deleted successfully")

# Load contacts into the listbox
def load_contacts_into_listbox():
    contacts = load_contacts()
    for contact in contacts:
        contacts_list.insert('', 'end', values=(contact[0], contact[1], contact[2]))

# Update selected contact
def update_contact():
    selected_item = contacts_list.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select a contact to update")
        return

    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if not (name and phone and email):
        messagebox.showwarning("Warning", "Please fill out all fields")
        return

    contacts = load_contacts()
    for contact in contacts:
        if contact[0] == contacts_list.item(selected_item, 'values')[0]:
            contact[0], contact[1], contact[2] = name, phone, email

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])
        writer.writerows(contacts)

    contacts_list.delete(selected_item)
    contacts_list.insert('', 'end', values=(name, phone, email))
    messagebox.showinfo("Success", "Contact updated successfully")

# Create main window
root = tk.Tk()
img=PhotoImage(file='C:/Users/91830/Desktop/INTERNSHIP/pic.png')
root.iconphoto(False,img)

root.title("Contact Management System")
root.geometry("600x400")

# Contact Form
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

label_name = tk.Label(frame_form, text="Name")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_form, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_form, text="Phone")
label_phone.grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(frame_form, width=30)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(frame_form, text="Email")
label_email.grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="Update Contact", command=update_contact)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=0, column=2, padx=5)

# Contact List
contacts_list = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show='headings')
contacts_list.heading("Name", text="Name")
contacts_list.heading("Phone", text="Phone")
contacts_list.heading("Email", text="Email")
contacts_list.pack(pady=20, fill="both", expand=True)

# Initialize CSV file and load contacts
initialize_csv()
load_contacts_into_listbox()

root.mainloop()
