from databases.postgres import pg_db
from databases.postgres.product import Product
from databases.postgres.shop import Shop


def create_table_in_postgres(db, models_list):
    db.connect()
    db.create_tables(models_list)


def product_setter(brand, minimum_market_price, capacity):
    product = Product(brand=brand, minimum_market_price=minimum_market_price, capacity=capacity)
    return product.save()


def shop_setter(name, price, product):
    shop = Shop(name=name, price=price, product=product)
    return shop.save()


create_table_in_postgres(pg_db, [Shop, Product])


