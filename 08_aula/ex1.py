##################################################
# Alterando itens da lista pelo seu indice

bancos = ["banco do Brasil", "Caixa", "Santander"]
print(bancos)
# Resultado: ['banco do Brasil', 'Caixa', 'Santander']
bancos[1] = "Itaú"
print(bancos)
# Resultado: ['banco do Brasil', 'Itaú', 'Santander']
bancos[-1] = "C6"
print(bancos)
# Resultado: ['banco do Brasil', 'Itaú', 'C6']


##################################################
# Encrementar o valor de uma lista

print(bancos)
#resultado: ['banco do Brasil', 'Itaú', 'C6']
bancos = bancos + ["Bradesco", "Nubank"]
print(bancos)
# Resultado: ['banco do Brasil', 'Itaú', 'C6', 'Bradesco', 'Nubank']
bancos += ["Safra"]
print(bancos)
# Resultado: ['banco do Brasil', 'Itaú', 'C6', 'Bradesco', 'Nubank', 'Safra']

##################################################
 #EXEMPLOS de utilisação de metodos para listas

lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(2)
print(lista)
lsita.insert(2, -3)
print(lista)
lista.remove(4)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)

qnt = lista.count(5)
print(qnt)
exc = lista.pop()
print(lista)
print(exc)
del lista[2]
print(lista)
del lista [2:5]
print(lista)
lista.clear()
print(lista)