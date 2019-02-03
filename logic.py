import sys
import os
import psycopg2

import view
import database


def show_pylighters():
    selected_stuff = database.select()
    return selected_stuff


def add_pylighter():
    database.insert(input('Insert new pylighter...'))
    selected_stuff = database.select()
    return selected_stuff


def remove_pylighter():
    database.delete(input('Remove desired pylighter...'))
    selected_stuff = database.select()
    return selected_stuff


def surprise_tool():
    try:
        database.create_table()
    except psycopg2.ProgrammingError:
        database.drop_table()
        database.create_table()


def quit_app():
    sys.exit(0)


def wrong_input_handling():
    os.system('clear')
    view.print_if_wrong()


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
    app_running = True
    while app_running:
        view.print_options()
        chosen_option = view.choose_option()
        handled_chosen_option = handle_chosen_option(chosen_option)
        os.system('clear')
        if handled_chosen_option:
            view.print_results(handled_chosen_option)
        else:
            view.zero_attendance()


start()

