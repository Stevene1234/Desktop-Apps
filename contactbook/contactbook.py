import tkinter as tk
from tkinter import filedialog



class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(contact)

    def delete_contact(self, index):
        del self.contacts[index]

    def edit_contact(self, index, new_name, new_phone_number, new_email):
        self.contacts[index]['name'] = new_name
        self.contacts[index]['phone_number'] = new_phone_number
        self.contacts[index]['email'] = new_email

    def get_contact(self, index):
        return self.contacts[index]

    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        for contact in self.contacts:
            if contact['name'].lower().find(search_term.lower()) != -1 or contact['phone_number'].lower().find(search_term.lower()) != -1 or contact['email'].lower().find(search_term.lower()) != -1:
                return contact
        return None




class ContactBookGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Contact Book")

        # Add contact frame
        self.add_contact_frame = tk.Frame(self.window)
        self.add_contact_frame.pack(fill=tk.X)

        self.name_label = tk.Label(self.add_contact_frame, text="Name:")
        self.name_label.pack(side=tk.LEFT)

        self.name_entry = tk.Entry(self.add_contact_frame)
        self.name_entry.pack(side=tk.LEFT)

        self.phone_number_label = tk.Label(self.add_contact_frame, text="Phone Number:")
        self.phone_number_label.pack(side=tk.LEFT)

        self.phone_number_entry = tk.Entry(self.add_contact_frame)
        self.phone_number_entry.pack(side=tk.LEFT)

        self.email_label = tk.Label(self.add_contact_frame, text="Email:")
        self.email_label.pack(side=tk.LEFT)

        self.email_entry = tk.Entry(self.add_contact_frame)
        self.email_entry.pack(side=tk.LEFT)

        self.add_contact_button = tk.Button(self.add_contact_frame, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(side=tk.LEFT)

        # Edit contact frame
        self.edit_contact_frame = tk.Frame(self.window)
        self.edit_contact_frame.pack(fill=tk.X)

        self.edit_contact_label = tk.Label(self.edit_contact_frame, text="Edit Contact")
        self.edit_contact_label.pack(side=tk.LEFT)

        self.edit_contact_listbox = tk.Listbox(self.edit_contact_frame, selectmode=tk.SINGLE)
        self.edit_contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.edit_contact_button = tk.Button(self.edit_contact_frame, text="Edit Contact", command=self.edit_contact)
        self.edit_contact_button.pack(side=tk.LEFT)

        # Delete contact frame
        self.delete_contact_frame = tk.Frame(self.window)
        self.delete_contact_frame.pack(fill=tk.X)

        self.delete_contact_label = tk.Label(self.delete_contact_frame, text="Delete Contact")
        self.delete_contact_label.pack(side=tk.LEFT)

        self.delete_contact_listbox = tk.Listbox(self.delete_contact_frame, selectmode=tk.SINGLE)
        self.delete_contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

        self.delete_contact_button = tk.Button(self.delete_contact_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(side=tk.LEFT)

        # Search contact frame
        self.search_contact_frame = tk.Frame(self.window)
        self.search_contact_frame.pack(fill=tk.X)

        self.search_contact_label = tk.Label(self.search_contact_frame, text="Search Contact")
        self.search_contact_label.pack(side=tk.LEFT)

        self.search_contact_entry = tk.Entry(self.search_contact_frame)
        self.search_contact_entry.pack(side=tk.LEFT)

        self.search_contact_button = tk.Button(self.search_contact_frame, text="Search", command=self.search_contact)
        self.search_contact_button.pack(side=tk.LEFT)

        # Save contact information frame
        self.save_contact_frame = tk.Frame(self.window)
        self.save_contact_frame.pack(fill=tk.X)

        self.save_contact_label = tk.Label(self.save_contact_frame, text="Save Contact Information")
        self.save_contact_label.pack(side=tk.LEFT)

        self.save_contact_button = tk.Button(self.save_contact_frame, text="Save", command=self.save_contacts)
        self.save_contact_button.pack(side=tk.LEFT)

        # Initialize contact book
        self.contact_book = ContactBook()

        # Populate edit and delete contact frames
        self.populate_edit_delete_frames()

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        self.contact_book.add_contact(name, phone_number, email)

        self.populate_edit_delete_frames()

    def edit_contact(self):
        selected_contact = self.edit_contact_listbox.get(self.edit_contact_listbox.curselection())
        index = self.edit_contact_listbox.curselection()[0]

        name = self.name_entry.get()
        phone_number = self.phone_number_entry.get()
        email = self.email_entry.get()

        self.contact_book.edit_contact(index, name, phone_number, email)

        self.populate_edit_delete_frames()

    def delete_contact(self):
        selected_contact = self.delete_contact_listbox.get(self.delete_contact_listbox.curselection())
        index = self.delete_contact_listbox.curselection()[0]

        self.contact_book.delete_contact(index)

        self.populate_edit_delete_frames()

    def search_contact(self):
        search_term = self.search_contact_entry.get()

        contact = self.contact_book.search_contact(search_term)

        if contact:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact['name'])

            self.phone_number_entry.delete(0, tk.END)
            self.phone_number_entry.insert(0, contact['phone_number'])

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact['email'])
        else:
            self.name_entry.delete(0, tk.END)
            self.phone_number_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)

    def save_contacts(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')

        if file_path:
            with open(file_path, 'w') as file:
                for contact in self.contact_book.get_all_contacts():
                    file.write('Name: {}\nPhone Number: {}\nEmail: {}\n\n'.format(contact['name'], contact['phone_number'], contact['email']))

    def populate_edit_delete_frames(self):
        self.edit_contact_listbox.delete(0, tk.END)
        self.delete_contact_listbox.delete(0, tk.END)

        for index, contact in enumerate(self.contact_book.get_all_contacts()):
            self.edit_contact_listbox.insert(index, '{} - {}'.format(contact['name'], contact['phone_number']))
            self.delete_contact_listbox.insert(index, '{} - {}'.format(contact['name'], contact['phone_number']))

app = ContactBookGUI()
app.window.mainloop()