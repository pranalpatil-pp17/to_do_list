# 📋 Flask ToDo List Application

This is a simple ToDo list application built with Flask and SQLAlchemy. It allows users to create, update, and delete tasks. The tasks are stored in a SQLite database.

## ✨ Features

- 📌 Add new tasks
- ✏️ Update existing tasks
- 🗑️ Delete tasks
- 📋 View all tasks

## 🛠️ Technologies Used

- Flask
- SQLAlchemy
- SQLite
- HTML
- CSS (optional, for styling)

## 🚀 Setup Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/todolist-flask.git
   cd todolist-flask

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt

4. **Set up the SQLite database:**

   ```sh
   python -c "from app import db; db.create_all()"

5. **Run the application:**

   ```sh
   python app.py

6. Open your web browser and navigate to http://127.0.0.1:5000/

## 📸 Screenshots

🏠 Home Page

➕ Add Task

✏️ Update Task

#### 📜 License
This project is licensed under the MIT License.
