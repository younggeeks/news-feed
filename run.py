import click
from api import get_posts, create_single_post
import os
import sys


def main_menu():

    print ("WELCOME TO NEWS FEED,\n")
    print ("Choose what you want to do:")
    print ("1. VIEW POST")
    print ("2. CREATE POST")
    print ("3. COMMENT ON POST")
    print ("\n0. Quit")
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice, arg=None):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return


def all_posts():
    for post in get_posts():
        print ("{} {}".format(post["id"], post["title"]))

    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def fetch_single(post_id):
    print "Fetching Post with id {} !\n".format(post_id)
    print fetch_single(post_id)
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def create_post(title, body, id, user_id):
    create_single_post(title=title, body=body, id=id, user_id=user_id)


def back():
    menu_actions['main_menu']()


def exit():
    sys.exit()


menu_actions = {
    'main_menu': main_menu,
    '1': all_posts,
    '2': fetch_single,
    '9': back,
    '0': exit,
}

if __name__ == "__main__":
    main_menu()
