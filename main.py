def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    return "Contact already exist."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."
    

@input_error
def show_phone(name: str, contacts: dict) -> str:
    return contacts[name]
    
def show_all(contacts: dict) -> print:
    if len(contacts) == 0:
        print("The list is empty")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    

def main():
    contacts = {}
    commands_to_close = ["close", "exit"]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        match command:
            case "hello":
                 print("How can I help you?")
            case "add":
                 print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args[0], contacts))
            case "show_all":
                show_all(contacts)
            case _ if command in commands_to_close:
                print("Good bye!")
                break
            case _:
                 print("Invalid command.")

if __name__ == "__main__":
    main()