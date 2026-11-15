# Info Imobiliária - 17 a 29 de novembro de 2026. Factos lidos no site (artigos e páginas publicados) a 15/11/2026; contas verificadas com assert.
import math, re
from modelos import V, C, I, END
pm = lambda P, t, n=360: (lambda r: P * r / (1 - (1 + r) ** -n))(t / 12)
fm = lambda v: f"{v:,.2f}".replace(",", " ").replace(".", ",")
# --- verificações das contas usadas ---
assert [fm(pm(150000, x)) for x in (.04177, .05177, .06177)] == ["731,51", "821,54", "916,47"]
assert round(pm(150000, .05177) - pm(150000, .04177)) == 90 and round(pm(150000, .06177) - pm(150000, .04177)) == 185
assert fm(pm(200000, .04177)) == "975,35" and fm(pm(200000, .04677)) == "1 034,51"
assert round(pm(200000, .04677) - pm(200000, .04177)) == 59
assert fm(pm(150000, .035)) == "673,57" and fm(pm(150000, .05)) == "805,23" and 805.23 / .45 == 1789.4
assert fm(pm(150000, .04023)) == "718,11" and fm(pm(150000, .04273)) == "739,93" and fm(pm(150000, .04523)) == "762,08"
assert round(250000 * .07 - 10457.96, 2) == 7042.04 and round(250000 * .07 - 9394.50, 2) == 8105.50 and 250000 * .008 == 2000
assert round(7042.04 + 2000, 2) == 9042.04 and round(8105.50 - 7042.04, 2) == 1063.46
assert 300000 / 3 == 100000 and 200000 * .003 == 600 and 206000 * .003 == 618 and 200000 * 1.03 == 206000
assert 250000 - 240000 == 10000 and 10000 / 250000 == .04 and 80000 * .04 == 3200 and 3200 / 2 == 1600 and 1600 * .3 == 480
assert 250000 - 248000 == 2000 and 80000 * (2000 / 250000) == 640 and 640 / 2 * .3 == 96 and 480 - 96 == 384
assert round(400000 - 330539, 0) == 69461 and round(69461 * .08, 2) == 5556.88 and round((400000 - 338141) * .08, 2) == 4948.72
assert round(1000 * 1.0256, 2) == 1025.6 and round(750 * 1.0256, 2) == 769.2 and round(1025.6 * 12 - 12000, 2) == 307.2
assert 250000 * .15 == 37500 and 250000 * .9 == 225000 and 250000 - 225000 == 25000
assert 1300000 - 600000 == 700000 and 400000 * .007 + 300000 * .01 == 5800
assert 250000 * .05 == 12500 and 200000 * .006 == 1200 and 2000 + 1200 == 3200
assert round(85 * 10.17, 2) == 864.45 and 80 * 3228 == 258240
assert round(80 * 2278 - 0, 0) == 182240 and 182240 * .9 == 164016 and 200000 * .9 == 180000 and 200000 - 164016 == 35984 and 35984 - 20000 == 15984
assert round(250000 * .0069, 2) == 1725 and round(800 * .0037, 2) == 2.96
D = {}; M = {}
LEG = "Informação geral. Confirma com um advogado ou solicitador."
TAIL = "Info Imobiliária, by OMNI"
LINK = "infoimobiliaria.com\n(Link também na bio.)"
H = lambda *a: ["#" + x for x in a]
def reg(key, spec, assunto, lines, fonte, tags, title=None, leg=True):
    D[key] = spec
    lines = [x for l in lines for x in re.split(r"(?<![0-9])(?<=[.!?]) (?=[A-ZÁÉÍÓÚ])", l)]
    t = "\n".join(lines) + "\n\n" + LINK + "\n\nFonte: " + fonte + ("\n" + LEG if leg else "") + "\n\n" + TAIL + "\n\n" + " ".join(tags)
    M[key] = dict(assunto=assunto, fonte=fonte, legenda=t, titulo_youtube=title)

# ================= TER 17 =================
reg("20261117v1", V("Notícia", "O QUE MUDA · JUROS", "Fonte: ECO, 12/11/2026. Expectativa de mercado, não decisão.", [
    [("h", "Euribor a subir: o que se sabe", 80), ("p", "Valores de 12 de novembro.", 44)],
    [("card", "EURIBOR A 12 DE NOVEMBRO", "3 meses: 2,766%. 6 meses: 3,023%. 12 meses: 3,293%.")],
    [("card", "O BCE", "Manteve as taxas em outubro. O mercado conta com uma possível subida em dezembro, mas nada está decidido.")],
    [("card", "A TUA PRESTAÇÃO", "Só muda na data de revisão do contrato, com a Euribor do prazo que lá está escrito.")],
    [("pn", "Isto é um cenário, não uma previsão.", 52)],
], ("Simula a tua prestação.", "Calculadora de crédito habitação")),
    "Euribor a subir e o BCE em dezembro",
    ["Euribor a 12 de novembro: 2,766% a 3 meses, 3,023% a 6 meses e 3,293% a 12 meses.", "O BCE manteve as taxas em outubro.", "O mercado conta com uma possível subida em dezembro, mas nada está decidido.", "A tua prestação só muda na data de revisão do contrato."],
    "ECO (12/11/2026), via Info Imobiliária.", H("euribor", "créditohabitação", "BCE", "imobiliário", "infoimobiliária"), "Euribor a subir: o que se sabe e o que não se sabe", leg=False)
reg("20261117v2", V("Pergunta", "PERGUNTA DA SEMANA · CRÉDITO", "Fonte: Banco de Portugal, via ECO e Portal da Literacia Financeira. Recomendação.", [
    [("h", "Quanto o banco te deixa gastar em prestações?", 74)],
    [("card", "O LIMITE", "Desde 1 de agosto de 2026, a taxa de esforço recomendada pelo Banco de Portugal desceu de 50% para 45% do rendimento líquido.")],
    [("pair", ("ANTES (50%)", "1 000 €"), ("AGORA (45%)", "900 €")), ("p", "Exemplo: 2 000 € líquidos por mês.", 42)],
    [("card", "ATENÇÃO", "Entram todos os créditos, não só o da casa. É uma recomendação, mas os bancos aplicam-na.")],
], ("Conta os teus créditos.", "Página «Taxa de esforço»")),
    "Taxa de esforço de 45%",
    ["Desde 1 de agosto de 2026, a taxa de esforço recomendada pelo Banco de Portugal desceu de 50% para 45%.", "Com 2 000 € líquidos por mês, o limite passou de 1 000 € para 900 € de prestações.", "Entram todos os créditos, não só o da casa.", "É uma recomendação, mas na prática os bancos aplicam-na."],
    "Info Imobiliária, «Taxa de esforço», com base em ECO e Portal da Literacia Financeira. Exemplo calculado por nós.", H("taxadeesforço", "créditohabitação", "comprarcasa", "imobiliário", "infoimobiliária"), "Taxa de esforço: o banco só deixa 45% do teu rendimento")
reg("20261117v3", V("Checklist", "CHECKLIST · CRÉDITO", "Informação geral. Confirma os prazos com o teu banco.", [
    [("h", "Antes de assinar o crédito habitação", 78)],
    [("chk", "Lê o contrato com calma: tens pelo menos 7 dias"), ("chk", "A proposta deve valer pelo menos 30 dias"), ("chk", "A pré-aprovação costuma valer 30 a 90 dias")],
    [("chk", "Compara a TAEG, não só o spread"), ("chk", "Confirma o indexante e a data de revisão"), ("card", "FALA COM MAIS DE UM BANCO", "Pede propostas por escrito e compara.")],
], ("Assina a perceber tudo.", "Como comprar casa, passo a passo")),
    "Antes de assinar o crédito: checklist",
    ["Antes de assinar o crédito habitação, confirma.", "Tens pelo menos 7 dias para ler o contrato.", "A proposta deve valer pelo menos 30 dias.", "A pré-aprovação costuma valer 30 a 90 dias.", "Compara a TAEG, não só o spread.", "Confirma o indexante e a data de revisão."],
    "Info Imobiliária, «Como comprar casa, passo a passo».", H("créditohabitação", "checklist", "comprarcasa", "imobiliário", "infoimobiliária"), "Antes de assinar o crédito habitação: o que confirmar")
reg("20261117c", C("Guia", "GUIA · CRÉDITO", "OS DOCUMENTOS DO CRÉDITO", "Fonte: ComparaJá e Caixa Geral de Depósitos. Regras de outubro de 2026.", [
    [("h", "Documentos para pedir crédito habitação", 72), ("p", "A lista essencial, em 3 grupos.", 44)],
    [("card", "PESSOAIS", "Cartão de Cidadão (ou BI e cartão de contribuinte) e comprovativo de morada recente."), ("card", "BANCÁRIOS", "Extratos dos últimos 3 a 6 meses, IBAN e mapa de responsabilidades de crédito do Banco de Portugal.")],
    [("card", "RENDIMENTOS", "Última declaração de IRS e nota de liquidação. Quem trabalha por conta de outrem: três últimos recibos de vencimento e declaração da entidade patronal.")],
    [("card", "DO IMÓVEL", "Certidão permanente, caderneta predial, licença de utilização e, nas casas licenciadas depois de abril de 2004, a ficha técnica.")],
    END("Reunir tudo demora 3 a 5 dias úteis."),
]),
    "Documentos para pedir crédito habitação",
    ["Documentos para pedir crédito habitação.", "Pessoais: Cartão de Cidadão e comprovativo de morada recente.", "Rendimentos: IRS e nota de liquidação, ou os três últimos recibos de vencimento.", "Bancários: extratos de 3 a 6 meses, IBAN e mapa de responsabilidades de crédito.", "Do imóvel: certidão permanente, caderneta predial, licença de utilização e, quando aplicável, ficha técnica.", "Guarda este carrossel."],
    "ComparaJá e Caixa Geral de Depósitos, via Info Imobiliária.", H("créditohabitação", "documentos", "comprarcasa", "imobiliário", "infoimobiliária"), leg=False)
reg("20261117i", I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «Imposto do Selo». Regras de outubro de 2026.", [
    ("h", "Imposto do Selo na compra de casa", 76), ("num", "0,8%", 160),
    ("pn", "Incide sobre o valor que serve de base ao IMT: o mais alto entre o preço e o VPT.", 44), ("p", "Paga-se antes da escritura. O comprovativo leva-se no dia.", 38)]),
    "Imposto do Selo: 0,8%",
    ["Imposto do Selo na compra de casa: 0,8%.", "Incide sobre o valor que serve de base ao IMT, o mais alto entre o preço e o VPT.", "Paga-se antes da escritura.", "Leva o comprovativo no dia."],
    "Info Imobiliária, página «Imposto do Selo».", H("impostodoselo", "IMT", "comprarcasa", "imobiliário", "infoimobiliária"))

# ================= QUA 18 =================
reg("20261118v1", V("Notícia", "O QUE MUDA · HERANÇAS", "Fonte: idealista/news (Lusa), 23/10/2026. Confirma o diploma publicado.", [
    [("h", "Heranças: vender a casa sem acordo", 78), ("p", "O que o Governo aprovou.", 44)],
    [("card", "O NOVO REGIME", "Decreto-lei aprovado em Conselho de Ministros a 23 de outubro: processo especial para vender imóveis de heranças indivisas.")],
    [("card", "OS PRAZOS", "Passados dois anos sem acordo, um herdeiro pode pedir a venda. Antes do leilão há seis meses para chegar a acordo.")],
    [("card", "A CASA DE FAMÍLIA", "Fica de fora, salvo consentimento expresso do cônjuge sobrevivo.")],
    [("pn", "A fonte não indica a data de entrada em vigor.", 48)],
], ("Faz as contas à venda.", "Calculadora de mais-valias")),
    "Heranças indivisas: vender sem acordo",
    ["O Governo aprovou um regime para vender imóveis de heranças indivisas quando os herdeiros não se entendem.", "Passados dois anos sem acordo, um herdeiro pode pedir a venda.", "Antes do leilão, os herdeiros têm seis meses para chegar a acordo.", "A casa de morada de família fica de fora, salvo consentimento expresso do cônjuge sobrevivo.", "A fonte não indica a data de entrada em vigor."],
    "idealista/news (Lusa), 23/10/2026.", H("heranças", "vendercasa", "partilhas", "imobiliário", "infoimobiliária"), "Heranças indivisas: o que muda para vender a casa")
