def print_welcome():
    print('\nHello! Welcome to our very advanced attendance list app.\n')


def print_options():
    print('''Would you like to:
a) Show pylighters
b) Add pylighter
c) Remove pylighter
d) Surprise tool
e) Quit\n''')


def print_results(results):
    print("\nAttendance: \n")
    for item in results:
        print("ID: {id} Order: {row_number} Name: {name} ".format(**item))
    print("\n")


def zero_attendance():
    print("\nNo one's here! \n")


def print_if_wrong():
    print("\nSomething went wrong... \n")


def choose_option():
    return input("Choose... ")
