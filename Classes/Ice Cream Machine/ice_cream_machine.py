class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        result = []
        if self.ingredients and self.toppings:
            for i in self.ingredients:
                for t in self.toppings:
                    result.append([i, t])
        return result


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())
    # should print:
    # [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
