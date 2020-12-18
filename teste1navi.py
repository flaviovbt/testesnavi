def multiplo_49(x): #função para checar se o número é multiplo de 49
    
    if (x % 49 == 0): #se o resto da divisão de n/x for 0 (múltiplo)
        #print ("é multiplo")
        return True

    #print("não é multiplo")
    return False

def multiplo_37(x):   #função para checar se o número é multiplo de 37
    
    if (x % 37 == 0): #se o resto da divisão de n/x for 0 (múltiplo)
        #print ("é multiplo")
        return True

    #print("não é multiplo")
    return False

contador=0 #declarando o contador dos números

# O range(0, numero + 1, 2) cria um objeto do tipo range.
# Iniciando com 0 indo até o numero, pulando de 2 em 2.
# Como 0 é par e está com saltos de 2 os numeros sempre serão par.
for i in range(2, 5000000 + 1, 2): 
    if multiplo_37(i) and multiplo_49(i): #verifica se o número atende os requisitos
        contador+=1 #se ele atender, soma-se 1

print("A quantidade de números pares  múltiplos de 37 e 49 no intervalo de 1 a 5000000 é ", contador)