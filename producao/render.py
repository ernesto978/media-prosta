#!/usr/bin/env python3
"""Produção das peças de redes sociais do prostata.pt (imagem, carrossel, vídeo).

Uso:  python3 render.py spec.json saida/
O spec.json tem uma lista "pecas". Ver LEIA-ME.md para o formato.
Requer: Pillow, numpy, ffmpeg. Fontes em ./fontes (Poppins).
"""
import json, os, sys, math, subprocess, struct, wave, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = lambda w, s: ImageFont.truetype(os.path.join(HERE, "fontes", f"Poppins-{w}.ttf"), s)
CREAM = (251, 227, 192)
WHITE = (255, 255, 255)
THEMES = {  # fundo do painel, cor da etiqueta, nome da etiqueta
    "alimentacao": ((18, 64, 44), (46, 139, 98), "ALIMENTAÇÃO"),
    "tratamento": ((18, 49, 95), (31, 95, 180), "TRATAMENTO"),
    "prevencao": ((107, 63, 18), (224, 138, 46), "PREVENÇÃO"),
}


def wrap(draw, text, font, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def cover_crop(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((math.ceil(img.width * r), math.ceil(img.height * r)), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def pill(d, theme, x, y, size=30):
    _, col, label = THEMES[theme]
    f = FONT("Bold", size)
    tw = d.textlength(label, font=f)
    d.rounded_rectangle((x, y, x + tw + 58, y + size + 30), radius=(size + 30) // 2, fill=col)
    d.text((x + 29, y + 13), label, font=f, fill=WHITE)


def brand(d, x, y, size=40):
    f = FONT("Bold", size)
    d.text((x, y), "prostata.pt", font=f, fill=WHITE)
    tw = d.textlength("pro", font=f)
    d.rounded_rectangle((x, y + size + 14, x + tw, y + size + 20), radius=3, fill=CREAM)


def paragraphs(d, x, y, paras, maxw, size, line_h, first_color=WHITE, hl_color=CREAM, gap=22):
    f = FONT("Regular", size)
    for i, p in enumerate(paras):
        hl = isinstance(p, dict)
        txt = p["destaque"] if hl else p
        for ln in wrap(d, txt, f, maxw):
            d.text((x, y), ln, font=f, fill=hl_color if hl else first_color)
            y += line_h
        y += gap
    return y


def tint(bg_img, theme, w, h, alpha, blur=0):
    base = cover_crop(bg_img.convert("RGB"), w, h)
    if blur:
        base = base.filter(ImageFilter.GaussianBlur(blur))
    col = Image.new("RGB", (w, h), THEMES[theme][0])
    return Image.blend(base, col, alpha)


# ---------- imagem única 1080x1350 ----------
def render_image(p, out):
    W, H = 1080, 1350
    panel = THEMES[p["tema"]][0]
    img = Image.new("RGB", (W, H), panel)
    photo = cover_crop(Image.open(p["fundo"]).convert("RGB"), W, 760)
    img.paste(photo, (0, 0))
    # degradé da foto para o painel
    grad = Image.new("L", (W, 760), 0)
    gd = ImageDraw.Draw(grad)
    for y in range(760):
        a = 0 if y < 420 else int(255 * min(1, (y - 420) / 130))
        gd.line((0, y, W, y), fill=a)
    img.paste(Image.new("RGB", (W, 760), panel), (0, 0), grad)
    d = ImageDraw.Draw(img)
    pill(d, p["tema"], 80, 70)
    ft = FONT("Bold", 68)
    y = 535
    for ln in wrap(d, p["titulo"], ft, 900):
        d.text((80, y), ln, font=ft, fill=WHITE)
        y += 84
    y += 22
    paragraphs(d, 80, y, p["texto"], 900, 38, 49)
    brand(d, 80, 1238)
    fs = FONT("Regular", 28)
    if p.get("fonte"):
        tw = d.textlength(p["fonte"], font=fs)
        d.text((W - 80 - tw, 1262), p["fonte"], font=fs, fill=WHITE)
    img.save(out, quality=82, optimize=True)


# ---------- carrossel 1080x1350 ----------
def carousel_slide(p, s, i, n, out):
    W, H = 1080, 1350
    bg = Image.open(p["fundo"])
    img = tint(bg, p["tema"], W, H, 0.86, blur=14)
    d = ImageDraw.Draw(img)
    pill(d, p["tema"], 80, 70)
    fc = FONT("Regular", 32)
    c = f"{i + 1}/{n}"
    d.text((W - 80 - d.textlength(c, font=fc), 84), c, font=fc, fill=WHITE)
    cover = i == 0
    ft = FONT("Bold", 76 if cover else 68)
    lines = wrap(d, s["titulo"], ft, 900)
    lh = 92 if cover else 90
    body = s.get("texto", [])
    fb = FONT("Regular", 46)
    blines = []
    for t in ([body] if isinstance(body, str) else body):
        blines += wrap(d, t, fb, 900) + [""]
    total = len(lines) * lh + (50 + len([b for b in blines]) * 60 if blines else 0)
    y = max(260, (H - total) // 2 - 40)
    for ln in lines:
        d.text((80, y), ln, font=ft, fill=WHITE)
        y += lh
    if blines:
        y += 14
        d.rounded_rectangle((80, y, 170, y + 8), radius=4, fill=CREAM)
        y += 40
        for ln in blines:
            if ln:
                d.text((80, y), ln, font=fb, fill=WHITE)
            y += 60 if ln else 22
    brand(d, 80, 1238)
    if i < n - 1:
        fd = FONT("Regular", 34)
        tx = "Deslize"
        tw = d.textlength(tx, font=fd)
        d.text((W - 80 - tw - 70, 1255), tx, font=fd, fill=CREAM)
        ay = 1280
        d.line((W - 80 - 58, ay, W - 80, ay), fill=CREAM, width=5)
        d.line((W - 80 - 20, ay - 18, W - 80, ay), fill=CREAM, width=5)
        d.line((W - 80 - 20, ay + 18, W - 80, ay), fill=CREAM, width=5)
    img.save(out, quality=82, optimize=True)


# ---------- vídeo 1080x1920 ----------
def scene_frame(p, sc, out, cover=False):
    W, H = 1080, 1920
    img = tint(Image.open(p["fundo"]), p["tema"], W, H, 0.80 if not cover else 0.86, blur=18)
    d = ImageDraw.Draw(img)
    pill(d, p["tema"], 90, 130, 32)
    ft = FONT("Bold", 96 if not cover else 100)
    lines = wrap(d, sc["titulo"], ft, 900)
    fs = FONT("Regular", 52)
    sl = wrap(d, sc["sub"], fs, 900) if sc.get("sub") else []
    total = len(lines) * 112 + (len(sl) * 68 + 30 if sl else 0)
    y = (H - total) // 2 + 20
    for ln in lines:
        d.text((90, y), ln, font=ft, fill=WHITE)
        y += 112
    y += 30
    for ln in sl:
        d.text((90, y), ln, font=fs, fill=CREAM)
        y += 68
    brand(d, 90, 1740, 52)
    img.save(out)


def music(path, dur, bpm, seed=0):
    sr = 44100
    n = int(sr * dur)
    t = np.arange(n) / sr
    beat = 60.0 / bpm
    out = np.zeros(n)
    roots = [196.0, 220.0, 174.61, 196.0]  # G A F G (Hz), tom maior alegre
    chords = [[1, 1.26, 1.5], [1, 1.2, 1.5], [1, 1.26, 1.5], [1, 1.26, 1.5]]
    arp = [1, 1.26, 1.5, 2, 1.5, 1.26, 1, 1.26]
    def env(length, a=0.01, r=0.12):
        e = np.ones(length)
        na, nr = int(a * sr), int(r * sr)
        e[:na] = np.linspace(0, 1, na)
        e[-nr:] = np.linspace(1, 0, nr)
        return e
    nb = int(dur / beat) + 1
    for b in range(nb):
        s = int(b * beat * sr)
        bar = (b // 4) % 4
        root = roots[bar]
        L = int(beat * sr * 0.9)
        if s + L > n:
            break
        tt = np.arange(L) / sr
        if b % 2 == 0:  # baixo
            out[s:s + L] += 0.30 * np.sin(2 * np.pi * root / 2 * tt) * env(L)
        if b % 2 == 1:  # acorde em contratempo
            for r_ in chords[bar]:
                out[s:s + L] += 0.07 * np.sin(2 * np.pi * root * r_ * tt) * env(L, r=0.2)
        for k in range(2):  # arpejo em colcheias
            s2 = s + int(k * beat / 2 * sr)
            L2 = int(beat / 2 * sr * 0.85)
            if s2 + L2 > n:
                break
            tt2 = np.arange(L2) / sr
            f = root * 2 * arp[(b * 2 + k) % 8]
            out[s2:s2 + L2] += 0.09 * np.sin(2 * np.pi * f * tt2) * env(L2, r=0.08)
    out *= np.minimum(1, np.minimum(t / 1.0, (dur - t) / 1.5))
    out = np.clip(out / max(1e-6, np.abs(out).max()) * 0.55, -1, 1)
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((out * 32767).astype("<i2").tobytes())


def render_video(p, out, tmp):
    os.makedirs(tmp, exist_ok=True)
    cover = {"titulo": p["capa"]}
    scene_frame(p, cover, f"{tmp}/s0.png", cover=True)
    scenes = p["cenas"]
    for i, sc in enumerate(scenes, 1):
        scene_frame(p, sc, f"{tmp}/s{i}.png")
    durs = [0.6] + [sc.get("seg", 5.0) for sc in scenes]
    X = 0.35  # crossfade
    inputs, filt = [], []
    for i, dsec in enumerate(durs):
        inputs += ["-loop", "1", "-t", f"{dsec + (X if i < len(durs) - 1 else 0):.2f}", "-i", f"{tmp}/s{i}.png"]
    cur = "[0:v]"
    off = 0.0
    for i in range(1, len(durs)):
        xd = 0.15 if i == 1 else X  # da capa para a 1.ª cena, corte quase seco
        off += durs[i - 1] - (0 if i == 1 else 0)
        filt.append(f"{cur}[{i}:v]xfade=transition=fade:duration={xd}:offset={off - xd:.2f}[v{i}]")
        cur = f"[v{i}]"
    total = off + durs[-1]
    music(f"{tmp}/m.wav", total, p.get("bpm", 112))
    # barra de progresso
    bar = Image.new("RGB", (1080, 12), CREAM)
    bar.save(f"{tmp}/bar.png")
    inputs += ["-i", f"{tmp}/bar.png", "-i", f"{tmp}/m.wav"]
    bi, ai = len(durs), len(durs) + 1
    filt.append(f"{cur}[{bi}:v]overlay=x='-W+W*t/{total:.2f}':y=H-h:shortest=0,format=yuv420p[vout]")
    cmd = ["ffmpeg", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(filt),
           "-map", "[vout]", "-map", f"{ai}:a", "-r", "30", "-c:v", "libx264", "-preset", "veryfast",
           "-crf", "26", "-c:a", "aac", "-b:a", "128k", "-t", f"{total:.2f}", "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    # capa solta
    Image.open(f"{tmp}/s0.png").convert("RGB").save(out.replace("vid-", "capa-").replace(".mp4", ".jpg"), quality=85)
    return total


def main():
    spec = json.load(open(sys.argv[1]))
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    for p in spec["pecas"]:
        if not os.path.isabs(p["fundo"]):
            p["fundo"] = os.path.join(base, p["fundo"])
        k = p["chave"]
        if p["tipo"] == "imagem":
            render_image(p, f"{outdir}/{k}.jpg")
        elif p["tipo"] == "carrossel":
            n = len(p["slides"])
            for i, s in enumerate(p["slides"]):
                carousel_slide(p, s, i, n, f"{outdir}/{k}-{i + 1:02d}.jpg")
        elif p["tipo"] == "video":
            render_video(p, f"{outdir}/{k}.mp4", f"{outdir}/_tmp_{k}")
            shutil.rmtree(f"{outdir}/_tmp_{k}", ignore_errors=True)
        print("ok", k)


if __name__ == "__main__":
    main()
