from django.db import models


# Create your models here.
class cnscl(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()


class cg(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()


class ss(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()


class os(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()


class opr(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()


class pyth(models.Model):
    qno = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
