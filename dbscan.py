import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("graficos_dbScan", exist_ok=True)

#distancia euclidiana
def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

#busca los puntos(vecinos) que están a una distancia menor o igual a eps del punto dado 
#puntos es l
def range_query(puntos, punto, eps):
    neighbors = []
    for other in puntos:
        if distance(punto, other) <= eps:
            neighbors.append(other)
    return neighbors

def dbscan(puntos, eps, min_pts):
    labels = {}  #diccionario de puntos con etiqueta: cluster_id o 'Noise'
    cluster_id = 0

    for point in puntos:
        if point in labels:
            continue

        neighbors = range_query(puntos, point, eps)

        if len(neighbors) < min_pts:
            labels[point] = 'Noise'
            continue

        cluster_id += 1
        labels[point] = cluster_id
        seed_set = [p for p in neighbors if p != point] #conjunto de vecinos para expandir el cluster

        #expansión por densidad: puntos conectados directa o indirectamente por cercania terminan en el mismo cluster
        i = 0
        while i < len(seed_set):
            q = seed_set[i]
            # si anteriormente habia sido marcado como noise, se agrega al cluster
            if labels.get(q) == 'Noise':
                labels[q] = cluster_id
            #si no tiene etiqueta, se añade al cluster y se buscan sus vecinos para ver si es core point
            elif q not in labels:
                labels[q] = cluster_id
                q_neighbors = range_query(puntos, q, eps)
                if len(q_neighbors) >= min_pts:
                    for n in q_neighbors:
                        if n not in seed_set:
                            seed_set.append(n)
            i += 1

    return labels


def plot_dbscan_result(labels_dict, eps_label):
    colors = ['green', 'orange', 'purple', 'blue', 'pink', 'cyan']
    puntos = list(labels_dict.keys())
    etiquetas = list(set(labels_dict.values()))

    plt.figure(figsize=(6, 6))
    for etiqueta in etiquetas:
        cluster_puntos = [p for p in puntos if labels_dict[p] == etiqueta]
        xs = [p[0] for p in cluster_puntos]
        ys = [p[1] for p in cluster_puntos]

        if etiqueta == 'Noise':
            plt.scatter(xs, ys, color='gray', label='Ruido', zorder=2)
        else:
            idx = etiqueta - 1  # para asignar color
            plt.scatter(xs, ys, color=colors[idx % len(colors)],
                        label=f'Cluster {etiqueta}', zorder=3)

    plt.grid(True, color='lightgray', linewidth=0.5, zorder=0)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title(f"DBSCAN (ε = {eps_label})")
    plt.legend()
    plt.savefig(f"graficos_dbScan/dbscan_eps_{eps_label}.png")
    plt.close()

if __name__ == "__main__":
    
    puntos = [
        (2, 10), # A
        (2, 5),  # B
        (8, 4),  # C
        (5, 8),  # D
        (7, 5),  # E
        (6, 4),  # F
        (1, 2),  # G
        (4, 9)   # H
    ]

    etiquetas_1 = dbscan(puntos, eps=2, min_pts=2)
    plot_dbscan_result(etiquetas_1, eps_label='2')
    
    etiquetas_2 = dbscan(puntos, eps=np.sqrt(10), min_pts=2)
    plot_dbscan_result(etiquetas_2, eps_label='sqrt(10)')

    print("CASO 1: eps=2, minpoints=2")
    for punto, etiqueta in etiquetas_1.items():
        print(f"Punto {punto}: {'Ruido' if etiqueta == 'Noise' else f'Cluster {etiqueta}'}")
        
    print("\n")

    print("CASO 2: eps=sqrt(10), minpoints=2")
    for punto, etiqueta in etiquetas_2.items():
        print(f"Punto {punto}: {'Ruido' if etiqueta == 'Noise' else f'Cluster {etiqueta}'}")