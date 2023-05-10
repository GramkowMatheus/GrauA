import csv
import os
import figurinha
import random

class usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = 0
    
    def validarLogin(self, login, senha):
        return self.login == login and self.senha == senha
    
class album:
    def __init__(self, login):
        self.login = login
        self.figurinhas = []
        self.ler_do_csv()
        
    def adicionar_figurinha(self, figurinha):
        self.figurinhas.append(figurinha)
        
    def verificar_figurinha(self, num_figurinha):
        for figurinha in self.figurinhas:
            if figurinha.numero == num_figurinha:
                return figurinha
        return None
        
    def ler_do_csv(self):
        if not os.path.exists(f"{self.login}.csv"):
            return
        with open(f"{self.username}.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                num_figurinha, status = row
                self.adicionar_figurinha(figurinha(num_figurinha, status))
                
    def salvar_no_csv(self):
        with open(f"{self.login}.csv", "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for figurinha in self.figurinhas:
                writer.writerow([figurinha.numero, figurinha.status])

class verificaAlbum:
    def __init__(self, numero, status="não colada"):
        self.numero = numero
        self.status = status

class pacote:
    def __init__(self):
        self.figurinhas = {}  
        self.colecao = set()  
         
        for numero in range(1, 221):
            self.figurinhas[(numero)] = f"Figurinha {numero}"
        
        self.sortearFigurinhas(3)
        
    def sortearFigurinhas(self, qtd):
        """Sorteia a quantidade de figurinhas especificada e adiciona na coleção do usuário."""
        for i in range(qtd):
            # sorteia um número de figurinha que o usuário não possui
            numero = random.choice(list(set(self.figurinhas.keys()) - self.colecao))
            
            # adiciona a figurinha na coleção do usuário
            self.colecao.add(numero)
            
            # exibe a figurinha sorteada
            print(f"Parabéns, você ganhou a figurinha {numero}: {self.figurinhas[numero]}!")
    
    def abrir_pacote(self):
        self.sortear_figurinhas(3)
                
class repetida:
    
    def disponibilizar_figurinha(self, numero):
        ##Disponibiliza a figurinha especificada para troca.
        if numero in self.colecao and numero not in self.figurinhas_disponiveis:
            self.figurinhas_disponiveis.add(numero)  
            print(f"A figurinha {numero} está agora disponível para troca!")
        else:
            print("Figurinha inválida ou já disponível para troca.")

class Troca:
    def __init__(self, usuario_inicial, parceiro_troca, figurinha_oferecida, figurinha_desejada, status='pendente'):
        self.usuario_inicial = usuario_inicial
        self.parceiro_troca = parceiro_troca
        self.figurinha_oferecida = figurinha_oferecida
        self.figurinha_desejada = figurinha_desejada
        self.status = status

class SistemaTrocas:
    def __init__(self):
        self.trocas = []

    def adicionar_troca(self, troca):
        self.trocas.append(troca)

    def listar_trocas_pendentes(self, usuario):
        pendentes = []
        for troca in self.trocas:
            if troca.parceiro_troca == usuario and troca.status == 'pendente':
                pendentes.append(troca)
        return pendentes

    def revisar_troca(self, troca):
        # exibe as informações da troca e permite ao usuário aceitar ou rejeitar
        pass

    def aceitar_troca(self, troca):
        troca.status = 'aceita'
        # atualiza as coleções de figurinhas dos usuários envolvidos na troca
        pass

    def rejeitar_troca(self, troca):
        troca.status = 'rejeitada'

class SistemaSolicitacoes:
    def __init__(self):
        self.solicitacoes = []

    def adicionarSolicitacao(self, solicitacao):
        self.solicitacoes.append(solicitacao)

    def listarSolicitacoes_pendentes(self, usuario):
        pendentes = []
        for solicitacao in self.solicitacoes:
            if solicitacao.usuario_destino == usuario and solicitacao.status == 'pendente':
                pendentes.append(solicitacao)
        return pendentes

    def revisarSolicitacao(self, solicitacao):
        # exibe as informações da solicitação e permite ao usuário aceitar ou rejeitar
        pass

    def aceitarSolicitacao(self, solicitacao):
        solicitacao.status = 'aceita'
        # atualiza as coleções de figurinhas dos usuários envolvidos na troca
        pass

    def rejeitarSolicitacao(self, solicitacao):
        solicitacao.status = 'rejeitada'

def login():
    login = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    return usuario(login, senha)

def cadastrarUsuario(self, login, senha):
        self.login = input("Digite o nome de usuário desejado: ")
        self.senha = input("Digite a senha desejada: ")
        return print("Parabens Você esta dadastrado")

def criarAlbum(usuario):
    num_figurinhas = 220
    for i in range(1, num_figurinhas+1):
        usuario.album.adicionar_figurinha(figurinha(i))
    usuario.album.salvar_no_csv()

def acessarAlbum(usuario):
    print("Álbum do usuário", usuario.login)
    print("Escolha uma das opções abaixo:")
    while True:
        print("1 - Ver figurinhas")
        print("2 - Adicionar figurinha")
        print("3 - Colar figurinha")
        print("4 - Disponibilizar figurinha para troca")
        print("5 - Ver solicitações de troca")
        print("6 - Sair do álbum")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            for figurinha in usuario.album.figurinhas:
                print(f"Figurinha {figurinha.numero} - {figurinha.status}")
        elif opcao == "2":
            num_figurinha = int(input("Digite o número da figurinha a ser adicionada: "))
            figurinha_existente = usuario.album.verificar_figurinha(num_figurinha)
            if figurinha_existente:
                print("Você já possui essa figurinha.")
            else:
                usuario.album

def colarFigurinha(self, numero):
        """Cola a figurinha especificada no álbum."""
        if numero in self.colecao and numero not in self.figurinhas_coladas:
            self.figurinhas_coladas.add(numero)  # adiciona a figurinha no álbum
            self.colecao.remove(numero)  # remove a figurinha da coleção do usuário
            print(f"A figurinha {numero} foi colada no álbum!")
        else:
            print("Figurinha inválida ou já colada no álbum.")
    
cadastrarUsuario()