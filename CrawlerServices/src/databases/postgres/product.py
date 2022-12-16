from peewee import CharField, BigIntegerField
from databases.postgres import BaseModel


class Product(BaseModel):
    brand = CharField(max_length=255, null=True, verbose_name='brand')
    minimum_market_price = BigIntegerField()
    capacity = CharField(max_length=255, null=True, verbose_name='capacity')

    class Meta:
        table_name = 'product'
