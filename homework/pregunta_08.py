"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    dic = {}
    result = []
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.split()
            numero = int(columnas[1])
            letras = columnas[0]
            if numero not in dic:
                dic[numero] = []
            if letras not in dic[numero]:
                dic[numero].append(letras)
    dic = dict(sorted(dic.items()))
    for numero, valor in dic.items():
        valor.sort(reverse=False)
        result.append((numero, valor))
    return result


if __name__ == "__main__":
    print(pregunta_08())