reg("20261118v2", V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. 30 anos, taxa total de 4,177%, sem seguros nem comissões.", [
    [("h", "E se a Euribor subir 1 ou 2 pontos?", 78), ("p", "Crédito de 150 000 €.", 44)],
    [("card", "HOJE (TAXA DE 4,177%)", "Prestação de 731,51 €.")],
    [("card", "MAIS 1 PONTO", "Prestação de 821,54 €. São cerca de 90 € a mais por mês.")],
    [("card", "MAIS 2 PONTOS", "Prestação de 916,47 €. São cerca de 185 € a mais por mês.")],
    [("pn", "Cenários, não previsões.", 52)],
], ("Testa o teu caso.", "Calculadora de crédito habitação")),
    "E se a Euribor subir 1 ou 2 pontos?",
    ["Crédito de 150 000 €, 30 anos, taxa total de 4,177%.", "Prestação de 731,51 € por mês.", "Com mais um ponto: 821,54 €, cerca de 90 € a mais.", "Com mais dois pontos: 916,47 €, cerca de 185 € a mais.", "São cenários, não previsões."],
    "Info Imobiliária e Portal da Literacia Financeira. Exemplo calculado por nós, sem seguros nem comissões.", H("euribor", "créditohabitação", "prestação", "imobiliário", "infoimobiliária"), "Euribor +1 ou +2 pontos: quanto sobe a prestação?", leg=False)
reg("20261118v3", V("Glossário", "GLOSSÁRIO · CRÉDITO", "Informação geral. Compara propostas com o mesmo valor e prazo.", [
    [("h", "TAN e TAEG", 110), ("p", "Qual olhar primeiro?", 46)],
    [("card", "TAN", "A taxa de juro: só os juros. Em taxa variável é a Euribor mais o spread.")],
    [("card", "TAEG", "O custo total por ano: juros, comissões, seguros obrigatórios e outros encargos. Costuma ser mais alta que a TAN.")],
    [("card", "COMO COMPARAR", "Usa a TAEG, com o mesmo valor e o mesmo prazo em todos os bancos.")],
], ("Compara com cabeça.", "Glossário imobiliário")),
    "TAN ou TAEG: qual comparar?",
    ["TAN: a taxa de juro, só os juros.", "Em taxa variável, a TAN é a Euribor mais o spread.", "TAEG: o custo total por ano, com juros, comissões, seguros obrigatórios e outros encargos.", "A TAEG costuma ser mais alta que a TAN.", "Para comparar bancos, usa a TAEG, com o mesmo valor e o mesmo prazo."],
    "Info Imobiliária, páginas «TAN» e «TAEG».", H("TAEG", "TAN", "créditohabitação", "imobiliário", "infoimobiliária"), "TAN ou TAEG: qual comparar no crédito habitação?")
reg("20261118c", C("Guia", "GUIA · CRÉDITO", "FIXA, VARIÁVEL OU MISTA", "Fonte: Info Imobiliária, «Taxa fixa, variável ou mista». Informação geral.", [
    [("h", "Taxa fixa, variável ou mista?", 78), ("p", "Cada uma reparte o risco de forma diferente.", 44)],
    [("card", "VARIÁVEL", "Indexada à Euribor, normalmente a 3, 6 ou 12 meses, mais um spread fixo. O custo inicial costuma ser mais baixo.")],
    [("card", "FIXA", "O juro é igual durante todo o prazo ou um período longo. Tende a ser mais cara no início, mas dá previsibilidade.")],
    [("card", "MISTA", "Período fixo, normalmente entre 2 e 10 anos, e depois variável. A proteção só dura enquanto a taxa é fixa.")],
    END("Compara a TAEG antes de decidir."),
]),
    "Taxa fixa, variável ou mista",
    ["Taxa fixa, variável ou mista?", "Variável: Euribor mais spread. O custo inicial costuma ser mais baixo.", "Fixa: o juro é igual durante todo o prazo ou um período longo. Tende a ser mais cara no início.", "Mista: período fixo, normalmente entre 2 e 10 anos, e depois variável.", "Compara a TAEG e pergunta quanto custa mudar de regime.", "Guarda este carrossel."],
    "Info Imobiliária, «Taxa fixa, variável ou mista».", H("taxafixa", "taxavariável", "créditohabitação", "imobiliário", "infoimobiliária"), leg=False)
reg("20261118i", I("Dado", "O DADO · MERCADO", "Fonte: Banco de Portugal, via ECO, 27/10/2026. Dados de setembro.", [
    ("h", "Stock de crédito à habitação", 76), ("num", "120 mil milhões €", 100),
    ("pn", "Passou esta marca pela primeira vez em setembro.", 46), ("p", "Foi o 32.º mês seguido de subida, apesar das regras mais apertadas do Banco de Portugal.", 38)]),
    "Crédito à habitação passa os 120 mil milhões",
    ["120 mil milhões de euros.", "É o stock de crédito à habitação, que passou esta marca pela primeira vez em setembro.", "Foi o 32.º mês seguido de subida.", "Aconteceu apesar das regras mais apertadas do Banco de Portugal desde agosto."],
    "Banco de Portugal, via ECO (27/10/2026).", H("créditohabitação", "bancodeportugal", "imobiliário", "infoimobiliária"), leg=False)

# ================= QUI 19 =================
reg("20261119v1", V("Notícia", "O QUE MUDA · ESCRITURA", "Fonte: ComparaJá, 2/11/2026. Regra em vigor desde 1 de outubro.", [
    [("h", "Escritura: o novo ponto a verificar", 78), ("p", "Em vigor desde 1 de outubro de 2026.", 44)],
    [("card", "A REGRA", "A escritura de venda de um edifício tem de dizer se há título urbanístico. Sem essa menção, o negócio pode ser anulado.")],
    [("card", "NÃO É PROIBIÇÃO", "Não ter título não torna a casa ilegal, mas tem de ficar registado.")],
    [("card", "FICHA TÉCNICA", "Desde 1 de janeiro de 2024, já não é preciso apresentá-la na escritura.")],
    [("pn", "Pede os documentos ao vendedor logo no início.", 50)],
], ("Compra com os papéis certos.", "Como comprar casa, passo a passo")),
    "Escritura: a casa tem título urbanístico?",
    ["Desde 1 de outubro de 2026, a escritura de venda tem de dizer se a casa tem título urbanístico.", "Sem essa menção, o negócio pode ser anulado.", "Não ter título não torna a casa ilegal, mas tem de ficar registado.", "A ficha técnica já não é exigida na escritura desde 1 de janeiro de 2024.", "Pede os documentos ao vendedor logo no início."],
    "ComparaJá (2/11/2026), via Info Imobiliária.", H("escritura", "comprarcasa", "licenciamento", "imobiliário", "infoimobiliária"), "Escritura: desde 1 de outubro tem de constar o título urbanístico")
reg("20261119v2", V("Conta", "A CONTA DA SEMANA · IMPOSTOS", "Exemplo calculado. Habitação própria e permanente no Continente, tabela de 2026.", [
    [("h", "Casa de 250 000 €: quanto pagas de impostos?", 74)],
    [("card", "IMT", "250 000 € × 7% = 17 500 €. Menos a parcela a abater de 10 457,96 €: 7 042,04 €.")],
    [("card", "IMPOSTO DO SELO", "250 000 € × 0,8% = 2 000 €.")],
    [("num", "9 042,04 €", 120), ("p", "de IMT e Selo, sem contar escritura nem crédito.", 44)],
], ("Faz a tua conta.", "Calculadora de custos de aquisição")),
    "Casa de 250 000 €: quanto pagas de IMT e Selo?",
    ["Casa de 250 000 € para habitação própria e permanente.", "IMT: 250 000 € × 7% = 17 500 €, menos a parcela a abater de 10 457,96 €. Ficam 7 042,04 €.", "Imposto do Selo: 250 000 € × 0,8% = 2 000 €.", "Total: 9 042,04 €, sem contar escritura nem crédito."],
    "Info Imobiliária, «Tabela do IMT 2026» (Ofício Circulado n.º 40129/2026 da AT). Exemplo calculado por nós.", H("IMT", "impostodoselo", "comprarcasa", "imobiliário", "infoimobiliária"), "Casa de 250 000 €: IMT e Selo a pagar")
reg("20261119v3", V("Notícia", "O QUE MUDA · MAIS-VALIAS", "Fonte: Contas Poupança, 24/10/2026. Resposta da AT a um caso concreto.", [
    [("h", "Vendeste casa e vais comprar outra?", 78), ("p", "O que a AT esclareceu.", 44)],
    [("card", "A REGRA", "A mais-valia da casa própria pode ficar isenta se reinvestires o valor da venda noutra casa própria e permanente.")],
    [("card", "O QUE A AT DISSE", "O IMT e o Imposto do Selo pagos na casa nova não contam como reinvestimento. Conta o preço da casa ou do terreno e os custos de construção documentados.")],
    [("card", "O PRAZO", "A compra pode ser feita entre 24 meses antes e 36 meses depois da venda.")],
    [("pn", "Não é mudança na lei: é a leitura da AT num caso.", 48)],
], ("Calcula a tua mais-valia.", "Calculadora de mais-valias")),
    "Reinvestimento: IMT e Selo não contam",
    ["Vendeste casa própria com lucro e vais comprar outra?", "Numa resposta a um caso concreto, a AT disse que o IMT e o Imposto do Selo da casa nova não contam como reinvestimento.", "Conta o preço da casa ou do terreno e os custos de construção documentados.", "A compra pode ser feita entre 24 meses antes e 36 meses depois da venda.", "Não é uma mudança na lei: é a leitura da AT num caso concreto."],
    "Contas Poupança (24/10/2026), via Info Imobiliária.", H("maisvalias", "vendercasa", "IRS", "imobiliário", "infoimobiliária"), "Mais-valias: IMT e Selo não contam como reinvestimento")
reg("20261119c", C("Guia", "GUIA · JOVENS", "A GARANTIA PÚBLICA", "Fonte: Info Imobiliária, «Garantia pública para jovens». Confirma no teu banco.", [
    [("h", "Garantia pública para jovens", 80), ("p", "Como funciona, em resumo.", 46)],
    [("card", "O QUE FAZ", "Permite financiar até 100% do valor da casa. O Estado garante até 15% do capital inicial, durante 10 anos.")],
    [("card", "QUEM PODE", "Jovens dos 18 aos 35 anos, com residência fiscal em Portugal, para a primeira habitação própria e permanente, sem outro imóvel habitacional.")],
    [("card", "LIMITES", "Imóvel até 450 000 €. Cobre contratos formalizados até 31 de dezembro de 2026, com possível prolongamento a confirmar no banco.")],
    END("Pergunta ao teu banco."),
]),
    "Garantia pública para jovens",
    ["Garantia pública para jovens: como funciona.", "Permite financiar até 100% do valor da casa.", "O Estado garante até 15% do capital inicial, durante 10 anos.", "É para jovens dos 18 aos 35 anos, na primeira habitação própria e permanente.", "O imóvel pode custar até 450 000 €.", "Cobre contratos formalizados até 31 de dezembro de 2026. Confirma o prolongamento no teu banco."],
    "Info Imobiliária, «Garantia pública do Estado no crédito habitação para jovens».", H("garantiapública", "jovens", "créditohabitação", "imobiliário", "infoimobiliária"))
