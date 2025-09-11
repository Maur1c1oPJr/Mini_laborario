from sinais.senoide import Senoide
from sinais.quadrada import Quadrada
from sistemas.passa_baixa import PassaBaixa
from utilis.plot import plotar

class Laboratorio:
    def __init__(self):
        self.sinais = {}      # dicionário para armazenar sinais
        self.filtros = {}     # dicionário para armazenar filtros

    def criar_senoide(self, nome, frequencia=5, amplitude=1, duracao=1, taxa_amostragem=1000):
        seno = Senoide(frequencia, amplitude, duracao, taxa_amostragem)
        self.sinais[nome] = seno.gerar()
        return self.sinais[nome], seno.tempo

    def criar_quadrada(self, nome, frequencia=5, amplitude=1, duracao=1, taxa_amostragem=1000):
        quad = Quadrada(frequencia, amplitude, duracao, taxa_amostragem)
        self.sinais[nome] = quad.gerar()
        return self.sinais[nome], quad.tempo

    def adicionar_filtro_passa_baixa(self, nome, cutoff=0.05):
        self.filtros[nome] = PassaBaixa(cutoff)

    def aplicar_filtro(self, nome_filtro, nome_sinal):
        if nome_filtro in self.filtros and nome_sinal in self.sinais:
            filtro = self.filtros[nome_filtro]
            sinal_filtrado = filtro.aplicar(self.sinais[nome_sinal])
            self.sinais[f"{nome_sinal}_filtrado"] = sinal_filtrado
            return sinal_filtrado
        else:
            raise ValueError("Filtro ou sinal não encontrado.")

    def plotar_sinal(self, nome_sinal, tempo, titulo=None):
        if titulo is None:
            titulo = nome_sinal
        if nome_sinal in self.sinais:
            plotar(tempo, self.sinais[nome_sinal], titulo)
        else:
            raise ValueError("Sinal não encontrado.")
