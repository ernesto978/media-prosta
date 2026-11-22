# Info Imobiliária - 30/11 a 06/12/2026. Factos lidos no site a 22/11/2026 (artigos e páginas publicados); contas verificadas abaixo.
import datetime as dt, calendar
from zoneinfo import ZoneInfo
from modelos import V, C, I, END

pm = lambda P, t, n=360: (lambda r: P * r / (1 - (1 + r) ** -n))(t / 12)
fm = lambda v: f"{v:,.2f}".replace(",", " ").replace(".", ",")
# comissão
assert 250000 * .05 == 12500 and 12500 * .23 == 2875 and 12500 + 2875 == 15375 and 15375 / 2 == 7687.5 and 250000 - 15375 == 234625
# prestação (Euribor 12 meses de outubro 3,239% + spread 1%)
assert fm(pm(150000, .04239)) == "736,94" and fm(pm(150000, .04739)) == "781,48" and fm(pm(150000, .03739)) == "693,74"
assert fm(pm(150000, .04739) - pm(150000, .04239)) == "44,53" and fm(pm(150000, .04239) - pm(150000, .03739)) == "43,21"
assert round((pm(150000, .04739) - pm(150000, .04239)) * 12) == 534
# selo arrendamento
assert 650 * .1 == 65 and 800 * .1 == 80 and 950 * .1 == 95 and (850 - 800) * .1 == 5
# prazo de comunicação: início a 1/12/2026 -> fim do mês seguinte
assert dt.date(2027, 1, calendar.monthrange(2027, 1)[1]) == dt.date(2027, 1, 31)
# mais-valias (sem coeficiente)
assert 220000 - 150000 - 8000 == 62000 and 62000 * .5 == 31000
# IMI
assert 120000 * .003 == 360 and round(200000 * .0035, 2) == 700
# preço por m2
assert 240000 / 80 == 3000 and 270000 / 100 == 2700

D = {}
# ================= SEG 30/11 =================
D["20261130v1"] = V("Conta", "A CONTA DA SEMANA · VENDER", "Exemplo calculado. Comissão de 5% mais IVA de 23%.", [
    [("h", "Comissão da imobiliária: quanto custa?", 78), ("p", "Casa vendida por 250 000 €.", 46)],
    [("card", "5% MAIS IVA A 23%", "Comissão de 12 500 €. IVA de 2 875 €. Total de 15 375 €.")],
    [("card", "DIVIDIDA EM DOIS MOMENTOS", "Metade no CPCV e metade na escritura: 7 687,50 € em cada.")],
    [("card", "O QUE FICA", "Depois de pagares a comissão, ficam 234 625 € do preço de venda.")],
    [("pn", "5% é a média apontada pela DECO PROteste. A tua pode ser outra: lê o contrato.", 44)],
], ("Lê o contrato antes de assinar.", "Como vender casa, passo a passo"))
D["20261130v2"] = V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. 150 000 €, 30 anos, spread de 1%, sem seguros nem comissões.", [
    [("h", "Meio ponto na Euribor: quanto muda a prestação?", 72), ("p", "Crédito de 150 000 € a taxa variável.", 44)],
    [("card", "EURIBOR A 12 MESES DE 3,239%", "Com 1% de spread, a prestação é de cerca de 736,94 €.")],
    [("card", "SE SUBIR 0,5 PONTOS", "Cerca de 781,48 € por mês. São 44,53 € a mais, mais de 500 € por ano.")],
    [("card", "SE DESCER 0,5 PONTOS", "Cerca de 693,74 € por mês. São 43,21 € a menos.")],
    [("pn", "3,239% foi a média de outubro. O valor da tua próxima revisão ainda não se sabe.", 44)],
], ("Testa a tua prestação.", "Calculadora de crédito habitação"))
D["20261130v3"] = V("Checklist", "CHECKLIST · CASA E VIDA", "Informação geral. Para furar paredes ou pintar, confirma o contrato de arrendamento.", [
    [("h", "Sala pequena: ganha espaço sem obras", 78)],
    [("chk", "Mede antes de comprar móveis"), ("chk", "Usa cores claras nas paredes e nos tecidos grandes"), ("chk", "Põe um espelho em frente à janela")],
    [("chk", "Instala as cortinas do teto ao chão"), ("chk", "Aproveita a altura com prateleiras"), ("card", "MENOS É MAIS", "Guarda o que não usas em móveis com arrumação.")],
], ("Uma sala mais ampla.", "Mais dicas no site"))
D["20261130c"] = C("Guia", "GUIA · IMPOSTOS", "ISENÇÃO DE IMI: OS PRAZOS", "Fonte: Portal da Literacia Financeira, idealista/news e gov.pt. Informação geral.", [
    [("h", "Isenção de IMI: os prazos que não podes falhar", 72), ("p", "Na compra de casa para viver.", 46)],
    [("card", "6 MESES", "Para fixar a morada fiscal na casa, a contar da compra ou do fim das obras.")],
    [("card", "MAIS 60 DIAS", "Se a isenção não aparecer sozinha, ou se a casa foi construída, ampliada ou melhorada, entregas o pedido até 60 dias depois dos seis meses.")],
    [("card", "SE TE ATRASARES", "O pedido é aceite, mas a isenção só começa a contar no ano em que o fazes.")],
    END("Confirma no Portal das Finanças."),
])
D["20261130i"] = I("Dado", "O DADO · ARRENDAR", "Fonte: Autoridade Tributária, via Info Imobiliária. Exemplo calculado por nós.", [
    ("h", "Contrato de arrendamento: até quando comunicar?", 66), ("num", "31 jan 2027", 110),
    ("pn", "Contrato com início a 1 de dezembro de 2026: é o prazo do senhorio.", 44), ("p", "O prazo é o fim do mês seguinte ao do início. O dia dentro do mês não muda nada.", 38)])
