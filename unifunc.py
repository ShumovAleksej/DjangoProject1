import json


# Преобразование листа в матрицу
def list_to_matrix(l, n):
    matrix = []
    for i in range(0, len(l), n):
        matrix.append(l[i:i + n])
    return matrix


# Загрузка категорий товаров в БД из JSON файла
def load_cats():
    with open('relef_nom.txt', encoding="utf8") as f:
        d = json.load(f)
        return d['categories']


# Загрузка товаров в БД из JSON файла
def load_prod():
    with open('relef_nom.txt', encoding="utf8") as f:
        d = json.load(f)
        return d['offers']
