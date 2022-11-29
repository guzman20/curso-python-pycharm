from abc import ABC


class Nombrable(ABC):
    def __init__(self, id_, nombre):
        self._id = id_
        self._nombre = nombre

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, _id):
        self._id = _id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