# ================= TER 01/12 =================
D["20261201v1"] = V("Conta", "A CONTA DA SEMANA · ARRENDAR", "Exemplo calculado. Contrato habitacional, renda fixa e um só senhorio.", [
    [("h", "Imposto do Selo do arrendamento", 84), ("p", "10% do valor da renda mensal.", 46)],
    [("card", "RENDA DE 650 €", "Imposto do Selo de 65 €.")],
    [("card", "RENDA DE 800 €", "Imposto do Selo de 80 €.")],
    [("card", "RENDA DE 950 €", "Imposto do Selo de 95 €.")],
    [("pn", "Paga-se no mesmo prazo da comunicação do contrato: o fim do mês seguinte ao do início.", 44)],
], ("Vê o que pesa além da renda.", "Calculadora arrendar ou comprar"))
D["20261201v2"] = V("Passo a passo", "PASSO A PASSO · VENDER", "Informação geral. Podes pedir a opinião de um agente da tua zona.", [
    [("h", "Como definir o preço de venda da tua casa", 74)],
    [("card", "1. AFASTA-TE DA CASA", "O que gastaste e as tuas memórias valem pouco para quem compra. Gasto e valor de mercado são coisas diferentes.")],
    [("card", "2. COMPARA O MERCADO", "Vê casas parecidas, na mesma zona, que estão à venda ou se venderam há pouco.")],
    [("card", "3. JUNTA SERVIÇOS", "Documentos reunidos e ajuda com o crédito do comprador podem inclinar a balança.")],
], ("Vende com o preço certo.", "Como vender casa, passo a passo"))
D["20261201v3"] = V("Checklist", "CHECKLIST · PROCESSO", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "CPCV: o que confirmar antes de assinar", 76)],
    [("chk", "As assinaturas são reconhecidas presencialmente"), ("chk", "O contrato refere a licença de utilização ou de construção"), ("chk", "A área e a descrição batem certo com o registo")],
    [("chk", "O prazo da escritura é realista"), ("chk", "Móveis e equipamentos que entram no negócio ficam por escrito"), ("card", "ANTES DE ASSINAR", "Pede a um advogado ou solicitador que reveja as cláusulas de incumprimento.")],
], ("Assina com calma.", "Como comprar casa, passo a passo"))
D["20261201c"] = C("Guia", "GUIA · VENDER", "O CONTRATO DE MEDIAÇÃO", "Fonte: Lei n.º 15/2013 e Portaria n.º 228/2018. Informação geral.", [
    [("h", "Contrato de mediação imobiliária: o que tem de ter", 70), ("p", "Antes de assinares com uma imobiliária.", 46)],
    [("card", "TEM DE SER ESCRITO", "Sem forma escrita ou sem algum dos elementos obrigatórios, o contrato é nulo, mas a imobiliária não pode invocar essa nulidade.")],
    [("card", "O QUE TEM DE CONSTAR", "Características do imóvel com ónus e encargos, negócio visado, remuneração, forma de pagamento e IVA, seguro de responsabilidade civil e exclusividade, se acordada.")],
    [("card", "O PRAZO", "Se o contrato não disser nada, são seis meses. Pode renovar-se se ficar escrito. No modelo da portaria, a denúncia faz-se 10 dias antes do fim do prazo.")],
    END("Compara pelo menos duas propostas."),
])
D["20261201i"] = I("Dado", "O DADO · IMPOSTOS", "Fonte: Portal da Literacia Financeira e Info Imobiliária, «O que é o IMI».", [
    ("h", "Isenção de IMI: sem meio-termo", 80), ("num", "125 000 €", 120),
    ("pn", "É o VPT máximo na isenção temporária de 3 anos.", 44), ("p", "Com 125 001 € não há isenção parcial. Vê o VPT na caderneta predial.", 38)])
# ================= QUA 02/12 =================
D["20261202v1"] = V("Conta", "A CONTA DA SEMANA · VENDER", "Exemplo calculado, sem coeficiente de correção. Residente em Portugal.", [
    [("h", "Mais-valias: só metade entra no IRS", 80), ("p", "Se és residente em Portugal.", 46)],
    [("card", "O EXEMPLO", "Compraste por 150 000 €, vendes por 220 000 € e gastaste 8 000 € em despesas dedutíveis.")],
    [("card", "A MAIS-VALIA", "220 000 € − 150 000 € − 8 000 € = 62 000 €.")],
    [("card", "O QUE ENTRA NO IRS", "50% de 62 000 €: 31 000 €. Soma-se aos teus outros rendimentos.")],
    [("pn", "Com o coeficiente de correção, a mais-valia desce. A calculadora trata disso.", 44)],
], ("Faz a tua conta.", "Calculadora de mais-valias"))
D["20261202v2"] = V("Pergunta", "PERGUNTA DA SEMANA · ARRENDAR", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "O senhorio não comunicou o contrato às Finanças?", 72)],
    [("card", "QUEM COMUNICA", "O senhorio, até ao fim do mês seguinte ao do início do arrendamento.")],
    [("card", "O INQUILINO PODE", "Desde 1 de agosto de 2025, depois de o prazo do senhorio terminar, no Portal das Finanças.")],
    [("card", "O QUE PRECISAS", "Do contrato assinado, a anexar. Sem contrato escrito, não consegues.")],
], ("Pede o contrato por escrito.", "Calculadora arrendar ou comprar"))
D["20261202v3"] = V("Erro comum", "ERRO COMUM · VENDER", "Informação geral. Lê o teu contrato de mediação.", [
    [("h", "Deixar passar a data para terminar o contrato de mediação", 70)],
    [("card", "O ERRO", "Assinar e esquecer o prazo e a renovação automática.")],
    [("card", "O RISCO", "Se a data passar, o contrato continua em vigor.")],
    [("card", "O PRAZO", "Se nada disser, são seis meses. No modelo da portaria, a denúncia faz-se 10 dias antes do fim do prazo.")],
    [("card", "O QUE FAZER", "Marca a data no calendário no dia em que assinas.")],
], ("Controla os prazos.", "Como vender casa, passo a passo"))
D["20261202c"] = C("Guia", "GUIA · CASA E VIDA", "SALA PEQUENA: 8 IDEIAS", "Fonte: Planner 5D e Sienge, via Info Imobiliária. Informação geral.", [
    [("h", "Sala pequena: 8 ideias sem obras", 84), ("p", "Para um fim de semana.", 46)],
    [("card", "1. MEDE ANTES DE COMPRAR", "Móveis grandes demais deixam o espaço apertado."), ("card", "2. CORES CLARAS", "Branco, cinzento claro, bege e pastel refletem a luz."), ("card", "3. ESPELHOS", "Não aumentam a área, mas dão profundidade.")],
    [("card", "4. MÓVEIS MULTIFUNCIONAIS", "Sofá com chaise, mesa de centro com arrumação."), ("card", "5. APROVEITA A ALTURA", "Prateleiras suspensas e estantes altas."), ("card", "6. LUZ EM CAMADAS", "Luz natural, de teto e de apoio.")],
    [("card", "7. TAPETES E CORTINAS", "O tapete define zonas. Cortinas do teto ao chão dão altura."), ("card", "8. MENOS OBJETOS", "Móveis com arrumação integrada.")],
    END("Vais vender? Prepara a casa."),
])
D["20261202i"] = I("Dado", "O DADO · ARRENDAR", "Fonte: ECO (13/11/2026), via Info Imobiliária.", [
    ("h", "Casa de investidor com benefícios fiscais", 72), ("num", "20 dias", 130),
    ("pn", "É o aviso ao IHRU antes de vender um imóvel abrangido.", 44), ("p", "E é preciso despacho do ministro da Habitação. Sem a assunção do contrato na escritura, a venda é nula.", 36)])
