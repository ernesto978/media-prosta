# Info Imobiliária - 10 a 16 de novembro de 2026. Factos lidos no site a 9/11/2026; contas recalculadas abaixo.
from modelos import V, C, I, END
pm = lambda P, t, n=360: (lambda r: P * r / (1 - (1 + r) ** -n))(t / 12)
fm = lambda v: f"{v:,.2f}".replace(",", " ").replace(".", ",")
assert 250000 * 0.9 == 225000 and 250000 - 225000 == 25000
assert 235000 * 0.9 == 211500 and 250000 - 211500 == 38500
assert fm(pm(150000, .03)) == "632,41" and fm(pm(150000, .0306)) == "637,27" and fm(pm(150000, .0406)) == "721,32"
assert fm(pm(150000, .0306) - pm(150000, .03)) == "4,86"
assert round(pm(150000, .0406) - pm(150000, .0306), 2) == 84.05
assert min(2400 * .15, 296) == 296 and 1500 * .15 == 225 and 2400 * .15 == 360
assert 800 * 2 == 1600 and 800 * 3 == 2400 and 800 * 3 == 2400 and 800 * 2 == 1600
assert 200000 * 1.2 == 240000 and 280000 - 240000 == 40000 and 280000 - 200000 == 80000
D = {}
# ================= TER 10 =================
D["d10v1"] = V("Glossário", "GLOSSÁRIO · CRÉDITO", "Exemplo calculado. Habitação própria e permanente.", [
    [("h", "LTV", 110), ("p", "A percentagem da casa que o banco financia.", 46)],
    [("card", "O QUE É", "Loan to value: a relação entre o crédito e o valor do imóvel. Quanto mais alto, menos entrada pagas.")],
    [("card", "O LIMITE", "Na habitação própria e permanente, o máximo costuma ser 90%.")],
    [("p", "Casa de 250 000 €:", 44), ("pair", ("FINANCIAMENTO", "225 000 €"), ("ENTRADA", "25 000 €"))],
    [("card", "ATENÇÃO", "O banco usa o menor valor entre o preço e a avaliação. À entrada somam-se IMT, Selo e escritura.")],
], ("Conta com a entrada.", "Calculadora de custos de aquisição"))
D["d10v2"] = V("Notícia", "O QUE MUDA · MAIS-VALIAS", "Fonte: ECO e Jornal de Negócios. Ainda é só proposta.", [
    [("h", "Segundas casas: isenção de mais-valias?", 76), ("p", "É uma proposta, não uma regra.", 46)],
    [("card", "A PROPOSTA", "Isentar de IRS as mais-valias da venda de segundas casas até 300 mil euros.")],
    [("card", "AS CONDIÇÕES", "Regime de três anos. O comprador usa a casa como habitação própria e permanente, em zona de pressão urbana.")],
    [("card", "ENTRE 300 E 500 MIL €", "Tributação reduzida. As fontes não indicam a taxa.")],
    [("pn", "Nada disto está em vigor. A informação vem sobretudo do relato do PS sobre a reunião de 5 de novembro.", 46)],
], ("Faz as contas com as regras de hoje.", "Calculadora de mais-valias"))
D["d10v3"] = V("Checklist", "CHECKLIST · CASA E VIDA", "Informação geral. Para obras, consulta um especialista.", [
    [("h", "Como evitar o bolor em casa", 80)],
    [("chk", "Ventila todos os dias, à tarde no inverno"), ("chk", "Usa os extratores na cozinha e na casa de banho"), ("chk", "Tapa os tachos ao cozinhar")],
    [("chk", "Evita secar roupa dentro de casa"), ("chk", "Aquece a casa de forma regular"), ("card", "NÍVEL IDEAL", "Humidade relativa entre 40% e 60%.")],
], ("Uma casa mais saudável.", "Mais dicas no site"))
D["d10c"] = C("Guia", "GUIA · PROCESSO", "OS DOCUMENTOS DA CASA", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "3 documentos da casa que deves conhecer", 72), ("p", "Licença, ficha técnica e certificado energético.", 44)],
    [("card", "LICENÇA DE UTILIZAÇÃO", "Autorização da câmara para usar a casa para o fim previsto. Costuma ser exigida na escritura. Sem ela, a escritura pode atrasar ou o banco recusar o crédito.")],
    [("card", "FICHA TÉCNICA DA HABITAÇÃO", "Obrigatória em casas com licença de construção a partir de 30 de março de 2004. Já não é preciso apresentá-la na escritura.")],
    [("card", "CERTIFICADO ENERGÉTICO", "Classe de A+ a F. É exigido na venda e no arrendamento, e a classe deve constar no anúncio. Em regra, vale 10 anos.")],
    END("Vê o passo a passo da compra."),
])
D["d10i"] = I("Dado", "O DADO · MERCADO", "Fonte: Banco de Portugal, via ECO, 2/11/2026.", [
    ("h", "Juros do crédito à habitação", 80), ("num", "3,06%", 150),
    ("pn", "Taxa média dos novos créditos em setembro. Sexta subida seguida.", 44), ("p", "É uma média: a tua taxa depende do spread, do indexante e do prazo.", 38)])
