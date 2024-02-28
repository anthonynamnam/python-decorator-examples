class Person:

    _my_name = "Anthony"

    # Like a get function
    @property
    def name(self):
        print("Getting your name...")
        return self._my_name

    # Like a set function
    @name.setter
    def name(self,new_name):
        print("Setting your new name...")
        self._my_name = new_name

    # Like a delete function
    @name.deleter
    def name(self):
        print("Deleting your name...")
        del self._my_name

me = Person()

# Get your name
print(me.name)

# Set your name
me.name = "New Anthony"

# Delete your name
del me.name


# -------------------------------------------
class Game_Person:

    _id = "0123"

    # Like a get function
    @property
    def id(self):
        print("Getting your id...")
        return self._id

    # Like a set function
    # @id.setter
    # def name(self,new_id):
    #     print("Setting your new id...")
    #     self._id = new_id

game_me = Game_Person()

# Get your name
print(game_me.id)

# Set your name
game_me.id = "9999"