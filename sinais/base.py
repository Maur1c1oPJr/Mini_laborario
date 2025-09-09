import numpy as np

class SinalBase:
    def __init__(self, frequencia=1.0, amplitude=1.0, duracao=1.0, taxa_amostragem=1000):
        self.frequencia = frequencia
        self.amplitude = amplitude
        self.duracao = duracao
        self.taxa_amostragem = taxa_amostragem
        self.tempo = np.linspace(0, duracao, int(taxa_amostragem * duracao), endpoint=False)

    def gerar(self):
        raise NotImplementedError("Método gerar() deve ser implementado nas subclasses.")
