from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox

class ContactManager:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                contacts = file.readlines()
            return [contact.strip() for contact in contacts]
        except FileNotFoundError:
            return []

    def add_contact(self, name, number):
        with open(self.filename, "a") as file:
            file.write(f"{name}!{number}\n")

    def edit_contact(self, index, new_name, new_number):
        contacts = self.load_contacts()
        contacts[index] = f"{new_name}!{new_number}"
        with open(self.filename, "w") as file:
            for contact in contacts:
                file.write(contact + "\n")

    def delete_contact(self, index):
        contacts = self.load_contacts()
        contacts.pop(index)
        with open(self.filename, "w") as file:
            for contact in contacts:
                file.write(contact + "\n")

class ContactManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Contactos")

        self.contact_manager = ContactManager()

        self.label = Label(master, text="Nombre:")
        self.label.pack()

        self.name_entry = Entry(master)
        self.name_entry.pack()

        self.label_number = Label(master, text="Número de Contacto:")
        self.label_number.pack()

        self.number_entry = Entry(master)
        self.number_entry.pack()

        self.add_button = Button(master, text="Agregar Contacto", command=self.add_contact)
        self.add_button.pack()

        self.edit_button = Button(master, text="Editar Contacto", command=self.edit_contact)
        self.edit_button.pack()

        self.delete_button = Button(master, text="Eliminar Contacto", command=self.delete_contact)
        self.delete_button.pack()

        self.show_button = Button(master, text="Mostrar Contactos", command=self.show_contacts)
        self.show_button.pack()

        self.contacts_listbox = Listbox(master)
        self.contacts_listbox.pack()

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name and number:
            self.contact_manager.add_contact(name, number)
            self.clear_entries()
            self.show_contacts()
        else:
            messagebox.showwarning("Error de Entrada", "Por favor, ingrese tanto el nombre como el número de contacto.")

    def edit_contact(self):
        selected_contact = self.contacts_listbox.curselection()
        if selected_contact:
            index = selected_contact[0]
            name = self.name_entry.get()
            number = self.number_entry.get()
            if name and number:
                self.contact_manager.edit_contact(index, name, number)
                self.clear_entries()
                self.show_contacts()
            else:
                messagebox.showwarning("Error de Entrada", "Por favor, ingrese tanto el nombre como el número de contacto.")
        else:
            messagebox.showwarning("Error de Selección", "Por favor, seleccione un contacto para editar.")

    def delete_contact(self):
        selected_contact = self.contacts_listbox.curselection()
        if selected_contact:
            index = selected_contact[0]
            self.contact_manager.delete_contact(index)
            self.show_contacts()
        else:
            messagebox.showwarning("Error de Selección", "Por favor, seleccione un contacto para eliminar.")

    def show_contacts(self):
        self.contacts_listbox.delete(0, END)
        for contact in self.contact_manager.load_contacts():
            self.contacts_listbox.insert(END, contact)

    def clear_entries(self):
        self.name_entry.delete(0, END)
        self.number_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    contact_manager_gui = ContactManagerGUI(root)
    root.mainloop()