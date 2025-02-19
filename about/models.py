from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel

AboutModel = get_user_model()


class AboutCategoryModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='children',
        verbose_name=_('parent')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about category')
        verbose_name_plural = _('about categories')


class About(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name