
alunos = {}

for i in range(1, 4):
    nome = input(f"Digite o nome do {i}º aluno: ")
    idade = int(input(f"Digite a idade do {i}º aluno: "))
    nota_final = float(input(f"Digite a nota final do {i}º aluno: "))
    
    # Armazena as informações no dicionário
    alunos[f'Aluno {i}'] = {'nome': nome, 'idade': idade, 'nota_final': nota_final}

# Exibe o dicionário completo
print("\nInformações dos alunos:")
for chave, valor in alunos.items():
 print(f"{chave}: {valor}")

# Calcula a média das notas finais
media_notas = sum(aluno['nota_final'] for aluno in alunos.values()) / 3

# Exibe a média das notas finais com 2 casas decimais
print(f"\nMédia das notas finais: {media_notas:.2f}")
