import pytest
from cash_register import CashRegister

def test_initialization_defaults():
    cr = CashRegister()
    assert cr.discount == 0
    assert cr.total == 0
    assert cr.items == []
    assert cr.previous_transactions == []

def test_add_item_single():
    cr = CashRegister()
    cr.add_item("apple", 5.00)
    assert cr.total == 5.00
    assert cr.items == ["apple"]
    assert len(cr.previous_transactions) == 1
    last = cr.previous_transactions[-1]
    assert last["item"] == "apple"
    assert last["price"] == 5.00
    assert last["quantity"] == 1

def test_add_item_quantity():
    cr = CashRegister()
    cr.add_item("banana", 2.5, 3)
    assert cr.total == 7.5
    assert cr.items == ["banana", "banana", "banana"]
    last = cr.previous_transactions[-1]
    assert last["quantity"] == 3
    assert last["amount"] == 7.5

def test_apply_discount_no_discount():
    cr = CashRegister()
    cr.add_item("item", 10, 2)
    msg = cr.apply_discount()
    assert msg == "There is no discount to apply."
    assert cr.total == 20

def test_apply_discount_with_discount():
    cr = CashRegister(discount=20)
    cr.add_item("item", 50, 1)
    cr.add_item("item2", 50, 1)
    msg = cr.apply_discount()
    assert msg == "After the discount, the total comes to $80."
    assert cr.total == 80

def test_void_last_transaction():
    cr = CashRegister()
    cr.add_item("a", 5, 2)
    cr.add_item("b", 3, 1)
    cr.void_last_transaction()
    assert cr.total == 10
    assert cr.items == ["a", "a"]
    assert len(cr.previous_transactions) == 1

def test_invalid_discount_prints(capsys):
    cr = CashRegister(discount=150)
    captured = capsys.readouterr()
    assert "Not valid discount" in captured.out
    assert cr.discount == 0
