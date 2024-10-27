from abc import ABC
from dataclasses import dataclass
import account


@dataclass
class Person(ABC):
    __name: str
    __surname: str
    __cpf: str

    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def get_name(self, value: str):
        self.__name = value

    @property
    def get_surname(self):
        return self.__surname
    @get_surname.setter
    def get_surname(self, value: str):
        self.__surname = value    

    @property
    def get_cpf(self):
        return self.__cpf
    @get_cpf.setter
    def get_cpf(self, value: str):
        self.__cpf = value 


class Person(Person):
    def __init__(self, name: str, surname: str, cpf: int, ) -> None:
        super().__init__(name, surname, cpf)
        self.__account: account.Account | None = None

    @property
    def get_account(self):
        return self.__account
    @get_account.setter
    def get_account(self, value: str):
        self.__account = value     

if __name__ == '__main__':
    #c1 = Customer('jhones', 'soares', '123', 321)
    
    ...