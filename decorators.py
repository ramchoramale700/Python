def star(func):
    def wrapper():
        print("*")
        func()
        print("*")
    return wrapper

def smile(func):
    def wrapper():
        print(":)")
        func()
        print(":)")
    return wrapper

@star
def hello():
    print("Hello!")

@smile
def welcome():
    print("Welcome!")

hello()
welcome()