# MyLibraPy

```text
__  __ _ _ _     _             
|  \/  (_) |   (_)            
| \  / |_| |__  _ _ __   __ _ 
| |\/| | | '_ \| | '_ \ / _` |
| |  | | | |_) | | | | | (_| |
|_|  |_|_|_.__/|_|_| |_|\__, |
                         __/ |
                        |___/ 
```

*A simple CLI library manager – built for learning, testing, and practical use in school settings.*

---

## 🔒 Inspiration From the Classroom

As a teacher at the **European School Karlsruhe**, I often look for ways to connect coding with real-life challenges my students face. One recurring theme in school life is **books**: borrowing, trading, and trying to remember what you’ve read or loaned out. That’s what inspired **MyLibraPy**.

This project started as a classroom experiment. I wanted to explore with my students how data could be managed effectively using Python, and how to build a usable, text-based tool that anyone could adapt. MyLibraPy is part of our ongoing journey toward building a full **BookExchange system** with database logic, GUI, and server integration. But this tool stands on its own, too – a tiny librarian in your terminal!

---

## ✨ Features

### Existing Features

- 📚 **Add Book**  
  Lets the user enter title, author, genre, and status (read/unread/wishlist). Data is saved instantly to `books.json`.

- 👀 **View Books**  
  Lists all stored books in a readable, numbered format.

- 🔍 **Search**  
  Users can search books by keyword (title, author, or genre).

- ✏️ **Edit Book**  
  Allows the user to update any field of a selected book.

- ❌ **Delete Book**  
  Users can safely delete a book with confirmation.

- 📤 **Export to CSV**  
  One-click export to `books_export.csv` for use in Excel or Google Sheets.

- 📊 **Statistics**  
  Displays total books, genre breakdown, and status distribution.

- 💾 **Persistent Storage**  
  All data is saved and loaded from `books.json`, making the app restart-safe.

---

## 🧪 Testing

All features were tested manually in the terminal. Testing included:

- Adding multiple books with different data
- Searching with partial and full keywords
- Editing and deleting entries by number
- Exporting CSV and checking file contents
- Re-running the app to verify persistent loading from JSON

Tested in:
- Windows Terminal (PowerShell, CMD)
- VS Code integrated terminal

Validator testing:
- No external HTML/CSS used, so not applicable
- Python code reviewed using pylint and black for formatting

---

## 🐛 Known Issues

- Input validation is basic: no blocking of empty genres or status typos
- Status field accepts any string – might benefit from choice restriction

---

## 🚀 Deployment

This CLI app runs locally via Python:

1. Clone the repo:
   ```bash
   git clone https://github.com/freewimoe/P3_MyLibraPy.git
   cd P3_MyLibraPy
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python main.py
   ```

---

## 📦 Requirements

```
colorama==0.4.6
```

Stored in `requirements.txt`. Install via `pip install -r requirements.txt`.

---

## 🧭 Future Features

- GUI version using Tkinter or PyQt
- Sync with cloud for shared book lists
- Multiple user profiles
- Book rating / review system

---

## 🙏 Credits

- [Colorama](https://github.com/tartley/colorama) for beautiful terminal output
- My students at the European School Karlsruhe for testing and feedback
- Code Institute for pushing us to think in full-stack terms

---

## 🔗 Live Repository

👉 [github.com/freewimoe/P3_MyLibraPy](https://github.com/freewimoe/P3_MyLibraPy)

---

Thanks for reading – and happy book tracking 📚
