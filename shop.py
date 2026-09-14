class Customer:
    def __init__(self,name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(amount*0.03)

    def get_discount_rate(self):
        if self.grade == "vip":
            return 0.10
        return 0.03

    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def total_price(self):
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

    def add_item(self,name, price):
        self.items.append((name, price))

    def pay(self):
        total = self.total_price()
        return self.customer.add_points(total)

c1 = Customer("피카츄", "vip")
c2 = Customer("꼬북이", "basic")
order1 = Order(1, c1, [("몬스터볼", 1000), ("상처약", 500)])
order2 = Order(2, c2, [("하이퍼볼", 1500), ("기술머신", 2000)])
order3 = Order(3, c1, [("마스터볼", 10000), ("고급상처약", 1000)])
order3.add_item("포켓몬카드", 700)
print(f"주문 1 총액: {order1.total_price()}")
print(f"주문 2 총액: {order2.total_price()}")
print(f"주문 3 총액: {order3.total_price()}")
order1.pay()
order2.pay()
order3.pay()
print(c1.summary())
print(c2.summary())