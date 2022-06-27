novaVerificacao = str

print('Inicio do Programa')
peso =  int(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))  
def calcula_imc(peso, altura):        
            imc = peso/altura**2
            print('IMC:{:.1f} '.format(imc))
            if imc < 18.5:
                print('A baixo do peso')
            elif imc < 25:
                print('Seu peso esta normal')
            elif imc < 30:
                print('Você esta com sobrepeso')
            else:
                print('Vocẽ esta obeso')
calcula_imc(peso, altura)
novaVerificacao = str(input(('Voce deseja fazer mais uma checagem? (s/n)')))
while novaVerificacao == "s":
    peso = int(input('digite seu peso: '))
    altura = int(input('Digite a sua altura: '))
    calcula_imc(peso,altura)
    novaVerificacao = str(input(('Voce deseja fazer mais uma checagem? (s/n)')))
while novaVerificacao != "s" and novaVerificacao != "n":
        print('Foi digitado um parametro incorreto favo digitar "s" para sim ou "n" para não')
        novaVerificacao = str(input(('Tente novamente! (s/n)')))
        while novaVerificacao == "s":
              peso = int(input('digite seu peso: '))
              altura = int(input('Digite a sua altura: '))
              calcula_imc(peso,altura)
              novaVerificacao = str(input(('Voce deseja fazer mais uma checagem? (s/n)')))
if novaVerificacao == "n": 
    print('Termino de programa')
