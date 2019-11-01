# Data Science Unit 3 Sprint Challenge 1

- [Data Science Unit 3 Sprint Challenge 1](#data-science-unit-3-sprint-challenge-1)
    - [Software Engineering - the Acme Way](#software-engineering---the-acme-way)
    - [Part 1 - Keeping it Classy](#part-1---keeping-it-classy)
    - [Part 2 - Objects that Go!](#part-2---objects-that-go)
    - [Part 3 - A Proper Inheritance](#part-3---a-proper-inheritance)
    - [Part 4 - Class Report](#part-4---class-report)
    - [Part 5 - Measure twice, Test once](#part-5---measure-twice-test-once)
    - [Part 6 - Style it Up](#part-6---style-it-up)
    - [Part 7 - Questions (and your Answers)](#part-7---questions-and-your-answers)
    - [Part 8 - Turn it in!](#part-8---turn-it-in)

---

## Software Engineering - the Acme Way

In this sprint challenge you will write code and answer questions related to object-oriented programming, code style/reviews, containers, and testing. You may use any tools and references you wish, but your final code should reflect your work and be saved in .py files (not notebooks), and (along with this file including your written answers) added to your DS-Unit-3-Sprint-1-Software-Engineering repository.

For all your code, you may only import/use the following:

- Other modules you write
- unittest (from the standard library)
- random (from the standard library)

As always, make sure to manage your time - get a section/question to "good enough" and then move on to make sure you do everything. You can always revisit and polish at the end if time allows.

This file is Markdown, so it may be helpful to add/commit/push it first so you can view it all nice and rendered on GitHub.

Good luck!

---

## Part 1 - Keeping it Classy

As an employee of Acme Corporation, you're always looking for ways to better organize the vast quantities and variety of goods your company manages and sells.

Everything Acme sells is considered a `Product`, and must have the following fields (variables that live "inside" the class):

- `name` (string with no default)
- `price` (integer with default value 10)
- `weight` (integer with default value 20)
- `flammability` (float with default value 0.5)
- `identifier` (integer, automatically genererated as a random (uniform) number anywhere from 1000000 to 9999999, includisve)(inclusive).

Write a Python class to model the above data. Make sure you are precise in your field names and types, and that your class has an __init__ constructor method with appropriate defaults (or lack thereof).

> Hint - random.randint should be able to serve your random number needs.

Save the class in `acme.py`, and you can test your code in a Python repl as follows:

    >>> from acme import Product
    >>> prod = Product('A Cool Toy')
    >>> prod.name
    'A Cool Toy'
    >>> prod.price
    10
    >>> prod.weight
    20
    >>> prod.flammability
    0.5
    >>> prod.identifier
    2812086  # your value will vary

---

## Part 2 - Objects that Go!

The class you wrote in part 1 is nice, but it doesn't do anything - that is, it doesn't have any methods. So let's add some! Specifically, add two methods:

1. `stealability(self)`

Calculates the price divided by the weight, and then returns a message: 

    if the ratio is less than 0.5 
        return "Not so stealable...", 
    if it is greater or equal to 0.5 but less than 1.0 
        return "Kinda stealable.", and 
    otherwise 
        return "Very stealable!"

2. `explode(self)`

Calculates the flammability times the weight, and then returns a message: 

    if the product is less than 10
        return "...fizzle.", 
    if it is greater or equal to 10 but less than 50 
        return "...boom!", and 
    otherwise 
        return "...BABOOM!!"

====== ∫ ======

Save your code, and you can test as follows:

    >>> from acme import Product
    >>> prod = Product('A Cool Toy')
    >>> prod.stealability()
    'Kinda stealable.'
    >>> prod.explode()
    '...boom!'

---

## Part 3 - A Proper Inheritance

Of course, Acme doesn't just sell generic products - it sells all sorts of special specific things!

Make a subclass of Product named `BoxingGlove` that does the following:

- Change the default weight to 10 (but leave other defaults unchanged)
- Override the explode method to always return "...it's a glove."
- Add a punch method that returns "That tickles." 

    if the weight is below 5,  
        "That tickles."  
    if the weight is greater or equal to 5 but less than 15  
        "Hey that hurt!"   
    otherwise  
        "OUCH!"  

====== ∫ ======

Example test run:

    >>> from acme import BoxingGlove
    >>> glove = BoxingGlove('Punchy the Third')
    >>> glove.price
    10
    >>> glove.weight
    10
    >>> glove.punch()
    'Hey that hurt!'
    >>> glove.explode()
    "...it's a glove."

---

## Part 4 - Class Report

Now you can represent your inventory - let's use these classes and write an `acme_report.py` module to generate random products and print a summary of them. For the purposes of these functions we will only use the Product class.

Your module should include two functions:

- `generate_products()` should generate a given number of products (default 30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary

For the purposes of generation, "random" means uniform - all possible values should vary uniformly across the following possibilities:

- name should be a random adjective from ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved'] followed by a space and then a random noun from ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???'], 
  - e.g. 'Awesome Anvil' and Portable Catapult' are both possible
- price and weight should both be from 5 to 100 (inclusive and independent, and remember - they're integers!)
- flammability should be from 0.0 to 2.5 (floats)

You should implement only depending on random from the standard library, your Product class from acme.py, and built-in Python functionality.

For the report, you should calculate and print the following values:

- Number of unique product names in the product list
- Average (mean) price, weight, and flammability of listed products
- At the bottom of acme_report.py you should put the following code:

Following is useful starting code for `acme_report.py`:

```python
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
```

The last lines let you test by running python `acme_report.py`. You should see output like:

    $ python acme_report.py
    ACME CORPORATION OFFICIAL INVENTORY REPORT
    Unique product names: 19
    Average price: 56.8
    Average weight: 54.166666666666664
    Average flammability: 1.258097155966675

It's OK for the specifics to vary (how you message/format), but it should output and clearly identify all four relevant numbers.

---

## Part 5 - Measure twice, Test once

Make a file acme_test.py starting from the following code:

```python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


if __name__ == '__main__':
    unittest.main()
```

If you run the tests you should see output like:

    $ python acme_test.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

Complete the following:

- Add at least 2 more test methods to AcmeProductTests for the base Product class: 
  - at least 1 that tests default values (as shown), 
  - and one that builds an object with different values and ensures their stealability() and explode() methods function as they should
- Write a new test class AcmeReportTests with at least 2 test methods: 
  - test_default_num_products which checks that it really does receive a list of length 30, 
  - and test_legal_names which checks that the generated names for a default batch of products are all valid possible names to generate (adjective, space, noun, from the lists of possible words)

> Hint - test_legal_names is the trickiest of these, but may not be as bad as you think.  
> Check out assertIn from unittest, and remember that Python is pretty handy at string processing.  
> But if you get stuck, move on and revisit.

Note that `inventory_report()` is pretty tricky to test, because it doesn't return anything - it just prints (a "side-effect"). For the purposes of this challenge, don't worry about testing it - but as a stretch goal/something to think about, it's a good ponderer.

---

## Part 6 - Style it Up

If you did the earlier parts in an editor that was linting your code (warning you about violations of PEP8 style) and you listened to it, you're already done!

If not, go back and fix things! If you don't have a built-in tool for checking, you can use PEP8 online.

Go for lint-free! If there's a stubborn warning or two you can't fix though, it's okay to leave a comment explaining it and move on.

---

## Part 7 - Questions (and your Answers)

Acme Corporation isn't just a few .py files. If you want to grow in your career here, you'll have to answer the following:

        What, in your opinion, is an important part of code reviews?  
        That is, what is something you pay attention to when you review code, 
        and that you appreciate when others do the same for your code?

The simple act of taking someone else through code that I've written allows me to view it from a different perspective. By doing so it forces you to go through it as if you were reading someone else's code, a process that will give you a good idea of how readable and understandable the code is. That being said, when I'm reading code I pay very close attention to that aspect of it–the readability and ease of understanding. Indeed, it's difficult not to, because you are quite literally _reading_ through it, trying to understand it. I also appreciate when others point that out about my code.

Additionally, I pay attention to is how neat and organized the code is, with special attention paid to naming and stylistic conventions.

---

We have an awful lot of computers here, and it gets pretty confusing with slightly different things running on all of them. 

        How could containers help us improve this situation? 

With containers, it is possible to isolating a specific environment, keeping it separate from the operating system of whatever machine is running the container. This way, it is much easier to recreate precisely the environment in which the application was _supposed_ to run. Not only does this make the execution of code more reproducible, it allows for easy deployment to any kind of machine—not just the kind of machine on which the code was first written. Whether the deployment is to a colleague's workstation for them to work on the code or to a production server, containers make the process repeatable and consistent.

---

## Part 8 - Turn it in!

Add all the files you wrote (`acme.py`, `acme_report.py`, and `acme_test.py`), as well as this file with your answers to part 7, to your weekly repo (DS-Unit-3-Sprint-1-Software-Engineering). 

Commit, push, and await feedback from Acme Corporation management. Thanks for your hard work!

Bonus! Got this far? Read up on the history of the fine Acme Corporation, with decades of quality products and many satisfied customers (mostly coyotes).
