class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        amount = price * quantity
        self.total += amount
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "amount": amount
        })

    def apply_discount(self):
        if self.discount == 0:
            return "There is no discount to apply."
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        if float(self.total).is_integer():
            self.total = int(self.total)
            return f"After the discount, the total comes to ${self.total}."
        return f"After the discount, the total comes to ${self.total}."

    def void_last_transaction(self):
        if not self.previous_transactions:
            self.total = 0
            return
        last = self.previous_transactions.pop()
        self.total -= last["amount"]
        qty = last["quantity"]
        for _ in range(qty):
            if self.items:
                self.items.pop()