# ================= QUA 11 =================
D["d11v1"] = V("Notícia", "O QUE MUDA · ARRENDAMENTO", "Fonte: ECO, 2/11/2026. Proposta em discussão.", [
    [("h", "Lei do arrendamento: o que se sabe", 80), ("p", "Nada mudou nos teus contratos.", 46)],
    [("card", "2 DE NOVEMBRO", "O ministro da Habitação disse que o Governo aceita as quatro propostas do Chega.")],
    [("card", "O QUE FALTA SABER", "Quais são essas propostas e quando há votação. A fonte não o indica.")],
    [("card", "ONDE ESTÁ", "Aprovada na generalidade a 30 de setembro. Segue para a especialidade, onde o texto pode mudar.")],
    [("pn", "Em vigor continuam as regras atuais.", 54)],
], ("Compara arrendar com comprar.", "Calculadora arrendar ou comprar"))
D["d11v2"] = V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. Casa de 250 000 € e LTV máximo de 90%.", [
    [("h", "E se o banco avaliar a casa abaixo do preço?", 76), ("p", "Casa de 250 000 €.", 44)],
    [("card", "AVALIAÇÃO DE 250 000 €", "Financiamento até 225 000 €. Entrada de 25 000 €.")],
    [("card", "AVALIAÇÃO DE 235 000 €", "Financiamento até 211 500 €. Entrada de 38 500 €.")],
    [("num", "+13 500 €", 130), ("p", "de entrada, por causa de uma avaliação mais baixa.", 44)],
], ("Conta com margem.", "Calculadora de custos de aquisição"))
D["d11v3"] = V("Erro comum", "ERRO COMUM · PROCESSO", "Informação geral. Em casas muito antigas pode haver dispensa.", [
    [("h", "Comprar casa sem pedir a licença de utilização", 74)],
    [("card", "O ERRO", "Deixar a licença para o fim e assumir que está tudo em ordem.")],
    [("card", "O RISCO", "Sem licença, a escritura pode atrasar ou o banco pode recusar o crédito.")],
    [("card", "CONFIRMA", "Que o uso autorizado é habitação. Se for outro, podem surgir problemas.")],
    [("card", "O QUE FAZER", "Pede a licença ao vendedor logo no início. Em dúvida, pergunta ao advogado ou ao solicitador.")],
], ("Compra com os papéis certos.", "Como comprar casa, passo a passo"))
D["d11c"] = C("Guia", "GUIA · CASA E VIDA", "OS 3 TIPOS DE HUMIDADE", "Fonte: Santander e Generali Tranquilidade. Informação geral.", [
    [("h", "Humidade em casa: de onde vem?", 76), ("p", "Nem sempre é do mesmo tipo.", 46)],
    [("card", "CONDENSAÇÃO", "Vapor de água que se condensa em superfícies frias. É o tipo mais comum. Sinais: manchas, bolor, cheiro a mofo e vidros embaciados.")],
    [("card", "HUMIDADE ASCENDENTE", "A água sobe do solo pelas paredes. Sinais: tinta a empolar, papel de parede solto e salitre.")],
    [("card", "INFILTRAÇÃO", "A água entra por paredes, telhados, terraços, fissuras ou canos danificados. Costuma estar ligada à chuva ou a uma zona concreta.")],
    END("Lê o artigo completo."),
])
D["d11i"] = I("Dado", "O DADO · IMPOSTOS", "Fonte: Info Imobiliária, «VPT». Está na caderneta predial.", [
    ("h", "O que é o VPT?", 84), ("pn", "O valor fiscal do imóvel, calculado pela Autoridade Tributária.", 46),
    ("pair", ("IMI", "usa o VPT"), ("IMT", "o mais alto")), ("p", "Não é o preço de mercado. O IMT calcula-se sobre o mais alto entre o preço e o VPT.", 38)])
