from api import get_posts, create_single_post


def show_menu():
    print ("WELCOME TO NEWS FEED,\n")
    print ("Choose what you want to do:")
    print ("1. VIEW POST")
    print ("2. CREATE POST")
    print ("3. COMMENT ON POST")
    print ("\n0. Quit")
    choice = input(" >>  ")
    show_menu(choice)

    return


def show_menu(choice, arg=None):
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            if arg:
                menu_actions[ch](arg)
            else:
                menu_actions[ch]()

        except KeyError:
            print "Wrong Choice"
            menu_actions['main_menu']()
    return


def all_posts():
    for post in get_posts():
        print ("{} {}".format(post["id"], post["title"]))

    choice = raw_input(" >>  ")
    show_menu(choice)
    return


def fetch_single(post_id):
    print "Fetching Post with id {} !\n".format(post_id)
    print fetch_single(post_id)
    choice = raw_input(" >>  ")
    show_menu(choice)
    return


def create_post(title, body, id, user_id):
    create_single_post(title=title, body=body, id=id, user_id=user_id)


menu_actions = {
    'main_menu': show_menu(),
    '1': all_posts,
    '2': fetch_single,
}

if __name__ == "__main__":
    show_menu()
