from django.db import models

# Create your models here.
class MarketCap(models.Model):
    name = models.CharField(
        max_length = 200
    )
    price = models.CharField(
        max_length = 20
    )
    one_h = models.CharField(
        max_length = 20
    )
    twenty_four_h = models.CharField(
        max_length = 20
    )
    seven_d =models.CharField(
        max_length = 20
    )
    market_cap = models.CharField(
        max_length = 20
    )
    volume = models.CharField(
        max_length = 20
    )
    circulating_supply = models.CharField(
        max_length = 20
    )

    def __str__(self) -> str:
        return '{}: {}'.format(self.name , self.price)
