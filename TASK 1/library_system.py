# HKMU COMP 8090SEF - 核心逻辑实现
# 董其臻 13937844

from models import Book, Student, Staff

class LibrarySystem:
    def __init__(self):
        self.books = {}  
        self.users = {}  
        print("--- HKMU 图书馆系统已就绪 ---")

    def add_book(self, book):
        b_id = book.get_book_id()
        self.books[b_id] = book
        print(f"录入课程教材: {book.title} ({b_id})")

    def register_user(self, user):
        u_id = user.get_user_id()
        self.users[u_id] = user
        print(f"欢迎新成员: {user.name}")

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users or book_id not in self.books:
            print("提示: ID 输入不正确。")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        if book.is_borrowed():
            print(f"'{book.title}' 目前不在馆内。")
            return

        if len(user.borrowed_books) >= user.get_max_books():
            print(f"借阅失败: {user.name} 的额度已满 ({user.get_max_books()}本)。")
            return

        book.set_borrowed_status(True)
        user.borrowed_books.append(book)
        print(f"借阅成功: {user.name} 领走了 '{book.title}'。")

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]
            if book in user.borrowed_books:
                book.set_borrowed_status(False)
                user.borrowed_books.remove(book)
                print(f"归还成功: '{book.title}' 已入库。")
            else:
                print("错误: 借阅列表匹配失败。")

    def show_status(self):
        print("\n--- HKMU 春季课程教材借阅清单 ---")
        for book in self.books.values():
            print(book)
        print("-" * 30)
        for user in self.users.values():
            user.display_info()
