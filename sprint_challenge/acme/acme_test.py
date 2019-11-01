"""
acme.acme_test :: Simple unit tests for acme module.
"""

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the topsest, since 1992!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod1 = Product("Test Product 1")
        self.assertEqual(prod1.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod2 = Product("Test Product 2")
        self.assertEqual(prod2.weight, 20)

    def test_product_methods(self):
        """
        Builds an object with non-default parameter values and ensures 
        their stealability() and explode() methods function as expected.
        """
        # Build the product with non-default parameter values
        prod3 = Product(
            "Test Product 3", price=40, weight=30, flammability=0.9
        )

        # Test if stealability() is functioning
        test_steal_return = "Very stealable!"
        self.assertEqual(prod3.stealability(), test_steal_return)

        # Test if explode is functioning
        test_explode_return = "...boom!"
        self.assertEqual(prod3.explode(), test_explode_return)


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the accuratest, since 1902!"""

    def test_default_num_products(self):
        """Checks that the report really does receive a list of length 30."""

        # Create list of 30 products (default)
        products = generate_products()

        # Assert that the length of products list is equal to 30
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """
        Checks that the generated names for a default batch of products 
        are all valid possible names to generate 
        (adjective, space, noun, from the lists of possible words).
        """

        # Create list of 30 products (default)
        products = generate_products()

        # Loop through products list
        for product in products:
            # Split up the name into components
            name_split = product.name.split()

            # Assert that components are in respective lists
            self.assertIn(name_split[0], ADJECTIVES)
            self.assertIn(name_split[1], NOUNS)


if __name__ == "__main__":
    unittest.main()
