import datetime

def show_time(func):
    def wrapper():
        # Preceding Operation
        print(f"Start talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        # The original function
        func()
        # Succeeding Operation
        print(f"End talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return wrapper

@show_time # Add the decorator here
def speak():
    print("I am a human")

@show_time # Add the decorator here
def bark():
    print("Bark! Bark!")

@show_time # Add the decorator here
def groot():
    print("I'm groot~ I'm groot~")

def main():
    speak()
    bark()
    groot()

if __name__ == "__main__":
    main()