# ================= QUI 12 =================
D["d12v1"] = V("Notícia", "O QUE MUDA · IRS", "Fonte: ComparaJá, 6/11/2026. Proposta para o OE2027.", [
    [("h", "Juros do crédito habitação no IRS?", 78), ("p", "O Chega quer voltar a permitir a dedução.", 44)],
    [("card", "HOJE", "Só deduzem os contratos celebrados até 31 de dezembro de 2011: 15% dos juros, com limite geral de 296 €.")],
    [("card", "A PROPOSTA", "Estender a dedução a contratos posteriores a 2011. O líder admite limitá-la a prestações até 1 200 €.")],
    [("pn", "Ainda sem aprovação e sem data de votação conhecida.", 52)],
], ("Simula a tua prestação.", "Calculadora de crédito habitação"))
D["d12v2"] = V("Pergunta", "PERGUNTA DA SEMANA · COMPRAR", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Posso desistir da compra depois de pagar o sinal?", 74)],
    [("card", "PODES, MAS COM CONSEQUÊNCIAS", "Se desistires, perdes o sinal. Se for o vendedor, devolve-o em dobro.")],
    [("card", "O SINAL", "A lei não fixa o valor. Na prática anda entre 10% e 20% do preço.")],
    [("card", "O BANCO RECUSA O CRÉDITO?", "Só recuperas o sinal se o CPCV tiver cláusula de financiamento.")],
], ("Lê o CPCV com calma.", "Como comprar casa, passo a passo"))
D["d12v3"] = V("Conta", "A CONTA DA SEMANA · CRÉDITO", "Exemplo calculado. Taxa fixa, 30 anos, sem seguros nem comissões.", [
    [("h", "Os juros sobem. Quanto pesa na prestação?", 76), ("p", "Crédito de 150 000 €.", 44)],
    [("card", "A 3,00% (MÉDIA DE AGOSTO)", "Prestação de 632,41 €.")],
    [("card", "A 3,06% (MÉDIA DE SETEMBRO)", "Prestação de 637,27 €. São 4,86 € a mais por mês.")],
    [("card", "A 4,06% (UM PONTO A MAIS)", "Prestação de 721,32 €. São 84,05 € a mais do que a 3,06%.")],
], ("Simula a tua prestação.", "Calculadora de crédito habitação"))
D["d12c"] = C("Guia", "GUIA · ARRENDAR", "DESPEJOS POR RENDAS EM ATRASO", "Fonte: ECO, 30/10/2026, com dados do BAS.", [
    [("h", "Despejos por rendas em atraso: o que dizem os dados", 70)],
    [("card", "O PESO", "Cerca de 7 400 pedidos em cinco anos, face a 1,4 milhões de contratos comunicados às Finanças.")],
    [("card", "2026 ATÉ OUTUBRO", "2 181 pedidos. 59% por falta de pagamento e 26% por oposição do senhorio à renovação.")],
    [("card", "A DURAÇÃO", "292 dias em média, quase dez meses, entre o pedido e a entrega da casa.")],
    END("Compara arrendar e comprar."),
])
D["d12i"] = I("Dado", "O DADO · CASA E VIDA", "Fonte: Santander e Generali Tranquilidade.", [
    ("h", "Humidade ideal dentro de casa", 78), ("num", "40% a 60%", 120),
    ("pn", "Humidade relativa recomendada.", 46), ("p", "Abaixo de 40% o ar fica seco. Acima de 60% é mais fácil crescerem fungos.", 38)])
