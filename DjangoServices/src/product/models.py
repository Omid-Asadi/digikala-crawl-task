from django.db import models
from django.utils.translation import ugettext_lazy as _
from khayyam import JalaliDatetime
from lib.base_model import BaseModel


class Product(BaseModel):
    brand = models.CharField(_('brand'), max_length=255)
    minimum_market_price = models.BigIntegerField(_('minimum price'))
    capacity = models.CharField(_('capacity'), max_length=255)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'product'

    def __str__(self):
        return f'{self.brand} {self.capacity}'

    @property
    def jalali_created_time(self):
        if self.created_time is None or self.created_time == "":
            return
        return JalaliDatetime(self.created_time).strftime('%Y-%m-%d %H:%m')

    @property
    def jalali_modified_time(self):
        if self.modified_time is None or self.modified_time == "":
            return
        return JalaliDatetime(self.modified_time).strftime('%Y-%m-%d %H:%m')
