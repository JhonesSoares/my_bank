from dataclasses import dataclass
import person

@dataclass
class Account:
    __agency: int
    __account: int
    __balance: float = 0.0

    @property
    def get_agency(self):
        return self.__agency
    @get_agency.setter
    def get_agency(self, value):
        self.__agency = value

    @property
    def get_account(self):
        return self.__account
    @get_account.setter
    def get_account(self, value):
        self.__account = value    

    def get_balance(self):
        return self.__balance
    
    def deposit(self, value):
        if value > 0:
            self.__balance += value
            print(f"Depósito de R$ {value:.2f} realizado com sucesso!")
        else:    
            print(f"O valor do depósito deve ser positivo.")

    def withdraw(self, value):
        if value > 0:
            if value <= self.__balance:
                self.__balance -= value
                print(f"Saque de R${value:.2f} realizado com sucesso!")
            else:    
                print("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def display_data(self, name, surname, cpf):
        print(f"\nNome: {name} {surname}")
        print(f"CPF: {cpf}")
        print(f"Saldo atual: R$ {self.get_balance():.2f}")



if __name__ == '__main__':
    c1 = person.Person('jhones', 'soares', '0-978')
    c1.account = Account(1, 2)

    print(c1)
    print(c1.account.__agency)