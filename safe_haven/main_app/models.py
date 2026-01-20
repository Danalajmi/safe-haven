from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

IMPACT = (
    ("F", "Friends"),
    ("f", "Family"),
    ("S", "Studies"),
    ("R", "Relationship"),
    ("W", "Work"),
    ("H", "Health"),
    ("C", "Current Events"),
)

# ! change these

SCALE = (
    (1, "Very Low"),
    (2, "Low"),
    (3, "Medium"),
    (4, "High"),
    (5, "Very High"),
)


class Journal(models.Model):

    title = models.TextField()
    description = models.TextField()
    impact = models.CharField(max_length=1, choices=IMPACT)
    rate = models.IntegerField(choices=SCALE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Journal_detail", kwargs={"pk": self.pk})

class Article(models.Model):
    title = models.TextField()
    category = models.CharField(max_length=1)
    content = models.TextField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("Art_detail", kwargs={"pk": self.pk})

