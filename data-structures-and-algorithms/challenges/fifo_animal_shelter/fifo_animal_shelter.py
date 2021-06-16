from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Animal:
    def __init__(self, name, age, _type='Animal'):
        self.name = name
        self.age = age
        self.type = _type


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Cat'


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Dog'


class AnimalShelter:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.animal_order = Queue()

    def enqueue(self, animal):
        """Add passed in animal object to the queue

        Args:
            animal (obj): Expects either Cat() or Dog() instance

        Raises:
            ValueError: If not Cat() or Dog() is passed in
        """
        if animal.type == 'Cat':
            self.cats.enqueue(animal)
            self.animal_order.enqueue('Cat')
        elif animal.type == 'Dog':
            self.dogs.enqueue(animal)
            self.animal_order.enqueue('Dog')
        else:
            raise ValueError('Must be either a cat or a dog!')

    def dequeue(self, preference=None):
        """Get the longest waiting in queue Cat() or Dog() depending on passed in preference. If no preference passed in get the longest waiting in queue animal

        Args:
            preference (str, optional): Animal to be returned (cat or dog). Defaults to None.

        Raises:
            ValueError: If not a cat or a dog is passed in as a preference
            AttributeError: When no animals is available

        Returns:
            obj: Cat() or Dog() instance
        """
        try:
            if not preference:
                preference = self.animal_order.dequeue()
            if preference.lower() == 'cat':
                animal = self.cats.dequeue()
            elif preference.lower() == 'dog':
                animal = self.dogs.dequeue()
            else:
                raise ValueError('Must be either a cat or a dog!')
            return animal

        except AttributeError as err:
            raise AttributeError('No animals available!')
