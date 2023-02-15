from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

from django.db.models import CASCADE
import uuid

class StandardModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Account(StandardModelMixin):
    name = models.CharField(max_length=256)
    created = models.DateField()
    activate = models.BooleanField()


class User(models.Model):
    user = models.OneToOneField(User)  

    def plant_tree():
        pass
    
    def plant_trees():
        pass


class Profile(StandardModelMixin):
    about = models.TextField()
    joined = models.DateTimeField()


class PlantedTree(StandardModelMixin):
    age = models.IntegerField()
    planted_at = models.DateTimeField()
    user = models.ForeignKey("User", on_delete=CASCADE)
    tree = models.ForeignKey("Tree", on_delete=CASCADE)
    account = models.ForeignKey("Account", on_delete=CASCADE)
    #(longitude, latitude)
    location = models.PointField(help_text="Represented as (longitude, latitude)")


class Tree(StandardModelMixin):
    name = models.CharField(max_length=256)
    scientific_name = models.CharField(max_length=256)