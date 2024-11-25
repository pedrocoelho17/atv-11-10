from models.usuario import Usuario
from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    services = UsuarioService(repository)

    while True:

        print("=== SENAI SOLUTION === ")
        print("1 - Adicionar usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        menu = int(input("Escolha uma opção: "))

        match menu:

            case 1:
                os.system("cls || clear")
                nome = str(input("Digite o seu nome: "))
                email = str(input("Digite o seu email: "))
                senha = str(input("Digite a sua senha: "))

                usuario = Usuario(name=nome, email=email, password=senha)
                session.add(usuario)
                session.commit()
                print()
            case 2:
                os.system("cls || clear")
                email_usuario = str(input("Digite o email do usuário: "))
                usuario = session.query(Usuario).filter_by(email=email_usuario).first()
                if usuario:
                    os.system("cls || clear")
                    print(f"{usuario.name} - {usuario.email} - {usuario.password}")
                else:
                    print("Usuário não encontrado!")
            case 3:
                os.system("cls || clear")
                email_usuario = str(input("Digite o email do usuário: "))
                usuario = session.query(Usuario).filter_by(email=email_usuario).first()
                if usuario:
                    os.system("cls || clear")
                    usuario.name = str(input("Digite o seu nome: "))
                    usuario.email = str(input("Digite o seu email: "))
                    usuario.password = str(input("Digite a sua senha: "))
                    session.commit()
                else:
                    print("Usuário não encontrado!")
            case 4:
                os.system("cls || clear")
                email_usuario = str(input("Digite o email do usuário: "))
                usuario = session.query(Usuario).filter_by(email=email_usuario).first()
                if usuario:
                    os.system("cls || clear")
                    session.delete(usuario)
                    session.commit()
                    print("Usuário deletado com sucesso!")
                else:
                    print("Usuário não encontrado!")
            case 5:
                os.system("cls || clear")
                print("\nListando usuários do banco de dados")
                os.system("cls || clear")
                listar_todos_usuarios = session.query(Usuario).all()
                for usuario in listar_todos_usuarios:
                    print(f"{usuario.name} - {usuario.email} - {usuario.password}")
            case 0:
                break

if __name__ == "__main__":
    os.system("cls||clear")
    main()







    