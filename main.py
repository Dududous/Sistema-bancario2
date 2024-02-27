global saldo
saldo = 0
operacoes = [[],[]]
limsaque = 0
contas = []
usuarios = []

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    num_conta = 0

    def __init__(self, agencia, usuario):
        Conta.num_conta += 1
        self.agencia = agencia
        self.numero = Conta.num_conta
        self.usuario = usuario
        contas.append(self)
        
def adicionar_usuario():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    cpf = input("CPF: ")
    endereco = input("Endereço (logradouro, número, bairro, cidade/estado): ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado.")
            return
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def adicionar_conta():
    cpf = input("Digite o CPF do usuário: ")
    usuario_existente = False  
    for usuario in usuarios:
        if usuario.cpf == cpf:
            usuario_existente = True
            break
    if not usuario_existente:
        print("Usuário não encontrado.")
        return
    agencia = "0001"
    usuario = next((u for u in usuarios if u.cpf == cpf), None)
    nova_conta = Conta(agencia, usuario)
    print(f"Conta criada com sucesso para o usuário {usuario.nome}. Número da conta: {nova_conta.numero}")

def depositar(valor):
    global saldo
    if valor < 0:
        print("Operação Inválida")
    else:
        operacoes[0].append(valor)
        saldo += valor
        print(f"Depósito de R${valor}")
    return saldo 

def sacar(valor):
    global saldo
    global limsaque
    if valor < 0:
        print("Operação Inválida")
    elif valor > 500:
        print("Operação Inválida")
    elif limsaque > 2:
        print("Limite de Saque atingido")
    elif saldo < valor:
        print("Saldo Insuficiente")
    else:
        operacoes[1].append(valor)
        saldo -= valor
        limsaque += 1
        print(f"Saque de R${valor}")

def extrato():
    print("=========EXTRATO=========")
    if len(operacoes[0]) == 0 and len(operacoes[1]) == 0:
        print("Sem operações registradas")
    for c in operacoes[0]:
        print(f"Depósito de R${c}")      
    for c in operacoes[1]: 
        print(f"Saque de R${c}")
    print("==========TOTAL==========") 
    print(f"R${sum(operacoes[0])-sum(operacoes[1])}")       
    print("===========FIM===========")       

def menu():
    resp = input("Digite a opção: ")
    if resp == 'd':
        valor = int(input("Digite o Valor: "))
        depositar(valor)
    elif resp == 's':
        valor = int(input("Digite o Valor: "))
        sacar(valor)
    elif resp == 'e':
        extrato()
    elif resp == 'c':
        adicionar_conta()  
    elif resp == 'u':
        adicionar_usuario()
    elif resp == "q":
        return False
    else:
        print("Digite uma opção válida")
        
while True:
    if menu() == False:
        break
