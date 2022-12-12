from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from khayyam import JalaliDatetime


class BaseModel(models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(_('modified time'), auto_now=True)

    class Meta:
        abstract = True

    @property
    def jalali_date_added(self):
        return JalaliDatetime(timezone.localtime(self.created_time)).strftime('%H:%M %y/%m/%d')

    @property
    def jalali_date_modify(self):
        return JalaliDatetime(timezone.localtime(self.modified_time)).strftime('%H:%M %y/%m/%d')
