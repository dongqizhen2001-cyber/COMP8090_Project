# TASK 1: models.py 
# 包含核心 OOP 概念: 类 (Classes), 继承 (Inheritance), 封装 (Encapsulation), 多态 (Polymorphism)

class Book:
    def __init__(self, book_id, title):
        # 封装 (Encapsulation): 使用 __ 让 book_id 和 is_borrowed 变成私有属性
        self.__book_id = book_id
        self.title = title
        self.__is_borrowed = False  
    
    # Getter 方法：安全地获取私有属性
    def get_book_id(self):
        return self.__book_id

    def is_borrowed(self):
        return self.__is_borrowed

    # Setter 方法：安全地修改借阅状态
    def set_borrowed_status(self, status):
        self.__is_borrowed = status

    def __str__(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"[{status}] {self.title} (ID: {self.__book_id})"

# 1. 基础父类 (Base Class)
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id  # 封装: 私有属性
        self.name = name
        self.borrowed_books = []  

    def get_user_id(self):
        return self.__user_id

    # 这个方法将被子类重写，展现多态 (Polymorphism)
    def get_max_books(self):
        return 0

    def display_info(self):
        print(f"User ID: {self.__user_id}, Name: {self.name}, Borrowed: {len(self.borrowed_books)}/{self.get_max_books()}")

# 2. 学生子类 (Subclass) - 继承自 User
class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    # 多态: 重写父类方法
    def get_max_books(self):
        return 5  

    def display_info(self):
        print("[Student]", end=" ")
        super().display_info()

# 3. 教职工子类 (Subclass) - 继承自 User
class Staff(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    # 多态: 重写父类方法
    def get_max_books(self):
        return 10 

    def display_info(self):
        print("[Staff]", end=" ")
        super().display_info()
