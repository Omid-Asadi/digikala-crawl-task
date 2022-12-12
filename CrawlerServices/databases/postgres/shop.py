from peewee import CharField, BigIntegerField, ForeignKeyField
from databases.postgres import BaseModel
from .product import Product


class Shop(BaseModel):
    name = CharField(max_length=255, null=True, verbose_name='name')
    price = BigIntegerField()
    product = ForeignKeyField(Product, backref="shops", verbose_name='product')

    class Meta:
        table_name = 'shop'
