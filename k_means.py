import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("graficos_Kmeans", exist_ok=True)

#distancia euclidiana
def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


#se calcula el centroide como el promedio de los puntos del cluster
def calculate_centroid(cluster):
    if not cluster:
        return (0, 0)
    mean = np.mean(cluster, axis=0)
    return tuple(float(x) for x in mean)  #promedio de todas las x e y


#grilla 10x10 con los clusters en distinto color
def plot_clusters(clusters, centroids, iteration):
    colors = ['purple', 'orange', 'green']
    plt.figure(figsize=(6, 6))
    for i, cluster in enumerate(clusters):
        if cluster:
            cluster_points = np.array(cluster)
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                        color=colors[i % len(colors)], label=f'Cluster {i + 1}', zorder=3)
            plt.scatter(*centroids[i], color=colors[i % len(colors)],
                        edgecolors='none', marker='D', s=80, zorder=4)

    plt.grid(True, color='lightgray', linewidth=0.5, zorder=0)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title(f'Iteración {iteration + 1}')
    plt.legend()
    plt.savefig(f"graficos_Kmeans/kmeans_iteracion_{iteration + 1}.png")
    plt.close()


def plot_initial_state(points, centroids):
    plt.figure(figsize=(6, 6))
    points_array = np.array(points)
    plt.scatter(points_array[:, 0], points_array[:, 1], color='black', label='Puntos', zorder=3)
    
    for i, c in enumerate(centroids):
        plt.scatter(*c, color='black', marker='D', s=60, label=f'Centroides' if i == 0 else None, zorder=4)

    plt.grid(True, color='lightgray', linewidth=0.5, zorder=0)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.title('Estado inicial')
    plt.legend()
    plt.savefig("graficos_Kmeans/kmeans_estado_inicial.png")
    plt.close()


#algoritmo kmeans
def k_means_cluster(k, points, initial_centroids):
    centroids = initial_centroids
    
    #3 iteraciones
    for iteration in range(3):
        clusters = [[] for _ in range(k)]

        #por cada punto se calcula la distancia hacia los centroides, y se asigna al centroide más cercano
        for point in points:
            distances = [distance(point, centroid) for centroid in centroids]
            cluster_idx = np.argmin(distances)
            clusters[cluster_idx].append(point)

        #calcular nuevos centroides
        new_centroids = [calculate_centroid(cluster) for cluster in clusters]

        print(f"\nIteración {iteration + 1}")
        for i, cluster in enumerate(clusters):
            print(f"Cluster {i + 1}: {cluster}")
            print(f"Nuevo centroide: {new_centroids[i]}")
            
        plot_clusters(clusters, new_centroids, iteration)

        centroids = new_centroids

    return clusters



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

    #A, D, G como centroides iniciales
    iniciales = [puntos[0], puntos[3], puntos[6]]
    
    plot_initial_state(puntos, iniciales)
    
    k_means_cluster(k=3, points=puntos, initial_centroids=iniciales)
