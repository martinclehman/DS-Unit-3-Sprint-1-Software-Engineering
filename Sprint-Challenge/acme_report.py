#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    from random import choice

    for i in range(num_products):
        name = choice(ADJECTIVES) + ' ' + choice(NOUNS)
        price = randint(5,100)
        weight = randint(5,100)
        flammability = uniform(0,2.5)

        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    
    def mean(list):
        return sum(list)/len(list)
    n_unique = len(set([p.name for p in products]))
    mean_price = mean([p.price for p in products])
    mean_weight = mean([p.weight for p in products])
    mean_flammability = mean([p.flammability for p in products])

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print("Unique produtc names: ", n_unique)
    print("Average price: ", mean_price)
    print("Average weight: ", mean_weight)
    print("Average flammability: ", mean_flammability)
    
    return

if __name__ == '__main__':
    inventory_report(generate_products())
