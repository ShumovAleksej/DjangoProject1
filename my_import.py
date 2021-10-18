import json


def load_cats():
    with open('relef_nom.txt', encoding="utf8") as f:
        d = json.load(f)
        return d['categories']


def load_prod():
    with open('relef_nom.txt', encoding="utf8") as f:
        d = json.load(f)
        return d['offers']