# ================= QUI 03/12 =================
D["20261203v1"] = V("Conta", "A CONTA DA SEMANA · COMPRAR", "Exemplo hipotético. Valores inventados para ilustrar o cálculo.", [
    [("h", "Comparar casas: o preço por metro quadrado", 74), ("p", "O preço total engana.", 46)],
    [("card", "CASA A", "240 000 € e 80 m²: 3 000 € por m².")],
    [("card", "CASA B", "270 000 € e 100 m²: 2 700 € por m².")],
    [("card", "DEPOIS AJUSTA", "Estado de conservação, piso, exposição solar, garagem e ano de construção.")],
    [("pn", "Um anúncio parado há meses, sem mudar de preço, costuma estar acima do que o mercado aceita.", 44)],
], ("Compara com método.", "Como comprar casa, passo a passo"))
D["20261203v2"] = V("Glossário", "GLOSSÁRIO · IMPOSTOS", "Exemplos calculados por nós. Taxas de 0,3% e 0,35% (cada município escolhe).", [
    [("h", "IMI: quem paga e quando", 94), ("p", "O imposto anual de quem tem casa.", 46)],
    [("card", "QUEM PAGA", "Quem for dono da casa a 31 de dezembro desse ano. Quem arrenda não paga.")],
    [("card", "COMO SE CALCULA", "VPT × taxa do município. Com VPT de 120 000 € e 0,3%: 360 € por ano.")],
    [("card", "QUANDO SE PAGA", "Até 100 €, em maio. Entre 100 € e 500 €, em maio e novembro. Acima de 500 €, em maio, agosto e novembro.")],
    [("pn", "Com VPT de 200 000 € e 0,35%: 700 € por ano, em três prestações.", 44)],
], ("Vê o IMI no custo de ter casa.", "Calculadora arrendar ou comprar"))
D["20261203v3"] = V("Checklist", "CHECKLIST · VENDER", "Informação geral. Para negociar, pede ajuda a um agente da tua zona.", [
    [("h", "O teu agente imobiliário: sinais de alerta", 76)],
    [("chk", "Semanas sem visitas e sem nenhuma explicação"), ("chk", "Pressão para baixares o preço logo nos primeiros dias"), ("chk", "Dificuldade em saber quantas visitas houve")],
    [("chk", "Pouca clareza sobre exclusividade e duração"), ("chk", "És tu a perguntar sempre como está o processo"), ("card", "O QUE FAZER", "Fala com ele antes de o problema crescer. Se não confiares, procura outro agente a tempo.")],
], ("Acompanha a tua venda.", "Como vender casa, passo a passo"))
D["20261203c"] = C("Guia", "GUIA · ARRENDAR", "COMUNICAR O CONTRATO ÀS FINANÇAS", "Fonte: AT, CGD, DECO PROteste e Doutor Finanças. Informação geral.", [
    [("h", "Porque comunicar o contrato de arrendamento importa", 66), ("p", "Também para o inquilino.", 46)],
    [("card", "DEDUÇÃO NO IRS", "A dedução das rendas só é possível quando o contrato está comunicado."), ("card", "APOIOS À RENDA", "Segundo a DECO PROteste, o Porta 65 e o apoio extraordinário à renda dependem de um contrato declarado.")],
    [("card", "RECIBOS DE RENDA", "O senhorio que declara rendas na categoria F tem de os emitir, e só o pode fazer depois de o contrato ser comunicado."), ("card", "A COIMA", "Para o senhorio, entre 75 € e 3 750 €, segundo a CGD.")],
    [("card", "SE ÉS INQUILINO", "Pede o comprovativo da comunicação e confirma no Portal das Finanças se as rendas aparecem no teu NIF.")],
    END("Compara arrendar e comprar."),
])
D["20261203i"] = I("Dado", "O DADO · CRÉDITO", "Fonte: Info Imobiliária, «Euribor».", [
    ("h", "A Euribor muda todos os dias", 80), ("num", "Só na revisão", 96),
    ("pn", "É quando a tua prestação muda.", 46), ("p", "Entre revisões, a prestação mantém-se, mesmo que a Euribor mexa. Vê a data no contrato.", 38)])
# ================= SEX 04/12 =================
D["20261204v1"] = V("Conta", "A CONTA DA SEMANA · ARRENDAR", "Exemplo calculado. Renda hipotética de 800 €.", [
    [("h", "A renda sobe: o que comunicar às Finanças?", 74), ("p", "Renda de 800 € que passa para 850 €.", 44)],
    [("card", "O AUMENTO", "Tem de ser comunicado até ao fim do mês seguinte ao da alteração.")],
    [("card", "O IMPOSTO DO SELO", "10% do aumento, não da renda toda: 50 € × 10% = 5 €.")],
    [("card", "O FIM DO CONTRATO", "Também se comunica, no mesmo prazo.")],
], ("Mantém tudo em ordem.", "Calculadora arrendar ou comprar"))
D["20261204v2"] = V("Checklist", "CHECKLIST · VENDER", "Informação geral. Confirma com um contabilista certificado.", [
    [("h", "Mais-valias: que despesas podes deduzir?", 76)],
    [("chk", "Escritura e registo da compra"), ("chk", "IMT e Imposto do Selo da compra"), ("chk", "Comissão imobiliária da venda")],
    [("chk", "Certificado energético"), ("chk", "Obras de conservação com fatura dos últimos 12 anos"), ("card", "ATENÇÃO", "As faturas têm de estar no teu NIF e referir o imóvel. Sem fatura, não deduzes.")],
], ("Guarda as faturas.", "Calculadora de mais-valias"))
D["20261204v3"] = V("Checklist", "CHECKLIST · VENDER", "Informação geral. Nada substitui um bom preço.", [
    [("h", "Casa pronta a vender: o que ter reunido", 76)],
    [("chk", "Caderneta predial"), ("chk", "Certidão de registo"), ("chk", "Certificado energético")],
    [("chk", "Facilita o acesso a quem trata do crédito do comprador"), ("chk", "Decide se há eletrodomésticos incluídos no preço"), ("card", "PORQUÊ", "Entre duas casas parecidas e ao mesmo preço, isto costuma inclinar a balança.")],
], ("Vende sem atrasos.", "Como vender casa, passo a passo"))
D["20261204c"] = C("Guia", "GUIA · MERCADO", "4 NÚMEROS QUE NÃO COINCIDEM", "Fonte: idealista, INE, Doutor Finanças e AT, via Info Imobiliária.", [
    [("h", "Preço pedido, de venda, avaliação e VPT", 76), ("p", "Porque os números não coincidem.", 46)],
    [("card", "PREÇO PEDIDO", "O que os vendedores pedem nos anúncios. É o ponto de partida e o teto da negociação.")],
    [("card", "PREÇO DE VENDA", "O que se pagou nas transações, medido pelo INE. Mostra a tendência real do mercado.")],
    [("card", "AVALIAÇÃO BANCÁRIA", "A estimativa do perito do banco. Define o crédito que podes ter."), ("card", "VPT", "O valor fiscal, na caderneta predial. Serve para o IMI e o IMT.")],
    END("Simula o teu crédito."),
])
D["20261204i"] = I("Dado", "O DADO · VENDER", "Fonte: Info Imobiliária, «Comissão da imobiliária» (22/11/2026).", [
    ("h", "Imobiliária: confirma o seguro", 84), ("num", "150 000 €", 120),
    ("pn", "É o capital mínimo do seguro de responsabilidade civil exigido por lei.", 44), ("p", "O contrato de mediação tem de identificar o seguro. Confirma também a licença do IMPIC.", 38)])
