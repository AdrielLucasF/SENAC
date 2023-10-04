contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

#01 Acessando informações de contato de Alice
info_alice = contatos['Alice']
telefone_alice = info_alice['telefone']
email_alice = info_alice['email']

# Imprimindo as informações de contato de Alice
print("Informações de contato de Alice:")
print("Telefone:", telefone_alice)
print("Email:", email_alice)

######################################################

#02 Adicionando um novo contato (por exemplo, "Eva")
contatos['Adriel'] = {'telefone': '84991486116', 'email': 'alfagundes76@.com'}

######################################################

#03 Modificando o email de Bob
contatos['Bob']['email'] = 'bob_@hotmail.com'

##########################################################
#04 Removendo o contato de Alice
del contatos['Alice']
############################################################
#05 Obtendo uma lista de nomes de pessoas em ordem alfabética
nomes_em_ordem_alfabetica = sorted(contatos.keys())

#ai ele imprime assim né?
print("Nomes em ordem alfabética:")
for nome in nomes_em_ordem_alfabetica:
    print(nome)


