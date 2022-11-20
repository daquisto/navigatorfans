from django.db import models


class Guitar(models.Model):
    model_name = models.CharField(max_length=30)
    serial_number = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year_of_manufacture = models.IntegerField()
    weight = models.FloatField()
    condition = models.CharField(max_length=200)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pk}-{self.model_name}"


