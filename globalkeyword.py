count = 0  # Global variable

def increment():
    global count  
    count += 1   
def show_count():
    print("Current count:", count)
increment()
increment()
show_count()

