from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Property(models.Model):
    # TODO: Define fields here
    address = models.TextField()

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Propertys"

    def __str__(self):
        return "{}".format(self.address)

    # def save(self):
    #     pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Define custom methods here




class HomeOwner(models.Model):
    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ManyToManyField(Property, blank=True, null=True)

    class Meta:
        verbose_name = "HomeOwner"
        verbose_name_plural = "HomeOwners"

    def __str__(self):
        return "{}".format(self.user.username)

    # def save(self):
    #     pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Define custom methods here


class Renter(models.Model):
    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Renter"
        verbose_name_plural = "Renters"

    def __str__(self):
        return "{}".format(self.user.username)

    # def save(self):
    #     pass

    @models.permalink
    def get_absolute_url(self):
        return ('')

    # TODO: Define custom methods here


