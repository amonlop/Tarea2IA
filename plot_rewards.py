import matplotlib.pyplot as plt
import os

carpeta = "rewards"

# Archivos organizados por ambiente
ambiente_1 = {
    "Rewards_qlearning_1.txt": "Q-Learning",
    "Rewards_sarsa_1.txt": "SARSA"
}
ambiente_2 = {
    "Rewards_qlearning_2.txt": "Q-Learning",
    "Rewards_sarsa_2.txt": "SARSA"
}

def cargar_datos(ruta_archivo):
    episodios, rewards = [], []
    try:
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.strip():
                    ep, rw = linea.strip().split(",")
                    episodios.append(int(ep))
                    rewards.append(float(rw))
    except FileNotFoundError:
        print(f"no se encontró el archivo: {ruta_archivo}")
    return episodios, rewards

def graficar_curvas(diccionario, nombre_ambiente, salida):
    plt.figure(figsize=(10, 5))
    for archivo, etiqueta in diccionario.items():
        ruta = os.path.join(carpeta, archivo)
        x, y = cargar_datos(ruta)
        plt.plot(x, y, label=etiqueta, linewidth=0.4)
    
    plt.title(f"Curva de Aprendizaje - Ambiente {nombre_ambiente}")
    plt.xlabel("Episodio")
    plt.ylabel("Reward acumulado")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta, salida))

graficar_curvas(ambiente_1, "1", "curva_ambiente1.png")
graficar_curvas(ambiente_2, "2", "curva_ambiente2.png")