# ================= SÁB 05/12 =================
D["20261205v1"] = V("Pergunta", "PERGUNTA DA SEMANA · VENDER", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Quando é devida a comissão da imobiliária?", 76)],
    [("card", "A REGRA", "Quando a venda se conclui. Sem venda, em regra, não há comissão.")],
    [("card", "NO CPCV", "Se o contrato de mediação o previr, é devida logo que o CPCV é celebrado.")],
    [("card", "COM EXCLUSIVIDADE", "Se a venda falhar por causa imputável a ti, a comissão acordada também é devida.")],
    [("card", "PREFERÊNCIA", "Se alguém exercer um direito legal de preferência, o direito à comissão não fica afastado.")],
], ("Lê a cláusula da remuneração.", "Como vender casa, passo a passo"))
D["20261205v2"] = V("Pergunta", "PERGUNTA DA SEMANA · VENDER", "Informação geral. Confirma com um contabilista certificado.", [
    [("h", "Vendeste uma casa herdada: como contam as mais-valias?", 70)],
    [("card", "A DATA DE COMPRA", "É a data da morte de quem deixou a casa.")],
    [("card", "O VALOR DE COMPRA", "É o que consta do Imposto do Selo.")],
    [("card", "A ISENÇÃO", "A isenção por reinvestimento aplica-se a quem vende a sua habitação própria e permanente. Numa casa herdada onde nunca viveste, normalmente não se aplica.")],
], ("Faz a tua conta.", "Calculadora de mais-valias"))
D["20261205v3"] = V("Glossário", "GLOSSÁRIO · CRÉDITO", "Informação geral. Confirma o indexante no teu contrato.", [
    [("h", "Euribor a 3, 6 ou 12 meses: qual conta?", 78)],
    [("card", "A DO TEU CONTRATO", "A do prazo de revisão da tua prestação. Se é revista de 6 em 6 meses, interessa-te a de 6 meses.")],
    [("card", "O QUE O BANCO FAZ", "Atualiza a taxa com a Euribor desse prazo e soma o spread.")],
    [("card", "EM AGOSTO", "A de 6 meses era o indexante de cerca de 40% dos créditos a taxa variável, a de 12 meses de 31% e a de 3 meses de 24%.")],
], ("Vê o teu contrato.", "Calculadora de crédito habitação"))
D["20261205c"] = C("Guia", "GUIA · VENDER", "O TEU AGENTE IMOBILIÁRIO", "Fonte: Info Imobiliária, «Como avaliar o trabalho do teu agente imobiliário».", [
    [("h", "Como avaliar o trabalho do teu agente", 76), ("p", "Quatro fases para acompanhar.", 46)],
    [("card", "1. O PREÇO", "Pede casas parecidas que se venderam há pouco na tua zona, não só as anunciadas."), ("card", "2. A PROMOÇÃO", "Pede o plano de marketing: fotografias, portais e como chega a compradores.")],
    [("card", "3. A NEGOCIAÇÃO", "Pergunta por negócios anteriores e por situações difíceis que resolveu."), ("card", "4. ATÉ À ESCRITURA", "Inspeções, avaliação, financiamento e documentos. Deve informar-te por iniciativa própria.")],
    [("card", "ANTES DE ASSINAR", "Lê os termos do contrato, sobretudo a exclusividade e a duração.")],
    END("Vende com acompanhamento."),
])
D["20261205i"] = I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «O que é o IMI».", [
    ("h", "Isenção temporária de IMI", 84), ("num", "3 anos", 140),
    ("pn", "Na compra de casa própria e permanente.", 46), ("p", "O município pode prolongá-la por mais 2 anos. Pode ser usada duas vezes por contribuinte ou agregado.", 36)])
# ================= DOM 06/12 =================
D["20261206v1"] = V("Glossário", "GLOSSÁRIO · IMPOSTOS", "Informação geral. Confirma com um contabilista certificado.", [
    [("h", "IMI ou IMT: qual é qual?", 100), ("p", "Dois impostos, duas regras.", 46)],
    [("card", "IMT", "Paga-se uma vez, quando compras.")],
    [("card", "IMI", "Paga-se todos os anos, enquanto fores dono. A receita vai para o município onde a casa fica.")],
    [("card", "E QUEM ARRENDA?", "Não paga IMI. É do proprietário, mesmo que a casa esteja arrendada.")],
], ("Faz as contas à compra.", "Calculadora de custos de aquisição"))
D["20261206v2"] = V("Notícia", "O QUE MUDA · ARRENDAR", "Fonte: ECO, 13/11/2026. Portaria 500/2026/1, em vigor desde 14/11.", [
    [("h", "Casas de investidores com benefícios fiscais", 76), ("p", "A venda passa a ter condições.", 46)],
    [("card", "O QUE SÃO", "Imóveis dos Contratos de Investimento para Arrendamento, criados pelo Decreto-Lei 97/2026.")],
    [("card", "O ÓNUS NO REGISTO", "Só podem ser vendidos por inteiro, a um comprador elegível que assuma o contrato.")],
    [("card", "O PROCEDIMENTO", "Aviso de 20 dias ao IHRU e despacho do ministro da Habitação. Sem a assunção na escritura, a venda é nula.")],
    [("pn", "Se vais comprar uma casa assim, confirma o ónus no registo.", 46)],
], ("Compra com tudo verificado.", "Como comprar casa, passo a passo"))
D["20261206v3"] = V("Erro comum", "ERRO COMUM · VENDER", "Informação geral. Pede a opinião de um agente da tua zona.", [
    [("h", "Preço da casa: os dois erros opostos", 78)],
    [("card", "COMEÇAR ALTO PARA NEGOCIAR", "A casa fica parada, perde quem procura nessa faixa e, quando baixas, parece que ninguém a quis.")],
    [("card", "BAIXAR POR PRESSA", "Sem estudo comparativo, podes deixar vários milhares de euros em cima da mesa.")],
    [("card", "O QUE FAZER", "Acerta no preço logo no início, com casas comparáveis.")],
], ("Define o preço com dados.", "Como vender casa, passo a passo"))
D["20261206c"] = C("Guia", "GUIA · VENDER", "OBRAS ANTES DE VENDER", "Fonte: Info Imobiliária, «Que obras valorizam a casa antes de vender».", [
    [("h", "Obras antes de vender: o que compensa", 76), ("p", "Cosméticas ou de fundo?", 46)],
    [("card", "COSMÉTICAS", "Pintura, chão, torneiras, puxadores, iluminação e portas interiores. Custam pouco e o retorno costuma compensar.")],
    [("card", "DE FUNDO", "Novo quarto ou suite, todas as janelas, cozinha de raiz, paredes abaixo. Para uma venda próxima, raramente compensam.")],
    [("card", "ANTES DE AVANÇAR", "Pede 2 ou 3 orçamentos, confirma se precisa de licença da câmara e repara primeiro fissuras e humidade.")],
    END("Vê como vender casa."),
])
D["20261206i"] = I("Dado", "O DADO · VENDER", "Fonte: Info Imobiliária, «Comissão da imobiliária» (Portaria n.º 228/2018).", [
    ("h", "Contrato de mediação sem prazo escrito", 72), ("num", "6 meses", 140),
    ("pn", "É a duração, se o contrato não disser nada.", 46), ("p", "Pode renovar-se se ficar escrito. Marca a data de denúncia no calendário.", 38)])

