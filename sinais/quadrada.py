import numpy as np
from .base import SinalBase

class Quadrada(SinalBase):
    def gerar(self):
        return self.amplitude * np.sign(np.sin(2 * np.pi * self.frequencia * self.tempo))
