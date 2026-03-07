from models import Book, User

class LibrarySystem:
    def __init__(self):
        self.books = []  # 用列表存所有的书
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def borrow_book(self, user_id, book_id):
        # 以后在这里写借书的逻辑
        # 1. 找到书
        # 2. 检查有没有被借走
        # 3. 更新状态
        pass  # 先占个位，还没写完