from django.db import models

class Card(models.Model): #creats the card model
    name = models.CharField(max_length=200)
    set_code = models.CharField(max_length=10)
    set_num = models.CharField(max_length=10)
    foil = models.BooleanField(default=False)
    
class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rel_card = models.ForeignKey(Card, on_delete=models.PROTECT) ## This should make it so that when a price record is delete the card is not
    date = models.DateField("date published")