from library_system import LibrarySystem
from models import Book

def main():
    # 创建一个图书馆系统
    my_lib = LibrarySystem()
    
    # 试着加一本书
    b1 = Book(101, "Python Learning")
    my_lib.add_book(b1)

    print("System is running...")

if __name__ == "__main__":
    main()