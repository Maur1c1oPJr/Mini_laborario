import matplotlib.pyplot as plt

def plotar(tempo, sinal, titulo="Sinal"):
    plt.plot(tempo, sinal)
    plt.title(titulo)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
