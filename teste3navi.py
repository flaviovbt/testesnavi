notas = {}; maiornota = 0 #declarando o dicionário e uma variável de controle

for i in range(1,6):
    nome = input("Insira o nome do aluno: ") #inserindo os dados doas alunos
    nota = int(input("Insira a sua nota: "))
    notas[nome] = nota #adicionando os dados do aluno para o dicionário
    if nota > maiornota: #se a nota do ultimo aluno for maior que a maior nota, este aluno passa a ter a maior nota
        maiornota = nota
        nomedomaior=nome

print('O aluno com a maior nota foi o ', nomedomaior)
print('A sua nota foi ', maiornota)