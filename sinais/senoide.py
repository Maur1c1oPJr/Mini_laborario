import numpy as np
from .base import SinalBase

class Senoide(SinalBase):
    def gerar(self):
        return self.amplitude * np.sin(2 * np.pi * self.frequencia * self.tempo)
