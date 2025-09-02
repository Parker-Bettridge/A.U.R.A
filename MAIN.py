import os
import time

users = ["Admin"]
passwords = ["Admin"]

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

def password_check(expected_password_value):
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
        password_check(expected_password_value)

    else:
        print("cool")

def select_user():
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║          Please Enter UserName:           ║")
    print("║            or Type 0 To Exit              ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    user = input(">>> ")

    try:
        user_index_position = users.index(user)

        expected_password_value = passwords[user_index_position]
        password_check(expected_password_value)

    except ValueError:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║       Please Enter A Valid UserName       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        select_user()

select_user()
