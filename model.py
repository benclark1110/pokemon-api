class Pokemon():

    def __init__(self, _id: int, name: str, type: str, caught: bool):
        self._id = _id
        self.name = name
        self.type = type
        self.caught = caught