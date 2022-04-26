''' Django model module '''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    ''' genre database and accostiated cost'''
    title = models.CharField(max_length=16, unique=True)
    price = models.DecimalField(decimal_places=2,
                                max_digits=10, default=0)

    def __str__(self):
        string_title = str(self.title)
        return string_title


class CommissionRequest(models.Model):
    '''
    Model for Request page
    '''
    status_choices = [
        ('PEND', 'Pending'),
        ('ORDR', 'Ordered'),
        ('URWE', 'Under Review'),
        ('ACPD', 'Accepted'),
        ('DECL', 'Declined'),
        ('IPRR', 'In progress'),
        ('DONE', 'Done'),
        ('USRW', 'User review')
    ]

    size_choices = [
        ('X256', '256 x 256'),
        ('X512', '512 x 512'),
        ('TX1K', '1024 x 1024'),
        ('TX2K', '2048 x 2048'),
        ('L108', '1080p (Landscape)'),
        ('P108', '1080p (Portrait)'),
        ('LA2k', '2k (Landscape)'),
        ('PO2K', '2k (Portait)'),
        ('LA4K', '4k (Landscape)'),
        ('PO4k', '4K (Portrait)')
    ]

    requested_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE, default=0)

    type = models.ForeignKey(Genre, on_delete=models.SET('Deleted Genre'))
    status = models.CharField(
        choices=status_choices,
        max_length=4,
        default='PEND')

    image_size = models.CharField(
        choices=size_choices,
        max_length=4)

    user_description = models.TextField()
    date_requested = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    archived = models.BooleanField(default=False)


class Comment(models.Model):
    '''
    Attaches comments to the request to have a feebackloop
    between user and commissioner
    '''
    comment_posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_atached_to = models.ForeignKey(
        CommissionRequest(),
        on_delete=models.CASCADE,
        related_name="comment")

    date_posted = models.DateTimeField(
        auto_now=True,
        editable=False)

    comment_content = models.TextField(max_length=255)

    class Meta:
        ''' Tells django to order be date posted '''
        ordering = ["-date_posted"]

    def __str__(self):
        return str(self.comment_content) + str(self.comment_atached_to)
