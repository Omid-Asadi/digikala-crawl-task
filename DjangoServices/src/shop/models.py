from django.db import models
from khayyam import JalaliDatetime

from lib.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _
from product.models import Product


class Shop(BaseModel):
    name = models.CharField(_('name'), max_length=255)
    price = models.BigIntegerField(_('price'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shops', verbose_name=_("product"))

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'
        db_table = 'shop'

    def __str__(self):
        return self.name

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