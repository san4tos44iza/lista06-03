n1 = 0
n2 = 1
numero_sequencia = int(input("Quantos termos quer mostrar? "))
print('{} -> {}'.format(n1,n2), end='')
conta = numero_sequencia -2
while conta !=0:

    n3 = n1 + n2
    print(' -> {}'.format(n3),end='')
    n1 = n2
    n2 = n3
    conta = conta-1
print ( " fim ")