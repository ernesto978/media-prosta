"""Renderiza uma semana de peças da Info Imobiliária.
Uso: python3 render_semana.py <modulo_com_D> <pasta_de_saida>
O módulo define D = {chave: peça}. Chaves: AAAAMMDD + v1|v2|v3 (vídeos), c (carrossel), i (imagem).
Saída (nomes finais, prontos a publicar):
  infoimobiliaria-AAAAMMDD-video-N.mp4  (+ -capa.jpg, só para ver)
  infoimobiliaria-AAAAMMDD-carrossel-N.jpg e infoimobiliaria-AAAAMMDD-imagem.jpg (1080x1350)
  versões para stories (1080x1920): ...-story.jpg
Os vídeos levam música (volume 0,35) e a capa é o fotograma dos 3 s."""
import sys, os, importlib, re
from PIL import Image
import engine as e
from modelos import walk
mod, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
D = walk(importlib.import_module(mod).D)
HERE = os.path.dirname(os.path.abspath(__file__))
M = sorted(os.listdir(os.path.join(HERE, "musica")))
T = [os.path.join(HERE, "musica", m) for m in M]
def nome(k, suf):
    m = re.fullmatch(r"(\d{8})(v[123]|c|i)", k)
    assert m, f"chave inválida: {k}"
    d, t = m.groups()
    return d, t
vi = 0
for k, spec in D.items():
    d, t = nome(k, "")
    if "kind" in spec:
        pre = os.path.join(out, f"tmp-{k}")
        for i, p in enumerate(e.render_static(spec, pre), 1):
            im = Image.open(p).convert("RGB"); bg = im.getpixel((5, 5))
            base = f"infoimobiliaria-{d}-" + (f"carrossel-{i}" if t == "c" else "imagem")
            im.save(os.path.join(out, base + ".jpg"), quality=84, optimize=True)
            s = Image.new("RGB", (1080, 1920), bg); s.paste(im, (0, (1920 - im.height) // 2))
            s.save(os.path.join(out, base + "-story.jpg"), quality=84, optimize=True); os.remove(p)
        print(k, "ok", flush=True)
    else:
        n = t[1]
        f = os.path.join(out, f"infoimobiliaria-{d}-video-{n}.mp4")
        dur = e.render_video(spec, f, audio=T[vi % len(T)]); vi += 1
        print(k, round(dur, 1), "s", flush=True)
print("FIM")