reg("20261119i", I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «Tabela do IMT 2026», AT. Continente, habitação própria e permanente.", [
    ("h", "Sem IMT na compra de casa", 76), ("num", "106 346 €", 120),
    ("pn", "Até este valor, a habitação própria e permanente no Continente não paga IMT.", 44), ("p", "Acima, o imposto é progressivo. O Imposto do Selo de 0,8% paga-se sempre.", 38)]),
    "IMT: isenção até 106 346 €",
    ["106 346 €.", "Até este valor, a compra de habitação própria e permanente no Continente não paga IMT.", "Acima dele, o imposto é progressivo.", "O Imposto do Selo de 0,8% paga-se sempre."],
    "Info Imobiliária, «Tabela do IMT 2026» (Ofício Circulado n.º 40129/2026 da AT).", H("IMT", "tabelaIMT", "comprarcasa", "imobiliário", "infoimobiliária"))

# ================= SEX 20 =================
reg("20261120v1", V("Notícia", "O QUE MUDA · IMI", "Fonte: ComparaJá, 28/10/2026, e Portaria n.º 457/2026/1. Confirma na caderneta predial.", [
    [("h", "IMI em 2027: o VPT pode subir 3%", 78), ("p", "Só para casas avaliadas em 2023.", 44)],
    [("card", "O QUE MUDOU", "A Portaria n.º 457/2026/1, de 15 de outubro, fixou o coeficiente de 1,04 para 2023. Segundo a ComparaJá, nas casas aplica-se 75%: o VPT sobe 3%.")],
    [("card", "QUANDO SE PAGA", "O IMI de 2026 é cobrado em 2027. A taxa do teu município não muda.")],
    [("pair", ("VPT 200 000 €", "IMI 600 €"), ("VPT 206 000 €", "IMI 618 €")), ("p", "Exemplo com taxa de 0,3%.", 40)],
    [("pn", "Confirma o ano da avaliação na caderneta predial.", 50)],
], ("Vê a tua caderneta.", "Tabela do IMI 2026")),
    "IMI: casas avaliadas em 2023 e o VPT +3%",
    ["Casas cuja última avaliação do VPT foi em 2023 podem ter o valor patrimonial atualizado em 3%.", "A Portaria n.º 457/2026/1 fixou o coeficiente de 1,04 para 2023. Segundo a ComparaJá, nas casas aplica-se 75% desse valor.", "O IMI de 2026 paga-se em 2027. A taxa do município não muda.", "Exemplo: VPT de 200 000 € e taxa de 0,3% dão 600 € de IMI. Com VPT de 206 000 €, são 618 €.", "Confirma o ano da avaliação na caderneta predial."],
    "ComparaJá (28/10/2026) e Portaria n.º 457/2026/1 (15/10/2026). Exemplo calculado por nós.", H("IMI", "VPT", "impostos", "imobiliário", "infoimobiliária"), "IMI em 2027: o VPT pode subir 3% nas casas avaliadas em 2023")
reg("20261120v2", V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. 200 000 €, 30 anos, Euribor a 12 meses de 3,177%, sem seguros nem comissões.", [
    [("h", "O spread conta mesmo?", 90), ("p", "Crédito de 200 000 € a 30 anos.", 44)],
    [("card", "SPREAD DE 1,0%", "Taxa total de 4,177%. Prestação de 975,35 €.")],
    [("card", "SPREAD DE 1,5%", "Taxa total de 4,677%. Prestação de 1 034,51 €.")],
    [("num", "+59 €", 140), ("p", "por mês, cerca de 710 € por ano, só por meio ponto de spread.", 44)],
], ("Negoceia o spread.", "Glossário imobiliário")),
    "Spread de 1% ou de 1,5%: quanto custa a diferença?",
    ["Crédito de 200 000 €, 30 anos, Euribor a 12 meses de 3,177%.", "Com spread de 1,0%, a prestação é de 975,35 €.", "Com spread de 1,5%, é de 1 034,51 €.", "São cerca de 59 € a mais por mês, mais de 700 € por ano.", "O spread é negociável. Pergunta ao banco."],
    "Info Imobiliária, página «Spread». Exemplo calculado por nós, sem seguros nem comissões.", H("spread", "créditohabitação", "prestação", "imobiliário", "infoimobiliária"), "O spread do crédito habitação conta: 1,0% ou 1,5%?", leg=False)
reg("20261120v3", V("Conta", "A CONTA DA SEMANA · AMORTIZAR", "Exemplo calculado. 200 000 €, 30 anos, taxa de 4,177%, amortização de 10 000 € ao fim de 2 anos.", [
    [("h", "Amortizar 10 000 €: prestação ou prazo?", 74)],
    [("card", "REDUZIR A PRESTAÇÃO", "Passa de 975,35 € para cerca de 924,82 €. Poupas cerca de 7 000 € de juros.")],
    [("card", "REDUZIR O PRAZO", "O crédito acaba cerca de 2 anos e 7 meses mais cedo. Poupas cerca de 20 500 € de juros.")],
    [("pn", "Reduzir o prazo costuma poupar mais juros. Reduzir a prestação alivia o orçamento.", 46)],
], ("Pergunta pelas comissões.", "Amortização antecipada")),
    "Amortizar 10 000 €: reduzir prestação ou prazo?",
    ["Crédito de 200 000 €, 30 anos, taxa de 4,177%. Ao fim de 2 anos, amortizas 10 000 €.", "Reduzir a prestação: passa de 975,35 € para cerca de 924,82 €, e poupas cerca de 7 000 € de juros.", "Reduzir o prazo: o crédito acaba cerca de 2 anos e 7 meses mais cedo, e poupas cerca de 20 500 € de juros.", "Reduzir o prazo costuma poupar mais juros. Pergunta ao banco pelas comissões."],
    "Info Imobiliária, página «Amortização antecipada». Exemplo calculado por nós, sem seguros nem comissões.", H("amortização", "créditohabitação", "juros", "imobiliário", "infoimobiliária"), "Amortizar o crédito: reduzir a prestação ou o prazo?")
reg("20261120c", C("Guia", "GUIA · OBRAS", "OBRAS EM CASA", "Fonte: Info Imobiliária, «Obras em casa», com ABANCA, idealista e Santander. Regras de outubro de 2026.", [
    [("h", "Obras em casa: por onde começar", 78), ("p", "Lista, orçamentos e licenças.", 44)],
    [("card", "ANTES DE COMEÇAR", "Faz a lista do que queres mudar e pede orçamentos. Confirma se a obra precisa de licença.")],
    [("card", "SIMPLEX URBANÍSTICO", "Há obras dispensadas de licença, como substituir janelas por idênticas. As câmaras têm entre 120 e 200 dias para decidir, e sem resposta a obra pode avançar.")],
    [("card", "MAIS-VALIAS", "As obras de melhoria dos últimos 12 anos, com faturas em teu nome, podem ser descontadas nas mais-valias.")],
    END("Lê o guia completo."),
]),
    "Obras em casa: orçamentos e licenças",
    ["Obras em casa: por onde começar.", "Faz a lista do que queres mudar e pede orçamentos.", "Confirma se a obra precisa de licença. O Simplex Urbanístico dispensa algumas, como substituir janelas por idênticas.", "As câmaras têm entre 120 e 200 dias para decidir, e sem resposta a obra pode avançar.", "As obras de melhoria dos últimos 12 anos podem ser descontadas nas mais-valias.", "Guarda este carrossel."],
    "Info Imobiliária, «Obras em casa», com ABANCA, idealista e Santander.", H("obras", "licenciamento", "casaevida", "imobiliário", "infoimobiliária"))
reg("20261120i", I("Dado", "O DADO · ARRENDAR", "Fonte: INE, 29/9/2026, via Info Imobiliária. Contratos novos no 2.º trimestre.", [
    ("h", "Renda mediana dos contratos novos", 74), ("num", "10,17 €/m²", 120),
    ("pn", "Mais 10,2% do que um ano antes. Novo recorde da série.", 46), ("p", "Na Grande Lisboa a renda mediana foi de 15,24 €/m². É a mediana dos contratos novos, não a renda de todos os inquilinos.", 36)]),
    "Rendas novas: 10,17 €/m²",
    ["10,17 € por metro quadrado.", "É a renda mediana dos contratos novos no 2.º trimestre de 2026, segundo o INE.", "Subiu 10,2% num ano e é um novo recorde da série.", "Na Grande Lisboa foi de 15,24 €/m².", "É a mediana dos contratos novos, não a renda de todos os inquilinos."],
    "INE (29/9/2026), via Info Imobiliária.", H("arrendamento", "rendas", "INE", "imobiliário", "infoimobiliária"), leg=False)

# ================= SÁB 21 =================
reg("20261121v1", V("Notícia", "O QUE MUDA · RENDAS 2027", "Fonte: ECO, 31/8/2026, e DECO Proteste, 6/10/2026. Cálculo com dados do INE.", [
    [("h", "Rendas em 2027: até 2,56%", 84), ("p", "Contratos já em vigor.", 44)],
    [("card", "O COEFICIENTE", "2,56% para 2027, contra 2,24% em 2026. A renda é multiplicada por 1,0256.")],
    [("card", "NÃO É OBRIGATÓRIO", "O senhorio decide se atualiza e em que mês. Tem de avisar por escrito com pelo menos 30 dias de antecedência.")],
    [("card", "QUEM ENTRA", "Contratos em vigor há mais de um ano. Nos contratos novos, a renda é acordada entre as partes.")],
    [("pn", "Se a conta ou o aviso estiverem errados, contesta por escrito.", 48)],
], ("Compara arrendar e comprar.", "Calculadora arrendar ou comprar")),
    "Rendas em 2027: o aumento até 2,56%",
    ["Em 2027, as rendas dos contratos em vigor podem subir até 2,56%, contra 2,24% em 2026.", "A atualização não é obrigatória: o senhorio decide se a aplica e em que mês.", "Tem de avisar por escrito com pelo menos 30 dias de antecedência.", "Só vale para contratos em vigor há mais de um ano.", "Se a conta ou o aviso estiverem errados, contesta por escrito."],
    "ECO (31/8/2026) e DECO Proteste (6/10/2026). Valor calculado com dados do INE.", H("arrendamento", "rendas2027", "senhorios", "inquilinos", "infoimobiliária"), "Rendas em 2027: o senhorio pode atualizar até 2,56%")
reg("20261121v2", V("Pergunta", "PERGUNTA DA SEMANA · COMPRAR", "Informação geral. A lei é interpretada caso a caso: pede aconselhamento jurídico.", [
    [("h", "Comprei casa e descobri um defeito. E agora?", 74)],
    [("card", "O PRAZO", "Tens um ano, a partir da deteção, para denunciar o defeito ao vendedor. Depois, seis meses para avançar com uma ação em tribunal.")],
    [("card", "OS TEUS DIREITOS", "Reparação, redução do preço e, nos casos graves, resolução do contrato.")],
    [("card", "PREVINE", "Faz uma vistoria técnica independente antes de comprar. «No estado em que se encontra» normalmente não afasta defeitos ocultos graves.")],
], ("Compra a ver bem.", "Defeitos ocultos na compra de casa")),
    "Defeitos ocultos: que prazos tens?",
    ["Compraste casa usada e descobriste um defeito escondido?", "Tens um ano, a partir da deteção, para o denunciar ao vendedor.", "Depois da denúncia, tens seis meses para avançar com uma ação judicial.", "Podes pedir reparação, redução do preço e, nos casos graves, a resolução do contrato.", "Antes de comprar, faz uma vistoria técnica independente."],
    "Info Imobiliária, «Defeitos ocultos na compra de casa usada» (Código Civil, artigos 913.º e seguintes).", H("defeitosocultos", "comprarcasa", "casausada", "imobiliário", "infoimobiliária"), "Defeitos ocultos na casa que compraste: prazos e direitos")
