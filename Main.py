from laboratorio.laboratorio import Laboratorio

def main():
    lab = Laboratorio()

    # Criar sinais
    sinal_seno, tempo_seno = lab.criar_senoide("senoide_5Hz")
    sinal_quad, tempo_quad = lab.criar_quadrada("quadrada_5Hz")

    # Adicionar filtro e aplicar
    lab.adicionar_filtro_passa_baixa("pb", cutoff=0.05)
    sinal_seno_filtrado = lab.aplicar_filtro("pb", "senoide_5Hz")

    # Plotar sinais
    lab.plotar_sinal("senoide_5Hz", tempo_seno, "Senoide Original")
    lab.plotar_sinal("senoide_5Hz_filtrado", tempo_seno, "Senoide Filtrada")
    lab.plotar_sinal("quadrada_5Hz", tempo_quad, "Quadrada Original")

if __name__ == "__main__":
    main()
