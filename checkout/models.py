import uuid
from django.db import models
from django.db.models import Sum

from gallery.models import ImageEntry


class ImageOrderInfo(models.Model):
    order_id = models.CharField(max_length=32, unique=True, null=False,
                                editable=False)
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    date_ordered = models.DateField(auto_now_add=True, editable=False)
    email_address = models.EmailField(max_length=255, null=False,)
    phone_number = models.CharField(max_length=15)

    order_total = models.DecimalField(
        max_digits=32,
        decimal_places=2,
        null=False,
        default=0
        )

    def update_total(self):
        self.order_total = self.ImageOrderLineItem.aggregate(
            Sum('image_lineitem_total'))['image_lineitem_total__sum']
        self.save()

    def _generate_order_id(self):
        '''generate a uuid for the order_id'''
        return uuid.uuid4().hex.upper()

    def save(self):
        if not self.order_id:
            self.order_number = self._generate_order_id()
        super().save()

    def __str__(self):
        return self.str(order_id)

class ImageOrderLineItem(models.Model):
    order = models.ForeignKey(ImageOrderInfo, on_delete=models.CASCADE)
    image_product = models.ForeignKey(ImageEntry, on_delete=models.CASCADE)
    image_lineitem_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False)

    def save(self):
        self.image_lineitem_total = self.image_product.price
        self.save()

        def __str__(self):
            return f'image {self.image_product.id} with order id: {self.order.order_id}'


# class RequestOrderInfo(models.Model):
#     order_id = models.CharField(max_length=32, null=False, editable=False)
#     first_name = models.CharField(max_length=64, null=False, blank=False)
#     last_name = models.CharField(max_length=64, null=False, blank=False)
#     date_ordered = models.DateField(auto_now_add=True, editable=False)
#     email_address = models.EmailField(max_length=255, null=False,)
#     phone_number = models.CharField(max_length=10)

#     total = models.DecimalField(
#         max_digits=32,
#         decimal_places=2,
#         null=False,
#         default=0
#         )
