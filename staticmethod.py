class Typical:
    my_name = "Anthony"
    def say_hello(self):
        print(f"Hello! {self.my_name}")

class Static:
    @staticmethod
    def say_hello():
        print("Hello-static!")

# Example 1 (Error occurred)
Typical.say_hello()

# Example 2 (Typical way to call a method of an instance)
t = Typical()
t.say_hello()

# Example 3 (Call a static method of a class, without instantiating an object)
Static.say_hello()