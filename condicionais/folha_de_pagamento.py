# Folha de Pagamento com INSS e IR
# Conceitos: variáveis, múltiplos blocos de if/elif/else, formatação :.2f

funcionario = "Marcos Oliveira"
cargo = "Analista"
salario = 5000.0

# Cálculo do INSS
if salario <= 1518:
    inss = 0.075
elif salario <= 2793:
    inss = 0.09
elif salario <= 4190:
    inss = 0.12
else:
    inss = 0.14

# Cálculo do IR
if salario <= 2259:
    ir = 0
elif salario <= 2826:
    ir = 0.075
elif salario <= 3751:
    ir = 0.15
elif salario <= 4664:
    ir = 0.225
else:
    ir = 0.275

desconto_inss = salario * inss
desconto_ir = salario * ir
salario_liquido = salario - desconto_inss - desconto_ir

print("=== FOLHA DE PAGAMENTO ===")
print(f"Funcionário: {funcionario}")
print(f"Cargo: {cargo}")
print(f"Salário bruto: R$ {salario:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IR: R$ {desconto_ir:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
