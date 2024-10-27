import account, person
class Bank:
    def __init__(
            self,
            agency: list[int] | None = None,
            customer: list[person.Person] | None = None,
            account: list[int] | None = None
            ):
        self.agency = agency or []
        self.customer = customer or []
        self.account = account or []

    def _check_agency(self, account):
        if account.get_agency in self.agency:
            return True
        return False

    def _check_customer(self, customer):
        if customer in self.customer:
            return True
        return False

    def _check_account(self, account):
        if account.get_account in self.account:
            return True
        return False
    
    def _check_customer_account(self, customer, account):
        if account is customer.get_account:
            return True
        return False

    def authenticate(self, customer: person.Person, account: account.Account):
        if self._check_agency(account) and self._check_customer(customer) and self._check_account(account) and self._check_customer_account(customer, account):
            return True
        return False
        
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.customer!r}, {self.account!r})'
        return f'{class_name} {attrs}'

if __name__ == "__main__":
    c1 = person.Person('jhones', 'soares', '98-8')
    c1.get_account = account.Account(1, 2)

    c2 = Bank()
    c2.account.extend([c1.get_account])
    c2.customer.extend([c1])
    c2.agency.extend([1, 2])
    print(c2.authenticate(c1, c1.get_account))