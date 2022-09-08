class Computer():
    def __init__(self, computer, ram, storage):
        self.computer = computer
        self.ram = ram
        self.storage = storage

# Class Mobile inherits Computer
class Mobile(Computer):
    def __init__(self, computer, ram, storage, model):
        super().__init__(computer, ram, storage)
        self.model = model

Apple = Mobile('Apple', 2, 64, 'iPhone X')
print('The mobile is:', Apple.computer)
print('The RAM is:', Apple.ram)
print('The storage is:', Apple.storage)
print('The model is:', Apple.model)