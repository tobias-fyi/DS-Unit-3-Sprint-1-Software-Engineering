"""
acme.acme_report :: Generates random products and provides a summary printout.

Returns
-------
stdout
    A brief summary of randomly-generated products.
"""

from random import randint, choice, uniform

from acme import Product

# Lists to be used in product name generation
ADJECTIVES = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
NOUNS = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]


def generate_products(num_products=30, adj=ADJECTIVES, noun=NOUNS):
    """
    Generates a list of Acme products.
    
    Parameters
    ----------
    num_products : int, optional
        Number of products to be generated, by default 30.
    adj : list, optional
        List of adjectives to use in product name generation,
        by default ADJECTIVES.
    noun : list, optional
        List of nouns to use in product name generation, 
        by default NOUNS.
    
    Returns
    -------
    list
        List of instances of acme.Product with randomly-generated names.
    """

    products = []  # List to hold generated products

    for i in range(num_products):
        # Create this instance's parameter values
        name = f"{choice(adj)} {choice(noun)}"
        price = randint(5, 100)
        weight = randint(5, 100)
        flam = uniform(0.0, 2.5)
        identifier = randint(1000000, 9999999)

        # Instantiate a product according to above parameters
        # and append it to the products list
        products.append(
            Product(
                name=name,
                price=price,
                weight=weight,
                flammability=flam,
                identifier=identifier,
            )
        )

    return products


def inventory_report(products):
    """
    Generates brief summary report of product inventory.
    
    Parameters
    ----------
    products : list
        List of adme.Product instances in inventory.
    """

    n_unique = len(set(products))

    # Lists of parameters to calculate means
    price_list = []
    weight_list = []
    flam_list = []

    # Loop through to fill lists above
    for product in products:
        price_list.append(product.price)
        weight_list.append(product.weight)
        flam_list.append(product.flammability)

    # Calculate means of each field
    price_mean = sum(price_list) / len(price_list)
    weight_mean = sum(weight_list) / len(weight_list)
    flam_mean = sum(flam_list) / len(flam_list)

    # Create the printed report as multi-line string
    report_text = f"""ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: {n_unique}
Average price: {round(price_mean, 2)}
Average weight: {round(weight_mean, 2)}
Average flammability: {round(flam_mean, 2)}"""

    # TODO: print in justified format

    print(report_text)


if __name__ == "__main__":
    inventory_report(generate_products())
