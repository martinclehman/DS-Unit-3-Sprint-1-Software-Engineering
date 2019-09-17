class Product:
    # Parent Class

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight

        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio <= 0.5 < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight

        if product < 10:
            return "...fizzle."
        elif product <= 10 < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "that tickles."
        elif self.weight <= 5 < 15:
            return "hey that hurt!"
        else:
            return "OUCH!"


class Product:
    # Parent Class

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        ratio = self.price / self.weight

        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio <= 0.5 < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        product = self.flammability * self.weight

        if product < 10:
            return "...fizzle."
        elif product <= 10 < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        from random import randint

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "that tickles."
        elif self.weight <= 5 < 15:
            return "hey that hurt!"
        else:
            return "OUCH!"
