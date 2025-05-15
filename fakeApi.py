import os
import time

# Lista para armazenar os filmes
filmes = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    print("=== Menu de Compra de Filmes ===")
    print("1. Cadastrar Filme")
    print("2. Deletar Filme")
    print("3. Listar Filmes")
    print("4. Mostrar Valor Total da Compra")
    print("5. Sair")
    return input("Escolha uma opção: ")

def cadastrar_filme():
    clear()
    nome = input("Digite o nome do filme: ")
    preco = float(input("Digite o preço do filme: "))
    filmes.append({"nome": nome, "preco": preco})
    print(f"Filme '{nome}' cadastrado com sucesso!")
    time.sleep(2)

def deletar_filme():
    clear()
    listar_filmes()
    indice = int(input("Digite o índice do filme que deseja deletar: "))
    if 0 <= indice < len(filmes):
        removido = filmes.pop(indice)
        print(f"Filme '{removido['nome']}' deletado com sucesso!")
    else:
        print("Índice inválido!")
    time.sleep(2)

def listar_filmes():
    clear()
    if not filmes:
        print("Nenhum filme cadastrado.")
    else:
        print("=== Lista de Filmes ===")
        for i, filme in enumerate(filmes):
            print(f"{i}. {filme['nome']} - R$ {filme['preco']:.2f}")
    input("\nPressione Enter para continuar...")

def mostrar_valor_total():
    clear()
    total = sum(filme['preco'] for filme in filmes)
    print(f"Valor total da compra: R$ {total:.2f}")
    input("\nPressione Enter para continuar...")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_filme()
        elif opcao == "2":
            deletar_filme()
        elif opcao == "3":
            listar_filmes()
        elif opcao == "4":
            mostrar_valor_total()
        elif opcao == "5":
            clear()
            print("Saindo... Obrigado por usar a aplicação!")
            time.sleep(2)
            break
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()