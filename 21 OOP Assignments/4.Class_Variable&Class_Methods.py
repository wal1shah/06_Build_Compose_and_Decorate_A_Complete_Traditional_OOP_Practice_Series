class Bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bn1 = Bank()
print(bn1.bank_name)
Bank.change_bank_name("State Bank")
print(bn1.bank_name)