reg("20261121v3", V("Passo a passo", "PASSO A PASSO · COMPRAR", "Fonte: DECO Proteste, idealista e Caixa Geral de Depósitos. Valores sem impostos; honorários variam.", [
    [("h", "Onde fazer a escritura?", 88), ("p", "Três vias, o mesmo ato.", 44)],
    [("card", "1. NOTÁRIO", "Escritura pública. Os honorários variam.")],
    [("card", "2. DOCUMENTO PARTICULAR AUTENTICADO", "Feito por advogados, solicitadores ou conservatórias.")],
    [("card", "3. CASA PRONTA", "375 € com um ato de registo. 700 € na compra com financiamento. Mais 50 € por cada prédio adicional.")],
    [("pn", "Paga o IMT e o Selo antes e leva os comprovativos.", 48)],
], ("Marca com tempo.", "Escritura: o que levar")),
    "Escritura: notário, DPA ou Casa Pronta?",
    ["Escritura: três vias para o mesmo ato.", "Notário, documento particular autenticado ou Casa Pronta.", "Na Casa Pronta: 375 € com um ato de registo e 700 € na compra com financiamento.", "Mais 50 € por cada prédio adicional.", "Paga o IMT e o Selo antes e leva os comprovativos no dia."],
    "DECO Proteste, idealista e Caixa Geral de Depósitos, via Info Imobiliária. Valores sem impostos.", H("escritura", "casapronta", "comprarcasa", "imobiliário", "infoimobiliária"), "Escritura de compra de casa: notário, DPA ou Casa Pronta")
reg("20261121c", C("Guia", "GUIA · ARRENDAR OU COMPRAR", "O QUE PESA ALÉM DA PRESTAÇÃO", "Fonte: Info Imobiliária, «Comprar ou arrendar casa», com Portal da Literacia Financeira. Valores de outubro de 2026.", [
    [("h", "Comprar ou arrendar: o que pesa além da prestação?", 70), ("p", "Comparar prestação com renda não chega.", 44)],
    [("card", "NA COMPRA", "IMT (isento até 106 346 € na habitação própria e permanente) e Selo de 0,8%. Comissões do banco entre 650 € e 900 €.")],
    [("card", "TODOS OS ANOS", "IMI entre 0,3% e 0,45% do VPT. O simulador do Portal da Literacia Financeira assume 1% a 2% do valor da casa em manutenção.")],
    [("card", "QUANDO ARRENDAR FAZ SENTIDO", "Se o horizonte é de dois ou três anos, os custos de compra dificilmente se recuperam.")],
    END("Faz a comparação."),
]),
    "Comprar ou arrendar: o que pesa além da prestação",
    ["Comprar ou arrendar: comparar prestação com renda não chega.", "Na compra há IMT, Selo de 0,8% e comissões do banco, entre 650 € e 900 €.", "Todos os anos há IMI, entre 0,3% e 0,45% do VPT.", "O simulador do Portal da Literacia Financeira assume 1% a 2% do valor da casa por ano em manutenção.", "Se o horizonte é de dois ou três anos, arrendar tende a fazer mais sentido.", "Guarda este carrossel."],
    "Info Imobiliária, «Comprar ou arrendar casa», com Portal da Literacia Financeira e idealista.", H("arrendarouromprar", "comprarcasa", "arrendamento", "imobiliário", "infoimobiliária"))
reg("20261121i", I("Dado", "O DADO · MERCADO", "Fonte: idealista/news, 1/10/2026. Preço mediano de oferta em setembro.", [
    ("h", "Preço pedido das casas", 80), ("num", "3 228 €/m²", 120),
    ("pn", "Novo recorde, com mais 7,9% do que um ano antes.", 46), ("p", "É o preço pedido nos anúncios, não o preço de venda nem a avaliação do banco. Lisboa: 6 256 €/m². Castelo Branco: 1 090 €/m².", 34)]),
    "Preço pedido: 3.228 €/m²",
    ["3 228 € por metro quadrado.", "É o preço mediano pedido nos anúncios em setembro, um novo recorde.", "Mais 7,9% do que um ano antes.", "Lisboa: 6 256 €/m². Castelo Branco: 1 090 €/m².", "É o preço pedido, não o preço de venda nem a avaliação do banco."],
    "idealista/news (1/10/2026), via Info Imobiliária.", H("preçosdecasas", "mercadoimobiliário", "imobiliário", "infoimobiliária"), leg=False)

# ================= DOM 22 =================
reg("20261122v1", V("Notícia", "O QUE MUDA · OE2027", "Fonte: idealista/news, 8/10/2026. Propostas por votar.", [
    [("h", "OE2027: o que traz para a habitação", 80), ("p", "Tudo ainda são propostas.", 44)],
    [("card", "IVA DA CONSTRUÇÃO", "Passaria de 23% para 6%.")],
    [("card", "IRS SOBRE RENDAS", "Descida para rendas moderadas, até 2 300 € por mês.")],
    [("card", "GARANTIA PÚBLICA", "Prevista, mas o ministro das Finanças não confirmou formalmente a continuidade.")],
    [("pn", "Votação final global marcada para 24 de novembro.", 50)],
], ("Faz as contas com as regras de hoje.", "Calculadora de custos de aquisição")),
    "OE2027: medidas para a habitação",
    ["Orçamento do Estado para 2027: o que traz para a habitação.", "Proposta de IVA da construção a 6%, em vez de 23%.", "Proposta de IRS mais baixo para rendas moderadas, até 2 300 € por mês.", "A garantia pública está prevista, mas a continuidade não foi confirmada formalmente.", "A votação final global está marcada para 24 de novembro. Nada disto está em vigor."],
    "idealista/news (8/10/2026), via Info Imobiliária.", H("OE2027", "habitação", "IRS", "imobiliário", "infoimobiliária"), "OE2027 e habitação: IVA a 6% e IRS mais baixo nas rendas")
reg("20261122v2", V("Conta", "A CONTA DA SEMANA · JOVENS", "Exemplo calculado. Casa de 250 000 €. Garantia de até 15% do valor da transação.", [
    [("h", "Garantia pública: quanto cobre?", 84), ("p", "Casa de 250 000 €.", 44)],
    [("card", "SEM GARANTIA (90%)", "Financiamento de 225 000 €. Entrada de 25 000 €.")],
    [("card", "A GARANTIA", "Cobre até 15% do valor: 37 500 €. Permite, em muitos casos, financiar 100%.")],
    [("pn", "Só para jovens até 35 anos, primeira casa, imóvel até 450 000 €. Confirma no teu banco.", 44)],
], ("Vê se tens direito.", "Garantia pública para jovens")),
    "Garantia pública: 15% de 250 000 €",
    ["Casa de 250 000 €.", "Sem garantia, o banco financia até 90%: 225 000 €, com entrada de 25 000 €.", "A garantia pública cobre até 15% do valor: 37 500 €.", "Em muitos casos, permite financiar 100%.", "É para jovens até 35 anos, na primeira casa, com imóvel até 450 000 €."],
    "Info Imobiliária, «Garantia pública» e ECO (22/10/2026). Exemplo calculado por nós.", H("garantiapública", "jovens", "comprarcasa", "imobiliário", "infoimobiliária"), "Garantia pública para jovens: quanto cobre numa casa de 250 000 €?")
reg("20261122v3", V("Pergunta", "PERGUNTA DA SEMANA · VENDER", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Vender primeiro ou comprar primeiro?", 84)],
    [("card", "VENDER PRIMEIRO", "Para a maioria, é a opção mais segura.")],
    [("card", "COMPRAR PRIMEIRO", "Só com folga financeira ou com cláusula suspensiva. Senão, arriscas dois créditos ou prestação mais renda.")],
    [("card", "AJUDAS", "Pré-aprovação do banco, cláusula suspensiva no contrato-promessa e escrituras com datas coordenadas.")],
], ("Decide com contas.", "Vender primeiro ou comprar primeiro")),
    "Vender primeiro ou comprar primeiro?",
    ["Vais mudar de casa: vendes primeiro ou compras primeiro?", "Para a maioria, vender primeiro é a opção mais segura.", "Comprar primeiro só com folga financeira ou cláusula suspensiva no contrato-promessa.", "Senão, arriscas dois créditos ou prestação mais renda.", "Pede a pré-aprovação ao banco e coordena as datas das duas escrituras."],
    "Info Imobiliária, «Vender primeiro ou comprar primeiro: como decidir».", H("vendercasa", "comprarcasa", "mudardecasa", "imobiliário", "infoimobiliária"), "Vender primeiro ou comprar primeiro: como decidir")
reg("20261122c", C("Checklist", "GUIA · VENDER", "PREPARAR A CASA", "Fonte: Info Imobiliária, «Como preparar a casa para vender, gastando pouco».", [
    [("h", "Preparar a casa para vender, gastando pouco", 72), ("p", "O que fazer primeiro.", 44)],
    [("card", "1. DESPERSONALIZA E ARRUMA", "Tira fotografias pessoais, esvazia armários e retira o excesso de mobília.")],
    [("card", "2. LIMPEZA E REPARAÇÕES", "Limpeza profunda, lâmpadas novas e pequenas reparações.")],
    [("card", "3. PINTURA E EXTERIOR", "Tons neutros e entrada ou jardim cuidados. Um fim de semana costuma chegar, e a pintura soma mais alguns dias.")],
    END("Obras de fundo raramente compensam."),
]),
    "Preparar a casa para vender, gastando pouco",
    ["Preparar a casa para vender, gastando pouco.", "1. Despersonaliza e arruma: menos fotografias pessoais e menos mobília.", "2. Limpeza profunda e pequenas reparações.", "3. Pintura em tons neutros e exterior cuidado.", "Um fim de semana costuma chegar, e a pintura soma mais alguns dias.", "Guarda este carrossel."],
    "Info Imobiliária, «Como preparar a casa para vender, gastando pouco».", H("vendercasa", "homestaging", "dicasdecasa", "imobiliário", "infoimobiliária"), leg=False)
reg("20261122i", I("Dado", "O DADO · CRÉDITO", "Fonte: INE, 21/10/2026, via ECO. Dados de setembro.", [
    ("h", "Prestação média do crédito habitação", 72), ("num", "423 €", 150),
    ("pn", "Juros: 213 €, ou 50,4%. Capital: 210 €.", 46), ("p", "É a média de todos os contratos, mais 30 € do que um ano antes. A tua prestação depende do capital, do prazo e da taxa.", 36)]),
    "Prestação média: 423 €",
    ["423 €.", "É a prestação média do crédito à habitação em setembro, segundo o INE.", "Os juros pesam 213 €, ou 50,4%, e o capital 210 €.", "Mais 30 € do que um ano antes.", "É uma média: a tua prestação depende do capital, do prazo e da taxa."],
    "INE, via ECO (21/10/2026).", H("créditohabitação", "prestação", "INE", "imobiliário", "infoimobiliária"), leg=False)

# ================= SEG 23 =================
reg("20261123v1", V("Notícia", "O QUE MUDA · IMT JOVEM", "Fonte: Info Imobiliária, «OE2027: IMT sobe 2,3%», com ECO e Contas Poupança, 8/10/2026. Proposta.", [
    [("h", "IMT Jovem em 2027: o que se propõe", 78), ("p", "Ainda só proposta.", 44)],
    [("card", "HOJE (2026)", "Isenção total de IMT e Selo até 330 539 € na primeira casa de jovens até 35 anos.")],
    [("card", "A PROPOSTA DO OE2027", "Subir a isenção para 338 141 €.")],
    [("pair", ("2026: 400 000 €", "5 556,88 €"), ("PROPOSTA", "4 948,72 €")), ("p", "IMT de uma casa de 400 000 €, sem Selo.", 40)],
    [("pn", "Depende da votação final. Em 2026 vale a tabela de 2026.", 48)],
], ("Vê quanto pagas.", "IMT Jovem: quem tem direito")),
    "IMT Jovem: a proposta para 2027",
    ["Jovens até 35 anos na primeira casa não pagam IMT até 330 539 €, em 2026.", "A proposta de Orçamento para 2027 sobe esse limite para 338 141 €.", "Numa casa de 400 000 €, o IMT passaria de 5 556,88 € para 4 948,72 €, sem contar o Selo.", "É só uma proposta, ainda por votar. Em 2026 vale a tabela de 2026."],
    "Info Imobiliária, «IMT Jovem» e «OE2027: IMT sobe 2,3%» (ECO e Contas Poupança, 8/10/2026). Exemplo calculado por nós.", H("IMTjovem", "OE2027", "jovens", "imobiliário", "infoimobiliária"), "IMT Jovem em 2027: o que o Orçamento propõe")
