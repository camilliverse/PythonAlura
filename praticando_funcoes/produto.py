produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = float(input("Digite os preços separados por vírgula: ").split(","))
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}")