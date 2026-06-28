# Avaliação de Desempenho de Funcionário
# Conceitos: variáveis, if/elif/else

funcionario = "Lucas Martins"
setor = "Comercial"
nota = 78

if nota >= 90:
    resultado = "Ótimo desempenho"
elif nota >= 70:
    resultado = "Bom desempenho"
elif nota >= 50:
    resultado = "Desempenho regular"
else:
    resultado = "Desempenho insatisfatório"

print("=== AVALIAÇÃO DE DESEMPENHO ===")
print(f"Funcionário: {funcionario}")
print(f"Setor: {setor}")
print(f"Nota: {nota}")
print(f"Resultado: {resultado}")
