
total_filhos = 0
numero_homem = 0
altura_total_mulher = 0
numero_mulher = 0
maior_altura = float('-inf')  
menor_altura = float('inf')   
total_pessoas = 0  

while True:
    
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura em cm: "))
    sexo = input("Digite seu sexo ('m' para masculino ou 'f' para feminino): ").lower()
    filhos = int(input("Quantos filhos você tem: "))
    
    
    total_filhos += filhos
    total_pessoas += 1
    
    if sexo == 'f':
        numero_mulher += 1
        altura_total_mulher += altura
    elif sexo == 'm':
        numero_homem += 1
    
    
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    

    continuidade = input("Quer continuar ou parar ('s' para continuar e 'n' para parar): ").lower()
    if continuidade == 'n':
        break


print(f"\nA maior altura do grupo é {maior_altura} cm e a menor altura é {menor_altura} cm.")


if numero_mulher > 0:
    media_altura_mulher = altura_total_mulher / numero_mulher
    print(f"A média de altura das mulheres é {media_altura_mulher:.2f} cm.")
else:
    print("Não há mulheres no grupo para calcular a média de altura.")


print(f"Número total de homens: {numero_homem}")


if total_pessoas > 0:
    media_filhos = total_filhos / total_pessoas
    print(f"A média de filhos do grupo é {media_filhos:.2f}.")
else:
    print("Não há pessoas no grupo para calcular a média de filhos.")
