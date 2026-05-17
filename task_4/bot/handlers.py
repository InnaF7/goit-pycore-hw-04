def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."
 
 
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: give me name and phone please."
    name, phone = args
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."
 
 
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: give me a name please."
    name = args[0]
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]
 
 
def show_all(args, contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts saved."