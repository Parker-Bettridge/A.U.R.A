import os
import time

users = ["Admin", "Moderator", "Guest"]
passwords = ["Admin", "Moderator", "Guest"]
role = ["Admin", "Moderator", "Guest"]

admin_commands = ["Exit"]
mod_commands = ["Exit"]
guest_commands = ["Exit"]


def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def panel():
    print("╔═══════════════════════════════════════════╗")
    print("║                                           ║")
    print("║         A.U.R.A Management Console        ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")

def panel_top():
    print("╔═══════════════════════════════════════════╗")
    print("║                                           ║")
    print("║         A.U.R.A Management Console        ║")
    print("║                                           ║")
    print("╠═══════════════════════════════════════════╣")

def password_check(expected_password_value, username, index_user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║       Please Enter User's PassWord        ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    entered_password = input(">>> ")

    if expected_password_value != entered_password:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║    Please Enter Correct User PassWord     ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        password_check(expected_password_value, username, index_user)

    else:
        role_check(username, index_user)

def select_user():
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║          Please Enter UserName:           ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    user = input(">>> ")

    try:
        user_index_position = users.index(user)

        expected_password_value = passwords[user_index_position]
        password_check(expected_password_value, user, user_index_position)

    except ValueError:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║       Please Enter A Valid UserName       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        select_user()

def role_check(username_action, index):
    clear_screen()
    panel()

    try:
        role_user = role[index]

        if role_user == "Admin":
            admin(username_action)

        if role_user == "Moderator":
            moderator(username_action)

        if role_user == "Guest":
            guest(username_action)

    except ValueError:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║                 Role Error                ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        select_user()


def admin(admin_user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║        Welcome To The Admin Console       ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    admin_action = input(admin_user + " >>> ")

    if admin_action in admin_commands:
        if admin_action == 'Exit':
            select_user()

    else:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║        Please Enter A Valid Command       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)
        admin(admin_user)

def moderator(mod_user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║      Welcome To The Moderator Console     ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    mod_action = input(mod_user + " >>> ")

    if mod_action in mod_commands:
        if mod_action == 'Exit':
            select_user()

    else:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║        Please Enter A Valid Command       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)
        moderator(mod_user)

def guest(guest_user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║        Welcome To The Guest Console       ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    guest_action = input(guest_user + " >>> ")

    if guest_action in mod_commands:
        if guest_action == 'Exit':
            select_user()

    else:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║        Please Enter A Valid Command       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)
        guest(guest_user)

select_user()
