# Verificação de Estoque em Lote
# Conceitos: loop for, if/else, listas

estoques = [50, 8, 30, 5, 25]

print("=== VERIFICAÇÃO DE ESTOQUE ===")
for i in range(1, 6):
    if estoques[i-1] >= 10:
        status = "Estoque OK"
    else:
        status = "Estoque baixo!"
    print(f"Produto {i}: {status}")
