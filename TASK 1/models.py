#这里定义书的类
class Book:  # 注意：这里首字母 B 要大写
    def __init__(self, book_id, title):
        self.book_id = book_id  # 统一用 book_id
        self.title = title
        self.is_borrowed = False  # 默认没被借走
    
    def __str__(self):
        # 打印的时候显示书名
        return f"{self.title} (ID: {self.book_id})"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name