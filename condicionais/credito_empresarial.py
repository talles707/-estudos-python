# Análise de Crédito Empresarial
# Conceitos: variáveis, múltiplos blocos de if, and, formatação :.2f

empresa = "Construtora Alpha"
faturamento = 500000.0
score = 780
tempo = 5

# Categoria com base no faturamento
if faturamento >= 1000000:
    categoria = "Grande empresa"
elif faturamento >= 500000:
    categoria = "Média empresa"
elif faturamento >= 100000:
    categoria = "Pequena empresa"
else:
    categoria = "Microempresa"

# Limite de crédito com base na categoria
if categoria == "Grande empresa":
    limite = 0.30
elif categoria == "Média empresa":
    limite = 0.20
elif categoria == "Pequena empresa":
    limite = 0.15
else:
    limite = 0.10

# Status com base no score e tempo de mercado
if score >= 800 and tempo >= 3:
    status = "Crédito aprovado automaticamente"
elif score >= 700 and tempo >= 2:
    status = "Crédito aprovado com análise documental"
elif score >= 600 and tempo >= 1:
    status = "Crédito aprovado com garantias"
else:
    status = "Crédito negado"

limite_credito = faturamento * limite

print("=== ANÁLISE DE CRÉDITO EMPRESARIAL ===")
print(f"Empresa: {empresa}")
print(f"Faturamento anual: R$ {faturamento:.2f}")
print(f"Score: {score}")
print(f"Tempo de mercado: {tempo} anos")
print(f"Categoria: {categoria}")
print(f"Limite de crédito: R$ {limite_credito:.2f}")
print(f"Status: {status}")
