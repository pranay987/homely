from django.db import models

from core.models import Property, HomeOwner, Renter

# Create your models here.
RESERVATION_STATUS = (
    ('RESERVED', 'RESERVED'),
    ('CANCELLED', 'CANCELLED')
)


class Reservation(models.Model):
    # TODO: Define fields here
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    booking_data = models.DateTimeField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS)


    class Meta:
        verbose_name = "Reservations"
        verbose_name_plural = "Reservations"

    def __str__(self):
        return "{0} booked {1}".format(
            self.renter.user.username, self.property.address
        )

    # def save(self):
    #     pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Define custom methods here


