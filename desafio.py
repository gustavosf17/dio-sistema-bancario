from datetime import date

#Menu visual
barra = '=-='*8
menu = f'''{barra}
|    SEJA BEM-VINDO    |
{barra}
    [ s ] Sacar
    [ d ] Depositar
    [ e ] Extrato
    [ q ] Sair
{barra}
'''
saldo = 1000
extrato = ''
LIMITE_SAQUE = 3

while True:
    opc = str(input(menu + 'Digite sua escolha: ')).lower().strip()
    if opc == 's':
        saque = float(input('Qual valor à sacar? R$'))
        if saldo >= saque:
            if (LIMITE_SAQUE > 0) and ((saque <= 500) and (saque > 0)):
                saldo -= saque
                LIMITE_SAQUE -= 1
                extrato += f'-Saque no valor: R${saque:.2f}, Data:{date.today()}\n'
                print('--'*20)
                print('*Saque efetuado com Sucesso.')
                print('--'*20)
            else:
                print('--'*20)
                print('*Limite para Saque Indisponível.')
                print('--'*20)
        else:
            print('--'*20)
            print('*Saldo Indisponível para Saque.')
            print('--'*20)
    elif opc == 'd':
        deposito = float(input('Qual valor à depositar? R$'))
        if deposito > 0:
            saldo += deposito
            extrato += f'-Deposito no valor: R${deposito:.2f} Data:{date.today()}\n'
            print('--'*20)
            print('*Deposito efetuado com Sucesso.')
            print('--'*20)
        else:
            print('--'*20)
            print('*Valor Inválido. Tente Novamente.')
            print('--'*20)
    elif opc == 'e':
        print('--'*25)
        print('EXTRATO FINAL'.center(50))
        print('--'*25)
        print('Não foram feitas movimentações.'.center(50) if not extrato else extrato)
        print(f'SALDO FINAL: R${saldo:.2f}'.center(50))
        print('--'*25)
    elif opc == 'q':
        print('--'*20)
        print('*Obrigado por ser nosso cliente.')
        print('--'*20)
        break
    else:
        print('--'*20)
        print('*Opção Inválida. Tente Novamente.')
        print('--'*20)
