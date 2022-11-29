class Apuesta:
    def __init__(self, apostantes=None):
        if apostantes is None:
            apostantes = []
        self._apostantes = apostantes

    @property
    def apostantes(self):
        return self._apostantes

    @apostantes.setter
    def apostantes(self, apostantes):
        self._apostantes = apostantes