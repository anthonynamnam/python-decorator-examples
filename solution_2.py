# solution_2.py
import datetime

def show_time(func):
    def wrapper():
        print(f"Start talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        func()
        print(f"End talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return wrapper

@show_time
def speak(name):
    print(f"I am {name}") # <-- add the name argument here

@show_time
def bark():
    print("Bark! Bark!")

@show_time
def groot(name = "grootttt"):
    print(f"I'm groot~ I'm {name}~") # <-- add the name argument here

def main():
    speak(name="Anthony")
    bark()
    groot(name="Groooooot")

if __name__ == "__main__":
    main()