# ======================= LEGENDAS, HORAS E ASSUNTOS =======================
LEG = "Informação geral. Confirma com um advogado ou solicitador."
LINK = "infoimobiliaria.com\n(Link também na bio.)"
def cap(lines, fonte, tags, leg=True):
    t = "\n".join(lines) + "\n\n" + LINK + "\n\nFonte: " + fonte
    if leg: t += "\n" + LEG
    return t + "\n\nInfo Imobiliária, by OMNI\n\n" + " ".join("#" + x for x in tags)
SITE = "Info Imobiliária, "
M = {}
def m(k, assunto, titulo, lines, fonte, tags, leg=True): M[k] = dict(assunto=assunto, titulo=titulo, legenda=cap(lines, fonte, tags, leg), fonte=fonte)

m("20261130v1", "Comissão da imobiliária: 5% de 250 000 €", "Comissão da imobiliária: quanto custa vender com 5%?",
  ["Casa vendida por 250 000 € e comissão de 5% mais IVA a 23%.", "Comissão de 12 500 €, IVA de 2 875 € e total de 15 375 €.", "Se o contrato previr metade no CPCV e metade na escritura, são 7 687,50 € em cada momento.", "Depois de pagares a comissão, ficam 234 625 € do preço de venda.", "A DECO PROteste aponta 5% como média, mas o valor é o do contrato."],
  "Info Imobiliária, «Comissão da imobiliária: quanto se paga, quando e o que diz a lei» (22/11/2026), com DECO PROteste e Lei n.º 15/2013. Exemplo calculado por nós.", ["comissão", "vendercasa", "mediaçãoimobiliária", "imobiliário", "infoimobiliária"])
m("20261130v2", "Euribor: meio ponto muda a prestação", "Meio ponto na Euribor: quanto muda a prestação?",
  ["Crédito de 150 000 € a 30 anos, spread de 1% e Euribor a 12 meses de 3,239% (média de outubro).", "Prestação de cerca de 736,94 € por mês.", "Se a Euribor subir 0,5 pontos: cerca de 781,48 €, mais 44,53 € por mês.", "Se descer 0,5 pontos: cerca de 693,74 €, menos 43,21 € por mês.", "Meio ponto a mais são mais de 500 € por ano."],
  "Info Imobiliária, «Prestação da casa sobe em novembro...» (2/11/2026), com Lusa/DNoticias e ECO (30/10/2026). Exemplo calculado por nós, sem seguros nem comissões.", ["euribor", "créditohabitação", "prestação", "imobiliário", "infoimobiliária"], leg=False)
m("20261130v3", "Sala pequena: ganha espaço sem obras", "Sala pequena: como ganhar espaço sem obras",
  ["Sala pequena? Começa por aqui.", "Mede antes de comprar móveis.", "Usa cores claras nas paredes e nos tecidos grandes.", "Põe um espelho em frente à janela.", "Instala as cortinas do teto ao chão e aproveita a altura com prateleiras."],
  "Info Imobiliária, «Sala pequena: 8 ideias de decoração que não pedem obras», com Planner 5D e Sienge.", ["decoração", "salapequena", "casaevida", "dicasdecasa", "infoimobiliária"], leg=False)
m("20261130c", "Isenção de IMI: os prazos", None,
  ["Isenção de IMI: os prazos que não podes falhar.", "Tens 6 meses para fixar a morada fiscal na casa.", "Se a isenção não aparecer sozinha, ou se a casa foi construída, ampliada ou melhorada, tens mais 60 dias para o pedido.", "Se te atrasares, a isenção só começa a contar no ano em que o fazes.", "Guarda este carrossel."],
  "Info Imobiliária, «Isenção de IMI: quem não paga, durante quanto tempo e como pedir» (Portal da Literacia Financeira, idealista/news e gov.pt).", ["IMI", "isençãoIMI", "comprarcasa", "imobiliário", "infoimobiliária"])
m("20261130i", "Arrendamento: comunicar até 31 de janeiro", None,
  ["Contrato de arrendamento com início a 1 de dezembro de 2026: o senhorio tem até 31 de janeiro de 2027 para comunicar às Finanças.", "O prazo é o fim do mês seguinte ao do início.", "O dia dentro do mês não muda nada."],
  "Info Imobiliária, «Como comunicar o contrato de arrendamento às Finanças e até quando» (21/11/2026), com a AT. Exemplo calculado por nós.", ["arrendamento", "senhorios", "inquilinos", "imobiliário", "infoimobiliária"])
m("20261201v1", "Imposto do Selo do arrendamento: 10% da renda", "Imposto do Selo do arrendamento: quanto é?",
  ["O Imposto do Selo do arrendamento é de 10% da renda mensal.", "Renda de 650 €: 65 €.", "Renda de 800 €: 80 €.", "Renda de 950 €: 95 €.", "Paga-se no mesmo prazo da comunicação: o fim do mês seguinte ao do início."],
  "Info Imobiliária, «Como comunicar o contrato de arrendamento às Finanças e até quando» (21/11/2026), com a AT. Exemplo calculado por nós.", ["arrendamento", "impostodoselo", "senhorios", "imobiliário", "infoimobiliária"])
