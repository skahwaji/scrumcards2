from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="List", on_delete=models.CASCADE, null=True)
    #
    def __str__(self):
        return "{}".format(self.name)

class CardsQuerySet(models.QuerySet):
    def cards_for_user(self, user):
        return self.filter()

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,blank=True)
    #adding more fields on existing databse, default should be set
    #if the fields are not null already
    list = models.ForeignKey(List, related_name="cards", on_delete=models.CASCADE)
    story_points = models.IntegerField(blank=True, null=True)
    business_value = models.IntegerField(blank=True, null=True)

    objects = CardsQuerySet.as_manager()

    def __str__(self):
        return "{}".format(self.title)





