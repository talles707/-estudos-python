# Classificação de Chamado de TI por Setor
# Conceitos: variáveis, if/elif/else

solicitante = "Roberta Lima"
setor = "Financeiro"
problema = "Sistema fora do ar"

if setor == "Financeiro" and problema == "Sistema fora do ar":
    prioridade = "Crítica"
elif setor == "Financeiro":
    prioridade = "Alta"
elif setor == "RH":
    prioridade = "Média"
else:
    prioridade = "Baixa"

if prioridade == "Crítica":
    prazo = "1 hora"
elif prioridade == "Alta":
    prazo = "4 horas"
elif prioridade == "Média":
    prazo = "8 horas"
else:
    prazo = "24 horas"

print("=== CLASSIFICAÇÃO DE CHAMADO ===")
print(f"Solicitante: {solicitante}")
print(f"Setor: {setor}")
print(f"Problema: {problema}")
print(f"Prioridade: {prioridade}")
print(f"Prazo de atendimento: {prazo}")
