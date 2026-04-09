#5
pais = input("Digite o nome do país:")
populacao = int(input("Digite sua população:"))
area = int(input("Digite sua área em km2::"))

densidade = populacao / area
print(f"A densidade demográfica do {pais} é de {densidade:.2f} hab/km2")