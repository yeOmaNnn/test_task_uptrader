from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField("URL", max_length=255)
    position = models.PositiveIntegerField("Position", default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = "Menu Items"
