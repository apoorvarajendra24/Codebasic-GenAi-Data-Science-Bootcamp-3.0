import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount('Amrendra Bahubali', 1000)
    assert account.owner == 'Amrendra Bahubali'
    assert account.balance == 1000

def test_deposit():
    account = BankAccount('Devasena Bahubali',100)
    account.deposit(10)
    account.deposit(20)
    assert account.balance == 130

    # test depositing a negative value
    with pytest.raises(ValueError):
        account.deposit(-10)

def test_withdrawal():
    account = BankAccount('Kattappa',100)
    account.withdraw(80)
    assert account.balance == 20
    
    # test if withdrawal amt greated than balance
    with pytest.raises(ValueError):
        account.withdraw(1200)

#@pytest.mark.skip(reason='just skipping')
def test_get_balance():
    account = BankAccount('Mahendra',200)
    assert account.get_balance() == 200