reg("20261123v2", V("Glossário", "GLOSSÁRIO · DOCUMENTOS", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Caderneta ou certidão?", 96), ("p", "Dois documentos, duas funções.", 46)],
    [("card", "CADERNETA PREDIAL", "Das Finanças: o «bilhete de identidade fiscal» da casa. Tem o VPT, as áreas e o proprietário.")],
    [("card", "CERTIDÃO PERMANENTE", "Do registo predial: a situação jurídica. Mostra o dono, hipotecas e penhoras. Costuma valer 6 meses.")],
    [("card", "NA COMPRA", "Precisas das duas. Compara áreas e descrição com o anúncio antes do CPCV.")],
], ("Pede as duas.", "Certidão permanente")),
    "Caderneta predial ou certidão permanente?",
    ["Caderneta predial: emitida pelas Finanças, tem o VPT, as áreas e o proprietário.", "Certidão permanente: do registo predial, mostra o dono, hipotecas e penhoras.", "Em regra, a certidão vale 6 meses.", "Na compra precisas das duas.", "Compara áreas e descrição com o anúncio antes do CPCV."],
    "Info Imobiliária, páginas «Caderneta predial» e «Certidão permanente».", H("cadernetapredial", "certidãopermanente", "comprarcasa", "imobiliário", "infoimobiliária"), "Caderneta predial ou certidão permanente: qual a diferença?")
reg("20261123v3", V("Notícia", "O QUE MUDA · VENDER", "Fonte: idealista/news, 20/10/2026. Dados do 3.º trimestre, no portal.", [
    [("h", "Quanto tempo demora a vender?", 84), ("p", "Anúncios no idealista, 3.º trimestre.", 44)],
    [("pair", ("EM MENOS DE 1 SEMANA", "12%"), ("DE 3 MESES A 1 ANO", "37%"))],
    [("card", "LISBOA", "Só 7% venderam em menos de uma semana. 42% demoraram entre 3 meses e 1 ano.")],
    [("card", "PORTO E AVEIRO", "No Porto, 14%. Em Aveiro, 15%.")],
    [("pn", "Cada caso é diferente. Prepara bem a casa e o preço.", 48)],
], ("Prepara a venda.", "Como vender casa, passo a passo")),
    "Só 12% das casas vendem-se numa semana",
    ["Quanto tempo demora a vender casa? Dados do 3.º trimestre no idealista.", "12% venderam em menos de uma semana e 37% demoraram entre 3 meses e 1 ano.", "Em Lisboa, só 7% venderam em menos de uma semana.", "No Porto foram 14% e em Aveiro 15%.", "Cada caso é diferente: o preço e a preparação pesam."],
    "idealista/news (20/10/2026), via Info Imobiliária.", H("vendercasa", "mercadoimobiliário", "idealista", "imobiliário", "infoimobiliária"), "Só 12% das casas vendem-se numa semana: e a tua?", leg=False)
reg("20261123c", C("Guia", "GUIA · IMPOSTOS", "O IMPOSTO DO SELO", "Fonte: Info Imobiliária, «Tabela do Imposto do Selo em 2026». Regras de outubro de 2026.", [
    [("h", "Imposto do Selo: o que pagas", 82), ("p", "Na compra e no crédito.", 46)],
    [("card", "NA COMPRA DA CASA", "0,8% sobre o valor que serve de base ao IMT. Em 250 000 €: 2 000 €.")],
    [("card", "NO CRÉDITO", "0,6% do capital emprestado, quando o prazo é de 5 anos ou mais. Em 200 000 €: 1 200 €.")],
    [("card", "NAS COMISSÕES DO BANCO", "4% sobre as comissões de análise, avaliação e formalização. Os juros do crédito para habitação própria não pagam Selo.")],
    END("Faz a conta toda."),
]),
    "Imposto do Selo: compra, crédito e comissões",
    ["Imposto do Selo: o que pagas.", "Na compra da casa: 0,8% sobre o valor que serve de base ao IMT.", "No crédito: 0,6% do capital, quando o prazo é de 5 anos ou mais.", "Nas comissões do banco: 4%.", "Exemplo: casa de 250 000 € e crédito de 200 000 € dão 2 000 € + 1 200 € = 3 200 € de Selo.", "Guarda este carrossel."],
    "Info Imobiliária, «Tabela do Imposto do Selo em 2026». Exemplo calculado por nós.", H("impostodoselo", "comprarcasa", "impostos", "imobiliário", "infoimobiliária"))
reg("20261123i", I("Dado", "O DADO · MERCADO", "Fonte: INE, 22/9/2026, via ComparaJá. 2.º trimestre de 2026.", [
    ("h", "Preços da habitação", 84), ("num", "+16,5%", 150),
    ("pn", "Subida homóloga no 2.º trimestre, segundo o INE.", 46), ("p", "Abrandou face aos 17,8% do 1.º trimestre. Mede transações de casas novas e existentes.", 38)]),
    "Preços da habitação: +16,5%",
    ["+16,5%.", "É a subida dos preços da habitação no 2.º trimestre de 2026, face a um ano antes, segundo o INE.", "Abrandou face aos 17,8% do 1.º trimestre.", "Mede transações de casas novas e existentes."],
    "INE (22/9/2026), via ComparaJá.", H("preçosdecasas", "INE", "mercadoimobiliário", "imobiliário", "infoimobiliária"), leg=False)

# ================= TER 24 =================
reg("20261124v1", V("Notícia", "O QUE MUDA · MERCADO", "Fonte: idealista/news (Lusa), 16/10/2026. Estudo do Banco de Portugal.", [
    [("h", "Mais procura: sobem mais os preços ou as rendas?", 72)],
    [("card", "O ESTUDO", "Um estudo do Banco de Portugal analisou os municípios entre 2017 e 2024.")],
    [("pair", ("PREÇOS", "+0,69%"), ("RENDAS", "+0,37%")), ("p", "Quando a procura sobe 1%.", 44)],
    [("card", "A CONCLUSÃO", "O efeito é maior onde há menos oferta, como Lisboa e Porto. A oferta é a peça em falta.")],
    [("pn", "É um estudo, não muda regras nem impostos.", 50)],
], ("Compara arrendar e comprar.", "Calculadora arrendar ou comprar")),
    "Mais procura: preços sobem mais do que as rendas",
    ["Um estudo do Banco de Portugal analisou os municípios entre 2017 e 2024.", "Quando a procura sobe 1%, os preços das casas sobem cerca de 0,69% e as rendas cerca de 0,37%.", "O efeito é maior onde há menos oferta, como Lisboa e Porto.", "A conclusão é que apoiar só a procura não chega: falta oferta.", "É um estudo, não muda regras nem impostos."],
    "idealista/news (Lusa), 16/10/2026, via Info Imobiliária.", H("bancodeportugal", "habitação", "preços", "imobiliário", "infoimobiliária"), "Banco de Portugal: mais procura sobe mais os preços do que as rendas", leg=False)
reg("20261124v2", V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. 150 000 €, 30 anos, taxa de 3,5%. Base: Portal da Literacia Financeira.", [
    [("h", "O banco não usa a tua prestação real", 76), ("p", "Crédito de 150 000 € a 3,5%.", 44)],
    [("card", "PRESTAÇÃO REAL", "673,57 € por mês.")],
    [("card", "COM O TESTE DE STRESS", "O banco simula mais 1,5 pontos num crédito com mais de 10 anos: taxa de 5%, prestação de 805,23 €.")],
    [("num", "1 789 €", 130), ("p", "de rendimento líquido mínimo, com o limite de 45%, só para este crédito.", 42)],
], ("Simula a tua prestação.", "Taxa de esforço")),
    "Teste de stress do banco: a prestação que conta",
    ["Crédito de 150 000 €, 30 anos, taxa de 3,5%.", "A prestação real é de 673,57 €.", "O banco simula uma subida de 1,5 pontos nos créditos com mais de 10 anos: taxa de 5%, prestação de 805,23 €.", "Com o limite de 45%, precisas de cerca de 1 789 € líquidos por mês, só para este crédito.", "Cada outro crédito que pagas aumenta o rendimento de que precisas."],
    "Info Imobiliária, «Taxa de esforço», com base no Portal da Literacia Financeira. Exemplo calculado por nós.", H("taxadeesforço", "stresstest", "créditohabitação", "imobiliário", "infoimobiliária"), "O teste de stress do banco: a prestação que realmente conta", leg=False)
reg("20261124v3", V("Erro comum", "ERRO COMUM · OBRAS", "Informação geral. Confirma licenças com a câmara municipal.", [
    [("h", "Começar as obras sem orçamentos", 82)],
    [("card", "O ERRO", "Chamar o primeiro empreiteiro e aceitar o primeiro preço.")],
    [("card", "O QUE FAZER", "Pede pelo menos dois ou três orçamentos e compara o que inclui cada um.")],
    [("card", "CONFIRMA A LICENÇA", "Há obras dispensadas de licença, outras não. Vê com a câmara antes de começar.")],
    [("card", "COMBINA O PAGAMENTO", "Por exemplo, 50% no início e 50% no fim, com tudo por escrito.")],
], ("Obras sem surpresas.", "Obras em casa: por onde começar")),
    "Erro comum: começar obras sem orçamentos",
    ["Erro comum: chamar o primeiro empreiteiro e aceitar o primeiro preço.", "Pede pelo menos dois ou três orçamentos.", "Confirma na câmara se a obra precisa de licença.", "Combina o pagamento por escrito, por exemplo 50% no início e 50% no fim.", "Se houver defeitos, avisa por carta registada com aviso de receção."],
    "Info Imobiliária, «Obras em casa: por onde começar, orçamentos e licenças».", H("obras", "empreiteiro", "casaevida", "imobiliário", "infoimobiliária"), "Erro comum: começar as obras em casa sem orçamentos")
reg("20261124c", C("Checklist", "GUIA · MUDAR DE CASA", "OS PRAZOS DA MUDANÇA", "Fonte: Info Imobiliária, «Mudar de casa», com gov.pt. Regras de outubro de 2026.", [
    [("h", "Mudar de casa: prazos a cumprir", 78), ("p", "Não acaba quando o camião sai.", 44)],
    [("card", "MORADA FISCAL", "Altera a morada do Cartão de Cidadão e confirma o código que chega por carta. Prazo: 60 dias após a mudança.")],
    [("card", "CARRO E ANIMAL", "Certificado de matrícula: 60 dias. Animal de companhia (SIAC): 15 dias.")],
    [("card", "CORREIO", "A reexpedição dos CTT demora cerca de 3 dias úteis a ficar ativa.")],
    END("Lê a lista completa."),
]),
    "Mudar de casa: os prazos",
    ["Mudar de casa: prazos a cumprir.", "Morada fiscal: 60 dias após a mudança, com o código enviado por carta para a nova morada.", "Certificado de matrícula do carro: 60 dias.", "Animal de companhia (SIAC): 15 dias.", "Reexpedição dos CTT: cerca de 3 dias úteis a ficar ativa.", "Guarda este carrossel."],
    "Info Imobiliária, «Mudar de casa: o que tratar e em que prazos», com gov.pt.", H("mudardecasa", "moradafiscal", "checklist", "imobiliário", "infoimobiliária"), leg=False)
reg("20261124i", I("Dado", "O DADO · CRÉDITO", "Fonte: Banco de Portugal, via Info Imobiliária. Recomendações em vigor desde 1 de agosto de 2026.", [
    ("h", "Prazo máximo do crédito habitação", 70), ("pair", ("ATÉ AOS 35 ANOS", "40 anos"), ("ACIMA DOS 35", "35 anos")),
    ("pn", "É uma recomendação do Banco de Portugal, com a lógica de cumprir ou explicar.", 44), ("p", "Cada banco pode fazer exceções limitadas.", 38)]),
    "Prazo máximo do crédito: 40 ou 35 anos",
    ["Prazo máximo do crédito habitação: 40 anos até aos 35 anos de idade e 35 anos acima disso.", "É uma recomendação do Banco de Portugal, em vigor desde 1 de agosto de 2026.", "Segue a lógica de cumprir ou explicar.", "Cada banco pode fazer exceções limitadas."],
    "Info Imobiliária, «Taxa de esforço» e «Crédito habitação: taxa de esforço máxima desce para 45%».", H("créditohabitação", "bancodeportugal", "prazo", "imobiliário", "infoimobiliária"), leg=False)

