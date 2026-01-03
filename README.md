# 📚 Library Management System (LMS)

A **Library Management System** built with **Python Tkinter** for the GUI and **SQLite** for the backend database.  
This application allows **Admin Staff** and **Students** to manage library operations through a user‑friendly interface with persistent storage.

---

## ✨ Features
- 🔑 **User Authentication**
  - Admin Staff and Student registration & login
- 📖 **Book Management**
  - Add new books
  - Delete books
  - View all books
  - Search books by subject
- 📦 **Issue/Return System**
  - Issue books to students
  - Return books to library
  - Track issued books
- 🖥️ **GUI Interface**
  - Built with Tkinter
  - Simple and intuitive navigation
- 💾 **Persistent Storage**
  - SQLite database stored locally
  - Auto‑creation of required tables

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
