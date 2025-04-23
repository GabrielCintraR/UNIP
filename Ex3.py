lista1 = [int(input("Digite um número inteiro para a lista 1: ")) for _ in range(5)]
lista2 = [int(input("Digite um número inteiro para a lista 2: ")) for _ in range(5)]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

uniao = conjunto1 | conjunto2 
intersecao = conjunto1 & conjunto2 
diferenca = conjunto1 - conjunto2
diferenca_simetrica = conjunto1 ^ conjunto2  

print("União dos dois conjuntos:", uniao)
print("Interseção dos dois conjuntos:", intersecao)
print("Diferença do primeiro conjunto em relação ao segundo:", diferenca)
print("Diferença simétrica entre os dois conjuntos:", diferenca_simetrica)
