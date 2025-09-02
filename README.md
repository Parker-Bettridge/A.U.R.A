# A.U.R.A Management Console  

This is a simple **Python-based role-based login system** with a command-line interface (CLI).  
It allows users to log in as an **Admin**, **Moderator**, or **Guest**, and each role has access to its own command console.  

---

## 🚀 Features
- Multi-user login system (**Admin, Moderator, Guest**)  
- Password verification for each user  
- Role-based command consoles  
- Simple and extendable structure for adding new roles and commands  
- User-friendly console interface with ASCII panels  

---

## 🛠️ Installation & Usage
Clone this repository or download the source code:  

```bash
git clone https://github.com/Parker-Bettridge/A.U.R.A.git
cd A.U.R.A

```
Run the main script:
```bash
python MAIN.py
```
---
## 👥 Default Users & Passwords
By default, the system ships with three accounts:

| Username  | Password  | Role      |
| --------- | --------- | --------- |
| Admin     | Admin     | Admin     |
| Moderator | Moderator | Moderator |
| Guest     | Guest     | Guest     |

---

📖 Commands

Currently, each role only supports one default command:

- Exit → Logs out the current user and returns to the login menu.

⚠️ Important: Users cannot add commands themselves. All available commands are pre-defined by the developer.

---

## 🧩 File Structure

```bash
├── MAIN.py       # Main program
├── README.md     # Project documentation
├── LICENSE       # MIT License for the project
```

---

## 📜 License

This project is open-source and licensed under the MIT License.
See the LICENSE file in this repository for the full license text.

---
