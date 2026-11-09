"""Construtores de peças (V=vídeo, C=carrossel, I=imagem, END=slide final)."""
def V(series, label, foot, scenes, cta):
    return dict(series=series, label=label, foot=foot, scenes=scenes, cta=cta)
def C(series, label, label2, foot, slides):
    return dict(kind="carousel", series=series, label=label, label2=label2, foot=foot, slides=slides)
def I(series, label, foot, elems):
    return dict(kind="image", series=series, label=label, foot=foot, slides=[elems])
END = lambda t: [("h", t, 70), ("btn", "infoimobiliaria.com")]

# ---- espaços inseparáveis: números, moeda e operadores nunca se partem a meio da linha ----
import re
NB = "\u00a0"
def nb(t):
    t = re.sub(r"(\d) (?=\d{3}\b)", r"\1" + NB, t)          # 7 042,04 / 20 500
    t = re.sub(r"(\d) (?=€|%|anos|meses|m²)", r"\1" + NB, t)  # 150 000 € / 4,177 %
    t = re.sub(r"([×−=+]) (?=[\d−])", r"\1" + NB, t)          # = 7 042,04 / − 10 457,96
    t = re.sub(r"(?<=\d) (?=[×−=+] )", NB, t)
    return t
def walk(o):
    if isinstance(o, str): return nb(o)
    if isinstance(o, tuple): return tuple(walk(x) for x in o)
    if isinstance(o, list): return [walk(x) for x in o]
    if isinstance(o, dict): return {k: walk(v) for k, v in o.items()}
    return o
