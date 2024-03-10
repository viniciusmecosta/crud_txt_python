import os
data_file = 'data.txt'
def get_users():
    users = []
    if os.path.exists(data_file):
        with open(data_file) as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(';')
                    if len(parts) == 4:
                        users.append([int(parts[0]), parts[1], parts[2], parts[3]])
    return users

def save_users(users):
    with open(data_file, 'w') as f:
        for user in users:
            f.write(f"{user[0]};{user[1]};{user[2]};{user[3]}\n")

def add_user(users):
    next_id = 1
    if users:
        for user in users:
            next_id = max(next_id, user[0] + 1)
    name = input("Nome: ")
    surname = input("Sobrenome: ")
    age = input("Idade: ")
    users.append([next_id, name, surname, age])
    print("Usuário adicionado com sucesso.")
    save_users(users)

def edit_user(users):
    user_id = int(input("ID do usuário para editar: "))
    found = False
    for i, user in enumerate(users):
        if user[0] == user_id:
            name = input("Novo nome: ")
            surname = input("Novo sobrenome: ")
            age = input("Nova idade: ")
            users[i] = [user_id, name, surname, age]
            print("Usuário editado com sucesso.")
            found = True
            break
    if not found:
        print("Usuário não encontrado.")
    save_users(users)

def delete_user(users):
    user_id = int(input("ID do usuário para deletar: "))
    found = False
    for i, user in enumerate(users):
        if user[0] == user_id:
            del users[i]
            print("Usuário deletado com sucesso.")
            found = True
            break
    if not found:
        print("Usuário não encontrado.")
    save_users(users)

def list_users(users):
    for user in users:
        print(f"\n{'*' * 20}\nID: {user[0]}\nNome: {user[1]}\nSobrenome: {user[2]}\nIdade: {user[3]}\n{'*' * 20}\n")

def main():
    users = get_users()
    while True:
        choice = input("1. Adicionar usuário\n2. Editar usuário\n3. Deletar usuário\n4. Listar usuários\n0. Sair\nEscolha: ")
        if choice == '1':
            add_user(users)
        elif choice == '2':
            edit_user(users)
        elif choice == '3':
            delete_user(users)
        elif choice == '4':
            list_users(users)
        elif choice == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()
