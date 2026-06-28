        #Importações
import time

saldo = 0

        #Funções da animação de carregamento
def depositar():
    print('DEPOSITANDO', end='', flush=True)
    for _ in range(3):
        time.sleep(1)
        print('.', end='', flush=True)
    time.sleep(0.5)
    print('\n')

def encerrando():
    print('Encerrando sistema', end='',flush=True)
    for x in range(3):
        time.sleep(0.7)
        print('.', end='', flush=True)
    time.sleep(0.5)
    print('\n')

def aguardando():
    print('Aguarde', end='', flush=True)
    time.sleep(1)
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(1)
    print()

def animated_cadastrando():
    print('Cadastrando', end='', flush=True)
    time.sleep(0.4)
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.6)
    print()

def carregamento():  
    for _ in range(3): 
        print('.', end='', flush=True) 
        time.sleep(0.3) 
    print()

        #Menu inicial e seleção de criação de conta
print(' ' * 10, '=========MENU INICIAL=========') 
choose = str(input('(1)>Criar uma conta< \n'))

        #Tentando novamente se acontecer de a seleção de opções não for correta (1)
while not choose.isnumeric() or choose != '1':
       carregamento()
       choose = str(input('Digite somente uma opção válida!!\n '))

        #Iniciando o cadastro informando o seu nome
print(' ' * 10, '=========CADASTRO========') 
nome = str(input('Digite o seu nome para Cadastrar-se: ')).strip().upper()
carregamento() 
senha = str(input('Agora crie uma senha somente com números: '))
carregamento()

        #tentandao novamente se a senha não for um número
while not senha.isnumeric(): 
    carregamento()
    senha = str(input('Inválido! Use uma senha APENAS com números: ')) 

        #Mensagem de sucesso na criação da conta e confirmção de senha
print('Senha criada com sucesso!!')
carregamento()
confirm = str(input('Agora confirme sua senha: ')) 

        #Tentando novamente se a confirmação de senha não for correspondente a senha
while confirm != senha: 
    carregamento()
    print('\nA senha não corresponde! Tente novamente.')
    confirm = str(input('Confirme sua senha: '))

        #Sucesso na confirmação de senha
print('Senha correta!') 
animated_cadastrando()
print(f'Ótimo {nome}!, Sua conta foi criad a com sucesso!!')
aguardando()

        #Logando na conta que foi criada
login = str(input('Agora vamos fazer LOGIN na sua conta:\n(1)>Para Logar<\n'))

        #tentando novamente se a opção selecionada não for igual a (1)
while login != '1':
    carregamento()
    login = str(input('Selecione somente uma opção válida! (1)'))

        #Logando o nome da conta
print(' ' * 10, '======LOGIN======')
login_nome = str(input('Nome da sua conta:  ')).strip().upper()

        #Tentando novamente se o nome do login não for correspondente ao nome da conta criada
while login_nome != nome:
    carregamento()
    login_nome = str(input('Essa conta não existe! tente novamente: ')).strip().upper()

        #Logando a senha da conta
login_senha = str(input('Senha da sua conta:  '))

        #Tentando novamente se a senha digitada não for correspondente a senha da conta criada
while login_senha != senha:
    carregamento()
    login_senha = str(input('Senha INCORRETA, tente novamente: '))

        #Mensagem de sucesso no login de acesso a conta
carregamento()
print(f'Login efetuado com sucesso! Seja bem-Vindo(a) a sua conta {nome.upper()}!')
print()
time.sleep(2)

        #Conta do banco
print(' ' * 10, '=====SEU BANCO PYTHON=====')
print(f'>>SEU SALDO: {saldo:.2f}')
print()
time.sleep(1)

        #Depósitando um valor em dinheiro
dep = str(input('DIGITE UM VALOR PARA DEPOSITAR: '))

while not dep.isnumeric() or int(dep) <=0:
    carregamento()
    dep = str(input('Digite somente um valor válido!!\n DEPÓSITO:'))

depositar()
dep = int(dep)

saldo += dep

print('DEPÓSITO CONCLUÍDO COM SUCESSO!!')
print()
time.sleep(1)

        #exibindo o seu novo saldo após o depósito
print(f'>>SEU NOVO SALDO: {saldo:.2f}')
carregamento()
print()

        #Escolha se deseja sacar uma certa quantia de dinheiro em sua conta
select = str(input('Você deseja sacar dinheiro na sua conta? \n>>(SIM) Para sacar \n>>(NÃO) para sair \n Digite:  ')).upper()

while select != 'SIM' and select != 'NAO' and select != 'NÃO':
    carregamento()
    select = str(input('Digite somente uma opção VÁLIDA! (Sim) ou (Não)\n')).upper()

if select == 'SIM':
    carregamento()
    print(' ' * 10, '=====MENU DE SAQUE=====')
    print(f'>> SEU SALDO ATUAL: {saldo:.2f}')
    carregamento()
    saque = str(input('Digite o valor que deseja sacar:  '))

    while not saque.isnumeric() or int(saque) > saldo or int(saque) <= 0:
        carregamento()
        saque = input('Digite somente um valor VÁLIDO para sacar: ')
    saque = int(saque)
    saldo -= saque
    print('\nSaque realizado com sucesso!!')
    time.sleep(0.4)
    print(f'>>Valor sacado: R$ {saque:.2f}')
    time.sleep(0.4)
    print(f'>>Seu saldo atual: R$ {saldo:.2f}')
    encerrando()

elif select == 'NÃO' or select == 'NAO':
    time.sleep(1)
    print('Ok, Depósito e Login concluídos com sucesso')
    encerrando()