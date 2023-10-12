def calc_imc (altura, peso):
    imc = peso // (altura * altura)
    print (f'SEU IMC É DE {imc:.2f}')
    if imc <= 17:
        print ('Muito Abaixo do peso !')
    elif imc > 17 and imc < 18.49:
        print ('Abaixo do peso !')
    elif imc > 18.5 and imc < 24.99:
        print ('Peso Normal')
    elif imc > 25 and imc < 29.99:
        print ('Acima do Peso !')
    elif imc > 30 and imc < 34.99:
        print ('Obesidade Nivel 1')
    elif imc >= 35 and imc < 39.99:
        print ('Obesidade Nivel 2')
    else:
        print ('Obesidade Nivel 3')


print('CALCULADORA DE IMC\nINFORME SUA ALTURA EM METROS E EM SEGUIDA SEU PESO\nIMC ABAIXO DE 17 = MUITO ABAIXO DO PESO\nIMC ENTRE 17 E 18,49 = ABAIXO DO PESO\nIMC ENTRE 18.5 E 24.99 = PESO NORMAL\nIMC ENTRE 25 E 29.99 = ACIMA DO PESO !\nIMC ENTRE 30 E 34,99 = OBESIDADE NIVEL 1\nIMC ENTRE 35 E 39,99 = OBESIDADE NIVEL 2\nIMC ACIMA DE 40 = OBESIDADE NIVEL 3 ')

altura = float (input('DIGITE A SUA ALTURA(m): '))
peso = int(input('DIGITE SEU PESO (kg): '))
calc_imc(altura,peso)