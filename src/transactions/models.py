from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    cost = models.DecimalField(max_digits=11, decimal_places=2, default=0)

    # define spending categories
    groc = 'Groceries'
    dinning = 'Dinning & Drinks'
    no_cat = 'Uncategorized'
    auto = 'Auto & Transport'
    charity = 'Charity'
    education = 'Education'
    entertainment = 'Entertainment'
    fees = 'Fees & Charges'
    finance = 'Financial'
    fitness = 'Fitness'
    gifts = 'Gifts'
    health = 'Health'
    loans = 'Loans'
    pets = 'Pets'
    shopping = 'Shopping'
    taxes = 'Taxes'
    travel = 'Travel'
    utilities = 'Utilities'

    # store them in list of tuples
    spending_categories = [
        (groc, 'Groceries'),
        (dinning, 'Dinning and Drinks'),
        (no_cat, 'Uncategorized'),
        (charity, 'Charity'),
        (education, 'Education'),
        (entertainment, 'Entertainment'),
        (fees, 'Fees & Charges'),
        (finance, 'Financial'),
        (fitness, 'Fitness'),
        (gifts, 'Gifts'),
        (health, 'Health'),
        (loans, 'Loans'),
        (pets, 'Pets'),
        (shopping, 'Shopping'),
        (taxes, 'Taxes'),
        (travel, 'Travel'),
        (utilities, 'Utilities'),
        (auto, 'Auto & Transport'),
    ]
    # create the category attribute
    category = models.CharField(
        max_length=250,
        choices=spending_categories,
        default=no_cat,
    )

    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.category
