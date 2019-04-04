from django.db import models


class ScoresModel(models.Model):
    score = models.IntegerField()