# ================= QUA 25 =================
reg("20261125v1", V("Notícia", "O QUE MUDA · AVALIAÇÃO", "Fonte: INE, 27/10/2026, via Jornal Económico e Executive Digest. Dados de setembro.", [
    [("h", "Avaliação bancária em recorde", 84), ("p", "Mediana de setembro.", 44)],
    [("num", "2 278 €/m²", 120), ("p", "Máximo histórico, mais 1,1% do que em agosto.", 44)],
    [("card", "FACE A UM ANO ANTES", "Mais 14,2%. A subida anual abrandou: em agosto era de 14,7%.")],
    [("card", "O EFEITO NO CRÉDITO", "O banco financia sobre o menor valor entre o preço e a avaliação.")],
    [("pn", "Se a avaliação ficar abaixo do preço, a diferença sai do teu bolso.", 46)],
], ("Faz as contas à entrada.", "Calculadora de custos de aquisição")),
    "Avaliação bancária: 2.278 €/m²",
    ["A avaliação bancária mediana das casas chegou a 2 278 €/m² em setembro, um máximo histórico.", "É mais 1,1% do que em agosto e mais 14,2% do que um ano antes.", "A subida anual abrandou: em agosto era de 14,7%.", "O banco financia sobre o menor valor entre o preço e a avaliação.", "Se a avaliação ficar abaixo do preço, a diferença sai do teu bolso."],
    "INE (27/10/2026), via Jornal Económico e Executive Digest.", H("avaliaçãobancária", "INE", "créditohabitação", "imobiliário", "infoimobiliária"), "Avaliação bancária em recorde: 2.278 €/m² em setembro", leg=False)
reg("20261125v2", V("Conta", "A CONTA DA SEMANA · IMPOSTOS", "Exemplo calculado. Valores de 2026. Taxas por escalão sobre a parte do valor em cada um.", [
    [("h", "AIMI: quem paga e quanto", 90), ("p", "Imóveis com VPT total de 1 300 000 €.", 42)],
    [("card", "ATÉ 600 000 €", "Isento, para uma pessoa singular.")],
    [("card", "DE 600 000 € A 1 000 000 €", "400 000 € × 0,7% = 2 800 €.")],
    [("card", "DE 1 000 000 € A 1 300 000 €", "300 000 € × 1% = 3 000 €. Total de AIMI: 5 800 €.")],
    [("pn", "Casal em tributação conjunta: dedução de 1 200 000 €, pedida às Finanças.", 44)],
], ("Confirma o teu VPT.", "O que é o AIMI")),
    "AIMI: quanto paga quem tem imóveis de 1,3 milhões?",
    ["AIMI: o adicional ao IMI só afeta quem tem imóveis com VPT total acima de 600 000 €.", "Exemplo: VPT total de 1 300 000 €.", "De 600 000 € a 1 000 000 €: 400 000 € × 0,7% = 2 800 €.", "De 1 000 000 € a 1 300 000 €: 300 000 € × 1% = 3 000 €.", "Total: 5 800 €."],
    "Info Imobiliária, «AIMI: quem paga o adicional ao IMI», com a Caixa Geral de Depósitos. Exemplo calculado por nós.", H("AIMI", "IMI", "impostos", "imobiliário", "infoimobiliária"), "AIMI: quanto paga quem tem 1,3 milhões em imóveis?")
reg("20261125v3", V("Erro comum", "ERRO COMUM · CPCV", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Assinar o CPCV sem cláusula de financiamento", 76)],
    [("card", "O ERRO", "Assinar o contrato-promessa a contar com o crédito, sem o escrever.")],
    [("card", "O RISCO", "Sem a cláusula, se o banco recusar o crédito o risco é teu. Com ela, recuperas o sinal.")],
    [("card", "O CASO", "O Tribunal da Relação de Évora, a 14 de julho de 2026, mandou devolver o sinal em singelo.")],
    [("pn", "Escreve no CPCV o que acontece ao sinal se o banco recusar.", 48)],
], ("Assina com a cláusula.", "CPCV: o contrato-promessa")),
    "Erro comum: CPCV sem cláusula de financiamento",
    ["Erro comum: assinar o CPCV a contar com o crédito, sem o escrever.", "Sem cláusula de financiamento, se o banco recusar o crédito o risco é teu.", "Com a cláusula, recuperas o sinal.", "Num caso de 14 de julho de 2026, a Relação de Évora mandou devolver o sinal em singelo.", "Escreve no CPCV o que acontece ao sinal se o banco recusar."],
    "Info Imobiliária, «E se o banco recusar o crédito depois de assinares o CPCV?», com LexPoint e Portal da Literacia Financeira.", H("CPCV", "sinal", "créditohabitação", "imobiliário", "infoimobiliária"), "Erro comum: assinar o CPCV sem cláusula de financiamento")
reg("20261125c", C("Guia", "GUIA · MERCADO", "A OFERTA DE CASAS", "Fonte: idealista/news, 15/10/2026, via Info Imobiliária. Junho a agosto de 2026.", [
    [("h", "Oferta de casas à venda cai 4%", 82), ("p", "Entre junho e agosto de 2026.", 44)],
    [("card", "O NÚMERO", "A oferta recuou 4% face ao ano anterior. É o 7.º trimestre seguido de quedas.")],
    [("card", "ONDE CAIU MAIS", "Nas capitais de distrito: Funchal -33%, Porto -21% e Viana do Castelo -17%.")],
    [("card", "ONDE SUBIU", "Vila Real +34%, Guarda +25% e Bragança +18%. Setúbal e Braga ficaram estáveis.")],
    END("Compara a tua zona."),
]),
    "Oferta de casas à venda: -4% no verão",
    ["Oferta de casas à venda cai 4%.", "Foi o 7.º trimestre seguido de quedas, entre junho e agosto de 2026.", "Nas capitais de distrito, caiu no Funchal (-33%), no Porto (-21%) e em Viana do Castelo (-17%).", "Subiu em Vila Real (+34%), na Guarda (+25%) e em Bragança (+18%).", "Há grandes diferenças entre zonas.", "Guarda este carrossel."],
    "idealista/news (15/10/2026), via Info Imobiliária.", H("mercadoimobiliário", "oferta", "idealista", "imobiliário", "infoimobiliária"), leg=False)
reg("20261125i", I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «O que é o AIMI», com a Caixa Geral de Depósitos. Regras de outubro de 2026.", [
    ("h", "AIMI: a partir de que valor?", 78), ("num", "600 000 €", 130),
    ("pn", "VPT total dos imóveis de uma pessoa singular. Abaixo disto, não há AIMI.", 44), ("p", "Casal em tributação conjunta: 1 200 000 €. Paga-se em setembro.", 38)]),
    "AIMI: acima de 600 000 €",
    ["600 000 €.", "É o VPT total dos imóveis a partir do qual uma pessoa singular paga AIMI.", "Abaixo disso, não há AIMI.", "Casal em tributação conjunta: 1 200 000 €.", "Paga-se em setembro."],
    "Info Imobiliária, «AIMI: quem paga o adicional ao IMI».", H("AIMI", "IMI", "impostos", "imobiliário", "infoimobiliária"))

# ================= QUI 26 =================
reg("20261126v1", V("Checklist", "CHECKLIST · CASA E VIDA", "Informação geral. Fonte: idealista/news e Cofidis. Para obras, consulta um especialista.", [
    [("h", "Casa mais quente sem obras", 88)],
    [("chk", "Deixa entrar o sol de dia e fecha ao fim da tarde"), ("chk", "Veda as frinchas de portas e janelas"), ("chk", "Isola a caixa dos estores")],
    [("chk", "Usa tecidos grossos nas cortinas"), ("chk", "Fecha as portas das divisões sem uso"), ("chk", "Ventila pouco tempo, de cada vez")],
    [("card", "TEMPERATURA DE CONFORTO", "Entre 18 ºC e 21 ºC em casa e 16 ºC a 20 ºC nos quartos.")],
], ("Mais conforto, sem obras.", "Casa mais quente no inverno")),
    "Casa mais quente no inverno sem obras",
    ["Casa mais quente no inverno, sem obras.", "Deixa entrar o sol de dia e fecha ao fim da tarde.", "Veda as frinchas e isola a caixa dos estores.", "Usa cortinas grossas e fecha as portas das divisões sem uso.", "Ventila pouco tempo, de cada vez.", "Temperatura de conforto: 18 ºC a 21 ºC em casa e 16 ºC a 20 ºC nos quartos."],
    "idealista/news e Cofidis, via Info Imobiliária.", H("casaquente", "inverno", "dicasdecasa", "casaevida", "infoimobiliária"), "Casa mais quente no inverno sem obras", leg=False)
reg("20261126v2", V("Conta", "A CONTA DA SEMANA · IMPOSTOS", "Exemplo calculado. Casa de 250 000 € no Continente, tabela de 2026, só IMT.", [
    [("h", "IMT: casa própria ou segunda casa?", 80), ("p", "A mesma casa de 250 000 €.", 44)],
    [("card", "HABITAÇÃO PRÓPRIA E PERMANENTE", "250 000 € × 7% menos 10 457,96 €: IMT de 7 042,04 €.")],
    [("card", "SEGUNDA HABITAÇÃO OU ARRENDAR", "250 000 € × 7% menos 9 394,50 €: IMT de 8 105,50 €.")],
    [("num", "+1 063,46 €", 120), ("p", "de IMT, só por não ser habitação própria e permanente.", 42)],
], ("Faz a tua conta.", "Calculadora do IMT")),
    "IMT numa segunda casa: quanto a mais?",
    ["Casa de 250 000 € no Continente, tabela de IMT de 2026.", "Habitação própria e permanente: IMT de 7 042,04 €.", "Segunda habitação ou casa para arrendar: IMT de 8 105,50 €.", "São 1 063,46 € a mais.", "O Imposto do Selo de 0,8% é igual nos dois casos."],
    "Info Imobiliária, «Tabela do IMT 2026» (Ofício Circulado n.º 40129/2026 da AT). Exemplo calculado por nós.", H("IMT", "segundahabitação", "comprarcasa", "imobiliário", "infoimobiliária"), "IMT: casa própria ou segunda casa? A diferença em 250 000 €")
reg("20261126v3", V("A ou B", "EXCLUSIVA OU ABERTA · VENDER", "Informação geral. A comissão varia: não há regra fixa.", [
    [("h", "Mediação exclusiva ou aberta?", 84), ("p", "Vais vender com agente.", 44)],
    [("card", "EXCLUSIVA", "Um agente, durante um período definido. Garante a comissão, por isso costuma investir mais na promoção. Ponto de contacto único.")],
    [("card", "ABERTA", "Várias agências ao mesmo tempo. Menos investimento por agência e risco de anúncios com preços e fotos diferentes.")],
    [("pn", "Para a maioria das vendas, a exclusiva tende a dar melhor resultado. Vender sozinho também é possível.", 42)],
], ("Escolhe com informação.", "Mediação exclusiva ou aberta")),
    "Mediação exclusiva ou aberta: qual escolher?",
    ["Mediação exclusiva: um agente, durante um período definido.", "Mediação aberta: várias agências ao mesmo tempo.", "Na aberta, há risco de anúncios com preços e fotos diferentes.", "Para a maioria das vendas, a exclusiva tende a dar melhor resultado.", "A comissão varia: não há regra fixa."],
    "Info Imobiliária, «Mediação exclusiva ou mediação aberta: qual escolher».", H("vendercasa", "mediação", "agenteimobiliário", "imobiliário", "infoimobiliária"), "Mediação exclusiva ou aberta: qual escolher ao vender casa?")
