
def greet_all(*args):
    for name in args:
        print(f"Hello, {name}!")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet_all("Alice", "Bob", "Charlie")
print_info(name="Sarthak", age=17,city="Akluj")