m("20261201v2", "Preço de venda em 3 passos", "Como definir o preço de venda da tua casa em 3 passos",
  ["Como definir o preço de venda da tua casa.", "1. Afasta-te da casa: o que gastaste e as tuas memórias valem pouco para quem compra.", "2. Compara o mercado: casas parecidas, na mesma zona, à venda ou vendidas há pouco.", "3. Junta serviços: documentos reunidos e ajuda com o crédito do comprador.", "Um preço certo atrai visitas e propostas."],
  "Info Imobiliária, «Como determinar o preço de venda da tua casa, em 3 passos».", ["vendercasa", "preçodevenda", "imobiliário", "dicas", "infoimobiliária"], leg=False)
m("20261201v3", "CPCV: o que confirmar antes de assinar", "CPCV: o que confirmar antes de assinar",
  ["CPCV: o que confirmar antes de assinar.", "As assinaturas são reconhecidas presencialmente.", "O contrato refere a licença de utilização ou de construção.", "A área e a descrição batem certo com o registo.", "O prazo da escritura é realista e o que entra no negócio ficou por escrito."],
  "Info Imobiliária, página «CPCV: o contrato-promessa de compra e venda».", ["CPCV", "comprarcasa", "escritura", "imobiliário", "infoimobiliária"])
m("20261201c", "Contrato de mediação: o que tem de ter", None,
  ["Contrato de mediação imobiliária: o que tem de ter.", "Tem de ser escrito, e a imobiliária não pode invocar a nulidade.", "Inclui o imóvel, a remuneração, o IVA, o seguro de responsabilidade civil e a exclusividade, se acordada.", "Se não disser nada sobre o prazo, são seis meses.", "Guarda este carrossel."],
  "Info Imobiliária, «Comissão da imobiliária» (22/11/2026), com Lei n.º 15/2013 (art. 16.º) e Portaria n.º 228/2018.", ["mediaçãoimobiliária", "vendercasa", "contrato", "imobiliário", "infoimobiliária"])
m("20261201i", "Isenção de IMI: VPT até 125 000 €", None,
  ["125 000 €.", "É o VPT máximo na isenção temporária de IMI de 3 anos.", "Com 125 001 € não há isenção parcial.", "O VPT está na caderneta predial."],
  "Info Imobiliária, «Isenção de IMI: quem não paga, durante quanto tempo e como pedir» (Portal da Literacia Financeira) e «O que é o IMI».", ["IMI", "VPT", "isençãoIMI", "imobiliário", "infoimobiliária"])
m("20261202v1", "Mais-valias: só 50% entra no IRS", "Mais-valias: só metade entra no IRS?",
  ["Se és residente em Portugal, só 50% da mais-valia entra no teu IRS.", "Exemplo: compra por 150 000 €, venda por 220 000 € e 8 000 € de despesas dedutíveis.", "A mais-valia é de 62 000 €.", "Entram no IRS 31 000 €, que se somam aos teus outros rendimentos.", "O imposto depende dos teus outros rendimentos."],
  "Info Imobiliária, página «O que são as mais-valias imobiliárias», com CRN Contabilidade. Exemplo calculado por nós, sem coeficiente de correção.", ["maisvalias", "IRS", "vendercasa", "imobiliário", "infoimobiliária"])
m("20261202v2", "Arrendamento: o inquilino pode comunicar o contrato", "Senhorio não comunicou o contrato de arrendamento? O que fazer",
  ["O senhorio não comunicou o contrato de arrendamento às Finanças?", "Quem comunica é o senhorio, até ao fim do mês seguinte ao do início.", "Desde 1 de agosto de 2025, o inquilino pode comunicar depois de esse prazo terminar.", "Tem de anexar o contrato assinado, no Portal das Finanças.", "Sem contrato escrito, não consegue."],
  "Info Imobiliária, «Como comunicar o contrato de arrendamento às Finanças e até quando» (21/11/2026), com DECO PROteste e Doutor Finanças.", ["arrendamento", "inquilinos", "senhorios", "finanças", "infoimobiliária"])
m("20261202v3", "Erro comum: deixar passar a data de denúncia da mediação", "Erro comum: deixar passar a data de denúncia do contrato de mediação",
  ["Erro comum: assinar o contrato de mediação e esquecer o prazo.", "Se o contrato não disser nada, a duração é de seis meses.", "Pode renovar-se automaticamente, se assim ficar escrito.", "No modelo da Portaria n.º 228/2018, a denúncia faz-se 10 dias antes do fim do prazo.", "Se a data passar, o contrato continua em vigor."],
  "Info Imobiliária, «Comissão da imobiliária» (22/11/2026), com a Portaria n.º 228/2018.", ["mediaçãoimobiliária", "vendercasa", "errocomum", "imobiliário", "infoimobiliária"])
m("20261202c", "Sala pequena: 8 ideias sem obras", None,
  ["Sala pequena: 8 ideias que não pedem obras.", "Mede antes de comprar e escolhe cores claras.", "Espelhos, móveis multifuncionais e prateleiras ajudam.", "Pensa a luz em camadas e usa cortinas do teto ao chão.", "Guarda este carrossel."],
  "Info Imobiliária, «Sala pequena: 8 ideias de decoração que não pedem obras», com Planner 5D e Sienge.", ["decoração", "salapequena", "casaevida", "dicasdecasa", "infoimobiliária"], leg=False)
m("20261202i", "Casas em CIA: aviso de 20 dias ao IHRU", None,
  ["20 dias.", "É o aviso ao IHRU antes de vender um imóvel dos Contratos de Investimento para Arrendamento.", "É preciso também despacho do ministro da Habitação.", "Sem a assunção do contrato na escritura, a venda é nula."],
  "ECO (13/11/2026) e Info Imobiliária, «Casas compradas com benefícios fiscais para arrendar: a venda passa a exigir autorização do Governo».", ["arrendamento", "habitação", "investimento", "imobiliário", "infoimobiliária"])
m("20261203v1", "Comparar casas pelo preço por m²", "Comparar casas: porque o preço por m² conta",
  ["O preço total engana. Compara o preço por metro quadrado.", "Casa A: 240 000 € e 80 m², ou 3 000 € por m².", "Casa B: 270 000 € e 100 m², ou 2 700 € por m².", "Depois ajusta pelo estado, piso, exposição solar, garagem e ano de construção.", "Um anúncio parado há meses costuma estar acima do que o mercado aceita."],
  "Info Imobiliária, «Como determinar o preço de venda da tua casa, em 3 passos». Exemplo hipotético calculado por nós.", ["comprarcasa", "preçopormetro", "vendercasa", "imobiliário", "infoimobiliária"], leg=False)
