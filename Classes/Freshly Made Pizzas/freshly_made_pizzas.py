class Pizza:
    order_number = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = Pizza.order_number
        Pizza.order_number += 1

    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])

    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])


p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
print(p1.ingredients)
# ➞ ["bacon", "parmesan", "ham"]

print(p2.ingredients)
# ➞ ["spinach", "olives", "mushroom"]

print(p1.order_number)
# ➞ 1

print(p2.order_number)
# ➞ 2