reg("20261126c", C("Guia", "GUIA · CRÉDITO", "BAIXAR A TAXA DE ESFORÇO", "Fonte: Info Imobiliária, «Taxa de esforço». Limite de 45% desde 1 de agosto de 2026.", [
    [("h", "Como baixar a tua taxa de esforço", 78), ("p", "Antes de pedir o crédito da casa.", 44)],
    [("card", "OS CRÉDITOS PEQUENOS", "Paga os créditos pequenos antes e cancela os cartões de crédito que não usas.")],
    [("card", "A ENTRADA", "Aumenta a entrada para pedir menos ao banco, ou junta um segundo proponente.")],
    [("card", "O PRAZO E A TAXA", "Alargar o prazo baixa a prestação, mas paga-se mais juros. Uma taxa fixa não sofre o acréscimo do teste de stress.")],
    END("Simula a tua prestação."),
]),
    "Como baixar a taxa de esforço",
    ["Como baixar a tua taxa de esforço antes de pedir o crédito.", "Paga os créditos pequenos e cancela os cartões de crédito que não usas.", "Aumenta a entrada para pedir menos ao banco, ou junta um segundo proponente.", "Alargar o prazo baixa a prestação, mas pagas mais juros no total.", "Uma taxa fixa não sofre o acréscimo do teste de stress.", "Guarda este carrossel."],
    "Info Imobiliária, «Taxa de esforço: quanto o banco te deixa gastar».", H("taxadeesforço", "créditohabitação", "comprarcasa", "imobiliário", "infoimobiliária"), leg=False)
reg("20261126i", I("Dado", "O DADO · CASA E VIDA", "Fonte: Cofidis e referências citadas pela Info Imobiliária, «Casa mais quente no inverno».", [
    ("h", "Temperatura de conforto em casa", 76), ("num", "18 a 21 ºC", 130),
    ("pn", "Nas divisões de estar. Nos quartos, 16 a 20 ºC.", 46), ("p", "Antes de gastares mais em aquecimento, resolve as perdas de calor.", 38)]),
    "Temperatura de conforto: 18 a 21 ºC",
    ["18 ºC a 21 ºC.", "É a temperatura de conforto em casa. Nos quartos, 16 ºC a 20 ºC.", "Antes de gastares mais em aquecimento, resolve as perdas de calor.", "As primeiras medidas custam pouco ou nada."],
    "Cofidis, via Info Imobiliária.", H("casaquente", "inverno", "casaevida", "dicasdecasa", "infoimobiliária"), leg=False)

# ================= SEX 27 =================
reg("20261127v1", V("Notícia", "O QUE MUDA · GARANTIA PÚBLICA", "Fonte: ECO, 22/10/2026, e Lusa/DNoticias, 2/9/2026.", [
    [("h", "Garantia pública: bancos a esgotar quotas", 76), ("p", "Para jovens até 35 anos.", 44)],
    [("card", "O BANKINTER", "Usou cerca de 45 dos 60 milhões atribuídos: cerca de 75% da quota.")],
    [("card", "O REFORÇO", "A 2 de setembro, o Diário da República reforçou o plafond em 100 milhões: 40 milhões para o Novo Banco e 60 para o Montepio.")],
    [("card", "ATÉ QUANDO", "A garantia cobre contratos assinados até ao final de 2026. Para 2027, ainda depende do Orçamento.")],
    [("pn", "Pergunta ao teu banco se ainda tem quota.", 50)],
], ("Vê se tens direito.", "Garantia pública para jovens")),
    "Garantia pública: bancos a esgotar quotas",
    ["O Bankinter já usou cerca de 45 dos 60 milhões atribuídos para a garantia pública: cerca de 75% da quota.", "A 2 de setembro, o plafond foi reforçado em 100 milhões: 40 milhões para o Novo Banco e 60 milhões para o Montepio.", "A garantia cobre contratos assinados até ao final de 2026.", "Para 2027, ainda depende do Orçamento do Estado.", "Pergunta ao teu banco se ainda tem quota."],
    "ECO (22/10/2026) e Lusa/DNoticias (2/9/2026), via Info Imobiliária.", H("garantiapública", "jovens", "créditohabitação", "imobiliário", "infoimobiliária"), "Garantia pública para jovens: bancos a esgotar as quotas")
reg("20261127v2", V("Glossário", "GLOSSÁRIO · IMPOSTOS", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Habitação própria e permanente", 70), ("p", "O que significa para a lei fiscal.", 44)],
    [("card", "O QUE É", "A casa onde moras e que é a tua morada fiscal. Não é segunda habitação, casa de férias ou investimento para arrendar.")],
    [("card", "PORQUE IMPORTA", "No IMT há uma tabela própria. No crédito, o financiamento máximo costuma ser mais alto. Nas mais-valias, há benefícios se reinvestires.")],
    [("card", "ATENÇÃO", "Se deixares de a usar como habitação própria e permanente, podem mudar as regras que te beneficiaram.")],
], ("Percebe os teus benefícios.", "Glossário imobiliário")),
    "Habitação própria e permanente: o que significa",
    ["Habitação própria e permanente: a casa onde moras e que é a tua morada fiscal.", "Não é segunda habitação, casa de férias ou investimento para arrendar.", "No IMT há uma tabela própria.", "No crédito, o financiamento máximo costuma ser mais alto.", "Se deixares de a usar como tal, podem mudar as regras que te beneficiaram."],
    "Info Imobiliária, «Habitação própria e permanente: o que significa».", H("habitaçãopróprio", "IMT", "créditohabitação", "imobiliário", "infoimobiliária"), "Habitação própria e permanente: o que significa")
reg("20261127v3", V("Erro comum", "ERRO COMUM · VENDER", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Anunciar a casa sem certificado energético", 78)],
    [("card", "O ERRO", "Deixar o certificado para depois de ter comprador.")],
    [("card", "A REGRA", "É exigido na venda, no arrendamento e na publicidade: o anúncio deve indicar a classe.")],
    [("card", "O PRAZO", "Em regra, vale 10 anos na habitação. É emitido por um perito qualificado.")],
    [("pn", "Trata dele cedo: alguns peritos demoram.", 52)],
], ("Vende com tudo pronto.", "Certificado energético")),
    "Erro comum: anunciar a casa sem certificado energético",
    ["Erro comum: deixar o certificado energético para depois de ter comprador.", "É exigido na venda, no arrendamento e na publicidade.", "O anúncio deve indicar a classe.", "Em regra, vale 10 anos na habitação e é emitido por um perito qualificado.", "Trata dele cedo, porque alguns peritos demoram."],
    "Info Imobiliária, «Certificado energético: classes e quando é obrigatório».", H("certificadoenergético", "vendercasa", "anúncio", "imobiliário", "infoimobiliária"), "Erro comum: anunciar a casa sem certificado energético")
reg("20261127c", C("Guia", "GUIA · VENDER", "7 DICAS PARA VENDER", "Fonte: Info Imobiliária, «7 dicas para vender casa mais rápido».", [
    [("h", "7 dicas para vender casa mais rápido", 78), ("p", "Pensa como quem vai visitar.", 44)],
    [("card", "1 E 2. VISITAS E PRIMEIRA IMPRESSÃO", "Facilita as visitas, ao fim de semana ou ao fim do dia. Cuida da entrada e da primeira divisão.")],
    [("card", "3 E 4. ESPAÇO E BENEFÍCIOS", "Livra-te do excesso de coisas e mostra os benefícios da casa, não só as medidas.")],
    [("card", "5, 6 E 7. LUZ, INSPEÇÃO E DOCUMENTOS", "Luz na entrada, cozinha e quartos. Inspeção prévia. Caderneta, certificado energético, licença de utilização e certidão permanente prontos.")],
    END("Prepara a venda."),
]),
    "7 dicas para vender casa mais rápido",
    ["7 dicas para vender casa mais rápido.", "Facilita as visitas, ao fim de semana ou ao fim do dia.", "Cuida da primeira impressão e livra-te do excesso de coisas.", "Mostra os benefícios da casa, não só as medidas.", "Aposta na luz e faz uma inspeção prévia.", "Tem os documentos prontos: caderneta, certificado energético, licença de utilização e certidão permanente.", "Guarda este carrossel."],
    "Info Imobiliária, «7 dicas para vender casa mais rápido».", H("vendercasa", "dicas", "homestaging", "imobiliário", "infoimobiliária"), leg=False)
reg("20261127i", I("Dado", "O DADO · CRÉDITO", "Fonte: Info Imobiliária, «Como vender casa, passo a passo», com a Caixa Geral de Depósitos.", [
    ("h", "Amortizar antes do tempo: o limite da comissão", 66), ("pair", ("TAXA VARIÁVEL", "0,5%"), ("TAXA FIXA", "2%")),
    ("pn", "Máximo da comissão de reembolso antecipado, sobre o capital em dívida.", 44), ("p", "Pergunta ao banco quanto vais pagar antes de amortizares.", 38)]),
    "Comissão de reembolso antecipado: 0,5% e 2%",
    ["Amortizar o crédito antes do tempo: a comissão tem limite.", "Taxa variável: máximo de 0,5% do capital em dívida.", "Taxa fixa: máximo de 2%.", "Pergunta ao banco quanto vais pagar antes de amortizares."],
    "Info Imobiliária, «Como vender casa, passo a passo», com a Caixa Geral de Depósitos.", H("amortização", "créditohabitação", "comissões", "imobiliário", "infoimobiliária"))

# ================= SÁB 28 =================
reg("20261128v1", V("Notícia", "O QUE MUDA · IRS E RENDAS", "Fonte: DECO Proteste, 1/6/2026, via Info Imobiliária, «Arrendar ou comprar».", [
    [("h", "Inquilino: deduzir a renda no IRS", 78), ("p", "O que diz a DECO Proteste.", 44)],
    [("card", "A DEDUÇÃO", "15% da renda anual paga, com limite.")],
    [("pair", ("EM 2026", "900 €"), ("EM 2027", "1 000 €")), ("p", "Limite da dedução, segundo a DECO Proteste.", 42)],
    [("card", "NO ORÇAMENTO 2027", "Há ainda uma proposta de IRS mais baixo para rendas moderadas. Está por votar.")],
    [("pn", "Confirma o teu caso no IRS.", 52)],
], ("Compara arrendar e comprar.", "Calculadora arrendar ou comprar")),
    "Inquilinos: dedução da renda no IRS",
    ["Se és inquilino, podes deduzir 15% da renda anual paga no IRS, com limite.", "O limite é de 900 € em 2026 e de 1 000 € em 2027, segundo a DECO Proteste.", "A proposta de IRS mais baixo para rendas moderadas, no Orçamento do Estado para 2027, ainda está por votar.", "Confirma o teu caso no IRS."],
    "DECO Proteste (1/6/2026), via Info Imobiliária.", H("IRS", "arrendamento", "inquilinos", "imobiliário", "infoimobiliária"), "Inquilinos: deduzir a renda no IRS, até 900 € em 2026")
reg("20261128v2", V("Conta", "A CONTA DA SEMANA · ARRENDAR", "Exemplo calculado. Rendas hipotéticas, aumento de 2,56% aplicado uma só vez.", [
    [("h", "Quanto sobe a renda em 2027?", 84), ("p", "Com o coeficiente de 2,56%.", 44)],
    [("card", "RENDA DE 750 €", "Passa para 769,20 €. São 19,20 € a mais por mês.")],
    [("card", "RENDA DE 1 000 €", "Passa para 1 025,60 €. São 25,60 € a mais por mês, ou 307,20 € por ano.")],
    [("pn", "O senhorio decide se aplica e tem de avisar por escrito com 30 dias de antecedência.", 44)],
], ("Faz a tua conta.", "Calculadora arrendar ou comprar")),
    "Renda de 750 € ou 1 000 €: quanto sobe em 2027?",
    ["Exemplo com o coeficiente de 2,56%, aplicado uma só vez.", "Renda de 750 €: passa para 769,20 €, mais 19,20 € por mês.", "Renda de 1 000 €: passa para 1 025,60 €, mais 25,60 € por mês, ou 307,20 € por ano.", "O senhorio decide se aplica e tem de avisar por escrito com 30 dias de antecedência."],
    "Info Imobiliária, «Rendas em 2027», com ECO e DECO Proteste. Exemplo calculado por nós, com rendas hipotéticas.", H("arrendamento", "rendas2027", "inquilinos", "senhorios", "infoimobiliária"), "Quanto sobe uma renda de 750 € ou de 1 000 € em 2027?")
