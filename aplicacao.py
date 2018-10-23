from sistema import *

def main():

    sistema = Sistema()

    comando = ""

    while comando != "exit" :
        print("em caso de alguma duvida digite help")
        comando = input()
        acao(sistema,comando)


def acao(sistema,comando):

    if comando == "init" :
        sistema.init()
    if comando == "touch":
        sistema.criar_arquivo()
    if comando == "ls" :
        sistema.listar_arquivos_locais()
    if comando == "status":
        sistema.status()
    if comando == "add":
        sistema.add()
    if comando == "reset":
        sistema.reset()
    if comando == "commit":
        sistema.commit()
    if comando == "log" :
        sistema.log()
    if comando == "create repo":
        sistema.criar_repositorio()
    if comando == "change repo":
        sistema.mudar_de_repositorio()
    if comando == "remote add":
        sistema.remote_add()
    if comando == "help":
        help()



def help():
    print("Comando touch -> criar um arquivo vazio\n"\
          "Comando ls -> listar arquivos do repositorio local\n" \
          "Comando init -> criar e entrar em um repositorio\n" \
          "Comando status -> mostra o estado atual do repositorio local\n" \
          "Comando add -> adiciona um arquivo modificado para a área de embarque\n" \
          "Comando reset -> retira um arquivo modificado para a área de embarque\n" \
          "Comando commit -> manda as modificações dos arquivos que estavam na área de embarque para o repositorio\n" \
          "Comando log -> lista todos os commits feitos no repositório\n" \
          "Comando create repo -> cria repositório fora do repositorio atual\n"\
          "Comando change repo -> muda de repositório local"
          "Comando remote add -> escolhe um dos repositorio para ser o remoto \n" \
          "Comando exit -> sai da aplicação")


if __name__ == '__main__':
    main()
