
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
        except KeyError:
            return "Specify the correct search parameter"
    return inner


@input_error
def main():
    print("Welcome to the assistant bot Fox!")
    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif "hello" == command:
            print("How can I help you?")
        elif "add" == command:
            print(add_contact(*args))
        elif "change" == command:
            print(change_contact(*args))
        elif "phone" == command:
            print(show_phone(*args))
        elif "all" == command:
            print(show_all())
        else:
            print("Invalid command.")


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(*add):
    if add[0] in contact:
        return "The contact already exists"
    else:
        contact[add[0]] = add[1]
        return "Contact added."


@input_error
def change_contact(*change):
    if change[0] in contact:
        contact[change[0]] = change[1]
        return "Contact updated."
    else:
        return "Contact not found"


def show_phone(*phone):
    if phone[0] in contact:
        return contact[phone[0]]
    else:
        return "Contact not found"


@input_error
def show_all():
    if len(contact) > 0:
        return contact
    return 'The phone book is empty'


if __name__ == "__main__":
    contact = {}
    main()
