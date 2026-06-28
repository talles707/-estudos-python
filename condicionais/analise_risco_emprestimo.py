# Análise de Risco de Empréstimo
# Conceitos: variáveis, cálculos, múltiplos blocos de if, and, formatação :.2f

cliente = "Sandra Melo"
renda = 6000.0
score = 750
valor_solicitado = 15000.0

# Cálculo do comprometimento de renda
comprometimento = (valor_solicitado / (renda * 6)) * 100

# Classificação do risco
if score >= 800 and comprometimento <= 30:
    risco = "Baixo"
elif score >= 700 and comprometimento <= 50:
    risco = "Moderado"
elif score >= 600 and comprometimento <= 70:
    risco = "Alto"
else:
    risco = "Muito alto"

# Status com base no risco
if risco == "Baixo":
    status = "Empréstimo aprovado com juros reduzidos"
elif risco == "Moderado":
    status = "Empréstimo aprovado com juros diferenciados"
elif risco == "Alto":
    status = "Empréstimo aprovado mediante análise adicional"
else:
    status = "Empréstimo negado"

print("=== ANÁLISE DE RISCO DE EMPRÉSTIMO ===")
print(f"Cliente: {cliente}")
print(f"Renda mensal: R$ {renda:.2f}")
print(f"Score de crédito: {score}")
print(f"Valor solicitado: R$ {valor_solicitado:.2f}")
print(f"Comprometimento da renda: {comprometimento:.2f}%")
print(f"Risco: {risco}")
print(f"Status: {status}")
