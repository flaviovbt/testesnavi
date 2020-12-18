import math #importando a blibioteca math

def fatorial(n): #função para calcular a fatorail
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1)

#print(math.log( 10 ))

X=[]; media=0 #definindo X como um vetor e criando a variável média

for i in range(0,10):
    if(i%2==0):
        X.append((3**i)+(7*fatorial(i))) #calcula o valor dos índices pares
    else:
        X.append((2**i)+(4*math.log(i))) #calcula o valor dos índices ímpares
    media+=X[i] #soma todos os elementos do vetor

media/=10 #calcula a média

#print(list(X))

print("O maior elemento de vetor é o ", max(X, key=float))
print("A média dos elementos contidos nesse vetor é ", round(media, 2))