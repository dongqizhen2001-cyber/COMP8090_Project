# HKMU COMP 8090SEF - Task 1: Data Models
# Student: Dong QiZhen (董其臻) | SID: 13937844

class Book:
    def __init__(self, book_id, title):
        # 按照封装原则，把 ID 和状态设为私有属性
        # 这里的双下划线可以防止这些核心数据被外部直接修改
        self.__book_id = book_id
        self.title = title
        self.__is_borrowed = False  
    
    # 外部需要获取书的 ID 时，通过这个 Getter 方法来实现
    def get_book_id(self):
        return self.__book_id

    # 简单检查一下这本书是不是已经借出去了
    def is_borrowed(self):
        return self.__is_borrowed

    # 这里的 Setter 方法用来规范地更新书的借阅状态
    def set_borrowed_status(self, status):
        self.__is_borrowed = status

    def __str__(self):
        # 这里的输出逻辑是为了在列表里一眼就能看到书是否可用
        status = "已借出" if self.__is_borrowed else "可借"
        return f"[{status}] {self.title} (代码: {self.__book_id})"

class User:
    def __init__(self, user_id, name):
        # 同样封装好用户 ID，并用一个列表来存储他借过的书
        self.__user_id = user_id 
        self.name = name
        self.borrowed_books = []  

    def get_user_id(self):
        return self.__user_id

    def get_max_books(self):
        # 这里定义一个基础方法，具体额度留给子类去实现（体现多态思想）
        return 0

    def display_info(self):
        # 打印用户的基本信息和当前的借阅进度
        print(f"ID: {self.__user_id}, 姓名: {self.name}, 已借: {len(self.borrowed_books)}/{self.get_max_books()}")

# 这里体现了继承，Student 和 Staff 都共享 User 的基础属性
class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def get_max_books(self):
        # 按照题目要求，学生的借书上限固定为 5 本
        return 5  

    def display_info(self):
        print("[学生]", end=" ")
        super().display_info()

class Staff(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def get_max_books(self):
        # 教职工的限额比较高，重写为 10 本
        return 10 

    def display_info(self):
        print("[教职工]", end=" ")
        super().display_info()
