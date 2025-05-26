##################################################
# Uma lista dentro de outra lista
compra = [10.2, 3.35, 16.3, ["tomate", "sabonete", "arroz"]]
print(compra)
produtos = compra[3]
print(produtos)
total = compra[0] + compra[1] + compra[2]
print(total)
letra = ["a", "b", "c"]
num = [2, 4, 6]
tudo = [letra, num]
print(tudo)
print(f"letras", tudo[0])
print(f"números", tudo[1])

##################################################
# TAMANHO DE LISTA

letra = ["a", "b", "c"]
print(f"Tamanho da lista: {len(letra)}")
print(f"Tamanho da letra b: {letra.index('b')}")

##################################################
# Metodos utilizados em listas'

# 1. obter o tamanho da lista len
# 2. obter o determinado elemento da lista index

letra = ["a", "b", "c"]
print(f"informe uma letra: ")
if var.lower() in letra:
    print(f"letra '{var.lower()}' está na lista")
else:
    print(f"letra '{var.lower()}' não está na lista")

##################################################
# ADICIONANDO ELEMENTOS FORNECIDOS PELO USUÁRIO À LISTA

nova = []
while True:
   mum = int(input("Informe um número (ou 0 para sair): "))
   if mum == 0:
       break
   nova.append(mum)
   print(nova)
# Exibindo a lista final

##################################################
