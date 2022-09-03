import datetime

def __post_init__(self):

    if not isinstance(self._id, int):
        raise ValueError('ID must be a valid int')
    if not isinstance(self.name, str):
        raise ValueError('Name must be a string')
    if not self.type in ('Fire', 'Grass', 'Water', 'Electric'):
        raise ValueError('Pokemon must be a valid type')
    if not isinstance(self.caught, bool):
        raise ValueError('Caught must be a bool')
 
class Pokemon():

    def __init__(self, _id: int, name: str, type: str, caught: bool):
        self._id = _id
        self.name = name
        self.type = type
        self.caught = caught
        self.lastUpdated = datetime.datetime.now()
        __post_init__(self)