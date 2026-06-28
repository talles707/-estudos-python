# Relatório de Funcionários
# Conceitos: loop for, range(), variáveis, f-string

setor = "Financeiro"
total = 5

print("=== RELATÓRIO DE FUNCIONÁRIOS ===")
print(f"Setor: {setor}")
print(f"Total de funcionários: {total}")
print()
for i in range(1, total + 1):
    print(f"Funcionário {i}")
