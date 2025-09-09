from sinais.senoide import Senoide
from sinais.quadrada import Quadrada
from sistemas.passa_baixa import PassaBaixa
from utils.plot import plotar

def main():
    # Gerar sinais
    seno = Senoide(frequencia=5, amplitude=1, duracao=1)
    quad = Quadrada(frequencia=5, amplitude=1, duracao=1)

    sinal_seno = seno.gerar()
    sinal_quad = quad.gerar()

    # Aplicar filtro passa-baixa
    filtro = PassaBaixa(cutoff=0.05)
    sinal_seno_filtrado = filtro.aplicar(sinal_seno)

    # Plotar
    plotar(seno.tempo, sinal_seno, "Senoide Original")
    plotar(seno.tempo, sinal_seno_filtrado, "Senoide Filtrada")
    plotar(quad.tempo, sinal_quad, "Quadrada Original")

if __name__ == "__main__":
    main()