# ================= SEX 13 =================
D["d13v1"] = V("Conta", "A CONTA DA SEMANA · ARRENDAR", "Exemplo ilustrativo. Renda hipotética de 800 €. Proposta ainda em discussão.", [
    [("h", "Arrendar: o que mudaria com a proposta?", 78), ("p", "Renda de 800 € por mês.", 44)],
    [("card", "CAUÇÕES", "Com duas cauções: 1 600 €. Com a proposta de três: 2 400 €.")],
    [("card", "RENDAS EM ATRASO", "Hoje, o despejo por falta de pagamento pode começar com três rendas em atraso: 2 400 €. A proposta fala em dois meses: 1 600 €.")],
    [("pn", "É uma proposta. Em vigor continuam as regras atuais.", 50)],
], ("Compara arrendar e comprar.", "Calculadora arrendar ou comprar"))
D["d13v2"] = V("Glossário", "GLOSSÁRIO · CRÉDITO", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Hipoteca", 110), ("p", "A garantia do teu crédito habitação.", 46)],
    [("card", "O QUE É", "O banco regista uma hipoteca sobre a casa. Continuas a ser o dono e a viver lá, mas o imóvel responde pela dívida.")],
    [("card", "SE DEIXARES DE PAGAR", "O banco pode cobrar e, no limite, vender o imóvel. Antes disso há procedimentos para renegociar.")],
    [("card", "O CONSELHO", "Se vês que não vais conseguir pagar, fala com o banco logo no início.")],
], ("Percebe o teu crédito.", "Calculadora de crédito habitação"))
D["d13v3"] = V("Erro comum", "ERRO COMUM · CASA E VIDA", "Informação geral. Para impermeabilização, consulta um especialista.", [
    [("h", "Limpar o bolor e achar que o problema acabou", 74)],
    [("card", "O ERRO", "Limpar resolve o sintoma, não a causa.")],
    [("card", "O QUE FAZER", "Procura a origem: condensação, canos com fugas, caleiras entupidas, vedantes gastos.")],
    [("card", "CHAMA UM ESPECIALISTA", "Se há fissuras e a humidade persiste, ou antes de impermeabilizar. Pode ser uma obra cara.")],
], ("Resolve a causa.", "Mais dicas no site"))
D["d13c"] = C("Guia", "GUIA · IMPOSTOS", "JUROS DO CRÉDITO NO IRS", "Fonte: ComparaJá, 6/11/2026. Proposta ainda por aprovar.", [
    [("h", "Posso deduzir os juros do crédito no IRS?", 72)],
    [("card", "A REGRA EM VIGOR", "Só para contratos celebrados até 31 de dezembro de 2011. Deduz-se 15% dos juros.")],
    [("card", "OS LIMITES", "O limite geral é de 296 €, e pode chegar a 450 € para rendimentos mais baixos.")],
    [("card", "A PROPOSTA DO CHEGA", "Estender a dedução a contratos posteriores a 2011, no Orçamento do Estado para 2027.")],
    END("Confirma o teu caso no IRS."),
])
D["d13i"] = I("Dado", "O DADO · PROCESSO", "Fonte: Info Imobiliária, «Ficha técnica da habitação».", [
    ("h", "Ficha técnica da habitação", 78), ("num", "30 mar 2004", 100),
    ("pn", "É obrigatória em casas com licença de construção a partir desta data.", 44), ("p", "Já não é preciso apresentá-la na escritura. O vendedor deve entregá-la ao comprador.", 38)])
