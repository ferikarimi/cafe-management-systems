from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class MenuItems(models.Model):
    category_choices =[
        ('Food', 'Food'),
        ('Hot Drinks', 'Hot Drinks'),
        ('Cold Drinks', 'Cold Drinks'),
        ('Dessert', 'Dessert'),
        ('Breakfast', 'Breakfast'),
        ('Launch', 'Launch'),
        ('Dinner','Dinner'),
    ]
    name = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices= category_choices)
    discount = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], default=0)
    serving_time_period = models.PositiveIntegerField()
    estimated_cooking_time = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name