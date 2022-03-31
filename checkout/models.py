import uuid
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from gallery.models import ImageEntry
from commission.models import CommissionRequest


def generate_order_id():
    ''' generate a uuid for the order_id '''
    return uuid.uuid4().hex.upper()


class ImageOrderInfo(models.Model):
    '''
    '''
    order_id = models.CharField(max_length=32, unique=True, null=False,
                                editable=False)
    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    date_ordered = models.DateField(auto_now_add=True, editable=False)
    email_address = models.EmailField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    client_id = models.CharField(max_length=255, null=False,
                                 blank=False, default='')
    user = models.ForeignKey(
        User,
        blank=False,
        default=2,
        on_delete=models.SET(2))

    order_total = models.DecimalField(
        max_digits=32,
        decimal_places=2,
        null=False,
        default=0
        )

    def update_total(self):
        self.order_total = self.image_lineitems.aggregate(
            Sum('image_lineitem_total'))['image_lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = 'I-'+generate_order_id()
        super().save()

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = 'Image order info entry'
        verbose_name_plural = 'Image order info'


class ImageOrderLineItem(models.Model):
    '''
    List of items ordered
    '''
    order = models.ForeignKey(
        ImageOrderInfo,
        on_delete=models.CASCADE,
        related_name='image_lineitems'
        )

    image_product = models.ForeignKey(
        ImageEntry,
        null=False,
        blank=False,
        on_delete=models.CASCADE
        )

    image_lineitem_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False
        )

    def save(self, *args, **kwargs):
        self.image_lineitem_total = self.image_product.price
        super().save(*args, **kwargs)

        def __str__(self):
            order_id = f'{self.order.order_id}'
            product_id = f'{self.image_product.id}'
            return f'image {product_id} with order id: {order_id}'


class RequestOrderInfo(models.Model):
    '''
    order information comming from the requests
    '''
    order_id = models.CharField(max_length=32, unique=True, null=False,
                                editable=True)
    request_order = models.ForeignKey(
        CommissionRequest,
        on_delete=models.CASCADE,
        related_name='request_order'
        )

    first_name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64, null=False, blank=False)
    date_ordered = models.DateField(auto_now_add=True, editable=False)
    email_address = models.EmailField(max_length=255, null=False,)
    phone_number = models.CharField(max_length=15)
    client_id = models.CharField(max_length=255, null=False,
                                 blank=False, default='')
    user = models.ForeignKey(
        User,
        blank=False,
        default=2,
        on_delete=models.SET(2))

    order_total = models.DecimalField(
        max_digits=32,
        decimal_places=2,
        null=False,
        default=0
        )

    def update_total(self):
        self.order_total = self.request_order.price
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = 'R-'+generate_order_id()
        self.save()

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = 'Request order info entry'
        verbose_name_plural = 'Request order info'
