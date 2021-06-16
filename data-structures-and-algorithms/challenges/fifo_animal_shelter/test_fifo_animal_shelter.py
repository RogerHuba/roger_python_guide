import pytest

from .fifo_animal_shelter import Animal, AnimalShelter, Cat, Dog


class TestAnimalShelter:

    @pytest.fixture()
    def shelter(self):
        return AnimalShelter()

    @pytest.fixture()
    def cat(self):
        return Cat('kitty', 5)

    @pytest.fixture()
    def dog(self):
        return Dog('Jessi', 4)

    def test_instance(self, shelter, cat, dog):
        assert shelter
        assert cat
        assert dog

    def test_enqueue_value_error(self, shelter):
        with pytest.raises(ValueError) as err:
            assert shelter.enqueue(Animal('John', 7, 'Turtle'))
        assert str(err.value) == 'Must be either a cat or a dog!'

    def test_enqueue_single_cat(self, shelter, cat):
        assert shelter.cats.front is None
        shelter.enqueue(cat)
        assert shelter.cats.front.val.type == 'Cat'

    def test_enqueue_single_dog(self, shelter, dog):
        assert shelter.dogs.front is None
        shelter.enqueue(dog)
        assert shelter.dogs.front.val.type == 'Dog'

    def test_enqueue_multiple_cats(self, shelter):
        cat1 = Cat('cat_1', 1)
        cat2 = Cat('cat_2', 2)
        cat3 = Cat('cat_3', 3)
        cat4 = Cat('cat_4', 4)
        assert shelter.cats.front is None

        shelter.enqueue(cat1)
        shelter.enqueue(cat2)
        shelter.enqueue(cat3)
        shelter.enqueue(cat4)

        assert len(shelter.cats) == 4
        assert shelter.cats.front.val.name == 'cat_1'
        assert shelter.cats.rear.val.name == 'cat_4'

    def test_enqueue_multiple_dogs(self, shelter):
        dog1 = Dog('dog_1', 1)
        dog2 = Dog('dog_2', 2)
        dog3 = Dog('dog_3', 3)
        dog4 = Dog('dog_4', 4)
        assert shelter.dogs.front is None

        shelter.enqueue(dog1)
        shelter.enqueue(dog2)
        shelter.enqueue(dog3)
        shelter.enqueue(dog4)

        assert len(shelter.dogs) == 4
        assert shelter.dogs.front.val.name == 'dog_1'
        assert shelter.dogs.rear.val.name == 'dog_4'

    def test_enqueue_mixed_animals(self, shelter):
        assert shelter.dogs.front is None
        assert shelter.cats.front is None

        cat1 = Cat('cat_1', 1)
        cat2 = Cat('cat_2', 2)
        dog1 = Dog('dog_1', 1)
        dog2 = Dog('dog_2', 2)

        shelter.enqueue(cat1)
        shelter.enqueue(dog1)
        shelter.enqueue(cat2)
        shelter.enqueue(dog2)

        assert len(shelter.dogs) == 2
        assert len(shelter.cats) == 2

    def test_dequeue_attribute_error(self, shelter):
        with pytest.raises(AttributeError) as err:
            shelter.dequeue()
        assert str(err.value) == 'No animals available!'

    def test_dequeue_value_error(self, shelter):
        with pytest.raises(ValueError) as err:
            shelter.dequeue('Turtle')
        assert str(err.value) == 'Must be either a cat or a dog!'

    def test_dequeue_cats(self, shelter):
        cat1 = Cat('cat_1', 1)
        cat2 = Cat('cat_2', 2)
        cat3 = Cat('cat_3', 3)
        cat4 = Cat('cat_4', 4)

        shelter.enqueue(cat1)
        shelter.enqueue(cat2)
        shelter.enqueue(cat3)
        shelter.enqueue(cat4)

        assert shelter.dequeue('cat').name == 'cat_1'
        assert shelter.dequeue('cat').name == 'cat_2'
        assert shelter.dequeue('cat').name == 'cat_3'
        assert shelter.dequeue('cat').name == 'cat_4'
        assert len(shelter.cats) == 0

    def test_dequeue_dogs(self, shelter):
        dog1 = Dog('dog_1', 1)
        dog2 = Dog('dog_2', 2)
        dog3 = Dog('dog_3', 3)
        dog4 = Dog('dog_4', 4)

        shelter.enqueue(dog1)
        shelter.enqueue(dog2)
        shelter.enqueue(dog3)
        shelter.enqueue(dog4)

        assert shelter.dequeue('dog').name == 'dog_1'
        assert shelter.dequeue('dog').name == 'dog_2'
        assert shelter.dequeue('dog').name == 'dog_3'
        assert shelter.dequeue('dog').name == 'dog_4'
        assert len(shelter.dogs) == 0
    def test_dequeue_mixed(self, shelter):
        dog1 = Dog('dog_1', 1)
        dog2 = Dog('dog_2', 2)
        cat1 = Cat('cat_1', 1)
        cat2 = Cat('cat_2', 2)

        shelter.enqueue(dog1)
        shelter.enqueue(dog2)
        shelter.enqueue(cat1)
        shelter.enqueue(cat2)

        assert shelter.dequeue('dog').name == 'dog_1'
        assert shelter.dequeue('cat').name == 'cat_1'
        assert shelter.dequeue('dog').name == 'dog_2'
        assert shelter.dequeue('cat').name == 'cat_2'
        assert len(shelter.dogs) == 0
        assert len(shelter.cats) == 0
