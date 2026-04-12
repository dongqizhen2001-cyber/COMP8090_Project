# COMP 8090SEF Course Project - Task 1
# Student: Dong QiZhen (董其臻) | SID: 13937844 | HKMU

class Book:
    def __init__(self, book_id, title):
        self.__book_id = book_id
        self.title = title
        self.__is_borrowed = False  
    
    def get_book_id(self):
        return self.__book_id

    def is_borrowed(self):
        return self.__is_borrowed

    def set_borrowed_status(self, status):
        self.__is_borrowed = status

    def __str__(self):
        status = "已借出" if self.__is_borrowed else "可借"
        return f"[{status}] {self.title} (代码: {self.__book_id})"

class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id 
        self.name = name
        self.borrowed_books = []  

    def get_user_id(self):
        return self.__user_id

    def get_max_books(self):
        return 0

    def display_info(self):
        print(f"ID: {self.__user_id}, 姓名: {self.name}, 已借: {len(self.borrowed_books)}/{self.get_max_books()}")

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def get_max_books(self):
        return 5  

    def display_info(self):
        print("[学生]", end=" ")
        super().display_info()

class Staff(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def get_max_books(self):
        return 10 

    def display_info(self):
        print("[教职工]", end=" ")
        super().display_info()
