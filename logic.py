import sys
import os

import view
import database


def show_pylighters():
    present_pylighters = database.select()
    return present_pylighters


def add_pylighter():
    database.insert(input('Insert new pylighter... '))
    present_pylighters = database.select()
    return present_pylighters


def remove_pylighter():
    database.delete(input('Remove desired pylighter... '))
    present_pylighters = database.select()
    return present_pylighters


def surprise_tool():
    if database.check_if_attendance_table_exists().get("exists"):
        database.drop_table()
        database.create_table()
    else:
        database.create_table()


def quit_app():
    database.disconnect()
    sys.exit(0)


def wrong_input_handling():
    return False


def handle_chosen_option(option):
    menu_options = {
        "a" : show_pylighters,
        "b" : add_pylighter,
        "c" : remove_pylighter,
        "d" : surprise_tool,
        "e" : quit_app
    }
    return menu_options.get(option, wrong_input_handling)()


def start():
    view.print_welcome()
    database.connect()
    app_running = True
    while app_running:
        view.print_options()
        chosen_option = input("Choose... ")
        handled_chosen_option = handle_chosen_option(chosen_option)
        os.system('clear')
        if handled_chosen_option:
            view.print_results(handled_chosen_option)
        elif handled_chosen_option == []:
            view.zero_attendance()
        else:
            view.print_wrong_input_alert()


start()

