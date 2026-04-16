# HKMU COMP 8090SEF Course Project - Entry Point
# Author: Dong QiZhen (董其臻) 13937844
# AI Declaration: Generative AI (Gemini) was used for optimizing code structure and comments.

import sys
from models import Book, Student, Staff
from library_system import LibrarySystem

def show_menu():
    # 菜单部分采用了清晰的中文指引，方便用户操作
    print("\n" + "="*45)
    print("  HKMU 课程管理系统 - 董其臻 (13937844)")
    print("="*45)
    print("  1. 添加课程教材")
    print("  2. 注册校内用户")
    print("  3. 教材借阅办理")
    print("  4. 教材归还办理")
    print("  5. 查看当前教材状态")
    print("  6. 退出系统")
    print("="*45)

def main():
    # 实例化系统后台逻辑
    my_lib = LibrarySystem()
    
    # 考虑到演示的方便，这里先预载一些咱们这学期的课程教材
    my_lib.add_book(Book("COMP8090", "Data Structures And Algorithms"))
    my_lib.add_book(Book("COMP8650", "Design And Analysis Of Algorithms"))
    my_lib.add_book(Book("COMP8670", "Operating Systems"))
    my_lib.add_book(Book("COMP8920", "AI and Machine Learning"))
    my_lib.add_book(Book("COMP8960", "Capstone Project"))

    # 预载一个学生账号（我的）和一个测试用的教工账号
    my_lib.register_user(Student("13937844", "董其臻 (David)"))
    my_lib.register_user(Staff("HKMU_Prof", "何文田校区教授"))

    # 进入主循环，直到用户手动选择退出
    while True:
        show_menu()
        cmd = input("请选择操作 (1-6): ").strip()

        if cmd == '1':
            bid = input("课程代码 (如 COMP8090): ")
            title = input("教材名称: ")
            my_lib.add_book(Book(bid, title))
        elif cmd == '2':
            uid = input("学号/教工号: ")
            name = input("姓名: ")
            role = input("身份 (1:学生, 2:教工): ")
            if role == '1':
                my_lib.register_user(Student(uid, name))
            else:
                my_lib.register_user(Staff(uid, name))
        elif cmd == '3':
            uid = input("用户 ID: ")
            bid = input("课程代码: ")
            my_lib.borrow_book(uid, bid)
        elif cmd == '4':
            uid = input("用户 ID: ")
            bid = input("课程代码: ")
            my_lib.return_book(uid, bid)
        elif cmd == '5':
            my_lib.show_status()
        elif cmd == '6':
            print("系统安全退出。")
            sys.exit()
        else:
            print("输入指令无效，请重新选择。")

if __name__ == "__main__":
    main()
