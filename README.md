# Tarea2IA

## Aprendizaje No Supervisado
El archivo k_means corresponde al desarrollo del algoritmo K-Means, mientras que el archivo dbscan corresponde al algoritmo DBSCAN.
Al ejecutarlos, se crean las gráficas correspondientes al problema.

El problema se consideran estos puntos: A= (2,10); B=(2, 5); C=(8,4); D=(5,8); E=(7,5); F=(6,4); G=(1,2); H=(4,9);
Se pide ejecutar K-means por 3 iteraciones con centroides iniciales A, G, D
Para dbscan se pide ejecutar pruebas con eps=2 y minpoints = 2, y eps=sqrt(10) y minpoints = 2

## Aprendizaje Por refuerzo
Se comparan dos algoritmos, Q-Learning y SARSA, en dos ambientes distintos con recompensas y penalizaciones. El primer ambiente es un small grid, mientras que el segundo es un Cliff Walking.

De acuerdo al archivo tutorial, se compila:
g++ -o tutorial tutorial.cpp
./tutorial

Esto dara un archivo .txt con los datos (episodio y reward acumulado). Los parámetros se cambian en el mismo encabezado del código. En la carpeta rewards se encuentran los resultados, y sus gráficas.
