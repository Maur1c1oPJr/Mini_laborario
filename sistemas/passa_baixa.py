import numpy as np
from .filtro_base import FiltroBase

class PassaBaixa(FiltroBase):
    def __init__(self, cutoff):
        self.cutoff = cutoff

    def aplicar(self, sinal):
        fft = np.fft.fft(sinal)
        freq = np.fft.fftfreq(len(sinal))
        fft[np.abs(freq) > self.cutoff] = 0
        return np.fft.ifft(fft).real