# ================= SÁB 14 =================
D["d14v1"] = V("Notícia", "O QUE MUDA · ARRENDAR", "Fonte: ECO, 30/10/2026 (dados do BAS).", [
    [("h", "Despejos por rendas em atraso", 84), ("p", "O que dizem os números.", 46)],
    [("num", "292 dias", 120), ("p", "em média, do pedido de despejo à entrega da casa. Quase dez meses.", 44)],
    [("card", "O PESO", "Cerca de 7 400 pedidos em cinco anos, face a 1,4 milhões de contratos.")],
    [("card", "AVISO", "Os 0,5% não são uma taxa anual e só cobrem as rendas em atraso. Dão a ordem de grandeza.")],
], ("Faz as contas ao arrendamento.", "Calculadora arrendar ou comprar"))
D["d14v2"] = V("Glossário", "GLOSSÁRIO · PROCESSO", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Certificado energético", 88), ("p", "A classe da tua casa, de A+ a F.", 46)],
    [("card", "O QUE É", "Emitido por um perito qualificado. Indica o consumo estimado e dá recomendações de melhoria.")],
    [("card", "VALIDADE", "Em regra, 10 anos para habitação.")],
    [("card", "QUANDO É EXIGIDO", "Na venda, no arrendamento e na publicidade, que deve indicar a classe.")],
    [("card", "SE VAIS VENDER", "Trata dele cedo. Alguns peritos demoram.")],
], ("Prepara a venda da tua casa.", "Como vender casa, passo a passo"))
D["d14v3"] = V("Passo a passo", "PASSO A PASSO · VENDER", "Informação geral. Pergunta ao teu banco.", [
    [("h", "Como cancelar a hipoteca depois de pagar o crédito", 72)],
    [("card", "1. PAGA O CRÉDITO", "Total, ou o restante em dívida.")],
    [("card", "2. PEDE A QUITAÇÃO", "O banco emite o documento a declarar que recebeu o dinheiro.")],
    [("card", "3. CANCELA NO REGISTO", "Pede o cancelamento da hipoteca no registo predial, online ou presencialmente.")],
    [("card", "SE VAIS VENDER", "Pergunta ao banco como fazer o pagamento e o cancelamento no mesmo ato.")],
], ("Vende com tudo em ordem.", "Como vender casa, passo a passo"))
D["d14c"] = C("Guia", "GUIA · VENDER", "MAIS-VALIAS E SEGUNDAS CASAS", "Fonte: ECO e Jornal de Negócios. Ainda é só proposta.", [
    [("h", "Mais-valias: o que está em cima da mesa", 72), ("p", "Venda de segundas casas.", 46)],
    [("card", "A PROPOSTA", "Isenção de IRS na venda de segundas habitações até 300 mil euros, num regime de três anos.")],
    [("card", "AS CONDIÇÕES", "O comprador usa a casa como habitação própria e permanente, em zona de pressão urbana.")],
    [("card", "E SE VENDER POR MAIS?", "Entre 300 e 500 mil euros haveria tributação reduzida. As fontes não indicam a taxa.")],
    END("Faz a conta com as regras de hoje."),
])
D["d14i"] = I("Dado", "O DADO · CRÉDITO", "Exemplo calculado. Habitação própria e permanente.", [
    ("h", "Casa de 250 000 €. Quanto financia o banco?", 70), ("pair", ("LTV 90%", "225 000 €"), ("ENTRADA", "25 000 €")),
    ("pn", "Ao valor da entrada somam-se IMT, Selo e escritura.", 44), ("p", "O banco usa o menor valor entre o preço e a avaliação.", 38)])
# ================= DOM 15 =================
D["d15v1"] = V("Conta", "A CONTA DA SEMANA · IRS", "Exemplo ilustrativo. Assume a regra atual (15% e limite de 296 €). Proposta ainda por aprovar.", [
    [("h", "Quanto poderias deduzir de juros no IRS?", 76), ("p", "Se a regra atual se aplicasse ao teu contrato.", 44)],
    [("card", "2 400 € DE JUROS", "15% são 360 €. Como passa o limite de 296 €, a dedução fica em 296 €.")],
    [("card", "1 500 € DE JUROS", "15% são 225 €, abaixo do limite. A dedução é de 225 €.")],
    [("pn", "A proposta do Chega ainda não define estas regras.", 50)],
], ("Simula o teu crédito.", "Calculadora de crédito habitação"))
D["d15v2"] = V("Passo a passo", "PASSO A PASSO · CRÉDITO", "Informação geral. Confirma com o teu banco.", [
    [("h", "A avaliação do banco veio baixa. E agora?", 76)],
    [("card", "1. NÃO ASSUMAS NADA", "A avaliação pode ser inferior ao preço. O banco financia a percentagem da avaliação.")],
    [("card", "2. RENEGOCIA O PREÇO", "Mostra o valor ao vendedor e tenta chegar a um acordo.")],
    [("card", "3. PEDE OUTRA AVALIAÇÃO", "Pede uma segunda avaliação a outro banco.")],
    [("card", "4. GUARDA MARGEM", "Conta com uma entrada maior do que a prevista.")],
], ("Compra com margem.", "Calculadora de custos de aquisição"))
D["d15v3"] = V("Checklist", "CHECKLIST · PROCESSO", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Antes de assinar, pergunta ao vendedor", 78)],
    [("chk", "Tens a licença de utilização?"), ("chk", "Tens o certificado energético?"), ("chk", "Há hipotecas por cancelar?")],
    [("chk", "A casa foi licenciada depois de março de 2004? Pede a ficha técnica."), ("card", "ONDE VER AS HIPOTECAS", "Na certidão permanente do registo predial.")],
], ("Compra com tudo verificado.", "Como comprar casa, passo a passo"))
D["d15c"] = C("Guia", "GUIA · ARRENDAR", "A REVISÃO DA LEI DO ARRENDAMENTO", "Fonte: ECO e DNoticias. Proposta em discussão.", [
    [("h", "Lei do arrendamento: onde estamos", 76), ("p", "Nada mudou nos teus contratos.", 46)],
    [("card", "30 DE SETEMBRO", "A proposta do Governo foi aprovada na generalidade, com votos a favor de PSD, IL e CDS-PP e abstenção do Chega.")],
    [("card", "O QUE PREVÊ", "Despejo por falta de pagamento ao fim de dois meses em atraso (hoje são três), três cauções em vez de duas e o fim do processo separado de execução.")],
    [("card", "2 DE NOVEMBRO", "O Governo diz aceitar as quatro propostas do Chega. A fonte não as lista.")],
    END("Compara arrendar e comprar."),
])
D["d15i"] = I("Dado", "O DADO · CASA E VIDA", "Fonte: Info Imobiliária, «Certificado energético».", [
    ("h", "Certificado energético", 80), ("num", "A+ a F", 150),
    ("pn", "A classe da casa. Em regra, vale 10 anos.", 46), ("p", "A classe deve constar no anúncio de venda ou de arrendamento.", 38)])
