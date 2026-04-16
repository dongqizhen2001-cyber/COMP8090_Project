# HKMU COMP 8090SEF - Library System Logic
# Developer: Dong QiZhen (董其臻) 13937844
# Logic reference: Python Software Foundation (2026) for Dictionary Time Complexity.

from models import Book, Student, Staff

class LibrarySystem:
    def __init__(self):
        # 这里我选择用字典（Dictionary）而不是列表，是因为哈希表的查找速度是 O(1)
        # 这对于处理图书馆大量的书籍和用户数据非常高效
        self.books = {}  
        self.users = {}  
        print("--- HKMU 图书馆系统已就绪 ---")

    def add_book(self, book):
        # 把书的对象存入系统字典，方便后续查找
        b_id = book.get_book_id()
        self.books[b_id] = book
        print(f"录入课程教材: {book.title} ({b_id})")

    def register_user(self, user):
        # 登记新用户到 users 字典
        u_id = user.get_user_id()
        self.users[u_id] = user
        print(f"欢迎新成员: {user.name}")

    def borrow_book(self, user_id, book_id):
        # 借书逻辑：先验证 ID 是否在我们的数据库中
        if user_id not in self.users or book_id not in self.books:
            print("提示: ID 输入不正确。")
            return

        user = self.users[user_id]
        book = self.books[book_id]

        # 检查书的状态，如果已被借出则跳过
        if book.is_borrowed():
            print(f"'{book.title}' 目前不在馆内。")
            return

        # 这里的核心逻辑是调用子类的 get_max_books() 
        # 系统会自动判断是按学生（5本）还是教工（10本）的限额来执行
        if len(user.borrowed_books) >= user.get_max_books():
            print(f"借阅失败: {user.name} 的额度已满 ({user.get_max_books()}本)。")
            return

        # 更新书的状态并加入用户的借书清单
        book.set_borrowed_status(True)
        user.borrowed_books.append(book)
        print(f"借阅成功: {user.name} 领走了 '{book.title}'。")

    def return_book(self, user_id, book_id):
        # 归还逻辑：核对用户和书籍的对应关系
        if user_id in self.users and book_id in self.books:
            user = self.users[user_id]
            book = self.books[book_id]
            # 确认该书确实是在该用户名下借出的
            if book in user.borrowed_books:
                book.set_borrowed_status(False)
                user.borrowed_books.remove(book)
                print(f"归还成功: '{book.title}' 已入库。")
            else:
                print("错误: 借阅列表匹配失败。")

    def show_status(self):
        # 展示全馆当前的状态汇总
        print("\n--- HKMU 春季课程教材借阅清单 ---")
        for book in self.books.values():
            print(book)
        print("-" * 30)
        for user in self.users.values():
            user.display_info()
