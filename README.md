# 📖 MyLibraPy

```text
__  __       _ _     _                           
|  \/  |     (_) |   | |                          
| \  / | __ _ _| |__ | |__   __ _ _ __  _ __  ___ 
| |\/| |/ _` | | '_ \| '_ \ / _` | '_ \| '_ \/ __|
| |  | | (_| | | |_) | | | | (_| | |_) | |_) \__ \
|_|  |_|\__,_|_|_.__/|_| |_|\__,_| .__/| .__/|___/
                                 | |   | |        
                                 |_|   |_|        
```

*A simple CLI library manager – built for learning, testing, and practical use in school settings.*

---

## 🎒 Inspiration From the Classroom

As a teacher at the **European School Karlsruhe**, I often look for ways to connect code with real-life problems my students face.  
One recurring theme in our school life is **books**: schoolbooks, reading logs, book exchanges, and personal collections.

In my ICT classes, we are currently developing a full-stack **BookExchange** platform that allows students to offer and find used textbooks. It's a collaborative learning project – complete with database, server logic and frontend interface.

But while working on that, I realized:  
Why not also create a simple **personal book tracker** that any student or teacher can use on their own device?

**MyLibraPy** was created to fill that gap – a small, practical command-line application where students (and colleagues!) can add and manage books locally, explore how data storage works, and even customize the program if they want to dive deeper into Python.

---

## 🚀 What It Does

- 📚 Add new books with title, author, genre, and reading status  
- 👀 View your collection  
- 🔍 Search books by keyword  
- 🧾 Edit and delete entries  
- 📤 Export your collection to CSV  
- 📈 See basic stats (how many books, genres, status types)  
- 💾 Save your data to `books.json` for persistence  
- 🌈 Terminal UI with simple color highlights using `colorama`

---

## 🛠️ Setup & Usage

1. Clone the repository:

```bash
git clone https://github.com/freewimoe/P3_MyLibraPy.git
cd P3_MyLibraPy
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate       # On macOS/Linux
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Start the app:

```bash
python main.py
```

---

## 📦 Requirements

- Python 3.9+  
- `colorama` (for colors in the terminal)

---

## 🧪 For Students & Educators

This project is great for:
- 🧑‍🎓 Students who want to learn how programs handle data
- 👩‍🏫 Teachers who need examples of small but complete CLI projects
- 🧠 Everyone curious about Python, JSON files, and how apps can grow from simple ideas

It’s intentionally kept simple, **easy to read**, and ready to be extended.

---

## 👨‍🏫 About the Author

Created by **Friedrich-Wilhelm Möller**,  
ICT teacher at the **European School Karlsruhe**,  
as part of the **Code Institute** Full Stack Diploma – and as a tool to help students and teachers alike learn through making.

---

## 📜 License

This is a free educational project.  
Use it, remix it, learn from it – and if you improve it, feel free to share it back.

---

🧡 *Learning is best when it starts with something useful.*