m("20261203v2", "IMI: quem paga e quando", "IMI: quem paga, quanto e quando",
  ["IMI: o imposto anual de quem tem casa.", "Paga quem for dono da casa a 31 de dezembro desse ano. Quem arrenda não paga.", "Calcula-se com VPT × taxa do município. VPT de 120 000 € a 0,3%: 360 € por ano.", "Até 100 €, em maio. Entre 100 € e 500 €, em maio e novembro. Acima de 500 €, em maio, agosto e novembro.", "VPT de 200 000 € a 0,35%: 700 € por ano, em três prestações."],
  "Info Imobiliária, página «O que é o IMI» (PwC, Guia Fiscal 2026). Exemplos calculados por nós.", ["IMI", "VPT", "imobiliário", "impostos", "infoimobiliária"])
m("20261203v3", "Agente imobiliário: sinais de alerta", "O teu agente imobiliário: 5 sinais de alerta",
  ["Sinais de que algo não está a correr bem com o teu agente.", "Semanas sem visitas e sem explicação.", "Pressão para baixares o preço logo nos primeiros dias.", "Dificuldade em saber quantas visitas houve.", "Pouca clareza sobre exclusividade e duração. Fala com ele antes de o problema crescer."],
  "Info Imobiliária, «Como avaliar o trabalho do teu agente imobiliário».", ["vendercasa", "agenteimobiliário", "mediação", "imobiliário", "infoimobiliária"], leg=False)
m("20261203c", "Comunicar o contrato de arrendamento: porque importa", None,
  ["Porque comunicar o contrato de arrendamento importa.", "A dedução das rendas no IRS e apoios como o Porta 65 dependem do contrato comunicado.", "O senhorio só pode emitir recibos de renda eletrónicos depois de o comunicar.", "Para o senhorio, a coima vai de 75 € a 3 750 €.", "Guarda este carrossel."],
  "Info Imobiliária, «Como comunicar o contrato de arrendamento às Finanças e até quando» (21/11/2026), com AT, CGD, DECO PROteste e Doutor Finanças.", ["arrendamento", "senhorios", "inquilinos", "IRS", "infoimobiliária"])
m("20261203i", "Euribor: a prestação só muda na revisão", None,
  ["A Euribor muda todos os dias.", "A tua prestação só muda na data de revisão do contrato.", "Entre revisões, mantém-se, mesmo que a Euribor mexa.", "Vê a data da próxima revisão no teu contrato."],
  "Info Imobiliária, página «Euribor: o que é e como afeta a tua prestação».", ["euribor", "créditohabitação", "prestação", "imobiliário", "infoimobiliária"], leg=False)
m("20261204v1", "Renda sobe: Selo só sobre o aumento", "A renda sobe: o que comunicar às Finanças?",
  ["Renda de 800 € que passa para 850 €.", "O aumento tem de ser comunicado até ao fim do mês seguinte ao da alteração.", "O Imposto do Selo é de 10% do aumento, não da renda toda.", "50 € × 10% = 5 €.", "O fim do contrato também se comunica, no mesmo prazo."],
  "Info Imobiliária, «Como comunicar o contrato de arrendamento às Finanças e até quando» (21/11/2026), com a AT. Exemplo calculado por nós.", ["arrendamento", "impostodoselo", "senhorios", "imobiliário", "infoimobiliária"])
m("20261204v2", "Mais-valias: despesas dedutíveis", "Mais-valias: que despesas podes deduzir na venda?",
  ["Mais-valias: que despesas podes deduzir?", "Escritura e registo da compra.", "IMT e Imposto do Selo da compra.", "Comissão imobiliária da venda e certificado energético.", "Obras de conservação com fatura dos últimos 12 anos. As faturas têm de estar no teu NIF."],
  "Info Imobiliária, página «O que são as mais-valias imobiliárias», com CRN Contabilidade.", ["maisvalias", "IRS", "vendercasa", "imobiliário", "infoimobiliária"])
m("20261204v3", "Casa pronta a vender: documentos", "Casa pronta a vender: o que ter reunido",
  ["Antes de pôr a casa à venda, reúne os documentos.", "Caderneta predial, certidão de registo e certificado energético.", "Facilita o acesso a quem trata do crédito do comprador.", "Decide se há eletrodomésticos incluídos no preço.", "Entre duas casas parecidas e ao mesmo preço, isto costuma inclinar a balança."],
  "Info Imobiliária, «Como determinar o preço de venda da tua casa, em 3 passos».", ["vendercasa", "documentos", "imobiliário", "dicas", "infoimobiliária"], leg=False)
m("20261204c", "4 números: preço pedido, venda, avaliação e VPT", None,
  ["Preço pedido, preço de venda, avaliação e VPT: porque não coincidem.", "Preço pedido: o que os vendedores pedem nos anúncios.", "Preço de venda: o que se pagou nas transações, medido pelo INE.", "Avaliação bancária: a estimativa do banco. VPT: o valor fiscal.", "Guarda este carrossel."],
  "Info Imobiliária, «Preço pedido, preço de venda e avaliação bancária: porque os números não coincidem», com idealista, INE e Doutor Finanças.", ["preços", "avaliaçãobancária", "VPT", "imobiliário", "infoimobiliária"])
m("20261204i", "Imobiliária: seguro de 150 000 €", None,
  ["150 000 €.", "É o capital mínimo do seguro de responsabilidade civil da imobiliária.", "O contrato de mediação tem de identificar o seguro.", "Confirma também a licença do IMPIC."],
  "Info Imobiliária, «Comissão da imobiliária: quanto se paga, quando e o que diz a lei» (22/11/2026).", ["mediaçãoimobiliária", "vendercasa", "contrato", "imobiliário", "infoimobiliária"])
m("20261205v1", "Comissão da imobiliária: quando é devida", "Quando é devida a comissão da imobiliária?",
  ["Quando é devida a comissão da imobiliária?", "Em regra, quando a venda se conclui. Sem venda, não há comissão.", "No CPCV, se o contrato de mediação o previr.", "Com exclusividade, se a venda falhar por causa imputável a ti.", "Se alguém exercer um direito de preferência, o direito à comissão mantém-se."],
  "Info Imobiliária, «Comissão da imobiliária» (22/11/2026), com a Lei n.º 15/2013 (art. 19.º) e DECO PROteste.", ["comissão", "mediaçãoimobiliária", "vendercasa", "imobiliário", "infoimobiliária"])
