import datetime

def show_start_time():
    print(f"Start talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def show_end_time():
    print(f"End talking --- {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def speak():
    show_start_time() # Newly Added
    print("I am a human")
    show_end_time() # Newly Added

def bark():
    show_start_time() # Newly Added
    print("Bark! Bark!")
    show_end_time() # Newly Added

def groot():
    show_start_time() # Newly Added
    print("I'm groot~ I'm groot~")
    show_end_time() # Newly Added

def main():
    speak()
    bark()
    groot()

if __name__ == "__main__":
    main()