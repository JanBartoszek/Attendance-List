import sys
import os
import psycopg2

import view
import database


def show_pylighters():
    present_pylighters = database.select()
    return present_pylighters


def add_pylighter():
    database.insert(input('Insert new pylighter...'))
    present_pylighters = database.select()
    return present_pylighters


def remove_pylighter():
    database.delete(input('Remove desired pylighter...'))
    present_pylighters = database.select()
    return present_pylighters


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
    view.print_wrong_input_alert()


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
        chosen_option = input("Choose... ")
        handled_chosen_option = handle_chosen_option(chosen_option)
        os.system('clear')
        if handled_chosen_option:
            view.print_results(handled_chosen_option)
        else:
            view.zero_attendance()


start()

