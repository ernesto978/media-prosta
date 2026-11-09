"""Info Imobiliária — motor de vídeos (1080x1920) e imagens/carrosséis (1080x1350).
Conteúdo definido como dados (ver semana1.py)."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fontes", "Inter-%s.otf")
NAVY = (20, 35, 62); AMBER = (218, 142, 0); YEL = (255, 193, 7)
BLUE = (56, 94, 158); GREY = (113, 128, 150); WHITE = (255, 255, 255)
LIGHT = (232, 238, 245)
BG = {
    "Conta": (234, 241, 250), "O Que Muda": (255, 246, 224), "Glossário": (231, 245, 238),
    "Pergunta": (241, 237, 251), "Passo a passo": (238, 234, 228), "Guia": (238, 234, 228),
    "Erro comum": (253, 235, 229), "Checklist": (232, 235, 239), "A ou B": (234, 241, 250),
    "Notícia": (255, 246, 224), "Dado": (234, 241, 250),
}
_fc = {}
def font(w, s):
    k = (w, int(s))
    if k not in _fc: _fc[k] = ImageFont.truetype(FONT_DIR % w, int(s))
    return _fc[k]

_logo = Image.open(os.path.join(HERE, "logo.png")).convert("RGBA")
def logo(w):
    return _logo.resize((w, int(_logo.height * w / _logo.width)), Image.LANCZOS)

def ease(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def wrap(text, f, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            t = (cur + " " + w).strip()
            if f.getlength(t) <= maxw or not cur: cur = t
            else: lines.append(cur); cur = w
        lines.append(cur)
    return lines

CW = 880  # largura útil

_FIXTITLE = False
def render_el(el, sc):
    """devolve imagem RGBA (CW x h) do elemento"""
    k = el[0]
    S = lambda v: int(v * sc)
    if k == "gap":
        return Image.new("RGBA", (CW, S(el[1])), (0, 0, 0, 0))
    def text_block(txt, w, size, color, lh=1.18, align="c", maxw=CW):
        sz = S(size)
        while True:
            f = font(w, sz); ls = wrap(txt, f, maxw)
            if max(f.getlength(l) for l in ls) <= maxw or sz <= 24: break
            sz = int(sz * 0.94)
        h = int(f.size * lh) * len(ls)
        im = Image.new("RGBA", (maxw, h + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        for i, l in enumerate(ls):
            y = int(f.size * lh) * i + int(f.size * lh) // 2
            if align == "c": d.text((maxw / 2, y), l, font=f, fill=color, anchor="mm")
            else: d.text((0, y), l, font=f, fill=color, anchor="lm")
        return im
    if k == "kick":
        txt = el[1]; sp = 5; fs = S(32)
        while True:
            f = font("Bold", fs); ws = [f.getlength(c) for c in txt]; tot = sum(ws) + sp * (len(txt) - 1)
            if tot <= CW - 20 or fs <= 18: break
            fs -= 2
        im = Image.new("RGBA", (CW, S(50)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        x = CW / 2 - tot / 2
        for c, w in zip(txt, ws):
            d.text((x, S(25)), c, font=f, fill=AMBER, anchor="lm"); x += w + sp
        return im
    if k == "h":   # título
        return text_block(el[1], "ExtraBold", el[2] if len(el) > 2 else 84, el[3] if len(el) > 3 else NAVY, 1.12)
    if k == "p":
        return text_block(el[1], "Medium", el[2] if len(el) > 2 else 46, GREY, 1.28)
    if k == "pn":  # parágrafo navy
        return text_block(el[1], "SemiBold", el[2] if len(el) > 2 else 52, NAVY, 1.22)
    if k == "num":
        return text_block(el[1], "ExtraBold", el[2] if len(el) > 2 else 150, el[3] if len(el) > 3 else AMBER, 1.05)
    if k == "card":  # [titulo], texto
        title, body = el[1], el[2]
        pad = S(36); inner = CW - 2 * pad
        tb = text_block(title, "Bold", (46 / sc if _FIXTITLE else 40), AMBER, 1.2, "l", inner) if title else None
        bb = text_block(body, "SemiBold", 58, NAVY, 1.25, "l", inner)
        h = pad * 2 + (tb.height + S(8) if tb else 0) + bb.height
        im = Image.new("RGBA", (CW, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, CW - 1, h - 1), radius=S(32), fill=WHITE)
        y = pad
        if tb: im.alpha_composite(tb, (pad, y)); y += tb.height + S(8)
        im.alpha_composite(bb, (pad, y)); return im
    if k == "row":  # etiqueta, valor, destaque
        lab, val, hi = el[1], el[2], (el[3] if len(el) > 3 else False)
        h = S(124); im = Image.new("RGBA", (CW, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, CW - 1, h - 1), radius=S(30), fill=YEL if hi else WHITE)
        fl = font("SemiBold", S(40)); fv = font("ExtraBold", S(56))
        vw = fv.getlength(val); maxl = CW - vw - S(100)
        while fl.getlength(lab) > maxl and fl.size > 24: fl = font("SemiBold", fl.size - 2)
        d.text((S(40), h // 2), lab, font=fl, fill=NAVY, anchor="lm")
        d.text((CW - S(40), h // 2), val, font=fv, fill=NAVY if hi else AMBER, anchor="rm"); return im
    if k == "chk":
        h0 = text_block(el[1], "SemiBold", 50, NAVY, 1.22, "l", CW - S(130))
        h = max(h0.height + S(40), S(110))
        im = Image.new("RGBA", (CW, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, CW - 1, h - 1), radius=S(28), fill=WHITE)
        c = S(30); cx, cy = S(60), h // 2
        d.ellipse((cx - c, cy - c, cx + c, cy + c), fill=AMBER)
        d.line([(cx - c * .45, cy), (cx - c * .1, cy + c * .4), (cx + c * .5, cy - c * .4)], fill=WHITE, width=max(4, S(7)), joint="curve")
        im.alpha_composite(h0, (S(110), (h - h0.height) // 2)); return im
    if k == "pair":  # (etA, valA), (etB, valB)
        (la, va), (lb, vb) = el[1], el[2]
        h = S(250); im = Image.new("RGBA", (CW, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        gw = (CW - S(24)) // 2
        for i, (l, v) in enumerate(((la, va), (lb, vb))):
            x0 = i * (gw + S(24))
            d.rounded_rectangle((x0, 0, x0 + gw, h - 1), radius=S(32), fill=WHITE)
            fl = font("Bold", S(34))
            while fl.getlength(l) > gw - S(30) and fl.size > 20: fl = font("Bold", fl.size - 2)
            d.text((x0 + gw / 2, S(58)), l, font=fl, fill=AMBER, anchor="mm")
            fv = font("ExtraBold", S(66))
            while fv.getlength(v) > gw - S(30) and fv.size > 30: fv = font("ExtraBold", fv.size - 2)
            d.text((x0 + gw / 2, S(160)), v, font=fv, fill=NAVY, anchor="mm")
        return im
    raise ValueError(k)

MAXSC = 1.5
def layout(elems, top, bottom):
    sc = MAXSC
    while True:
        ims = [render_el(e, sc) for e in elems]
        gap = int(24 * sc)
        tot = sum(i.height for i in ims) + gap * (len(ims) - 1)
        if tot <= bottom - top or sc < 0.45: break
        sc -= 0.05
    y = top + (bottom - top - tot) // 2; out = []
    for im in ims:
        out.append((im, y)); y += im.height + gap
    return out

def dur_of(elems):
    n = sum(len(" ".join(str(x) for x in e[1:3] if isinstance(x, str))) for e in elems)
    return max(3.4, min(6.8, 2.0 + 0.045 * n + 0.25 * len(elems)))

# ---------- vídeo ----------
W, H, FPS = 1080, 1920, 30
def video_scenes(spec):
    """spec: series, label, scenes=[elems...], cta=(titulo, sub), foot"""
    bg = BG[spec["series"]]
    sc = []
    first = True
    for el in spec["scenes"]:
        els = ([("kick", spec["label"])] + el) if first else el
        first = False
        sc.append(dict(elems=els, dur=dur_of(el)))
    cta = [("h", spec["cta"][0], 96), ("btn", "infoimobiliaria.com"), ("p", spec["cta"][1], 42),
           ("kick", "BY OMNI"), ("p", "Informação geral. Confirma sempre com um advogado ou solicitador.", 26)]
    sc.append(dict(elems=cta, dur=4.6, cta=True))
    return bg, sc

_orig = render_el
def render_el(el, sc):  # noqa: F811  (extensão: botão)
    if el[0] == "btn":
        S = lambda v: int(v * sc)
        im = Image.new("RGBA", (CW, S(150)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((20, 0, CW - 20, S(150) - 1), radius=S(75), fill=NAVY)
        d.text((CW / 2, S(75)), el[1], font=font("Bold", S(58)), fill=WHITE, anchor="mm"); return im
    return _orig(el, sc)

def base_frame(bg, logo_w=380, logo_y=175):
    im = Image.new("RGBA", (W, H), bg + (255,))
    lg = logo(logo_w); im.alpha_composite(lg, ((W - lg.width) // 2, logo_y)); return im

def render_video(spec, out, still=None, audio=None):
    bg, scenes = video_scenes(spec)
    total = sum(s["dur"] for s in scenes)
    for s in scenes: s["lay"] = layout(s["elems"], 470, 1400)
    base = base_frame(bg)
    foot = spec["foot"]
    def frame(t):
        acc = 0
        for s in scenes:
            if t < acc + s["dur"] or s is scenes[-1]: break
            acc += s["dur"]
        lt = t - acc; last = s is scenes[-1]
        f = base.copy(); d = ImageDraw.Draw(f)
        d.rounded_rectangle((90, 120, 990, 126), radius=3, fill=LIGHT)
        d.rounded_rectangle((90, 120, 90 + max(6, int(900 * t / total)), 126), radius=3, fill=NAVY)
        out_a = 1.0 if last else 1 - ease((lt - (s["dur"] - 0.25)) / 0.25)
        for i, (im, y) in enumerate(s["lay"]):
            p = ease((lt - (0.15 + 0.38 * i)) / 0.5)
            if p <= 0: continue
            a = p * out_a
            lay = im if a >= 1 else im.copy()
            if a < 1: lay.putalpha(im.getchannel("A").point(lambda v, a=a: int(v * a)))
            f.alpha_composite(lay, (100 + (CW - im.width) // 2, y + int((1 - p) * 40)))
        d = ImageDraw.Draw(f)
        d.text((W / 2, 1480), foot, font=font("Medium", 28), fill=GREY, anchor="mm")
        return f.convert("RGB")
    if still is not None:
        frame(still).save(out); return total
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
           "-preset", "medium", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    # Capa: a 1.ª frame do vídeo é a frame dos 3 s (a capa automática das redes é a 1.ª frame).
    # Fica 0,5 s (HOLD) e depois o vídeo continua com o texto a entrar desde o início.
    ct = min(spec.get("cover_t", 3.0), total - 0.1)
    cf = frame(ct)
    cf.save(os.path.splitext(out)[0] + "-capa.jpg", quality=92)
    HOLD = 0.5  # a capa fica 0,5 s no início (combinado a 22/10); as redes que ignoram 1 frame apanham-na na mesma
    cb = cf.tobytes()
    for _ in range(int(HOLD * FPS)): p.stdin.write(cb)
    for i in range(int(total * FPS)): p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close(); p.wait()
    if audio: add_music(out, audio, total + HOLD)
    return total + HOLD

def add_music(video, track, total, vol=0.35, fade=1.5):
    """Junta a faixa ao vídeo (sem recodificar a imagem): volume 0,35 e fade-out de 1,5 s."""
    tmp = video + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-stream_loop", "-1", "-i", track,
        "-filter_complex", f"[1:a]volume={vol},afade=t=in:d=0.5,afade=t=out:st={max(0, total - fade):.2f}:d={fade}[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.2f}",
        "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, video)

# ---------- estático ----------
SW, SH = 1080, 1350
def static_slide(series, label, elems, foot, idx=None, n=None, cta=False):
    bg = BG[series]
    im = Image.new("RGBA", (SW, SH), bg + (255,)); d = ImageDraw.Draw(im)
    lg = logo(300); im.alpha_composite(lg, ((SW - lg.width) // 2, 70))
    global _FIXTITLE
    if n and idx and label:
        kk = render_el(("kick", label), 1.2)
        im.alpha_composite(kk, (100 + (CW - kk.width) // 2, 215))
        els = elems; top = 300
    else:
        els = ([("kick", label)] if label else []) + elems; top = 250
    _FIXTITLE = bool(n and idx and label)
    lay = layout(els, top, 1130 if n else 1180)
    _FIXTITLE = False
    if n and idx and label:
        dy = 310 - lay[0][1]; lay = [(e, y + dy) for e, y in lay]
    for e, y in lay:
        im.alpha_composite(e, (100 + (CW - e.width) // 2, y))
    if n:
        for i in range(n):
            x = SW / 2 + (i - (n - 1) / 2) * 34
            d.ellipse((x - 9, 1196 - 9, x + 9, 1196 + 9), fill=NAVY if i == idx else LIGHT)
        if idx < n - 1:
            d.text((SW - 90, 1196), "Desliza →", font=font("Bold", 30), fill=AMBER, anchor="rm")
    d.text((SW / 2, 1262), foot, font=font("Medium", 26), fill=GREY, anchor="mm")
    d.text((SW / 2, 1306), "infoimobiliaria.com · by OMNI", font=font("Bold", 28), fill=NAVY, anchor="mm")
    return im.convert("RGB")

def render_static(spec, outprefix):
    paths = []
    sl = spec["slides"]; n = len(sl) if spec["kind"] == "carousel" else None
    for i, s in enumerate(sl):
        p = f"{outprefix}-{i + 1}.png" if n else f"{outprefix}.png"
        static_slide(spec["series"], spec["label"] if i == 0 else spec.get("label2"), s, spec["foot"], i, n).save(p)
        paths.append(p)
    return paths
