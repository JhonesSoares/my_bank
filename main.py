import person, account, bank
from validate_cpf import cpf_user, validating_users_cpf

def main():
    print("\n---Bem-vindo ao Banco MyBank!---")
    
    # Solicitando dados do usuário
    name = input("\nInforme seu nome: ")
    surname = input("Informe seu sobrenome: ")

    cpf = input("Informe seu CPF: ")
    cpf = cpf.replace('.', '').replace('-', '')
    if cpf_user(cpf) == False: return print(f"\nCPF INCORRETO!")
    if validating_users_cpf(cpf) == False: return print(F'\nCPF INVÁLIDO')

    agency_user = int(input('Informe sua Agência: '))
    account_user = int(input('Informe sua conta: '))

    # Criando uma instância da conta bancária
    conta_cliente = person.Person(name, surname, cpf )
    conta_cliente.get_account = account.Account(agency_user, account_user)

    mybank = bank.Bank()
    mybank.agency.extend([1, 2, 3, 4])
    mybank.customer.extend([conta_cliente])
    mybank.account.extend([18])

    if mybank.authenticate(conta_cliente, conta_cliente.get_account) == False:
        print(f'\nConta Inválida!')
        return 
    
    print("\n---Acesso Liberado---")

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar saldo")
        print("2. Realizar depósito")
        print("3. Realizar saque")
        print("4. Encerrar")
        
        opcao = input("Opção: ")

        if opcao in '1, 2, 3, 4':
        
            if opcao == '1': conta_cliente.get_account.display_data(conta_cliente.get_name, conta_cliente.get_surname, conta_cliente.get_cpf)

            if opcao == '2':
                value = float(input("\nInforme o valor para depósito: R$ "))
                conta_cliente.get_account.deposit(value)

            if opcao == '3':
                value = float(input("\nInforme o valor para saque: R$ "))
                conta_cliente.get_account.withdraw(value)

            if opcao == '4':
                print("\nEncerrando o uso da aplicação. Obrigado!")
                break
        
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
    print()