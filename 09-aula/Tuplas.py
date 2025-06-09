# Podemos acessar os elementos da tupla pelo indice e usar fatiamento países

paises = ("Brasil", "Praguai", "Uruguai", "mexico")
pais = paises[0]
print(pais) #Brasil

fatia = paises[1:3]
print(fatia) #('Praguai', 'Uruguai')

# ALTERAR UMA TUPLA
# Se tentarmos alterar um item da tupla, é gerado o erro "Objeto não suporta a atribuição de itens"

paises = brasil, praguai, uruguai, mexico
paises 



# CONVERTENDO UMA LISTA EM TUPLA
#             break  # Sai do loop e encerra o programa
lista_carros= ["Fusca", "Civic", "Corolla", "Onix"]
tupla_carros = tuple(lista_carros)  # Converte a lista em tupla
print(tupla_carros)  # Imprime a tupla convertida
#Resultado: ('Fusca', 'Civic', 'Corolla', 'Onix')

# CONVERTENDO UMA TUPLA EM LISTA
tupla = ("Brasil", "Praguai", "Uruguai", "Mexico")
lista = list(tupla)  # Converte a tupla em lista
print(lista)  # Imprime a lista convertida

# IMPRIMIR TUPLAS
# Imprime a tupla diretamente
print(tupla)  # Exibe a tupla completa
# Imprime cada elemento da tupla em uma linha separada
for pais in tupla:
    print(pais)  # Exibe cada país em uma linha separada

#DESEMPACOTANDO ELEMENTOS DAS TUPLAS
# Atribui os valores da tupla a variáveis separadas
tupla_carros = ("Fusca", "Civic", "Corolla", )
carro1, carro2, carro3, carro4 = tupla_carros
print(f"Carro1: {carro1}")  # Exibe o primeiro carro
print(f"Carro2: {carro2}")  # Exibe o segundo carro
print(f"Carro3: {carro3}")  # Exibe o terceiro carro

#Resultado:
# Carro1: Fusca
# Carro2: Civic
# Carro3: Corolla


#DESENPACOTANDO ELEMENTOS DA TUPLA USANDO ATRIBUIÇÃO MULTIPLA
tupla_carros = (
    "Fusca", "Civic", "Corolla", "Onix", #\ --> O backlash indica que a linha continua na próxima, mas está dando erro.
    "tucson", "hb20"
)
carro1, *carros = tupla_carros  # Atribui o primeiro carro a carro1 e o restante a carros
print(f"Carro1: {carro1}")  # Exibe o primeiro carro
print(f"Carros restantes: {carros}")  # Exibe os carros restantes como uma lista
# Resultado:
# Carro1: Fusca
# Carros restantes: ['Civic', 'Corolla', 'Onix', 'tucson', 'hb20']



