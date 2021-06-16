class ForceUser:

    def attacking(self) -> str:
        return f'{self.name} is attacking!'

    def getting_hit(self) -> str:
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls) -> int:
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):
    '''
    Jedi Master Class
    '''
    count = 0

    def __init__(self, name='Random Master'):
        self.name = name
        JediMaster.count += 1

    def __str__(self) -> str:
        return f'{self.name} is in the House!'

    def attacking(self) -> str:
        return f'{self.name} is Force attacking!'

    @staticmethod
    def get_code() -> str:
        return 'There is no emotion, there is PEACE.'

    @classmethod
    def get_count(cls) -> int:
        return cls.count


class SithLord(ForceUser):
    '''
    Sith Lord Class
    '''

    count = 0

    def __init__(self, name='Random Sith'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def get_code() -> str:
        return 'Peace is a lie, there is only PASSION'

    @classmethod
    def get_count(cls) -> int:
        return cls.count


if __name__ == '__main__':
    newJedi = JediMaster('Yoda')
