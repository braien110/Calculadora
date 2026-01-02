def menu():
    num1 = int(input('Qual o primeiro numero? \n'))

    operador = int(input('''Qual sera o operador?
1 - Adicao
2 - Subtracao
3 - Multiplicacao
4 - Divisao
5 - Sair
Insira apenas Numeros
'''))

    if operador == 5:
        print('Obrigado por ter apoiado nosso projeto :)')
        exit()

    num2 = int(input('Qual o segundo numero? \n'))
    operacao(num1, operador, num2)


def operacao(num1, operador, num2):
    match operador:
        case 1:
            resultado = num1 + num2
        case 2:
            resultado = num1 - num2
        case 3:
            resultado = num1 * num2
        case 4:
            if num2 == 0:
                print('Nao podemos dividir por 0')
                menu()
                return
            resultado = num1 / num2
        case _:
            print('Erro no operador, escolha um numero valido')
            menu()
            return

    reset = input(
        f'O resultado da sua conta e {resultado}\nDeseja realizar uma nova conta? (s/n): '
    )

    if reset.lower() == 's':
        menu()
    else:
        print('Obrigado por ter apoiado nosso projeto :)')
        exit()


menu()
