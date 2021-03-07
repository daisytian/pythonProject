# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def spam():
    eggs = 31338
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()
# 一个函数的局部变量完全与其他函数中的局部变量分隔开来
# 全局变量可以在局部作用域中读取
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)




