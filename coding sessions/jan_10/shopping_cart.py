class ShoppingCart:

    def __init__(self):
        self.item = {}

    def add_item(self, item, price):
        if item in self.item:
            self.item[item] += price
        else:
            self.item[item] = price
        print("Item added.")

    def remove_item(self, item):
        if item in self.item:
            del self.item[item]
            print("Item removed.")
        else:
            print("Item not found.")

    def view_cart(self):
        if not self.item:
            return "Cart is empty."

        data = "item       price\n-----------------------\n"
        for i, j in self.item.items():
            data += f"{i:<10} {j}\n"
        return data

    def calculate_total(self):
        return sum(self.item.values())

    def apply_discount(self):
        per = int(input("per"))
        per = self.calculate_total() * per / 100
        return per

    def checkout(self):
        total = self.calculate_total()
        discount = self.apply_discount()
        final = total - discount

        data = f"""
TOTAL BILL
----------------------------
{self.view_cart()}
TOTAL AMOUNT        : {total}
TOTAL DISCOUNT      : {discount}
FINAL AMOUNT        : {final}
        """
        print(data)
        self.item.clear()
        
        return "done"






a = ShoppingCart()

a.add_item("milk",50)
a.add_item("carrot",40)
a.add_item("candy",60)
a.add_item("choc",80)
a.add_item("water",330)
a.add_item("fr",455)
a.add_item("dvs",545)

print(a.checkout())