class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce_self(self):
        print(f"Hello! I am {self.name}.")
        print(f"I am a {self.color} colored robot. Nice to meet you!")

my_robot = Robot("Chiti", "Blue")

my_robot.introduce_self()