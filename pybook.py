'''
PyBook is a mini-project implementation of a phonebook in Python 
'''
def create():
    name     = input("Enter name: ");
    number   = input("Enter phone number: ");
    email    = input("Enter e-mail address: ");
    birthday = input("Enter birthday (DD/MM): ");
    file = open('data.pb','a')
    file.write(name+','+number+','+email+','+birthday)
    file.close()
    

def main():
    from subprocess import call 
    call(["clear"])
    print("Welcome to PyBook - The Python Phonebook\n")
    print("(C)reate contact\n(D)elete Contact\n(V)iew Contact\n(S)earch Contact\n")
    choice = input("Enter a valid choice: ");
    if choice=='C':
        create()
    else:
        quit()

if __name__ == "__main__":
    main();

