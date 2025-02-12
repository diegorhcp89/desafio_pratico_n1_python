def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "♥" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato} - {novo_telefone_contato} - {novo_email_contato}")
    else:
        print("Índice de contato inválido.")
    return

def marcar_contato_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    else:
        print("Índice de contato inválido.")
    return

def deletar_contatos(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if 0 <= indice_contato_ajustado < len(contatos):
        del contatos[indice_contato_ajustado]
        print(f"Contato {indice_contato} deletado com sucesso")
    else:
        print("Índice de contato inválido.")
    return

contatos = []
while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar Contato")
    print("4. Marcar Contato como Favorito")
    print("5. Deletar Contato")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        email_contato = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        atualizar_nome_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
        marcar_contato_favorito(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contatos(contatos, indice_contato)
    elif escolha == "6":
        break

print("Programa finalizado")
