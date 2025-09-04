import os
import time
import ast
from cryptography.fernet import Fernet

# ----- Encryption Setup -----
KEY_FILE = "secret.key"
DATA_FILE = "user_data.dat"

def generate_key():
    """Generate encryption key (run once)."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def save_data(users, passwords, roles):
    key = load_key()
    f = Fernet(key)
    data = str({"users": users, "passwords": passwords, "roles": roles}).encode()
    encrypted_data = f.encrypt(data)
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)

def load_data():
    if not os.path.exists(DATA_FILE):
        return None
    key = load_key()
    f = Fernet(key)
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    data = ast.literal_eval(decrypted_data.decode())
    return data["users"], data["passwords"], data["roles"]

# ----- Commands -----
admin_commands = ["Exit", "Help", "Create", "Delete", "Edit"]
mod_commands = ["Exit", "Help"]
guest_commands = ["Exit", "Help"]

role_options = ["Admin", "Moderator", "Guest"]

# ----- User Interface -----
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def amdin_panel(user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║            Availible Commands:            ║")
    print("║        Exit - Displays LogIn Menu         ║")
    print("║        Help - Displays This Menu          ║")
    print("║        Create - Creates User              ║")
    print("║        Delete - Deletes User              ║")
    print("║        Edit - Edits User                  ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    time.sleep(3)
    admin(user)

def mod_panel(user):
    clear_screen()
    panel_top()    
    print("║                                           ║")
    print("║            Availible Commands:            ║")
    print("║        Exit - Displays LogIn Menu         ║")
    print("║        Help - Displays This Menu          ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    time.sleep(3)
    moderator(user)

def guest_panel(user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║            Availible Commands:            ║")
    print("║        Exit - Displays LogIn Menu         ║")
    print("║        Help - Displays This Menu          ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    time.sleep(3)
    guest(user)

# ----- User creation and deletion -----

def create_user(user):
    # --- Get unique username ---
    while True:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║        What Is New User's UserName?       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        new_user = input(user + " >>> ")
        if new_user == 'Exit':
            admin(user)
        if new_user not in users:
            users.append(new_user)
            save_data(users, passwords, roles)
            break
        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║ Please Enter A UserName That Isn't In Use ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)

    # --- Get password ---
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║        What Is New User's PassWord?       ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    new_user_password = input(user + " >>> ")
    if new_user_password == 'Exit':
        admin(user)
    passwords.append(new_user_password)
    save_data(users, passwords, roles)

    # --- Get valid role ---
    valid_roles = ["Admin", "Moderator", "Guest"]
    while True:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║          What Is New User's Role?         ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        new_user_role = input(user + " >>> ")
        if new_user_role == 'Exit':
            admin(user)        
        if new_user_role in valid_roles:
            roles.append(new_user_role)
            save_data(users, passwords, roles)
            break
        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║         Please Enter Valid Role           ║")
            print("║  (Valid Roles: Admin, Moderator, Guest)   ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)

    # --- Success message ---
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║     New User Was Successfully Created     ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    time.sleep(3)
    admin(user)

    # ---

def delete_user(user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║      What User Do You Want To Delete?     ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    selete = input(user + " >>> ")
        
    if selete == 'Exit':
        admin(user)
        
    if selete in users:
        index_delete = users.index(selete)

        if selete == 'Admin':
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║    You Can't Delete Default Admin User    ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            delete_user(user)
        
        if selete != 'Admin':
            index_delete = users.index(selete)
            del users[index_delete]
            del passwords[index_delete]
            del roles[index_delete]        
            save_data(users, passwords, roles)
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║       User Was Successfully Deleted       ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            admin(user)

    else:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║       Please Enter A Valid UserName       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)
        delete_user(user)

def edit_user(user):
    while True:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║       What User Do You Want To Edit?      ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        edit = input(user + " >>> ")

        if edit == 'Exit':
            admin(user)

        if edit == "Admin":
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║  The Default Admin User Can't Be Edited   ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            continue  # go back to asking for a username

        if edit in users:
            index_edit = users.index(edit)
            edit_user_action(user, index_edit)
            break  # exit the loop after editing
        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║       Please Enter A Valid UserName       ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)


def edit_user_action(user, index):
    while True:
        valid_options = ["UserName", "PassWord", "Role", "Exit"]

        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║         What Do You Want To Edit?         ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        edit_action = input(user + " >>> ")

        if edit_action == 'Exit':
            admin(user)

        if edit_action in valid_options:
            break
        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║        Please Enter A Valid Option        ║")
            print("║ (Valid Options: UserName, PassWord, Role) ║")
            print("║           Or Type Exit To Leave           ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)

    if edit_action == 'Exit':
        admin(user)
        
    if edit_action == 'UserName':
        while True:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║      What Is The User's New UserName?     ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            new_userName = input(user + " >>> ")

            if new_userName == 'Exit':
                admin(user)

            if new_userName not in users:
                users[index] = new_userName
                save_data(users, passwords, roles)
                clear_screen()
                panel_top()
                print("║                                           ║")
                print("║     UserName Was Successfully Changed     ║")
                print("║                                           ║")
                print("╚═══════════════════════════════════════════╝")
                time.sleep(3)
                edit_user_action(user, index)
            else:
                clear_screen()
                panel_top()
                print("║                                           ║")
                print("║ Please Enter A UserName That Isn't In Use ║")
                print("║                                           ║")
                print("╚═══════════════════════════════════════════╝")
                time.sleep(3)

    if edit_action == 'PassWord':
        while True:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║      What Is The User's New PassWord?     ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            new_user_password = input(user + " >>> ")

            if new_user_password == 'Exit':
                admin(user)

            passwords[index] = new_user_password
            save_data(users, passwords, roles)
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║     PassWord Was Successfully Changed     ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            edit_user_action(user, index)
        
    # --- Get valid role ---
    valid_roles = ["Admin", "Moderator", "Guest"]
    while True:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║          What Is User's New Role?         ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        uses_role = input(user + " >>> ")

        if new_user_password == 'Exit':
            admin(user)

        if uses_role in valid_roles:
            roles[index] = uses_role
            save_data(users, passwords, roles)
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║       Role Was Successfully Changed       ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            edit_user_action(user, index)
        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║         Please Enter Valid Role           ║")
            print("║  (Valid Roles: Admin, Moderator, Guest)   ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)

# ----- Login and Role Checking -----
def password_check(expected_password, username, index_user):
    clear_screen()
    panel_top()
    print("║                                           ║")
    print("║       Please Enter User's PassWord        ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    entered_password = input(">>> ")

    if expected_password != entered_password:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║    Please Enter Correct User PassWord     ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        password_check(expected_password, username, index_user)
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

    if user == 'Exit':
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        # Convert current time to minutes since midnight
        current_minutes = current_hour * 60 + current_minute

        # Define open and closed times in minutes
        open_start = 6 * 60       # 06:00
        open_end = 18 * 60        # 18:00

        # Check if current time is within open or closed hours
        if open_start <= current_minutes < open_end:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║       GoodBye, Have An Amazing Day        ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            os._exit(0)

        else:
            clear_screen()
            panel_top()
            print("║                                           ║")
            print("║       GoodBye, Have An Amazing Night      ║")
            print("║                                           ║")
            print("╚═══════════════════════════════════════════╝")
            time.sleep(3)
            os._exit(0)


    if user != 'Exit':
        try:
            user_index = users.index(user)
            expected_password = passwords[user_index]
            password_check(expected_password, user, user_index)
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
    try:
        role_user = roles[index]

        if role_user == "Admin":
            admin(username_action)
        elif role_user == "Moderator":
            moderator(username_action)
        elif role_user == "Guest":
            guest(username_action)
        else:
            raise ValueError

    except ValueError:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║                 Role Error                ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)        
        select_user()

# ----- Role Consoles -----
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

        if admin_action == 'Help':
            amdin_panel(admin_user)

        if admin_action == 'Create':
            create_user(admin_user)

        if admin_action == 'Delete':
            delete_user(admin_user)

        if admin_action == 'Edit':
            edit_user(admin_user)

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
        if mod_action == 'Help':
            mod_panel(mod_user)

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

    if guest_action in guest_commands:
        if guest_action == 'Exit':
            select_user()
        if guest_action == 'Help':
            guest_panel(guest_user)

    else:
        clear_screen()
        panel_top()
        print("║                                           ║")
        print("║        Please Enter A Valid Command       ║")
        print("║                                           ║")
        print("╚═══════════════════════════════════════════╝")
        time.sleep(3)
        guest(guest_user)

# ----- Main Execution -----
if not os.path.exists(KEY_FILE):
    generate_key()

loaded = load_data()
if loaded:
    users, passwords, roles = loaded
else:
    users = ["Admin", "Moderator", "Guest"]
    passwords = ["Admin", "Moderator", "Guest"]
    roles = ["Admin", "Moderator", "Guest"]

try:
    select_user()
finally:
    # Save user, password, and role lists encrypted on exit
    save_data(users, passwords, roles)
