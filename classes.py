from datetime import datetime

class Arquivo:

    def __init__(self,nome):
        self.nome = nome
        self.linhas = []
        self.mudancas = [Mudanca(self,"New File")]
        self.tracked = False
        self.changed = True

    def __str__(self):
        return self.nome

    def new_line(self,linha):
        self.mudancas.append(Mudanca(self,"New Line"))
        self.tracked = False
        self.changed = True

    def stagged(self):
        return self.tracked and self.changed

    def unstagged(self):
        return not self.tracked and self.changed

    def add(self):
        for mudanca in self.mudancas :
            if  not mudanca.commited :
                mudanca.stage()
        self.tracked = True

    def reset(self):
        for mudanca in self.mudancas :
            if  not mudanca.commited :
                mudanca.unstage()
        self.tracked = False

    def commit(self):
        mudancas = []
        for mudanca in self.mudancas:
            if mudanca.ready_to_commit():
                mudanca.commit()
                mudancas.append(mudanca)
        self.changed = False
        return mudancas


class Mudanca:

    def __init__(self,arquivo,tipo):
        self.tipo = tipo
        self.arquivo = arquivo
        self.stagged = False
        self.commited = False

    def stage(self):
        self.stagged = True

    def unstage(self):
        self.stagged = False

    def ready_to_commit(self):
        return self.stagged and not self.commited

    def commit(self):
        self.commit = True

class Commit:

    def __init__(self,mudancas,comment):
        self.comment = comment
        self.mudancas = mudancas
        self.time = datetime.now()
        self.sincronizado = False

    def __str__ (self):
        return str(self.time)+"||"+str(self.comment)

class Repositorio:

    def __init__(self,nome):
        self.nome = nome
        self.arquivos = []
        self.commits = []

    def __str__(self):
        return self.nome


    def novo_arquivo(self):
        nome = input("Digite o nome do novo arquivo:")
        if nome in [a.nome for a in self.arquivos]:
            raise NameError("Arquivo com esse nome já existente")
        else :
            arquivo = Arquivo(nome)
            self.arquivos.append(arquivo)

    def get_arquivo(self,nome):
        if nome in [a.nome for a in self.arquivos]:
            for arq in self.arquivos :
                if arq.nome == nome :
                    return arq
        else :
            raise NameError("Arquivo com esse nome não existe")

    def listar(self):
        for arq in self.arquivos:
            print(arq)

    def add(self,nome):

        if nome in [a.nome for a in self.arquivos]:
            for arq in self.arquivos :
                if arq.nome == nome :
                    arq.add()
                    break
        else :
            print("Arquivo com esse nome não existe")

    def reset(self,nome):

        if nome in [a.nome for a in self.arquivos]:
            for arq in self.arquivos :
                if arq.nome == nome :
                    arq.reset()
                    break
        else :
            print("Arquivo com esse nome não existe")

    def commit(self):
        if len(self.get_staged_changes()) >= 1:
            mudancas = []
            for arquivo in self.arquivos:
                mudancas += arquivo.commit()
            comentario = input("Digite o comentario do commit:")
            self.commits.append(Commit(mudancas,comentario))
        else :
            print("Nenhuma mudança para ser commitada")


    def get_staged_changes(self):
        return [i for i in self.arquivos if i.stagged()]

    def get_unstaged_changes(self):
        return [i for i in self.arquivos if i.unstagged()]


    def status(self):
        print("Unstagged Changes:")
        for arquivo in self.get_unstaged_changes():
            print(arquivo)
        print("Stagged Changes:")
        for arquivo in self.get_staged_changes():
            print(arquivo)

    def log(self):
        for commit in self.commits:
            print(commit)