# ================= SEG 16 =================
D["d16v1"] = V("Conta", "A CONTA DA SEMANA · MAIS-VALIAS", "Exemplo hipotético. Casa comprada em 2019 por 200 000 € e vendida por 280 000 €.", [
    [("h", "Mais-valias: quanto conta a correção monetária?", 72), ("p", "Casa comprada em 2019 por 200 000 €.", 44)],
    [("card", "VENDA POR 280 000 €", "Sem correção, a mais-valia seria de 80 000 €.")],
    [("card", "COM CORREÇÃO", "Coeficiente de 1,20: 200 000 € passam a 240 000 €. A mais-valia fica em 40 000 €.")],
    [("pn", "Exemplo ilustrativo, com os pressupostos do artigo do site.", 46)],
], ("Faz a tua conta.", "Calculadora de mais-valias"))
D["d16v2"] = V("Checklist", "CHECKLIST · CRÉDITO", "Informação geral. Confirma com o teu banco.", [
    [("h", "Antes de pedir crédito, confirma", 80)],
    [("chk", "Quanto financia o banco (LTV, em regra até 90%)"), ("chk", "Quanto tens para a entrada"), ("chk", "Os custos de compra: IMT, Selo e escritura")],
    [("chk", "E se a avaliação for inferior ao preço?"), ("chk", "Quanto custa a avaliação (paga quem pede o crédito)"), ("card", "COMPARA", "Pede propostas a mais do que um banco.")],
], ("Faz as contas primeiro.", "Calculadora de custos de aquisição"))
D["d16v3"] = V("Erro comum", "ERRO COMUM · PROCESSO", "Informação geral. Confirma com um advogado ou solicitador.", [
    [("h", "Comprar uma casa sem ver as hipotecas", 78)],
    [("card", "O ERRO", "Não verificar se a casa tem hipotecas por cancelar.")],
    [("card", "ONDE VER", "Na certidão permanente do registo predial.")],
    [("card", "O QUE FAZER", "A hipoteca deve ser cancelada na escritura. Se o vendedor tem crédito, pergunta como é feito o pagamento.")],
], ("Compra com segurança.", "Como comprar casa, passo a passo"))
D["d16c"] = C("Guia", "GUIA · MERCADO", "JUROS DO CRÉDITO: O QUE FAZER", "Fonte: Banco de Portugal, via ECO, 2/11/2026.", [
    [("h", "Juros a subir: o que fazer?", 82), ("p", "Taxa média de 3,06% em setembro.", 46)],
    [("card", "VAIS COMPRAR", "Pede propostas a mais do que um banco. Compara a TAEG e simula a prestação com margem de segurança.")],
    [("card", "JÁ TENS CRÉDITO", "Confirma no extrato o indexante, o spread e a data da próxima revisão.")],
    [("card", "PENSAS RENEGOCIAR", "Compara com outros bancos e conta os custos da mudança antes de decidir.")],
    END("Simula a tua prestação."),
])
D["d16i"] = I("Dado", "O DADO · CASA E VIDA", "Fonte: Santander e Generali Tranquilidade.", [
    ("h", "Humidade ascendente: os sinais", 78),
    ("card", "SINAIS", "Manchas, tinta a empolar, papel de parede solto e salitre."),
    ("pn", "A água sobe do solo pelas paredes.", 46), ("p", "Pede normalmente uma intervenção na casa. Consulta um especialista.", 38)])
