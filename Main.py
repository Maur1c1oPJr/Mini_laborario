from laboratorio.laboratorio import Laboratorio

def main():
    lab = Laboratorio()

    # Criar sinais
    sinal_seno, tempo_seno = lab.criar_senoide("senoide_5Hz")
    sinal_quad, tempo_quad = lab.criar_quadrada("quadrada_5Hz")

    # Adicionar filtro e aplicar
    lab.adicionar_filtro_passa_baixa("pb", cutoff=0.05)
    sinal_seno_filtrado = lab.aplicar_filtro("pb", "senoide_5Hz")

    # Escolher qual senoide plotar
    print("Opções de senoide para plotar:")
    print("1 - Senoide Original")
    print("2 - Senoide Filtrada")
    print("3 - Senoide Quadrada")
    escolha = input("Digite o número da senoide que deseja plotar: ")

    if escolha == "1":
        lab.plotar_sinal("senoide_5Hz", tempo_seno, "Senoide Original")
    elif escolha == "2":
        lab.plotar_sinal("senoide_5Hz_filtrado", tempo_seno, "Senoide Filtrada")
    elif escolha == "3":
        lab.plotar_sinal("quadrada_5Hz", tempo_quad, "Quadrada Original")
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
