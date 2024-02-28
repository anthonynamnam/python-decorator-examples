class Typical:
    my_name = "Anthony"

    @classmethod
    def say_hello(self):
        print(f"Hello! {self.my_name}")

    def say_morning(self):
        print(f"Good Morning! {self.my_name}")

# Example 1 (Alloed to access a class method without instantiating an instance)
Typical.say_hello()

print("--------------")
# Example 2 (Error Occurred)
Typical.say_morning()