reg("20261128v3", V("Passo a passo", "PASSO A PASSO · MUDAR DE CASA", "Informação geral. Fonte: gov.pt e Info Imobiliária, «Como alterar a morada fiscal».", [
    [("h", "Como alterar a morada fiscal", 84), ("p", "Sem perder a isenção de IMI.", 44)],
    [("card", "1. CARTÃO DE CIDADÃO", "Altera a morada no gov.pt, num Espaço Cidadão ou num balcão dos Registos.")],
    [("card", "2. O CÓDIGO", "Espera a carta com o código na morada nova e confirma-o. Sem isso, a morada não muda.")],
    [("card", "3. CONFIRMA NAS FINANÇAS", "Alguns dias depois, vê no Portal das Finanças. Tens 6 meses após a compra para fixar a morada fiscal.")],
], ("Muda sem perder benefícios.", "Mudar de casa: o que tratar")),
    "Como alterar a morada fiscal sem perder a isenção de IMI",
    ["Como alterar a morada fiscal, passo a passo.", "1. Altera a morada do Cartão de Cidadão.", "2. Espera a carta com o código na morada nova e confirma-o.", "3. Confirma no Portal das Finanças alguns dias depois.", "Para a isenção de IMI, tens 6 meses após a compra para fixar a morada fiscal."],
    "gov.pt e Info Imobiliária, «Como alterar a morada fiscal sem perder a isenção de IMI».", H("moradafiscal", "IMI", "mudardecasa", "imobiliário", "infoimobiliária"), "Como alterar a morada fiscal sem perder a isenção de IMI")
reg("20261128c", C("Guia", "GUIA · COMPRAR", "O DIA DA ESCRITURA", "Fonte: Info Imobiliária, «Escritura de compra de casa», com DECO Proteste, idealista e CGD. Valores sem impostos.", [
    [("h", "Escritura: o que levar e o que pagar", 76), ("p", "Para chegares preparado.", 44)],
    [("card", "O QUE LEVAR", "Identificação, comprovativos do IMT e do Selo, caderneta predial, licença de utilização, certidão permanente e, se houver, o distrate da hipoteca.")],
    [("card", "O QUE PAGAS", "Registo predial da compra: 225 € online ou 250 € ao balcão. Declaração de direito de preferência: 15 €.")],
    [("card", "DEPOIS", "O registo na conservatória costuma ficar tratado cerca de 30 dias após a escritura.")],
    END("Lê o guia completo."),
]),
    "Escritura: o que levar e o que pagar",
    ["Escritura de compra de casa: o que levar e o que pagar.", "Leva identificação, comprovativos do IMT e do Selo, caderneta predial, licença de utilização e certidão permanente.", "Se houver hipoteca, o distrate.", "Registo predial da compra: 225 € online ou 250 € ao balcão.", "Declaração de direito de preferência: 15 €.", "Guarda este carrossel."],
    "Info Imobiliária, «Escritura de compra de casa», com DECO Proteste, idealista e Caixa Geral de Depósitos. Valores sem impostos.", H("escritura", "comprarcasa", "documentos", "imobiliário", "infoimobiliária"))
reg("20261128i", I("Dado", "O DADO · DOCUMENTOS", "Fonte: Info Imobiliária, «Caderneta predial e VPT», com Portal da Literacia Financeira.", [
    ("h", "Caderneta predial online", 80), ("num", "12 meses", 120),
    ("pn", "É a validade da caderneta. Pede-se grátis no Portal das Finanças.", 44), ("p", "Só o titular ou um representante a pode pedir. O PDF gera-se na hora.", 38)]),
    "Caderneta predial: grátis e válida 12 meses",
    ["12 meses.", "É a validade da caderneta predial.", "Pede-se grátis no Portal das Finanças e o PDF gera-se na hora.", "Só o titular ou um representante a pode pedir."],
    "Info Imobiliária, «Caderneta predial e VPT», com Portal da Literacia Financeira.", H("cadernetapredial", "VPT", "documentos", "imobiliário", "infoimobiliária"))

# ================= DOM 29 =================
reg("20261129v1", V("Notícia", "O QUE MUDA · MAIS-VALIAS", "Fonte: Portaria n.º 457/2026/1 (15/10/2026) e idealista/news, 16/10/2026.", [
    [("h", "Mais-valias em 2026: os coeficientes", 78), ("p", "Para quem vende este ano.", 44)],
    [("card", "COMO SE ESCOLHE", "Pelo ano em que compraste, não pelo da venda.")],
    [("pair", ("COMPRA EM 2025", "1,00"), ("COMPRA EM 2022", "1,08")), ("pair", ("COMPRA EM 2021", "1,19"), ("DE 2018 A 2020", "1,20"))],
    [("card", "EXEMPLO", "Comprada em 2019 por 200 000 €: o valor de compra passa a 240 000 €.")],
    [("pn", "Segundo as fontes, só com pelo menos dois anos entre a compra e a venda.", 44)],
], ("Faz a tua conta.", "Calculadora de mais-valias")),
    "Mais-valias em 2026: coeficientes de correção",
    ["A Portaria n.º 457/2026/1 fixou os coeficientes para quem vende em 2026.", "Escolhe-se pelo ano da compra.", "Compra em 2025: 1,00. Compra em 2022: 1,08.", "Compra em 2021: 1,19. De 2018 a 2020: 1,20.", "Exemplo: casa comprada em 2019 por 200 000 € passa a contar 240 000 €.", "Segundo as fontes, só se aplica com pelo menos dois anos entre a compra e a venda.", "O IRS final depende dos teus outros rendimentos."],
    "Portaria n.º 457/2026/1 (Diário da República, 15/10/2026) e idealista/news (16/10/2026). Exemplo calculado por nós.", H("maisvalias", "vendercasa", "IRS", "imobiliário", "infoimobiliária"), "Mais-valias em 2026: os coeficientes de correção para quem vende")
reg("20261129v2", V("Conta", "A CONTA DA SEMANA · VENDER", "Exemplo hipotético. Comissão de 5% mais IVA, que é dedutível nas mais-valias.", [
    [("h", "Quanto custa vender com mediador?", 80), ("p", "Casa vendida por 250 000 €.", 44)],
    [("card", "A COMISSÃO", "Costuma rondar 5% mais IVA. Sobre 250 000 €, 5% são 12 500 €, antes de IVA.")],
    [("card", "A MAIS-VALIA", "A comissão do mediador é uma despesa que podes descontar no cálculo da mais-valia.")],
    [("pn", "Guarda a fatura, em teu nome.", 54)],
], ("Faz a conta da venda.", "Calculadora de mais-valias")),
    "Quanto custa vender com mediador?",
    ["Casa vendida por 250 000 €, com mediador.", "A comissão costuma rondar 5% mais IVA.", "Sobre 250 000 €, 5% são 12 500 €, antes de IVA.", "A comissão é uma despesa que podes descontar no cálculo da mais-valia.", "Guarda a fatura, em teu nome."],
    "Info Imobiliária, «Como vender casa, passo a passo», com a Caixa Geral de Depósitos. Exemplo calculado por nós.", H("vendercasa", "mediador", "maisvalias", "imobiliário", "infoimobiliária"), "Quanto custa vender casa com mediador?")
reg("20261129v3", V("Erro comum", "ERRO COMUM · IRS", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Vender a casa e não declarar no IRS", 78)],
    [("card", "O ERRO", "Achar que, se a mais-valia está isenta, não há nada a declarar.")],
    [("card", "A REGRA", "A venda declara-se no IRS do ano seguinte, no anexo G, mesmo se estiver isenta.")],
    [("card", "ANTES DE 1989", "Casas compradas antes de 1 de janeiro de 1989 não pagam imposto, mas declaram-se no anexo G1.")],
    [("pn", "Guarda a escritura e as faturas.", 52)],
], ("Declara a venda.", "Como vender casa, passo a passo")),
    "Erro comum: não declarar a venda da casa no IRS",
    ["Erro comum: achar que, se a mais-valia está isenta, não há nada a declarar.", "A venda declara-se no IRS do ano seguinte, no anexo G, mesmo se estiver isenta.", "Casas compradas antes de 1 de janeiro de 1989 não pagam imposto, mas declaram-se no anexo G1.", "Guarda a escritura e as faturas."],
    "Info Imobiliária, «Mais-valias na venda de casa: como se calculam» e «Como vender casa, passo a passo».", H("maisvalias", "IRS", "vendercasa", "imobiliário", "infoimobiliária"), "Erro comum: vender a casa e não declarar no IRS")
reg("20261129c", C("Guia", "GUIA · IMPOSTOS", "O IMI", "Fonte: Info Imobiliária, «Tabela do IMI em 2026». Taxas fixadas por cada município.", [
    [("h", "IMI: como se calcula e quando se paga", 74), ("p", "Em 3 passos.", 44)],
    [("card", "O CÁLCULO", "VPT × taxa do município. Nos prédios urbanos, a taxa fica entre 0,3% e 0,45%.")],
    [("card", "QUANDO SE PAGA", "Até 100 €: uma prestação, em maio. De 100 € a 500 €: maio e novembro. Acima de 500 €: maio, agosto e novembro.")],
    [("card", "ISENÇÕES", "Há duas: habitação própria e permanente (VPT até 125 000 €) e famílias de baixo rendimento. Confirma no Portal das Finanças.")],
    END("Vê a tabela completa."),
]),
    "IMI: como se calcula e quando se paga",
    ["IMI: como se calcula e quando se paga.", "Cálculo: VPT × taxa do município, entre 0,3% e 0,45% nos prédios urbanos.", "Até 100 €: uma prestação, em maio.", "De 100 € a 500 €: maio e novembro.", "Acima de 500 €: maio, agosto e novembro.", "Guarda este carrossel."],
    "Info Imobiliária, «Tabela do IMI em 2026».", H("IMI", "impostos", "VPT", "imobiliário", "infoimobiliária"), leg=False)
reg("20261129i", I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «Tabela do IMI em 2026». Taxa fixada por cada município.", [
    ("h", "Taxa de IMI nos prédios urbanos", 74), ("num", "0,3% a 0,45%", 110),
    ("pn", "Do VPT, todos os anos. Cada município fixa a sua taxa.", 46), ("p", "O IMI calcula-se assim: VPT × taxa do município.", 38)]),
    "IMI: de 0,3% a 0,45%",
    ["0,3% a 0,45%.", "É a taxa de IMI nos prédios urbanos, fixada por cada município.", "O IMI calcula-se assim: VPT × taxa.", "Confirma a taxa do teu município."],
    "Info Imobiliária, «Tabela do IMI em 2026».", H("IMI", "VPT", "impostos", "imobiliário", "infoimobiliária"))

# ---------- horas de Lisboa (v1, v2, v3, c, i); em novembro Lisboa = UTC ----------
T = {17: ("09:30", "13:30", "19:45", "11:15", "16:45"), 18: ("10:15", "14:15", "20:15", "15:30", "17:15"),
     19: ("09:00", "13:00", "19:30", "12:00", "16:00"), 20: ("11:00", "14:30", "20:45", "10:45", "15:45"),
     21: ("09:45", "13:45", "19:00", "12:30", "17:30"), 22: ("10:30", "14:00", "20:00", "11:30", "16:30"),
     23: ("09:15", "15:00", "19:15", "15:15", "17:00"), 24: ("10:00", "13:15", "20:30", "11:45", "16:15"),
     25: ("09:30", "14:45", "19:45", "10:30", "15:30"), 26: ("10:45", "13:30", "20:15", "15:45", "17:45"),
     27: ("09:00", "14:00", "19:00", "12:15", "16:45"), 28: ("11:15", "15:15", "20:45", "11:00", "17:15"),
     29: ("10:15", "13:45", "19:30", "12:00", "16:00")}
