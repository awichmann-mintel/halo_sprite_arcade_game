from django.db import models


class ScoresModel(models.Model):
    score = models.IntegerField()
    user = models.CharField(max_length=50, default="AWichmann")