m("20261205v2", "Mais-valias de casa herdada", "Vendeste uma casa herdada? Como contam as mais-valias",
  ["Casa herdada: como contam as mais-valias?", "A data de aquisição é a da morte de quem deixou a casa.", "O valor de compra é o que consta do Imposto do Selo.", "A isenção por reinvestimento aplica-se à venda da tua habitação própria e permanente.", "Numa casa herdada onde nunca viveste, normalmente não se aplica."],
  "Info Imobiliária, página «O que são as mais-valias imobiliárias», com CRN Contabilidade.", ["maisvalias", "heranças", "IRS", "imobiliário", "infoimobiliária"])
m("20261205v3", "Euribor a 3, 6 ou 12 meses: qual conta", "Euribor a 3, 6 ou 12 meses: qual conta no teu crédito?",
  ["Qual Euribor conta no teu crédito?", "A do prazo de revisão do contrato.", "O banco atualiza a taxa com essa Euribor e soma o spread.", "Em agosto, a de 6 meses era o indexante de cerca de 40% dos créditos a taxa variável, a de 12 meses de 31% e a de 3 meses de 24%.", "Confirma o indexante no teu contrato."],
  "Info Imobiliária, página «Euribor» e «Prestação da casa sobe em novembro...» (2/11/2026), com dados do Banco de Portugal via Lusa/DNoticias (30/10/2026).", ["euribor", "créditohabitação", "indexante", "imobiliário", "infoimobiliária"], leg=False)
m("20261205c", "Como avaliar o trabalho do teu agente", None,
  ["Como avaliar o trabalho do teu agente imobiliário.", "1. O preço: pede casas parecidas que se venderam há pouco.", "2. A promoção: pede o plano de marketing.", "3. A negociação e 4. O acompanhamento até à escritura.", "Guarda este carrossel."],
  "Info Imobiliária, «Como avaliar o trabalho do teu agente imobiliário».", ["vendercasa", "agenteimobiliário", "mediação", "imobiliário", "infoimobiliária"], leg=False)
m("20261205i", "Isenção temporária de IMI: 3 anos", None,
  ["3 anos.", "É a isenção temporária de IMI na compra de casa própria e permanente.", "O município pode prolongá-la por mais 2 anos.", "Pode ser usada duas vezes por contribuinte ou agregado."],
  "Info Imobiliária, página «O que é o IMI» e «Isenção de IMI: quem não paga, durante quanto tempo e como pedir».", ["IMI", "isençãoIMI", "comprarcasa", "imobiliário", "infoimobiliária"])
m("20261206v1", "IMI ou IMT: qual é qual", "IMI ou IMT: qual é qual?",
  ["IMI ou IMT: qual é qual?", "O IMT paga-se uma vez, quando compras.", "O IMI paga-se todos os anos, enquanto fores dono. A receita vai para o município.", "Quem arrenda não paga IMI: é do proprietário.", "Faz as contas à compra no site."],
  "Info Imobiliária, página «O que é o IMI».", ["IMI", "IMT", "impostos", "imobiliário", "infoimobiliária"])
m("20261206v2", "Casas de investidores em CIA: venda condicionada", "Casas de investidores com benefícios fiscais: venda condicionada",
  ["Casas de investidores com benefícios fiscais para arrendar: a venda tem condições.", "Falamos dos Contratos de Investimento para Arrendamento (Decreto-Lei 97/2026).", "Só podem ser vendidos por inteiro, a um comprador elegível que assuma o contrato.", "É preciso avisar o IHRU com 20 dias e haver despacho do ministro da Habitação.", "Sem a assunção do contrato na escritura, a venda é nula."],
  "ECO (13/11/2026) e Info Imobiliária, «Casas compradas com benefícios fiscais para arrendar: a venda passa a exigir autorização do Governo». Portaria 500/2026/1, em vigor desde 14/11/2026.", ["arrendamento", "habitação", "investimento", "imobiliário", "infoimobiliária"])
m("20261206v3", "Preço da casa: os dois erros opostos", "Preço da casa: os dois erros opostos",
  ["Preço da casa: os dois erros opostos.", "Começar alto para negociar: a casa fica parada e, quando baixas, parece que ninguém a quis.", "Baixar por pressa, sem estudo comparativo: podes deixar milhares de euros em cima da mesa.", "Acerta no preço logo no início, com casas comparáveis."],
  "Info Imobiliária, «Como determinar o preço de venda da tua casa, em 3 passos».", ["vendercasa", "preçodevenda", "errocomum", "imobiliário", "infoimobiliária"], leg=False)
m("20261206c", "Obras antes de vender: o que compensa", None,
  ["Obras antes de vender: o que compensa?", "Cosméticas: pintura, chão, torneiras e iluminação. Custam pouco e costumam compensar.", "De fundo: quarto novo, janelas, cozinha de raiz. Para uma venda próxima, raramente compensam.", "Antes de avançar, pede 2 ou 3 orçamentos e confirma se precisa de licença da câmara.", "Guarda este carrossel."],
  "Info Imobiliária, «Que obras valorizam a casa antes de vender».", ["vendercasa", "obras", "imobiliário", "dicas", "infoimobiliária"], leg=False)
m("20261206i", "Mediação: 6 meses se o contrato não disser nada", None,
  ["6 meses.", "É a duração do contrato de mediação, se o contrato não disser nada.", "Pode renovar-se, se ficar escrito.", "Marca a data de denúncia no calendário."],
  "Info Imobiliária, «Comissão da imobiliária: quanto se paga, quando e o que diz a lei» (22/11/2026), com a Portaria n.º 228/2018.", ["mediaçãoimobiliária", "vendercasa", "contrato", "imobiliário", "infoimobiliária"])

# horas de Lisboa (v1, v2, v3, c, i)
T = {30: ("09:30", "14:00", "20:15", "11:45", "16:30"), 1: ("10:15", "13:30", "19:45", "15:15", "17:00"),
     2: ("09:00", "14:30", "20:30", "12:15", "16:00"), 3: ("10:30", "13:15", "19:30", "15:30", "17:15"),
     4: ("09:45", "14:15", "21:00", "11:15", "16:45"), 5: ("10:45", "13:45", "20:00", "15:45", "16:20"),
     6: ("09:15", "14:45", "19:15", "12:00", "16:15")}
def utc(key_day, hhmm, add=0):
    mth, d = (11, 30) if key_day == 30 else (12, key_day)
    h, mi = map(int, hhmm.split(":"))
    x = dt.datetime(2026, mth, d, h, mi, tzinfo=ZoneInfo("Europe/Lisbon")) + dt.timedelta(minutes=add)
    return x.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:00.000Z")
assert set(M) == set(D)
assert not any("—" in v["legenda"] or "—" in (v["titulo"] or "") for v in M.values())
assert all(len(v["titulo"] or "") <= 100 for v in M.values())
assert all(v["legenda"].rsplit(chr(10), 1)[1].count("#") == 5 for v in M.values())
