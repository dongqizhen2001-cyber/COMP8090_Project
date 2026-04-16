# HKMU COMP 8090SEF - Task 1: Course Material Management System

Student Name: Dong QiZhen (董其臻)
Student ID: 13937844

---

## Video Link
[此处替换为你的视频链接]

---

## Project Overview
This system uses OOP to manage library books for Students and Staff. It uses Hash Tables (Dictionaries) for fast O(1) searches.

### OOP Concepts Applied:
- Encapsulation: Used private attributes like __is_borrowed to protect data.
- Inheritance: Student and Staff inherit from the base User class.
- Polymorphism: get_max_books() is overridden to enforce limits (5 for students, 10 for staff).

---

## User Guide (How to Run)
1. Open your terminal and navigate to the TASK 1 directory.
2. Run the command: python main.py
3. Use the menu (1-6) to interact with the system:
   - Press 5 to view the initialized course list.
   - Press 3 to test the borrowing limit.
   - Press 4 to return a book.