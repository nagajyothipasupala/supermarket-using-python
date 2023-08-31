class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Cart:
    def __init__(self):
        self.items=[]
    def add_item(self,product,quantity):
        self.items.append((product,quantity))
    def calculate_total(self):
        total=0
        for product,quantity in self.items:
            total+=product.price*quantity
        return total
    def generate_receipt(self):
        receipt="Receipt\n"
        receipt+="--------------------\n"
        for product,quantity in self.items:
            receipt+=f"{product.name}X{quantity}:${product.price*quantity}"
        receipt+="---------------------\n"
        receipt+=f"total:${self.calculate_total():.2f}\n"
        return receipt            
