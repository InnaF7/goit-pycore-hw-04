from cmd_parser import parse_input
from handlers import add_contact, change_contact, show_phone, show_all
 
 
def main():
    contacts = {}
 
    commands = {
        "add":    add_contact,
        "change": change_contact,
        "phone":  show_phone,
        "all":    show_all,
    }
 
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
 
        match command:
            case "exit" | "close":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case cmd if cmd in commands:
                print(commands[cmd](args, contacts))
            case _:
                print("Invalid command.")
 
 
if __name__ == "__main__":
    main()