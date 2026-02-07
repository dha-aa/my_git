import os

name = input("What is your name : ")
age = input("How old are you : ")


def write(a):
    with open("user.txt",a) as f:
        f.write(f"User name:{name}\n"),
        f.write(f"User age:{age}\n")


if os.path.exists("user.txt"):
    write(a="a")
else:
    write(a="w")
    