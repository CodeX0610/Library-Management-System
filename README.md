# 📚 Library Management System (LMS)

A **Library Management System** built with **Python Tkinter** for the GUI and **SQLite** for the backend database.  
This application allows **Admin Staff** and **Students** to manage library operations through a user‑friendly interface with persistent storage.

---

## 🗄️ Database Schema
The system uses **SQLite** with the following tables:

| Table Name   | Purpose                                |
|--------------|----------------------------------------|
| `empdetail`  | Employee/Admin staff credentials       |
| `studetail`  | Student credentials                    |
| `books`      | Book records (ID, Title, Subject, etc.)|
| `issuedetail`| Issued book records                    |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.x
- Tkinter (comes pre‑installed with Python)
- SQLite3 (comes bundled with Python)

### Steps
```bash
# Clone the repository
git clone https://github.com/CodeX0610/Library-Management-System.git

# Navigate into the project directory
cd Library-Management-System

# Run the application
python LMS.py
```
---

## 🚀 Usage
- ▶️ **Launch the application**
  - Run the program using:
    ```bash
    python LMS.py
    ```
- 📝 **Register**
  - Sign up as **Admin Staff** or **Student**.
- 🔑 **Login**
  - Enter your credentials to access the system.
- 📚 **Library Operations**
  - Add/Delete/Search/View books  
  - Issue or Return books  
  - View issued book records
- 🚪 **Logout**
  - End your session securely when finished.

---

## 🧑‍💻 Author
- CodeX0610

---

## 🤝 Contributing
Contributions are welcome!
  - Fork the repository
  - Create a new branch (feature-xyz)
  - Commit your changes
  - Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with attribution.

---
