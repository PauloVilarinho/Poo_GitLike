from classes import *


def rep_local_linkado(foo):
    def decorated(*args,**kwargs):
        if args[0].rep_local != None :
            return foo(*args,**kwargs)
        else :
            print("Nenhum repositorio local ligado ao sistema. Entre em um para executar essa ação")
    return decorated

def rep_remoto_linkado(foo):
    def decorated(*args,**kwargs):
        if args[0].rep_remoto != None :
            return foo(*args,**kwargs)
        else :
            print("Nenhum repositorio remoto ligado ao sistema. Entre em um para executar essa ação")
    return decorated

class Sistema :

    def __init__(self):
        self.repositorios = []
        self.rep_local = None
        self.rep_remoto = None


    def init(self):
        if self.rep_local == None :
            nome = input("Nome do repositório ")
            repositorio = Repositorio(nome)
            self.repositorios.append(repositorio)
            self.rep_local = repositorio
        else :
            print("Já está em um repositório")

    def criar_repositorio(self):
        nome = input("Nome do repositório ")
        repositorio = Repositorio(nome)
        self.repositorios.append(repositorio)

    def mudar_de_repositorio(self):
        print("Repositórios disponíveis: ")
        self.listar_repositorios()
        nome = input("Digite qual repositorio deseja utilizar como remoto ")
        if nome in [rep.nome for rep in self.repositorios]:
            for repr in self.repositorios :
                if repr.nome == nome :
                    self.rep_local = repr
                    break
        else :
            print("Repositorio não existe")

    def listar_repositorios(self):
        for repositorio in self.repositorios:
            print(repositorio)

    def remote_add(self):
        print("Repositórios disponíveis: ")
        self.listar_repositorios()
        nome = input("Digite qual repositorio deseja utilizar como remoto ")
        if nome in [rep.nome for rep in self.repositorios]:
            for repr in self.repositorios :
                if repr.nome == nome :
                    self.rep_remoto == repr
                    break
        else :
            raise NameError("Repositorio não existe")

    def remote_remove(self):
        self.rep_remoto = None

    @rep_local_linkado
    def status(self):
        self.rep_local.status()

    @rep_local_linkado
    def listar_arquivos_locais(self):
        print("Arquivos no repositorio local:")
        self.rep_local.listar()

    @rep_local_linkado
    def criar_arquivo(self):
        self.rep_local.novo_arquivo()

    @rep_local_linkado
    def get_arquivo(self):
        nome = input("Qual o nome do arquivo a ser buscado?")
        self.rep_local.criar_arquivo(nome)

    @rep_local_linkado
    def deletar_arquivo(self):
        nome = input("Qual arquivo deve ser deletado?")
        self.rep_local.deletar_arquivo(nome)

    @rep_local_linkado
    def add(self):
        nome = input("Qual o nome do arquivo a ser Adicionado?")
        self.rep_local.add(nome)

    @rep_local_linkado
    def reset(self):
        nome = input("Qual o nome do arquivo a ser Retirado?")
        self.rep_local.reset(nome)

    @rep_local_linkado
    def commit(self):
        self.rep_local.commit()

    @rep_local_linkado
    def log(self):
        self.rep_local.log()
