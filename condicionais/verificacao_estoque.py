# Verificação de Estoque
# Conceitos: variáveis, if/else

produto = "Papel A4"
quantidade_em_estoque = 15

if quantidade_em_estoque > 20:
    status = "Estoque normal"
else:
    status = "Estoque baixo, reposição necessária!"

print("=== VERIFICAÇÃO DE ESTOQUE ===")
print(f"Produto: {produto}")
print(f"Quantidade em estoque: {quantidade_em_estoque}")
print(f"Status: {status}")
