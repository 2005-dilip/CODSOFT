import tkinter as tk
from  tkinter import  messagebox

root = tk.Tk()
root.title('Contact Book')
root.geometry("800x660")

input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, pady=10, padx=20, sticky='w') 

lb = tk.LabelFrame(input_frame, text="Customer Name")
lb.grid(row=0, column=0, pady=10, padx=20)
name1 = tk.Entry(lb, font=("Helvetica", 15))
name1.pack()

search_frame = tk.LabelFrame(input_frame, text="Search Contact")
search_frame.grid(row=0, column=1, pady=10, padx=20)

ph = tk.LabelFrame(input_frame, text="Phone Number")
ph.grid(row=1, column=0, pady=5, padx=20)
name2 = tk.Entry(ph, font=("Helvetica", 15))
name2.pack()

email = tk.LabelFrame(input_frame, text="Email")
email.grid(row=2, column=0, pady=5, padx=20)
name3 = tk.Entry(email, font=("Helvetica", 15))
name3.pack()

add = tk.LabelFrame(input_frame, text="Address")
add.grid(row=3, column=0, pady=5, padx=20)
name4 = tk.Entry(add, font=("Helvetica", 15))
name4.pack()

details = []

def save():
    customer_name = name1.get()
    phone_number = name2.get()
    email = name3.get()
    address = name4.get()
    if(customer_name!=''):
        detail = {
            "Name": customer_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address
        }
        details.append(detail)
        list_box.delete(0, "end")  # Clear the Listbox
        for i in details:
            list_box.insert("end", f"{i['Name']} - {i['Phone Number']}")
        name1.delete(0, "end")  # Clear the Entry fields
        name2.delete(0, "end")
        name3.delete(0, "end")
        name4.delete(0, "end")
    else:
        tk.messagebox.showwarning(title="Warning!", message="Empty Contact can't be Added")


def show_contact(event):
    selected_contact_index = list_box.curselection()[0]
    selected_contact = details[selected_contact_index]
    contact_details_label.config(text=f"Name: {selected_contact['Name']}\nPhone Number: {selected_contact['Phone Number']}\nEmail: {selected_contact['Email']}\nAddress: {selected_contact['Address']}")

def search_contact():
    search_term = search_entry.get()
    if search_term:
        matching_contacts = [contact for contact in details if search_term.lower() in contact['Name'].lower()]
        list_box.delete(0, "end")
        for contact in matching_contacts:
            list_box.insert("end", f"{contact['Name']} - {contact['Phone Number']}")
    else:
        list_box.delete(0, "end")
        for i in details:
            list_box.insert("end", f"{i['Name']} - {i['Phone Number']}")
    if len(details) > 10:
        listbox_scrollbar.set(0, 1)

def update_contact():
    selected_contact_index = list_box.curselection()
    if selected_contact_index:
        selected_contact_index = selected_contact_index[0]  # Get the first selected item
        updated_name = name1.get()
        updated_phone_number = name2.get()
        updated_email = name3.get()
        updated_address = name4.get()
        updated_contact = {
            "Name": updated_name,
            "Phone Number": updated_phone_number,
            "Email": updated_email,
            "Address": updated_address
        }
        details[selected_contact_index] = updated_contact
        list_box.delete(selected_contact_index)
        list_box.insert(selected_contact_index, f"{updated_contact['Name']} - {updated_contact['Phone Number']}")
    else:
        tk.messagebox.showwarning(title="Warning!",message="You must select the Contact.")

def delete_contact():
    selected_contact_index = list_box.curselection()
    if selected_contact_index:
        selected_contact_index = selected_contact_index[0]
        list_box.delete(selected_contact_index)
        details.pop(selected_contact_index)
    else:
        tk.messagebox.showwarning(title="Warning!",message="You must select the Contact.")
my_button = tk.Button(input_frame, text="Add Contact", command=save)
my_button.grid(row=4, column=0, pady=5, padx=20)

listbox_frame = tk.Frame(input_frame)
listbox_frame.grid(row=5, column=0, pady=5, padx=20)  # Move it below the button
list_box = tk.Listbox(listbox_frame)
list_box.grid(row=0, column=0, padx=5)
list_box.bind("<<ListboxSelect>>", show_contact)

listbox_scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=list_box.yview)
listbox_scrollbar.grid(row=0, column=1, sticky="ns")

search_label = tk.Label(search_frame, text="Search Contact:", font=("Helvetica", 15))
search_label.grid(row=0, column=0)
search_entry = tk.Entry(search_frame, font=("Helvetica", 15))
search_entry.grid(row=0, column=1)
search_button = tk.Button(search_frame, text="Search", command=search_contact)
search_button.grid(row=0, column=2)

update_button = tk.Button(listbox_frame, text="Update Contact", command=update_contact)
update_button.grid(row=1, column=0, pady=5, padx=20)
delete_button = tk.Button(listbox_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=2, column=0, pady=5, padx=20)
contact_details_label = tk.Label(input_frame, text="", font=("Helvetica", 15))
contact_details_label.grid(row=6, column=0, pady=5, padx=20, sticky="w")

list_box.config(yscrollcommand=listbox_scrollbar.set)
root.mainloop()